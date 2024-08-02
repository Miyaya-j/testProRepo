from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.zhihu.com//')

# 定位email和电话字段，并输入
email_field = driver.find_element(By.NAME, 'username')
email_field.send_keys('your_email_or_phone')
# 定位密码字段，并输入
password_field = driver.find_element_by_id('pass')
password_field.send_keys('your_password')
# 定位登录按钮，并点击
login_button = driver.find_element_by_id('loginbutton')
login_button.click()


'''
driver = webdriver.Chrome()
driver.get('https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/first_script/')
title = driver.title
print(title)
text_box = driver.find_element(by=By.ID, value="4-建立等待策略")
#submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
print(text_box.size,text_box)
'''
