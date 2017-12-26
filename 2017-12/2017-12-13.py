"""
9 9 乘法表
展示如何打印 9 9 乘法表
"""
for x in range(1,10):
    for y in range(1,x+1):
        print('{}*{}={}\t'.format(y,x,x*y),end='')
    print()

i = -1
counter = 1
sum = 1
while counter < 100:
    i = (i**counter)/(counter+1)
    counter+=1
    sum = sum+i
    print(i,counter,sum)

print("at last: ",sum)

