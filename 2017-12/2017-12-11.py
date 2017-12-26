'''
if 条件控制语句
'''


var1 = 100
if var1:
    print("100 is True")
else:
    print('100 is False')

var2 = 0
if var2:
    print('0 is Ture')
else:
    print('0 is False')


season = int(input("月份:"))
if season > 0 and season <=3:
    print(" 春季")
elif season > 3 and season <=6 :
    print('夏季')
elif season >6 and season <=9:
    print('秋季')
elif season > 9 and season <=12:
    print('冬季')
else:
    print('无效的值')