#!/usr/bin/env python3
"""Complex types-functins"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """"""
    def f_multiplier(number: float) -> float:
        return multiplier * number
    return f_multiplier
