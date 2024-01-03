#!/usr/bin/env python3
"""
FIFO caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Caching system inherited from BaseCaching module
    """

    def put(self, key, item):
        """
        put new item in the cache
        """
        keys = self.cache_data.keys()

        if key and item:
            if key in keys:
                self.cache_data[key] = item
            elif len(keys) >= BaseCaching.MAX_ITEMS:
                first_key = list(keys)[0]
                print("DISCARD: {}".format(first_key))
                del self.cache_data[first_key]

            self.cache_data[key] = item

    def get(self, key):
        """
        get the value linked to key in the cache
        """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
