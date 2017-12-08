"""
python 字典
"""

student=['xiaohong','xiaoming','xiaozhang','xiaoli']
numbers=[1001,1002,1003,1004]

print('xiaoming number: ',numbers[student.index('xiaoming')])

students = { '1001':'xiaoming','1002':'xiaohong','1003':'xiaoming' }

print(students['1003'])

dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258','Alice':'4321'}

print(dict['Alice'])

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8;  
print(dict['Age'])

# dict.clear()     # 删除字典
# del dict
print(dict)

print(dict.copy())
print(dict)
print(dict.fromkeys('Name'))


