#!/usr/bin/env python2
"""Type checking"""


from typing import List, Tuple, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """function to be validated using annotations"""
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
