#!/usr/bin/env python3
"""Module for element_length function."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input iterable.

    Args:
        lst: An iterable containing sequences

    Returns:
        A list of tuples, each containing a sequence and its length
    """
    return [(i, len(i)) for i in lst]
