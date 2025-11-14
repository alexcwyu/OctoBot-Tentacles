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
import pytest

import octobot_commons.dsl_interpreter as dsl_interpreter
import octobot_commons.enums as commons_enums
import octobot_commons.constants as commons_constants


async def get_x_value_async() -> int:
    return 666


class SumPlusXOperatorWithoutInit(dsl_interpreter.NaryOperator):
    def __init__(self, *parameters: dsl_interpreter.OperatorParameterType, **kwargs: typing.Any):
        super().__init__(*parameters, **kwargs)
        self.x_value = 42
    
    @staticmethod
    def get_name() -> str:
        return "plus_42"

    def compute(self) -> dsl_interpreter.ComputedOperatorParameterType:
        computed_parameters = self.get_computed_parameters()
        return sum(computed_parameters) + self.x_value


class SumPlusXOperatorWithInit(dsl_interpreter.NaryOperator):
    def __init__(self, *parameters: dsl_interpreter.OperatorParameterType, **kwargs: typing.Any):
        super().__init__(*parameters, **kwargs)
        self.x_value = 42
    
    @staticmethod
    def get_name() -> str:
        return "plus_x"

    async def initialize(self) -> None:
        await super().initialize()
        self.x_value = await get_x_value_async()

    def compute(self) -> dsl_interpreter.ComputedOperatorParameterType:
        computed_parameters = self.get_computed_parameters()
        return sum(computed_parameters) + self.x_value


class TimeFrameToSecondsOperator(dsl_interpreter.CallOperator):
    def __init__(self, operand: dsl_interpreter.OperatorParameterType, **kwargs: typing.Any):
        super().__init__(operand, **kwargs)

    @staticmethod
    def get_name() -> str:
        return "time_frame_to_seconds"

    def compute(self) -> dsl_interpreter.ComputedOperatorParameterType:
        computed_parameters = self.get_computed_parameters()
        return commons_enums.TimeFramesMinutes[commons_enums.TimeFrames(computed_parameters[0])] * commons_constants.MINUTE_TO_SECONDS


@pytest.fixture
def interpreter():
    return dsl_interpreter.Interpreter(
        dsl_interpreter.get_all_operators() + [
            SumPlusXOperatorWithoutInit, SumPlusXOperatorWithInit, TimeFrameToSecondsOperator
        ]
    )


@pytest.mark.asyncio
async def test_interpreter_basic_operations(interpreter):
    assert await interpreter.interprete("plus_42()") == 42
    assert await interpreter.interprete("plus_42(6)") == 48
    assert await interpreter.interprete("plus_42(1, 2, 3)") == 48
    assert await interpreter.interprete("plus_42(1, 1 + 1, 1.5 * sqrt(4))") == 48
    assert await interpreter.interprete("plus_x(1, 1)") == 668
    assert await interpreter.interprete("10 * (plus_x(1, 1) + plus_x(1, 1))") == 10 * (668 + 668) == 13360
    assert await interpreter.interprete("time_frame_to_seconds('1m')") == 60
    assert await interpreter.interprete("min(time_frame_to_seconds('1m'), time_frame_to_seconds('1h'))") == 60
    assert await interpreter.interprete("max(time_frame_to_seconds('1m'), time_frame_to_seconds('1h'))") == 3600
    assert await interpreter.interprete("time_frame_to_seconds('1d')") == 86400
    assert await interpreter.interprete("time_frame_to_seconds('1'+'h')") == 3600
