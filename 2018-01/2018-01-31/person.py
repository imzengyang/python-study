
class Person:

    # username="xiaoming"
    # passwd="123456"
    # email="xiaoming@123.com"

    
    
    def __init__(self,username,passwd,email):
        self.username = username
        self.__passwd = passwd
        self.email = email


    def get_passwd(self):
        return self.__passwd
    
    def set_passwd(self,val):
        self.__passwd = val

    def register(self):
        print("user register ",self.username,self.__passwd,self.email)

    def login(self):
        print("user login",self.username,self.__passwd)

p= Person("xiaohong",'12345','1234@123.com')
p.login()
p.set_passwd("1231232131232321")
p.login()
