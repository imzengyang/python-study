"""
python3 list 列表
"""



list1 = ['Google', 'Runoob', 1997, 2000]

print(list1,list1[0],list1[1:])

list1[0] = 1
list1[1:] = ['a','b','c']
print(list1)
# list1[4] = "abcdefg"

del list1[0]
print(list1)

a = ['a', 'b', 'c']
b = [1,2,3]
x = [a,b]
print(x,len(x),x[0],x[0][1])




a = list("我爱学习")

a[1:] = "超级爱学习"
print(a)



'''
作业

'''
# max(list) 返回列表元素最大值

# list = [1,2,3,4,5]

# list = [[1,2,3],[4,5,6]]

# list = ["a",1,2,3]

# min(list) 返回列表元素最小值

# list = [1,2,3,4,5]

# list = [[1,2,3],[4,5,6]]

# list = ["a",1,2,3]


list = ["study","make","me","happy","i","love","study"]
obj = ["真","的","吗","?"]

# list.append(obj)
print(list)

print(list.count('study'))

#	list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
#	list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
#	list.insert(index, obj) 将对象插入列表
#	list.pop(obj=list[-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
#	list.remove(obj) 移除列表中某个值的第一个匹配项
#	list.reverse() 反向列表中元素
#	list.sort([func]) 对原列表进行排序
#	list.clear() 清空列表
# 	list.copy() 复制列表



