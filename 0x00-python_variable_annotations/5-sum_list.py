#!/usr/bin/env python3
"""complex types-list of floats"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """type annotated function sum_list which takes
    input_list of floats as an argument and returns
    their sum as a float"""
    return sum(input_list)
