.. contents:: :local:

Introduction
==============

This project is for converting CSV to nested JSON. The CSV have a hierarchical structure. The code reads in the CSV file and runs a recursion function to remove whitespaces from each level and add them as a node in the json tree. The code can be used to convert any level of hierarchy to a nested json tree

It works on Windows, OSX and Linux platforms with Python 3.x versions.

Orignal author: Tarun Kumar Singh
Maintainer: Tarun Kumar Singh

`Support and issues on Github <https://github.com/tarunRR/csv_to_json>`_.


Usage
=====

* Install requirements using 

  * pip install requirements.txt*

* Configure your aws credentials using command

  *aws configure*

    AWS Access Key ID [None]: *your_key*

    AWS Secret Access Key [None]: *secret key*

    Default region name [None]: *region*

    Default output format [None]: json

* For aws run, from csv_to_json directory run the main.py file in source folder using command

  *python .source/main.py

* You can also pass access_key and secret key as parameters to main file

  *python ./source/main.py --access_key *your_key* --secret_key *secret key* *

Local Run
=========

* For local run, from csv_to_json directory run the example.py file in local_example folder using command

  *python ./local_example/example.py*

* If you want to run the code in your python console use the following lines

  *import sys*

  *sys.path.append(*path to source folder*)*

  *from file_ops import Local*

  *from get_tree import ConvertCsvToJson*

  *data = Local().read_file(*path to data file*)*

  *csv_object = ConvertCsvToJson(data)*

  *out_json = csv_object.create_tree()*

  *print(out_json)*



AWS Connections
===============

* The code is integrated to AWS Elastic Beanstalk. The code reads CSV file from S3 (Simple Storage Services) buckets. After the conversion of CSV to nested json , it writes it back to S3. Also, it checks whether the CSV has the desired format of Parent and Child levels.

* All the S3 and Elastic Beanstalk related info are present in config file and and loaded from there

* The code is also integrated to a jenkins task which runs test cases on the build pushed and push it again to ealstic beanstalk



Sample Input
============

```
Base URL,Level 1 - Name,Level 1 - ID,Level 1 - URL,Level 2 - Name,Level 2 - ID,Level 2 - URL,Level 3 - Name,Level 3 - ID,Level 3 - URL,Level 4 - Name,Level 4 - ID,Level 4 - URL
https://groceries.morrisons.com/browse,THE BEST,178974,https://groceries.morrisons.com/browse/178974,,,,,,,,,
,,,,,,,,,
https://groceries.morrisons.com/browse,THE BEST,178974,https://groceries.morrisons.com/browse/178974,FRESH,178969,https://groceries.morrisons.com/browse/178974/178969,,,,,,
,,,,,,,,,
https://groceries.morrisons.com/browse,THE BEST,178974,https://groceries.morrisons.com/browse/178974,BAKERY & CAKES,178971,https://groceries.morrisons.com/browse/178974/178971,,,,,,
https://groceries.morrisons.com/browse,THE BEST,178974,https://groceries.morrisons.com/browse/178974,BAKERY & CAKES,178971,https://groceries.morrisons.com/browse/178974/178971,BREAD & BREAD ROLLS,179023,https://groceries.morrisons.com/browse/178974/178971/179023,,,
https://groceries.morrisons.com/browse,THE BEST,178974,https://groceries.morrisons.com/browse/178974,BAKERY & CAKES,178971,https://groceries.morrisons.com/browse/178974/178971,"CAKES, PIES & TARTS",179024,https://groceries.morrisons.com/browse/178974/178971/179024,,,
https://groceries.morrisons.com/browse,THE BEST,178974,https://groceries.morrisons.com/browse/178974,BAKERY & CAKES,178971,https://groceries.morrisons.com/browse/178974/178971,CROISSANTS & BREAKFAST BAKERY,179025,https://groceries.morrisons.com/browse/178974/178971/179025,,,
https://groceries.morrisons.com/browse,THE BEST,178974,https://groceries.morrisons.com/browse/178974,BAKERY & CAKES,178971,https://groceries.morrisons.com/browse/178974/178971,DESSERTS & PUDDINGS,179026,https://groceries.morrisons.com/browse/178974/178971/179026,,,
https://groceries.morrisons.com/browse,THE BEST,178974,https://groceries.morrisons.com/browse/178974,BAKERY & CAKES,178971,https://groceries.morrisons.com/browse/178974/178971,"FRUITED BREAD, SCONES & HOT CROSS BUNS",179027,https://groceries.morrisons.com/browse/178974/178971/179027,,,
,,,,,,,,,
https://groceries.morrisons.com/browse,THE BEST,178974,https://groceries.morrisons.com/browse/178974,BAKERY & CAKES,178971,https://groceries.morrisons.com/browse/178974/178971,BREAD & BREAD ROLLS,179023,https://groceries.morrisons.com/browse/178974/178971/179023,BREAD,179078,https://groceries.morrisons.com/browse/178974/178971/179023/179078
https://groceries.morrisons.com/browse,THE BEST,178974,https://groceries.morrisons.com/browse/178974,BAKERY & CAKES,178971,https://groceries.morrisons.com/browse/178974/178971,"CAKES, PIES & TARTS",179024,https://groceries.morrisons.com/browse/178974/178971/179024,CAKES,179079,https://groceries.morrisons.com/browse/178974/178971/179024/179079
```

