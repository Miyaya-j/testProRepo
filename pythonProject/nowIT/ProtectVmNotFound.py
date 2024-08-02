import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pvmnf():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://now.ingka.com/now/nav/ui/classic/params/target/%24pa_dashboard.do')
    # time.sleep(200)

    input = driver.find_element(By.XPATH, '//input[@id="username"]')
    input.send_keys('miya.peng2@ingka.com')
    driver.find_element(By.NAME, 'action').click()
    time.sleep(20)
    # 等待页面元素全部加载出来，时间为5秒
    # driver.implicitly_wait(20)
    # 期望检查某个元素是否出现在页面的DOM中且可见。可见性意味着元素不仅被显示，而且其高度和宽度都大于0。
    # locator = (By.XPATH, "//a[text()='INC1003722337']")
    # ele = WebDriverWait(driver, 100).until(EC.visibility_of_element_located(locator))
    # ele.click()
    # driver.find_element(By.XPATH, "//a[text()='INC1003722337']").click()

    print("======================")
    a = WebDriverWait(driver, 30,0.5).until(
        EC.presence_of_element_located((By.LINK_TEXT,'INC1003721491')))
    print("--------------------------")
    a.click()
    print("]]]]]]]]]]]]]]]]]]]]]]]]]]")

    # time.sleep(2)
    # locator2 = (By.XPATH, "//*[contains(text(), 'Protected VM(s) Not Found')]")
    # ele2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator2))

    # driver.find_element(By.XPATH, "//input[@id='sys_display.incident.assigned_to']")
    # 通过文本定位任意元素
    b = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Protected VM(s) Not Found')]")))
    if b:
        ele = driver.find_element(By.XPATH, '//textarea[@id="incident.description"]')
        print("----------------")
        print(ele.text)
    print('!!!!!!!!!!!!!!!!!!!!!!!!')
    time.sleep(50)
if __name__ == '__main__':
    pvmnf()




