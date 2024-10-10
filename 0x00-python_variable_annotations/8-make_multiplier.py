#!/usr/bin/env python3

"""
function make_multiplier that takes a float multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return
    """

    def multiplier_function(value: float) -> float:
        """returns
        """

        return value * multiplier
    return multiplier_function