Sample Output
==============

```
[
  {
    "label": "THE BEST",
    "id": "178974",
    "link": "https://groceries.morrisons.com/browse/178974",
    "children": [
      {
        "label": "FRESH",
        "id": "178969",
        "link": "https://groceries.morrisons.com/browse/178974/178969",
        "children": []
      },
      {
        "label": "BAKERY & CAKES",
        "id": "178971",
        "link": "https://groceries.morrisons.com/browse/178974/178971",
        "children": [
          {
            "label": "BREAD & BREAD ROLLS",
            "id": "179023",
            "link": "https://groceries.morrisons.com/browse/178974/178971/179023",
            "children": [
              {
                "label": "BREAD",
                "id": "179078",
                "link": "https://groceries.morrisons.com/browse/178974/178971/179023/179078",
                "children": []
              }
            ]
          },
          {
            "label": "CAKES, PIES & TARTS",
            "id": "179024",
            "link": "https://groceries.morrisons.com/browse/178974/178971/179024",
            "children": [
              {
                "label": "CAKES",
                "id": "179079",
                "link": "https://groceries.morrisons.com/browse/178974/178971/179024/179079",
                "children": []
              }
            ]
          },
          {
            "label": "CROISSANTS & BREAKFAST BAKERY",
            "id": "179025",
            "link": "https://groceries.morrisons.com/browse/178974/178971/179025",
            "children": []
          },
          {
            "label": "DESSERTS & PUDDINGS",
            "id": "179026",
            "link": "https://groceries.morrisons.com/browse/178974/178971/179026",
            "children": []
          },
          {
            "label": "FRUITED BREAD, SCONES & HOT CROSS BUNS",
            "id": "179027",
            "link": "https://groceries.morrisons.com/browse/178974/178971/179027",
            "children": []
          },
          {
            "label": "BREAD & BREAD ROLLS",
            "id": "179023",
            "link": "https://groceries.morrisons.com/browse/178974/178971/179023",
            "children": [
              {
                "label": "BREAD",
                "id": "179078",
                "link": "https://groceries.morrisons.com/browse/178974/178971/179023/179078",
                "children": []
              }
            ]
          },
          {
            "label": "CAKES, PIES & TARTS",
            "id": "179024",
            "link": "https://groceries.morrisons.com/browse/178974/178971/179024",
            "children": [
              {
                "label": "CAKES",
                "id": "179079",
                "link": "https://groceries.morrisons.com/browse/178974/178971/179024/179079",
                "children": []
              }
            ]
          }
        ]
      }
    ]
  }
]

```