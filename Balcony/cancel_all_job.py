from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webwait import waituntil
from time import sleep

driver = webdriver.Chrome('../chromedriver.exe')

# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)

# 웹 드라이버 주소로 이동
driver.get('http://192.168.100.130:4728/')

# 발코니 로그인
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("1234")
driver.find_element_by_xpath("//span[text()='Sign In']").click()
sleep(1)

pending_list = driver.find_element_by_xpath("//*[@class='fc-time-grid-event fc-v-event fc-event fc-start fc-end']")
for pending in pending_list:
    print(pending)
    sleep(3)
    pending.click()
    waituntil(driver, "xpath", "//span[contains(.,'OK')]").click()

# pending 된 것들 배열화

driver.close()