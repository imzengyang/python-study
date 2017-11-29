"""
字符串的操作
"""

name = 'xiaoming'
address = "china"
age = 18
money = 100.1021

print(name,address)

print(name+" "+address)


#作业 修改下面语句 能够打印出来  my name is xiaoming, i live in china. i am 18 years old, i hava 100.1021 money
print("my name is %s, i live in %s. i am %d years old, i hava %d money "%(name,address,age,money))

print("my name is %s, i live in %s. i am %d years old, i hava %f money "%(name,address,age,money))

print(name * 2)




