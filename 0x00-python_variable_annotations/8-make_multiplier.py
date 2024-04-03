#!/usr/bin/env python3
"""Complex types-functins"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Funcation that takes a float as argument and reutrns
    a function that multiplies a float by the given number
    """
    def f_multiplier(number: float) -> float:
        return multiplier * number
    return f_multiplier
