#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List, Tuple


def index_range(page, page_size):
    """
    index range for page and size
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


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
        """
        Return the appropriate page of the dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        data_size = len(dataset)
        if start_index >= data_size or end_index > data_size:
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dictionary with keys:
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        dic = {}
        data = self.get_page(page, page_size)
        dic['page_size'] = len(data)
        dic['page'] = page
        dic['data'] = data
        total_page = math.ceil(len(self.dataset()) / page_size)
        dic['next_page'] = None if page >= total_page else page + 1
        dic['prev_page'] = None if page == 1 else page - 1
        dic['total_pages'] = total_page
        return dic
