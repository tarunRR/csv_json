
"""
Description: Convert csv data with hierarchy to a json hieraarchy tree
"""

import json
from itertools import repeat



class ConvertCsvToJson:
    """
    Instantiate this class to convert CSV data to json tree
    """
    def __init__(self, data):
        """
        Initializes the object.
        """
        self.max_depth = 0
        self.data_to_use = data

    def create_tree(self):
        """
        - Finds out depth of tree
        - Calls the create nodes function to create all the nodes to be pushed into tree
        """
        self.max_depth = int(len(self.data_to_use.columns) / 3)
        return json.dumps(self.add_nodes(0, self.data_to_use))

    def add_nodes(self, level, data):
        """
        - Creates an empty tree and push nodes to the tree
        - Calls create_node function to create nodes
        :parameters:
            level - level of node to be pushed
            data - filtered data of the node to be pused
        """
        if level < self.max_depth:
            return list(filter(None.__ne__, list(map(self.create_nodes,
            	                                 data.iloc[:, (3*(level+1))-1].unique(),
                                                     repeat(level), repeat(data)))))
        else:
            return []

    def create_nodes(self, level_id, level, data):
        """from csv_to_
        Creates nodes to be pushed into the tree
        :parameters:
            level_id - id of current node to be created
            level - level of node to be created
            data - filtered data for note t create
        """
        data = data[data.iloc[:, 3*(level)+2] == level_id]
        if data.empty:
            return None
        return {"label":data.iloc[:, 3*(level)+1].iloc[0].strip(),
        	"id":str(level_id).strip(),
        	"link":data.iloc[:, 3*(level+1)].iloc[0].strip(),
        	"children":self.add_nodes((level+1), data)}
