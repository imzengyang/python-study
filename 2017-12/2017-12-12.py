"""
python3 循环 while ....  for ....
"""


n=100
counter = 0
sum = 0
while counter < n:
    counter+=1
    sum+=counter
print("1 - %d 之和:%d"%(counter,sum))

# while True:
#     print("true...")


count = 0
while count<5:
    print("count",count)
    count+=1
    
else:
    print("count now is",count)




# list1 = [1,2,3,5]
# for x in list1:
#     if x == 2:
#         continue
#     print(x)


for x in range(1,9,2):
    print(x)




















"""
阿姆斯特朗数

如果一个n位正整数等于各位数字n次方的和,我们就称改数为阿姆斯特朗数.例如1^3 + 5^3 + 3^3 = 153, 那么153就为阿姆斯特朗数.

1000以内的阿姆斯特朗数有:1,2,3,4,5,6,7,8,9,153,370,371,407.

写一个程序,检测输入的数字是否为阿姆斯特朗数.
"""
