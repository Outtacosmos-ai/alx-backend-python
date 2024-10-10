#!/usr/bin/env python3
"""Module for safe_first_element function."""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely get the first element of a sequence.

    Args:
        lst: A sequence of any type

    Returns:
        The first element of the sequence if it exists, None otherwise
    """
    if lst:
        return lst[0]
    else:
        return None
