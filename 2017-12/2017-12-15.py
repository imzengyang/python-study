"""
斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,
特别指出：第0项是0，第1项是第一个1。
从第三项开始，每一项都等于前两项之和。
"""

# num = int(input("请输入你要获得的数列个数: "))

# n1 = 0
# n2 = 1

# counter = 2

# if num < 0:
#     print("输入值不合法")
# elif num == 1:
#     print(n1)
# else:
#     print("斐波那契数列:")
#     print(n1,",",n2,end=' , ')
#     while num > counter:
#         nth = n1+n2
#         print(nth,end=' , ')
#         n1 = n2
#         n2 = nth
#         counter+=1

"""
next 去解决阿姆斯特朗数
"""
import sys

num = int(input('input a num > 0 : '))

if num < 0:
    print("num cant < 0")

n = len(str(num))

list = list(str(num))

it = iter(list)
sum = 0
while True:
    try:
        sum+=int(next(it))**n
    except StopIteration as identifier:
        if num == sum:
            print("num %d is 阿姆斯特朗数"%num)
        else:
            print("num %d is not 阿姆斯特朗数"%num)
        sys.exit()