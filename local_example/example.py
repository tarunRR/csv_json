import sys
sys.path.append('./')
from source.file_ops import Local
from source.get_tree import ConvertCsvToJson


data = Local().read_file("./local_example/data_file.csv")

csv_object = ConvertCsvToJson(data)
out_json = csv_object.create_tree()

print(out_json)