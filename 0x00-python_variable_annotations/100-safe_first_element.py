#!/usr/bin/env python3

"""
duck-typed annotations:
"""


from typing import Sequence, Optional, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    return s any
    """

    if lst:
        return lst[0]
    else:
        return
