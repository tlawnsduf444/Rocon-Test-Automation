from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cycle=4
# 웹 드라이버 선언
driver = webdriver.Chrome('../chromedriver.exe')

# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)

# # 웹 드라이버 주소로 이동
driver.get('http://192.168.100.130:4728/')


for i in range(cycle):
#Sign-up
    driver.find_element_by_xpath("//span[contains(.,'SignUp')]").click()

    driver.find_element_by_id("username").send_keys("QATest"+str(i+1))
    driver.find_element_by_id("email").send_keys(str(i)+"1234@hana.com")
    driver.find_element_by_id("password").send_keys("1234")
    driver.find_element_by_xpath("//span[contains(.,'Sign Up')]").click()

    print("make success"+str(i) +"th" )
    driver.implicitly_wait(5)

print("finish")


