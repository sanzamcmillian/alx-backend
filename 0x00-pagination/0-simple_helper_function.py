#!/usr/bin/env python3
"""simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """returns a tuple of size two"""
    start = (page -  1) * page_size
    end = start + page_size
    return (start, end)
