
from commonTool.commonNowIT import loginNowITDashboad
import http.client
import random
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select


def closeCases(INum):

    driver = loginNowITDashboad()
    wait = WebDriverWait(driver, 20)
    time.sleep(10)

    # slector = (By.XPATH,'/html/body/macroponent-f51912f4c700201072b211d4d8c26010//div/sn-canvas-appshell-root/sn-canvas-appshell-layout/sn-polaris-layout//div[2]/div[2]/div[1]/sn-polaris-header//nav/div/div[3]/div[1]/div[1]/div/sn-search-input-wrapper//sn-component-workspace-global-search-typeahead//div/div/div/div/input')
    # a = driver.find_element(By.ID, 'sncwsgs-typeahead-input')
    a= driver.find_element(By.CLASS_NAME,'experience-title')

    time.sleep(10)
    # a.send_keys(INum)
    # time.sleep(10)
    # trlist = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'odd')))
    # slector =(By.ID, 'sncwsgs-typeahead-input')
    # searchinput1 = wait.until(EC.element_to_be_clickable((By.ID ,'sncwsgs-typeahead-input')))
    # searchinput1.send_keys(INum)

    slector2 = (By.CLASS_NAME, 'now-icon -md')
    searchbutton = wait.until(EC.visibility_of_element_located(slector2))
    searchbutton.click()

    slector3 = (By.ID ,'incident.close_code')
    ResolutionCode= wait.until(EC.visibility_of_element_located(slector3))
    select = Select(ResolutionCode)
    select.select_by_visible_text('Solved (Permanently)')

    slector4 =(By.ID, 'sys_display.incident.u_cause_service')
    CauseService = wait.until(EC.visibility_of_element_located(slector4))
    CauseService.send_keys('Siab')

    slector5 = (By.ID, 'incident.close_notes')
    ResolutionNotes = wait.until(EC.visibility_of_element_located(slector5))
    ResolutionNotes.send_keys('It is a temporary issue and now disappear')

    slector6 = (By.ID, 'sysverb_update_and_stay')
    saveButton = wait.until(EC.visibility_of_element_located(slector6))
    saveButton.click()


if __name__ == '__main__':
    closeCases('INC1003727763')
