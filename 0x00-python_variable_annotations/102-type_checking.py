#!/usr/bin/env python3

"""Use mypy to validate
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ returns
    """

    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
