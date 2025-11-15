# pylint: disable=missing-class-docstring,missing-function-docstring
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
import typing

import octobot_commons.constants
import octobot_commons.dsl_interpreter.operator as dsl_interpreter_operator
import octobot_trading.exchanges
import octobot_trading.exchange_data
import octobot_trading.api

import tentacles.Meta.DSL_operators.exchange_operators.exchange_operator as exchange_operator
import tentacles.Meta.Keywords.scripting_library as scripting_library



class OHLCVOperator(exchange_operator.ExchangeOperator):
    def __init__(self, *parameters: dsl_interpreter_operator.OperatorParameterType, **kwargs: typing.Any):
        super().__init__(*parameters, **kwargs)
        self.value: dsl_interpreter_operator.ComputedOperatorParameterType = exchange_operator.UNINITIALIZED_VALUE # type: ignore

    @staticmethod
    def get_library() -> str:
        # this is a contextual operator, so it should not be included by default in the get_all_operators function return values
        return octobot_commons.constants.CONTEXTUAL_OPERATORS_LIBRARY

    def get_symbol_and_time_frame(self) -> typing.Tuple[typing.Optional[str], typing.Optional[str]]:
        if parameters := self.get_computed_parameters():
            symbol = parameters[0] if len(parameters) > 0 else None
            time_frame = parameters[1] if len(parameters) > 1 else None
            return (
                str(symbol) if symbol is not None else None,
                str(time_frame) if time_frame is not None else None
            )
        return None, None

    def compute(self) -> dsl_interpreter_operator.ComputedOperatorParameterType:
        if self.value is exchange_operator.UNINITIALIZED_VALUE:
            raise ValueError("{self.__class__.__name__} has not been initialized")
        return self.value


def create_ohlcv_operators(
    exchange_manager: octobot_trading.exchanges.ExchangeManager,
    symbol: str,
    time_frame: str
) -> typing.List[type[OHLCVOperator]]:

    def _get_candle_manager(
        input_symbol: typing.Optional[str], input_time_frame: typing.Optional[str]
    ) -> octobot_trading.exchange_data.CandlesManager:
        return octobot_trading.api.get_symbol_candles_manager(
            octobot_trading.api.get_symbol_data(
                exchange_manager, input_symbol or symbol, allow_creation=False
                ), 
                input_time_frame or time_frame
        )

    class _ClosePriceOperator(OHLCVOperator):
        @staticmethod
        def get_name() -> str:
            return "close"

        async def initialize(self) -> None:
            await super().initialize()
            self.value = _get_candle_manager(*self.get_symbol_and_time_frame()).get_symbol_close_candles(-1)

    class _VolumePriceOperator(OHLCVOperator):
        @staticmethod
        def get_name() -> str:
            return "volume"

        async def initialize(self) -> None:
            await super().initialize()
            self.value = _get_candle_manager(*self.get_symbol_and_time_frame()).get_symbol_volume_candles(-1)

    return [_ClosePriceOperator, _VolumePriceOperator]