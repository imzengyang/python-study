"""
生成器
"""
# def genarator_func():
#     for i in range(10):
#         yield i

# for x in genarator_func():
#     print(x)

# def fibon(n):
#     a = b = 1
#     result = []
#     for i in range(n):
#         result.append(a)
#         a, b = b, a + b
#     return result

# print(fibon(10000000000))

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fibon(10000000000):
    print(x)