#!/usr/bin/env python3

"""Use mypy to validate
"""

from typing import List, Tuple


def zoom_array(lst: Tuple[int], factor: int = 2) -> List[int]:
    """ use mypy
    """

    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
