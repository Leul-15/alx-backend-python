#!/usr/bin/env python3
"""
    Callable function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Args:
    """

    def x(f: float) -> float:
        """ Get the second argument"""
        return float(f * multiplier)

    return x
