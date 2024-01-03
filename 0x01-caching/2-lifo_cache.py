#!/usr/bin/env python3
"""
LIFO caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Caching system inherited from BaseCaching module
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
                last_key, last_value = self.cache_data.popitem()
                print("DISCARD: {}".format(last_key))

            self.cache_data[key] = item

    def get(self, key):
        """
        get the value linked to key in the cache
        """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
