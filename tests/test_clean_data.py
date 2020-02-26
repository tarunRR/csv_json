""" This file checks remove empty rows function """
import pandas as pd
from source.clean_data import Operations

def test_remove_empty_rows():
    """ This function tests if empty rows are being removed or not"""
    data = [['www.sample.com', 'category 1', "12", 'www.sample.com/category1',
             'product 1', "15", 'www.sample.com/category1/product1'],
            [],
            ['www.sample.com', 'category 2', "13", 'www.sample.com/category1',
             'product 3', "17", 'www.sample.com/category2/product3']]
    dataframe = pd.DataFrame(data, columns=['url', 'level 1 name', 'level 1 id', 'level 1 url',
                                            'level 2 name', 'level 2 id', 'level 2 url'])
    data = [['www.sample.com', 'category 1', "12", 'www.sample.com/category1',
             'product 1', "15", 'www.sample.com/category1/product1'],
            ['www.sample.com', 'category 2', "13", 'www.sample.com/category1',
             'product 3', "17", 'www.sample.com/category2/product3']]
    desired_output = pd.DataFrame(data, columns=['url', 'level 1 name',
                                                 'level 1 id', 'level 1 url',
                                                 'level 2 name', 'level 2 id', 'level 2 url'])
    csv_object = Operations(dataframe)
    data = csv_object.remove_empty_rows().reset_index(drop=True)
    pd.testing.assert_frame_equal(data, desired_output.reset_index(drop=True))
