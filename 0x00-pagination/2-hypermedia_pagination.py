#!/usr/bin/env python3
"""Hypermedia Paginate"""
import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """gets page from data provided"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """implements a dictionary"""
        start, end = index_range(page, page_size)
        page_data = self.get_page(page, page_size)
        dictionary = {
            "page_size": page_data,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if end < len(self.__dataset) else None,
            "prev_page": page - 1 if start > 0 else None,
            "total_pages": math.ceil(len(self.__dataset) / page_size)
        }
        return dictionary


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of size two"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
