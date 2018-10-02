from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
TestID = "QATest"
cycle=5
# def checkobj(path, kinds):
#     if kinds == 'xpath':
#         return WebDriverWait(driver, 10) \
#             .until(EC.element_to_be_clickable((By.XPATH, path)))
#     elif kinds == 'name':
#         return WebDriverWait(driver, 10) \
#             .until(EC.element_to_be_clickable((By.NAME, path)))
#     elif kinds == 'id':
#         return WebDriverWait(driver, 10) \
#             .until(EC.element_to_be_clickable((By.ID, path)))


# 웹 드라이버 선언
driver = webdriver.Chrome('../chromedriver.exe')

# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)

# # 웹 드라이버 주소로 이동
driver.get('http://192.168.100.130:4728/')
for i in range(cycle):
    driver.find_element_by_id("username").send_keys(TestID+str(i))
    driver.find_element_by_id("password").send_keys("1234")
    driver.find_element_by_xpath("//span[contains(.,'Sign In')]").click()

    sleep(0.5)
    print("Log in success "+TestID+str(i))

    sleep(1)


