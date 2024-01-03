#!/usr/bin/env python3
"""
LRU caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRU Caching system inherited from BaseCaching module
    """

    def __init__(self):
        """
        Initialization
        """
        super().__init__()
        self.__listItems = []

    def put(self, key, item):
        """
        put new item in the cache
        """

        if key and item:
            if key not in self.__listItems:
                self.__listItems.append(key)
            else:
                pop_key = self.__listItems.pop(self.__listItems.index(key))
                self.__listItems.append(pop_key)

            self.cache_data[key] = item
            if len(self.__listItems) > BaseCaching.MAX_ITEMS:
                last_key = self.__listItems.pop(0)
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))

    def get(self, key):
        """
        get the value linked to key in the cache
        """
        if not key or key not in self.cache_data.keys():
            return None
        last_key = self.__listItems.pop(self.__listItems.index(key))
        self.__listItems.append(last_key)
        return self.cache_data[key]
