from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os, shutil, time

url = "https://airasia.smartkargo.com/loginframe.aspx"
browser = webdriver.PhantomJS()
browser.get(url)

browser.find_element_by_name("txtUserName").send_keys('1024349')
browser.find_element_by_name("txtPwd").send_keys('bruhWhat#9')
browser.find_element_by_id("btnLogin").click()

browser.get("https://airasia.smartkargo.com/ePouchNew.aspx")

allFiles = os.listdir()
awbNums = [i.split('.') if (i != '.DS_Store') else '' for i in allFiles]
awbNums.remove(['adr','py'])
awbNums.remove(['ghostdriver','log'])
print(awbNums)

prefix = browser.find_element_by_xpath("//input[@id='ctl00_ContentPlaceHolder1_txtAWBPrefix']")
awbInput = browser.find_element_by_xpath("//input[@id='ctl00_ContentPlaceHolder1_txtAWBNo']")
showBtn = browser.find_element_by_xpath("//input[@id='ctl00_ContentPlaceHolder1_btnShow']")

for i in awbNums:
    if len(i) > 1 :
        imagePath = os.getcwd() + ('/' + i[0] + '.' + i[1])

        prefix.clear()
        prefix.send_keys(i[0][:3])
        awbInput.click()
        awbInput.send_keys(i[0][4:])
        showBtn.click()
        fileBtn = browser.find_element_by_xpath("//input[@id='ctl00_ContentPlaceHolder1_grdePouch_ctl07_fileupload_ePouch']")

        fileBtn.send_keys(imagePath)
        browser.find_element_by_xpath("//tbody//tr[7]//td[6]//input[1]").click()

        # os.remove(i[0] + '.' + i[1])
        shutil.copy(i[0] + '.' + i[1], 'bruh/' + i[0] + '.' + i[1])
        print(i[0] + " Uploaded")
    else:
        pass

print("DONE")
