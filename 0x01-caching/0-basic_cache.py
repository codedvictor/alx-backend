#!/usr/bin/env python3
"""
Basic caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Caching system inherited from BaseCaching module
    """

    def put(self, key, item):
        """
        put new item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        get the value linked to key in the cache
        """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
