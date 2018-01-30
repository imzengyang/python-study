

# class Myclass:
#     i = 1234
#     def f(self):
#         print(self.i)


# my = Myclass()
# my.f()

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://118.31.19.120:3000/signin')

class LoginPage:

    username_id = "name"
    passwd_id = "pass"
    login_btn_className = "span-primary"

    def user_logind(self,username,passwd):
        driver.find_element_by_id(self.username_id).send_keys(username)
        driver.find_element_by_id(self.passwd_id).send_keys(passwd)
        driver.find_element_by_class_name(self.login_btn_className).click()


login = LoginPage()
login.user_logind('helloworld','123456')
