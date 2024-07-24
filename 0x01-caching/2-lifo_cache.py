#!/usr/bin/env python3
"""Last in first out"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""
    def __init__(self):
        """inherited method"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assignment method"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last, _ = self.cache_data.popitem(True)
                print(f"DISCARD: {last}")
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """retrieve item by key"""
        return self.cache_data.get(key, None)
