#!/usr/bin/env python3
"""More involved type annotaions"""


from re import T
from types import NoneType
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
 -> Union[Any, T]:
    """function that accepts with typed value"""
    if key in dct:
        return dct[key]
    else:
        return default
