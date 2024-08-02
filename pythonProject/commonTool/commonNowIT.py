import random
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class commonNowIT:
    def loginNowITDashboad(username):
        pass



def loginNowITDashboad():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://now.ingka.com/now/nav/ui/classic/params/target/%24pa_dashboard.do')
    # time.sleep(200)

    input = driver.find_element(By.XPATH, '//input[@id="username"]')
    username = 'miya.peng2@ingka.com'
    input.send_keys(username)
    driver.find_element(By.NAME, 'action').click()
    return driver

