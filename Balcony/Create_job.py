from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


def checkobj(path, kinds):
    if kinds == 'xpath':
        return WebDriverWait(driver, 10) \
            .until(EC.element_to_be_clickable((By.XPATH, path)))
    elif kinds == 'name':
        return WebDriverWait(driver, 10) \
            .until(EC.element_to_be_clickable((By.NAME, path)))
    elif kinds == 'id':
        return WebDriverWait(driver, 10) \
            .until(EC.element_to_be_clickable((By.ID, path)))


# 만들어질 Preset 갯수, 로봇 , 태스크 이름
how_many_create = 100
robot_name = 'GCS30-0006'
task_name = 'Yujin Test'

# 웹 드라이버 선언
driver = webdriver.Chrome('../chromedriver.exe')

# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)

# 웹 드라이버 주소로 이동
driver.get('http://192.168.100.130:4728/')

# 발코니 로그인
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("1234")
driver.find_element_by_xpath("//span[text()='Sign In']").click()

# 잡 생성
for i in range(how_many_create):
    checkobj("//mat-icon[text()='playlist_add']", "xpath").click()
    # 이름 설정 띄어쓰기 + 특수문자 + 영어 + 한글 + 숫자(번호)
    # driver.find_element_by_xpath("//button[@ng-reflect-placeholder='/signup']").click()
    checkobj("jobTitle", "name").clear()
    checkobj("jobTitle", "name").send_keys(" @A한" + str(i))

    # 로봇 이름 설정
    checkobj("//span[contains(.,'AUTO')]", "xpath").click()
    checkobj("//span[contains(.,'" + robot_name + "')]", "xpath").click()

    # 태스크 설정
    checkobj("//span[contains(.,'Tasks')]", "xpath").click()
    checkobj("//mat-option[@ng-reflect-message='" + task_name + "']", "xpath").click()

    # 행동 설정
    checkobj("//span[contains(.,'Add Instruction')]", "xpath").click()
    checkobj("//span[contains(.,'Empty Instruction')]", "xpath").click()
    checkobj("//span[contains(.,'action')]", "xpath").click()
    checkobj("//span[contains(.,'move')]", "xpath").click()

    # ok버튼 클릭
    checkobj("//span[text()='Submit']", "xpath").click()
    WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
    driver.switch_to_alert().accept()

# 웹 페이지 종료
driver.close()

# xpath
# driver.find_element_by_xpath("//button[@ng-reflect-router-link='/signup']").click()
