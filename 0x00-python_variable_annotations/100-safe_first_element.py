#!/usr/bin/env python3
"""Duck typing - first element of a sequence"""


from types import NoneType
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    if lst:
        return lst[0]
    else:
        return None