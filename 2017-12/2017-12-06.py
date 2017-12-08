'''
python3 字符串
'''
var1 = 'Hello World!'
var2 = "Runoob"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

var1 = 'Hello World!'
 
print ("已更新字符串 : ", var1[:6] + 'Runoob!')

# var1[:6] = "123456"

var1 = "abc"

print(var1*3)

print('5' in var1)

errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''

print(errHTML)


str = "abcddefg"
print(str.capitalize())

print(str.center(20, '_') )

print(str.count('d'))