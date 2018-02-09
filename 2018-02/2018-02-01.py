
class Animal(object):

    name = "animal"
    __pass = "1234"
    def run(self):
        print('running.....')
    
    def __info(slef):
        print('this private info')


class Dog(Animal):

    def speak(self):
        print('dog....')


class Cat(Animal):

    def speak(self):
        print('cat.....')

# d = Dog()
# d.run()
# print(d.name)
# d.speak()
# # d.__info()
# d.__pass


# c = Cat()
# c.run()
# print(d.name)



class Person(object):

    user='1234'
    
    def __init__(self,username,passwd):
        self.username = username
        self.passwd = passwd

    @property
    def userinfo(self):
        print(self.username,self.passwd)
    
    @staticmethod
    def uinfo():
        print(Person.user)
    
p = Person('zack','123445')
p.userinfo

Person.uinfo()