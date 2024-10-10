#!/usr/bin/env python3

"""
return values, add type annotations to the function
"""

from typing import TypeVar, Mapping, Optional

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: T,
    default: Optional[T] = None
) -> Optional[T]:
    """
    returns
    """

    if key in dct:
        return dct[key]
    else:
        return default
