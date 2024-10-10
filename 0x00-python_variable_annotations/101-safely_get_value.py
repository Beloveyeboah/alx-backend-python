#!/usr/bin/env python3
"""
iven the parameters and the return values, add
type annotations to the function
"""


from typing import TypeVar, Mapping, Any, Union, Optional


T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, T],
        key: Any,
        default: Optional[T] = None) -> Union[T, None]:
    """
    returns a dictionary
    """

    if key in dct:
        return dct[key]
    else:
        return default
