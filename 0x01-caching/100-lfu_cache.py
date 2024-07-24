#!/usr/bin/env python3
"""Least Frequently Used Cache"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Cache system"""
    def __init__(self):
        """Initializes the cache"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.freq = []

    def order_items(self, mru):
        """Reorders the items in this cache based on the most
        recently used item.
        """
        max_positions = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0
        for i, key_freq in enumerate(self.freq):
            if key_freq[0] == mru:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(max_positions) == 0:
                max_positions.append(i)
            elif key_freq[1] < self.freq[max_positions[-1]][1]:
                max_positions.append(i)
        max_positions.reverse()
        for pos in max_positions:
            if self.freq[pos][1] > mru_freq:
                break
            ins_pos = pos
        self.freq.pop(mru_pos)
        self.freq.insert(ins_pos, [mru, mru_freq])

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu, _ = self.freq[-1]
                self.cache_data.pop(lfu)
                self.freq.pop()
                print("DISCARD:", lfu)
            self.cache_data[key] = item
            ins_index = len(self.freq)
            for i, key_freq in enumerate(self.freq):
                if key_freq[1] == 0:
                    ins_index = i
                    break
            self.freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.order_items(key)

    def get(self, key):
        """Retrieves an item by key"""
        if key is not None and key in self.cache_data:
            self.order_items(key)
        return self.cache_data.get(key, None)
