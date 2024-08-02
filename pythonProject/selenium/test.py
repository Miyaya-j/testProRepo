import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# ---------------Chrome浏览器
browser = webdriver.Edge()
# browser.implicitly_wait(30)  # 隐性等待，最长等30秒
# ---------------设置浏览器大小：全屏
browser.maximize_window()
# 设置分辨率 500*500
# browser.set_window_size(500, 500)

browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
browser.switch_to.window(browser.window_handles[1])
time.sleep(2)

browser.get('https://www.baidu.com')
browser.switch_to.window(browser.window_handles[0])
#---------------browser.get
browser.get('https://google.com/')
# -----------------time.sleep(1)



# 打开bilibli页面
#browser.get('https://www.bilibili.com/')
# time.sleep(1)

# --------------------后退到谷歌页面
#browser.back()
#time.sleep(20)


'''
# -------------------前进的blbl页面
browser.forward()
time.sleep(2)
# 网页标题
print(browser.title)
# 当前网址
print(browser.current_url)
# 浏览器名称
print(browser.name)
# 网页源码
print(browser.page_source)
# 关闭浏览器
'''

# ----------------ID获取输入框，输入selenium
browser.find_element(By.ID,'APjFqb').send_keys('neymar')


#-----------------  xpath使用相对路径id定位 -- driver.find_element_by_xpath('//input[@id="kw"]')
# browser.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys(Keys.ENTER)
# browser.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys('neymar')
# ------------------xpath使用绝对路径
# browser.find_element(By.XPATH,"/html/body/div/div/form/div/div/div/div/div/textarea").send_keys('neymar')

#--------------class定位by class name
#browser.find_element(By.CLASS_NAME, 'gLFyf')

#--------------tag定位by tag name
#browser.find_element(By.TAG_NAME,'textarea')
# time.sleep(4)

#------ -------------xpath使用相对路径name定位
# browser.find_element(By.XPATH,"//*[@name='btnK']").click()
# browser.find_element(By.NAME,'btnK').click()

#------------------------submit
# inquiry = browser.find_element(By.XPATH,"//*[@name='btnK']")
# inquiry.submit()

#----------------键盘事件
#Keys.ENTER通过定位密码框，enter（回车）来代替登陆按钮
# browser.find_element(By.ID,'APjFqb').send_keys(Keys.ENTER)
#也可定位登陆按钮，通过 enter（回车）代替 click()
# browser.find_element(By.XPATH,"//*[@name='btnK']").send_keys(Keys.ENTER)
##ctrl+x 剪切输入框内容
browser.find_element(By.ID,'APjFqb').send_keys(Keys.CONTROL,'a')
browser.find_element(By.ID,'APjFqb').send_keys('特朗普',Keys.ENTER)

#------鼠标双击事件
from selenium.webdriver.common.action_chains import ActionChains
#定位到要双击的元素
qq=browser.find_element(By.ID,'APjFqb')
#对定位到的元素执行鼠标双击操作
ActionChains(browser).double_click(qq).perform()




time.sleep(5)
browser.minimize_window()

# 退出浏览器
# browser.quit()



