"""
迭代器
"""


list = [1,2,3,4]
print(list)

for x in list:
    print(x)

b = iter(list)

print(b)
print(next(b))
next(b)

for x in b:
    print("b==",x)
