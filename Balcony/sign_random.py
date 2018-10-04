from selenium import webdriver
from webwait import waituntil
from time import sleep
import random

cycle=100

with open("saveid.txt", 'r') as f:
    lines = f.readlines()
# for i in range(10):
#     aa = random.choice(lines)
#     bb = aa.split('\t')

# 웹 드라이버 선언
driver = webdriver.Chrome('../chromedriver.exe')

# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)

# # 웹 드라이버 주소로 이동
driver.get('http://192.168.100.130:4728/')

for i in range(cycle):
    aa = random.choice(lines)
    bb = aa.split('\t')
    TestID = bb[0]
    Password = bb[1]
    sleep(0.5)
    driver.find_element_by_id("username").send_keys(TestID)
    driver.find_element_by_id("password").send_keys(Password)
    driver.find_element_by_xpath("//span[contains(.,'Sign In')]").click()

    # driver.find_element_by_xpath("//span[contains(.,'str(TestID)')]").click()
    waituntil(driver, "xpath", "//span[contains(.,'"+TestID+"')]").click()

    sleep(0.5)
    waituntil(driver, "xpath", "//button[contains(.,' SignOut')]").click()

