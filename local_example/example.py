import sys
sys.path.append('./source')
from file_ops import Local
from get_tree import ConvertCsvToJson


data = Local().read_file("./local_example/data_file.csv")

csv_object = ConvertCsvToJson(data)
out_json = csv_object.create_tree()

print(out_json)