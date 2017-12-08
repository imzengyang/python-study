"""
python 处理 csv 文件
"""

import os
import csv

# get csv file path
filepath = os.path.join(os.getcwd(),'data','userinfo.csv')

# open csv file

f = open(filepath) 

users = []
# parse csv
reader = csv.reader(f)
print(reader)
# delete the first row
next(reader,None)

# iterate
for row in reader:
    # print(row)
    users.append(row)

print(users)