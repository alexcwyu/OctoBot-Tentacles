#  Drakkar-Software OctoBot-Commons
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
import mock
import pytest

import numpy as np

import octobot_commons.enums
import octobot_commons.dsl_interpreter as dsl_interpreter
import tentacles.Meta.DSL_operators.exchange_operators as exchange_operators


SYMBOL = "BTC/USDT"
TIME_FRAME = "1h"


@pytest.fixture
def historical_prices():
    return np.array([
        81.59, 81.06, 82.87, 83, 83.61, 83.15, 82.84, 83.99, 84.55, 84.36, 85.53, 86.54, 86.89, 
        87.77, 87.29, 87.18, 87.01, 89.02, 89.68, 90.36, 92.83, 93.37, 93.02, 93.45, 94.13, 
        93.12, 93.18, 92.08, 92.82, 92.92, 92.25, 92.22
    ])


@pytest.fixture
def exchange_manager(historical_prices):
    candles_manager = mock.Mock(
        get_symbol_open_candles=mock.Mock(return_value=historical_prices),
        get_symbol_high_candles=mock.Mock(return_value=historical_prices),
        get_symbol_low_candles=mock.Mock(return_value=historical_prices),
        get_symbol_close_candles=mock.Mock(return_value=historical_prices),
        get_symbol_volume_candles=mock.Mock(return_value=historical_prices),
        get_symbol_time_candles=mock.Mock(return_value=historical_prices),
    )
    return mock.Mock(
        exchange_symbols_data=mock.Mock(
            get_exchange_symbol_data=mock.Mock(
                return_value=mock.Mock(
                    symbol_candles={
                        octobot_commons.enums.TimeFrames(TIME_FRAME): candles_manager
                    }
                )
            )
        )
    )


@pytest.fixture
def interpreter(exchange_manager):
    return dsl_interpreter.Interpreter(
        dsl_interpreter.get_all_operators() + 
        exchange_operators.create_ohlcv_operators(exchange_manager, SYMBOL, TIME_FRAME)
    )


@pytest.mark.asyncio
async def test_mocks(interpreter, historical_prices):
    assert np.array_equal(await interpreter.interprete("close"), historical_prices)
    assert await interpreter.interprete("close[-1]") == historical_prices[-1] == 92.22


@pytest.mark.asyncio
async def test_rsi_operators(interpreter):
    rsi = await interpreter.interprete("rsi(close, 14)")
    rounded_rsi = [round(v, 2) for v in rsi]
    assert rounded_rsi == [
        79.56, 78.6, 77.04, 81.67, 82.88, 84.06, 87.44, 88.03, 85.21, 85.81, 86.73, 
        78.58, 78.71, 70.4, 72.5, 72.78, 67.78, 67.55
    ]
    assert await interpreter.interprete("round(rsi(close, 26)[-1], 2)") == 74.3
    assert await interpreter.interprete("round(rsi(close, 14)[-1], 2)") == 67.55
    assert await interpreter.interprete("round(rsi(close, 26)[-1] - rsi(close, 14)[-1], 2)") == 6.74
