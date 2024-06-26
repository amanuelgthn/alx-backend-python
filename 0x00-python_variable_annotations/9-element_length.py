#!/usr/bin/env python3
"""
Let's duck type an iterable object
"""


from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function annotated and return values of appropriate length values"""
    return [(i, len(i)) for i in lst]
