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
import tulipy
import numpy as np

import octobot_commons.dsl_interpreter.operators.call_operator as dsl_interpreter_call_operator
import octobot_commons.dsl_interpreter.operator as dsl_interpreter_operator


def _to_numpy_array(data):
    if isinstance(data, list):
        return np.array(data)
    elif isinstance(data, tuple):
        return np.array(list(data))
    elif isinstance(data, np.ndarray):
        return data
    else:
        raise ValueError(f"Unsupported data type: {type(data)}")


class RSIOperator(dsl_interpreter_call_operator.CallOperator):
    @staticmethod
    def get_name() -> str:
        return "rsi"

    def compute(self) -> dsl_interpreter_operator.ComputedOperatorParameterType:
        operands = self.get_computed_parameters()
        if len(operands) != 2:
            raise ValueError("rsi() requires at two arguments: (data, period)")
        return list(tulipy.rsi(_to_numpy_array(operands[0]), period=int(operands[1])))


class MACDOperator(dsl_interpreter_call_operator.CallOperator):
    @staticmethod
    def get_name() -> str:
        return "macd"

    def compute(self) -> dsl_interpreter_operator.ComputedOperatorParameterType:
        operands = self.get_computed_parameters()
        if len(operands) != 4:
            raise ValueError("macd() requires at three arguments: (data, short_period, long_period, signal_period)")
        macd, macd_signal, macd_hist = tulipy.macd(
            _to_numpy_array(operands[0]), short_period=int(operands[1]), long_period=int(operands[2]), signal_period=int(operands[3])
        )
        return list(macd_hist)


class ADXOperator(dsl_interpreter_call_operator.CallOperator):
    @staticmethod
    def get_name() -> str:
        return "adx"

    def compute(self) -> dsl_interpreter_operator.ComputedOperatorParameterType:
        operands = self.get_computed_parameters()
        if len(operands) != 4:
            raise ValueError("adx() requires at four arguments: (high, low, close, period)")
        return list(tulipy.adx(_to_numpy_array(operands[0]), _to_numpy_array(operands[1]), _to_numpy_array(operands[2]), period=int(operands[3])))


class MAOperator(dsl_interpreter_call_operator.CallOperator):
    @staticmethod
    def get_name() -> str:
        return "ma"

    def compute(self) -> dsl_interpreter_operator.ComputedOperatorParameterType:
        operands = self.get_computed_parameters()
        if len(operands) != 2:
            raise ValueError("ma() requires at two arguments: (data, period)")
        return list(tulipy.sma(_to_numpy_array(operands[0]), period=int(operands[1])))


class EMAOperator(dsl_interpreter_call_operator.CallOperator):
    @staticmethod
    def get_name() -> str:
        return "ema"

    def compute(self) -> dsl_interpreter_operator.ComputedOperatorParameterType:
        operands = self.get_computed_parameters()
        if len(operands) != 2:
            raise ValueError("ema() requires at two arguments: (data, period)")
        return list(tulipy.ema(_to_numpy_array(operands[0]), period=int(operands[1])))


class VWMAOperator(dsl_interpreter_call_operator.CallOperator):
    @staticmethod
    def get_name() -> str:
        return "vwma"

    def compute(self) -> dsl_interpreter_operator.ComputedOperatorParameterType:
        operands = self.get_computed_parameters()
        if len(operands) != 3:
            raise ValueError("vwma() requires at three arguments: (data, volume, period)")
        return list(tulipy.vwma(_to_numpy_array(operands[0]), _to_numpy_array(operands[1]), period=int(operands[2])))
