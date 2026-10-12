#  Drakkar-Software OctoBot-Tentacles
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
import contextvars
import ccxt.pro as ccxt_pro
import octobot_trading.exchanges as exchanges
from octobot_trading.enums import WebsocketFeeds as Feeds
import tentacles.Trading.Exchange.kraken.kraken_exchange as kraken_exchange


class KrakenIntervalClient(ccxt_pro.kraken):
    """Keep native candle subscriptions and resolutions distinct per interval."""
    _ohlcv_interval = contextvars.ContextVar("kraken_ohlcv_interval", default=None)

    def get_message_hash(self, channel, interval, symbol):
        if channel == "ohlcv" and interval is None:
            interval = self._ohlcv_interval.get()
        return super().get_message_hash(channel, interval, symbol)

    async def watch_ohlcv(self, symbol, timeframe="1m", since=None, limit=None, params=None):
        token = self._ohlcv_interval.set(timeframe)
        try:
            return await super().watch_ohlcv(symbol, timeframe, since, limit, params or {})
        finally:
            self._ohlcv_interval.reset(token)

    def handle_ohlcv(self, client, message):
        first = message["data"][0]
        token = self._ohlcv_interval.set(self.find_timeframe(first["interval"]))
        try:
            return super().handle_ohlcv(client, message)
        finally:
            self._ohlcv_interval.reset(token)


class KrakenCCXTWebsocketConnector(exchanges.CCXTWebsocketConnector):
    EXCHANGE_FEEDS = {
        Feeds.TRADES: True,
        Feeds.KLINE: True,
        Feeds.TICKER: True,
        Feeds.CANDLE: True,
    }

    @classmethod
    def get_name(cls):
        return kraken_exchange.Kraken.get_name()

    def get_client_class(self):
        return KrakenIntervalClient

    def _get_generator(self, method_name):
        generator = super()._get_generator(method_name)
        if method_name == "watchOHLCV" and generator != Feeds.UNSUPPORTED:
            async def watch_candles(symbol, timeframe="1m", since=None, limit=None, params=None):
                # Current CCXT Kraken filters candle arrays with the dictionary
                # key "timestamp", discarding every row when since is supplied.
                # Fetch unchanged venue data and apply the array timestamp
                # contract here, also ordering Kraken's snapshot chronologically.
                candles = await generator(symbol, timeframe, None, None, params or {})
                candles = sorted(candles, key=lambda candle: candle[0])
                if since is not None:
                    candles = [candle for candle in candles if candle[0] >= since]
                return candles[-limit:] if limit is not None else candles

            return watch_candles
        return generator
