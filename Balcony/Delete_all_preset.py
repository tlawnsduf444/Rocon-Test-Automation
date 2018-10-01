from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 웹 드라이버 선언
driver = webdriver.Chrome('chromedriver.exe')

# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)

# 웹 드라이버 주소로 이동
driver.get('http://192.168.100.130:4728/')

# 발코니 로그인
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("1234")
driver.find_element_by_xpath("//span[text()='Sign In']").click()

# 프리셋 리스트 선언
preset_list = driver.find_elements_by_class_name("expand-area")

# 프리셋 지우기
for preset in preset_list:
    preset.click()
    driver.find_element_by_xpath("//b[text()='Delete']").click()
    WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
    driver.switch_to_alert().accept()
    WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
    driver.switch_to_alert().accept()
# 웹 페이지 종료
driver.close()