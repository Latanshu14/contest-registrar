from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import json
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
driver.get("https://codeforces.com/")
driver.find_element(by=By.LINK_TEXT, value="Enter").click()
time.sleep(2)
print(driver.title)
driver.find_element(by=By.ID, value="handleOrEmail").send_keys(<id>)
driver.find_element(by=By.ID, value="password").send_keys(<password>)
time.sleep(1)
driver.find_element(by=By.CLASS_NAME, value="submit").click()
time.sleep(3)
driver.get("https://codeforces.com/contests")
tempData = requests.get(f'https://contest-seeker.onrender.com/api/contests/cf')
tempData = tempData.json()
for element in tempData:
    driver.get(element['url'])
print(tempData)

# driver.find_element(by="xpath", value="//*[@id='body']/div[3]/div/ul/li[4]/a").click()
# time.sleep(3)
# lnks = driver.find_elements(by=By.CLASS_NAME, value="contestParticipantCountLinkMargin")
# for lnk in lnks:
#     lnk.get_attribute('href').click()
#     time.sleep(2)
#     try:
#         driver.find_element(by=By.CLASS_NAME, value="submit").click()
#     except:
#         print("You are already registered.")

# driver.get("https://leetcode.com/")
# time.sleep(1)
# driver.find_element(by=By.LINK_TEXT, value="Sign in").click()
# time.sleep(2)
# driver.find_element(by=By.ID, value="id_login").send_keys("latanshuvarshney@gmail.com")
# driver.find_element(by=By.ID, value="id_password").send_keys("Lava1409@")
# time.sleep(1)
# driver.find_element(by=By.XPATH, value="//*[@id='signin_btn']/div").click()
# time.sleep(5)
# driver.get("https://leetcode.com/contest")
# driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/a").click()
# try:
#     driver.find_element(by=By.XPATH, value="//*[@id='contest-app']/div/div/div[3]/span/a").click()
#     driver.find_element(by=By.XPATH, value="/html/body/div[7]/div/div[2]/div/div[2]/div/div[3]/button[2]").click()
# except:
#     driver.find_element(by=By.XPATH, value="//*[@id='contest-app']/div/div/div[3]/a[1]").click()
#     driver.find_element(by=By.XPATH, value="/html/body/div[7]/div/div[10]/button[1]").click()
    


