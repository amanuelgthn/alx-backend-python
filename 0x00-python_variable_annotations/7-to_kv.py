#!/usr/bin/env python3
"""Complex types -string and int/float to tuple"""


from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[Union[int, float]]:
    """ function that takes string and an inr or float
    and returns a tuple"""
    return tuple([k, v * v])
