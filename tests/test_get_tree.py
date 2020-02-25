import pytest
import sys
import pandas as pd
import json
sys.path.append('./source')
from get_tree import ConvertCsvToJson

class TestConvertCsvToJson:

    def __init__(self):
        self.max_depth = 0
        data = [['www.sample.com', 'category 1', "12", 'www.sample.com/category1',
                 'product 1', "15", 'www.sample.com/category1/product1'],
                ['www.sample.com', 'category 2', "13", 'www.sample.com/category1',
                 'product 3', "17", 'www.sample.com/category2/product3']]
        self.dataframe = pd.DataFrame(data, columns=['url', 'level 1 name', 'level 1 id', 'level 1 url',
                                                'level 2 name', 'level 2 id', 'level 2 url'])

    def test_create_tree(self):
        csv_object = ConvertCsvToJson(self.dataframe)
        out_tree = csv_object.create_tree()
        desired_output = '[{"label": "category 1", "id": "12", "link": "www.sample.com/category1", "children": [{"label": "product 1", "id": "15", "link": "www.sample.com/category1/product1", "children": []}]}, {"label": "category 2", "id": "13", "link": "www.sample.com/category1", "children": [{"label": "product 2", "id": "16", "link": "www.sample.com/category2/product2", "children": []}, {"label": "product 3", "id": "17", "link": "www.sample.com/category2/product3", "children": []}]}]'
        assert out_tree == desired_output