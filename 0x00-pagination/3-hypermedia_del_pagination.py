#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary with the key-value pairs
        """
        assert isinstance(index, int)
        assert index >= 0 and index < len(self.dataset())
        assert isinstance(page_size, int) and page_size > 0

        index_dataset = self.indexed_dataset()
        next_index = page_size + index
        data = []

        current = index
        while current < next_index and next_index <= len(index_dataset):
            if index_dataset.get(current):
                data.append(index_dataset[current])
            else:
                next_index += 1
            current += 1
        dic = {}
        dic['index'] = index
        dic['data'] = data
        dic['page_size'] = page_size
        dic['next_index'] = next_index
        return dic
