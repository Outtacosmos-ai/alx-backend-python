#!/usr/bin/env python3
"""Module for make_multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by multiplier.

    Args:
        multiplier: The float multiplier

    Returns:
        A function that takes a float and returns a product
    """
    def multiply(n: float) -> float:
        return multiplier * n
    return multiply
