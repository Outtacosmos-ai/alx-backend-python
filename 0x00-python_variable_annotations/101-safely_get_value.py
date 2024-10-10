#!/usr/bin/env python3
"""Module for safely_get_value function."""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely get a value from a mapping.

    Args:
        dct: A mapping
        key: A key to look up in the mapping
        default: A default value to return if key is not found

    Returns:
        The value from the mapping if key exists, otherwise the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
