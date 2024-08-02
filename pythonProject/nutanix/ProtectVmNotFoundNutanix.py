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


# 拿到incident涉及信息-----nowIT

'''
done
INum ='INC1003719412'
shortDescreption = "RETDE343-NXC000#Protection domain RETDE343-NXC000-Gold_CCG replication failed"
descriptionTime = "retde343-nxc000 has severity Medium since Wed Jul 17 02:39:08 2024 UTC"
description = "Protection domain RETDE343-NXC000-Gold_CCG replication to remote site RS_RETDE223-NXC000 failed. Target site does not have enough space available'"
mainCluster = 'RETDE343-NXC000'
'''




'''
dp正常，alert还在
unhealthy decommission or creation process
INum ='INC1003723230'
shortDescreption = "RETAUC01-NXC000#Latest snapshot of protection domain is missing entities"
descriptionTime = "retde343-nxc000 has severity Medium since Wed Jul 17 02:39:08 2024 UTC"
description = "Latest snapshot of protection domain RETAUSO-NXC000-Gold_CCG is missing entities RETAU555-LX2000"
mainCluster = 'RETAUC01-NXC000'
'''


# autoresolve,alert无，但是有很多页加载不了
INum ='INC1003720673'
shortDescreption = "retusphi-nxp001#PE-PC Connection Failure"
descriptionTime = "retusphi-nxp001 has severity Medium since Wed Jul 17 07:39:11 2024 UTC"
description = "The remote PE 10.26.158.203 is unreachable"
mainCluster = 'retusphi-nxp001'



'''
INum='INC1003727763'
shortDescreption = "RETUS257-NXC000#Protected VM(s) Not Found"
descriptionTime = "retus257-nxc000 has severity Medium since Fri Jul 19 07:24:09 2024 UTC"
description = "Unable to locate VM(s) RETUS727-LX4020 protected by protection domain 'RETUS257-NXC000-Gold_CCG'"
mainCluster = 'retus257-nxc000'
'''







#拿到所有cluster名字和对应uuid------nutanix

shortDescreptionLength = len(shortDescreption)
indexf = shortDescreption.find('#',0,shortDescreptionLength)
print(indexf,shortDescreption[0:indexf])
nutanixCluster = shortDescreption[0:indexf]

driver = webdriver.Edge()
driver.maximize_window()
ClusterUrl = '%s'%nutanixCluster
ClusterUrl = 'https://'+ClusterUrl+'.ikea.com:9440'
print(ClusterUrl)
options = webdriver.EdgeOptions()
options.add_experimental_option('detach', True)
# driver.get(ClusterUrl)

AlertUrl = ClusterUrl+'/console/#page/alert_explorer'
driver.get(AlertUrl)

wait = WebDriverWait(driver, 15)
input1 = wait.until(EC.element_to_be_clickable((By.ID,'inputUsername')))
input1.send_keys('gstmipen20@ikea.com')
input2 = wait.until(EC.element_to_be_clickable((By.ID,'inputPassword')))
input2.send_keys('PN?*Rh2*L?9zn!I30VoJ8?9t!rzD2#h2',Keys.ENTER)
print("-----------------")
time.sleep(5)

wait = WebDriverWait(driver, 30)
sele =(By.XPATH,'//div[@class="filter-box" and @title="Severity = Critical"]/div[@class="close-btn"]')
# sele =(By.XPATH,'//div[@class="filter-box" and @title="Severity = Critical"]/div[@class="close-btn"]')
CHACHA = wait.until(EC.visibility_of_element_located(sele))
CHACHA.click()
# driver.find_element(By.XPATH,'//div[@class="filter-box" and @title="Severity = Warning"]/div[@class="close-btn"]').click()
time.sleep(2)

summary = driver.find_element(By.XPATH,'//div[@class="description"]')
des = summary.text
desNumS = des[8:9]
# desNum =int(desNumS)
desNum =2919
if desNum != 0:
    wait = WebDriverWait(driver, 30)
    trlist = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'odd')))
    if desNum != 1:
        trlist2 = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME,'even')))
        trlist3 = trlist + trlist2
    else:
        trlist3 = trlist
    print("=========================================")
    print(len(trlist3))
    flag = 0
    for tr in trlist3:
        # 获取tr中的所有td
        # tdlist = tr.find_elements(By.TAG_NAME, "td")
        # 获取td[0]的文本
        text = tr.find_elements(By.TAG_NAME, "td")[1].text
        trState = tr.find_elements(By.TAG_NAME, "td")[5].text
        trTime = tr.find_elements(By.TAG_NAME, "td")[7].text
        # 当td[0]的内容为小李时，获取当前tr的id属性
        if text in shortDescreption and trState == '-':
            flag = 1
            print(text)
            print(INum + mainCluster + 'still not be resolved,now need to evaluate')
            break
        else:
            continue
    if flag == 0:
        print(INum + mainCluster + 'resolved,now need to close case')
else:
    print(INum + mainCluster + 'resolved,now need to close case')
#获取所有的tr
# trlist=driver.find_element(By.CLASS_NAME,'odd')
# trlist=driver.find_element(By.TAG_NAME,'tr')

# if trlist:
#     flag =0
#     for tr in trlist3:
#         #获取tr中的所有td
#         tdlist=tr.find_elements(By.TAG_NAME,"td")
#         # 获取td[0]的文本
#         text = tr.find_elements(By.TAG_NAME,"td")[1].text
#         trState = tr.find_elements(By.TAG_NAME,"td")[5].text
#         trTime = tr.find_elements(By.TAG_NAME,"td")[7].text
#         # 当td[0]的内容为小李时，获取当前tr的id属性
#         if text in shortDescreption3 and trState == '-':
#             flag=1
#             print(text)
#             print(INum3+mainCluster3+'still not be resolved,now need to evaluate')
#             break
#         else:
#             continue
#     if flag == 0:
#         print(INum3+mainCluster3 + 'resolved,now need to close case')
# else:
#     print(INum3+mainCluster3+'resolved,now need to close case')
#xpath=".//*[@id='"+trid+"']/td[9]/div/a[2]/i"
#brower.find_element_by_xpath(xpath).click()
#td_tags = soup.select('tr td')
# for i in range(0, len(td_tags), 2):
# school_name = td_tags[i].get_text()
# address = td_tags[i + 1].get_text()
# score = td_tags[i + 2].get_text()
# time.sleep(0.1)
# print(f'正在爬取：--{school_name}--{address}--')




#对定位到的元素执行鼠标双击操作
# ActionChains(driver).click(input3).perform()

time.sleep(1000)





#找到incident对应cluster的uuid，登录对应alert------selenium
a = 'https://ssp-na-ntx.ikea.com:9440/console/#page/alert_explorer/?clusterid=0005f3a7-f9e4-328c-3504-84160c496298'

#点击clear------selenium

#找到对应incident check 解决状态------selenium


#已解决，打印已解决
#未解决打印未解决

if __name__ == '__main__':
    pass