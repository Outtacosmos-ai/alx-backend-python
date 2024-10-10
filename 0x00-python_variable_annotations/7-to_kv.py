#!/usr/bin/env python3
"""Module for to_kv function."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and int/float.

    Args:
        k: A string
        v: An int or float

    Returns:
        A tuple containing the string k and the square of v as a float
    """
    return (k, float(v ** 2))
