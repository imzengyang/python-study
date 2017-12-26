"""
利用生成器 写入csv文件
"""

import csv

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b



with open('data.csv',mode='a',newline="") as f:
    w = csv.writer(f)
    for x in fibon(10000):
        w.writerow([str(x)])

    f.close()