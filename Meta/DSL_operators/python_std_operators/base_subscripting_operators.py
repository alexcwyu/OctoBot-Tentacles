# pylint: disable=missing-function-docstring
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
import ast
import numpy as np

import octobot_commons.dsl_interpreter.operators.subscripting_operator as dsl_interpreter_subscripting_operator
import octobot_commons.dsl_interpreter.operator as dsl_interpreter_operator


class SubscriptOperator(dsl_interpreter_subscripting_operator.SubscriptingOperator):
    """
    Base class for subscripting operators: array[index]
    Subscripting operators have three operands: the array/list, the index or slice and the context.
    """

    @staticmethod
    def get_name() -> str:
        return ast.Subscript.__name__

    def compute(self) -> dsl_interpreter_operator.ComputedOperatorParameterType:
        # Compute the test condition
        array_or_list, index, context = self.get_computed_array_or_list_and_index_or_slice_and_context_parameters()
        if isinstance(context, ast.Load):
            return array_or_list[index]
        if isinstance(context, ast.Del):
            del array_or_list[index]
            return array_or_list
        raise ValueError(f"Unsupported {self.__class__.__name__} context type: {type(context).__name__}")



class SliceOperator(dsl_interpreter_subscripting_operator.SubscriptingOperator):
    """
    Operator for creating slice objects: slice(lower, upper, step)
    Used for array slicing like array[start:stop:step]
    """

    @staticmethod
    def get_name() -> str:
        return ast.Slice.__name__

    def compute(self) -> slice:
        """
        Compute and return a Python slice object.
        """        
        array_or_list, slice, context = self.get_computed_array_or_list_and_index_or_slice_and_context_parameters()

        if not isinstance(slice, (list, tuple, np.ndarray)):
            raise ValueError(f"Unsupported {self.__class__.__name__} slice type: {type(slice).__name__}")
        lower = int(slice[0]) if len(slice) > 0 else None
        upper = int(slice[1]) if len(slice) > 1 else None
        step = int(slice[2]) if len(slice) > 2 else None
        if isinstance(context, ast.Load):
            if lower is not None:
                if upper is not None:
                    if step is not None:
                        return array_or_list[lower:upper:step]
                    return array_or_list[lower:upper]
                return array_or_list[lower:]
            if upper is not None:
                return array_or_list[:upper]
            return array_or_list
        raise ValueError(f"Unsupported {self.__class__.__name__} context type: {type(context).__name__}")
