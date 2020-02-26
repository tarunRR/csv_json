"""This file tests the create_tree function """
import json
import pandas as pd
from source.get_tree import ConvertCsvToJson

class TestConvertCsvToJson:
    """ Tests the crete tree function which converts the pandas dataframe to json"""

    def test_create_tree(self):
        """ create tree from dataframe and compares it with predefined output """
        data = [['www.sample.com', 'category 1', "12", 'www.sample.com/category1',
                 'product 1', "15", 'www.sample.com/category1/product1'],
                ['www.sample.com', 'category 2', "13", 'www.sample.com/category1',
                 'product 3', "17", 'www.sample.com/category2/product3']]
        dataframe = pd.DataFrame(data, columns=['url', 'level 1 name',
                                                'level 1 id', 'level 1 url',
                                                'level 2 name', 'level 2 id',
                                                'level 2 url'])
        csv_object = ConvertCsvToJson(dataframe)
        out_tree = csv_object.create_tree()
        with open('tests/output.json') as json_file:
            out_data = json.load(json_file)
        assert out_tree == out_data
