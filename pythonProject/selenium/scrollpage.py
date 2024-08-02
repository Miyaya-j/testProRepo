import random
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get('https://www.baidu.com')


# wait = WebDriverWait(driver, 3)
# wait.until(EC.presence_of_all_elements_located())
driver.set_window_size(700,900)
driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('webdriver api')
driver.find_element(By.XPATH,'//*[@id="su"]').click()
driver.find_element(By.XPATH,'//*[@id="kw"]').clear()

title = WebDriverWait(driver, 5).until(EC.title_is('百度一下，你就知道'))
print(f'title标题：真是True, 假是False. 结果：{title}')

result = EC.title_contains('一下下')
print(result)

url = WebDriverWait(driver, 5).until(EC.url_to_be('https://www.baidu.com/'))
print(f'url网址：真是True, 假是False. 结果：{url}')

# 存在非可见
# presence_of_element_located()
# 检查元素是否出现在页面的DOM上的期望。 这并不一定意味着元素是可见的。
locator = (By.XPATH, '//input[@id="alert"]')
ele = WebDriverWait(driver, 3).until(EC.presence_of_element_located(locator))


# 存在且可见
# visibility_of_element_located ()
# 期望检查某个元素是否出现在页面的DOM中且可见。可见性意味着元素不仅被显示，而且其高度和宽度都大于0。
locator = (By.XPATH, '//input[@id="alert"]')
ele = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locator))
ele.click()
# # 移动到页面最底部
# driver.execute_script('window.scrollTo(0, 700)')
#
# # 移动到指定的坐标(相对当前的坐标移动)
# driver.execute_script('window.scrollBy(0, 1400)')
# # 结合上面的scrollBy语句，相当于移动到700+800=1600像素位置
# driver.execute_script('window.scrollBy(0, 1600)')
#
# # 移动到窗口绝对位置坐标，如下移动到纵坐标1600像素位置
# driver.execute_script('window.scrollTo(0, 2600)')
# # 结合上面的scrollTo语句，仍然移动到纵坐标1200像素位置
# driver.execute_script('window.scrollTo(0, 6300)')

# for i in range(1, 9):
#     time.sleep(random.randint(100, 300) / 1000)
#     driver.execute_script('window.scrollTo(0,{})'.format(i * 700))  # scrollTo 不叠加 700 1400 2100
#
# 通过js新打开一个窗口
# driver.execute_script('window.open("http://google.com");')

# driver.get('https://www.douban.com/')
# login_iframe = driver.find_element(By.XPATH,'//div[@class="login"]/iframe')
# driver.switch_to.frame(login_iframe)
# time.sleep(2)
# # driver.find_element(By.CLASS_NAME,'account-tab-phone on').click()
# driver.find_element(By.XPATH,"//input[@name='phone']").send_keys('13094507659')
# driver.find_element(By.CLASS_NAME,'account-form-field-code ').click()
# time.sleep(15)
# driver.find_element(By.CLASS_NAME,'btn btn-phone ').click()



# url = 'https://pic.netbian.com/4kmeinv/index.html'
# driver.get(url)
# src = driver.find_elements(By.XPATH,'//img')
# for i in src:
#     url = i.get_attribute('src')
#     print(url)


# wait = WebDriverWait(driver, 10)
# input = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
# button = wait.until(EC.element_to_be_clickable((By.ID, 'su')))
# print(input,'----------------------------', button)


time.sleep(3000)

