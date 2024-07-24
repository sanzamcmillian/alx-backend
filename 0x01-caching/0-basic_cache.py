#!/usr/bin/env python3
"""Basic Cache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """a class for a basic caching system"""
    def put(self, key, item):
        """assignment method"""
        if key or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """get method"""
        return self.cache_data.get(key, None)
