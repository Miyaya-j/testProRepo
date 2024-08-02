import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Chrome浏览器
browser = webdriver.Edge()

# 设置浏览器大小：全屏
browser.maximize_window()
browser.get('file:///C:/my/pypro/pythonProject/selenium/testSelenium.html')


browser.find_element(By.XPATH, "//button[text()='登录3']").click()
time.sleep(5)
from selenium.webdriver.common.action_chains import ActionChains
#定位元素的原位置
# element = browser.find_element(By.XPATH, "//button[text()='登录2']")
# #定位元素要移动到的目标位置
# target = browser.find_element(By.XPATH, "//button[text()='登录4']")
# #执行元素的移动操作
# ActionChains(browser).drag_and_drop(element, target).perform()
# time.sleep(50)


#首先需要切换到弹出框中，获取Alert对象。
alert = browser.switch_to.alert
#获取弹窗文本内容
alert.text
#点击确定按钮
alert.accept()
#点击取消按钮
# alert.dismiss()

cars = browser.find_element(By.ID,'cars')
se = Select(cars)
se.select_by_visible_text('比亚迪')
se.select_by_index(0)
se.select_by_value('bc')
se.deselect_by_value('bc')



time.sleep(10)



