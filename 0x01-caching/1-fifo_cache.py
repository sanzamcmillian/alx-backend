#!/usr/bin/env python3
"""first in first out"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """FIFO class caching system"""
    def __init__(self):
        """inehrited method"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assignment method"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first, _ = self.cache_data.popitem(False)
            print(f"DISCARD: {first}")

    def get(self, key):
        """retrive a value from the dictionary"""
        return self.cache_data.get(key, None)
