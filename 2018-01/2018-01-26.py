from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver =  webdriver.Chrome()

driver.get("http://118.31.19.120:3000/signin")

driver.find_element_by_id('name').send_keys('helloworld')
driver.find_element_by_id('pass').send_keys('123456')


driver.find_element_by_class_name('span-primary').click()

driver.find_element_by_id('create_topic_btn').click()

driver.find_element_by_id('tab-value').click()

driver.find_element_by_css_selector('#tab-value > option:nth-child(3)').click()
driver.find_element_by_id('title').send_keys('1234567890')

# 写入文本

# driver.find_element_by_css_selector('#create_topic_form > fieldset > div > div > div.CodeMirror.cm-s-paper > div.CodeMirror-scroll').send_keys('123213213123123123123123123123')
contentInput= driver.find_element_by_css_selector('#create_topic_form > fieldset > div > div > div.CodeMirror.cm-s-paper > div.CodeMirror-scroll')
ActionChains(driver).move_to_element(contentInput).click().perform()
contentArea = driver.find_element_by_css_selector('#create_topic_form > fieldset > div > div > div.CodeMirror.cm-s-paper > div.CodeMirror-scroll > div.CodeMirror-sizer > div > div > div > div.CodeMirror-code')
ActionChains(driver).move_to_element(contentArea).send_keys('1231231231232312412412').perform()