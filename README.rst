.. contents:: :local:

Introduction
==============

This project is for converting CSV to nested JSON. The CSV have a hierarchical structure. The code reads in the CSV file and runs a recursion function to remove whitespaces from each level and add them as a node in the json tree. The code can be used to convert any level of hierarchy to a nested json tree

It works on Windows, OSX and Linux platforms with Python 3.x versions.

Orignal author: Tarun Kumar Singh
Maintainer: Tarun Kumar Singh

`Support and issues on Github <https://github.com/tarunRR/csv_json>`_.


Usage
=====

* Install requirements using 

  * pip install requirements.txt *

* Configure your aws credentials using command

  * aws configure *

    AWS Access Key ID [None]: <your_key>

    AWS Secret Access Key [None]: <secret key>

    Default region name [None]: <region>

    Default output format [None]: json

* For aws run, from csv_json directory run the main.py file in source folder using command

  * python source/main.py *

* You can also pass access_key and secret key as parameters to main file

  * python source/main.py --access_key <your_key> --secret_key <secret key> *

Local Run
=========

* For local run, from csv_json directory run the example.py file in local_example folder using command

  * python local_example/example.py *

* If you want to run the code in your python console use the following lines

  * import sys *

  * sys.path.append(<path to source folder>) *

  * from source.file_ops import Local *

  * from source.get_tree import ConvertCsvToJson *

  * data = Local().read_file(<path to data file>) *

  * csv_object = ConvertCsvToJson(data) *

  * out_json = csv_object.create_tree() *

  * print(out_json) *

Test Cases Run
==============

* Create virtual environment

* From csv_json directory use the following command to run test cases

    * python -m pytest tests/ *
    


AWS Connections
===============

* The code is integrated to AWS Elastic Beanstalk. The code reads CSV file from S3 (Simple Storage Services) buckets. After the conversion of CSV to nested json , it writes it back to S3. Also, it checks whether the CSV has the desired format of Parent and Child levels.

* All the S3 and Elastic Beanstalk related info are present in config file and and loaded from there

* The code is also integrated to a jenkins task which runs test cases on the build pushed and push it again to ealstic beanstalk



Sample Input
============

```
'url'            'level 1 name' 'level 1 id' 'level 1 url'              'level 2 name' 'level 2 id' 'level 2 url'])
'www.sample.com' 'category 1'    12          'www.sample.com/category1' 'product 1'    15           'www.sample.com/category1/product1'
'www.sample.com' 'category 2'    13          'www.sample.com/category2' 'product 3'    17           'www.sample.com/category2/product3'
```

Sample Output
==============

```
"[{"label": "category 1", "id": "12", "link": "www.sample.com/category1", 

   "children": [{"label": "product 1", "id": "15", "link": "www.sample.com/category1/product1", "children": []}]}, 

{"label": "category 2", "id": "13", "link": "www.sample.com/category2", 
  
   "children": [{"label": "product 3", "id": "17", "link": "www.sample.com/category2/product3", "children": []}]}]"

```