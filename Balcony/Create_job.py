from time import sleep
from selenium import webdriver
from webwait import waituntil

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
    waituntil(driver, "xpath", "//mat-icon[text()='playlist_add']").click()

    # 이름 설정 띄어쓰기 + 특수문자 + 영어 + 한글 + 숫자(번호)
    waituntil(driver, "name", "jobTitle").clear()
    waituntil(driver, "name", "jobTitle").send_keys(" @A한" + str(i))

    # 로봇 이름 설정
    waituntil(driver, "xpath", "//span[contains(.,'AUTO')]").click()
    waituntil(driver, "xpath", "//span[contains(.,'" + robot_name + "')]").click()

    # 태스크 설정
    waituntil(driver, "xpath", "//span[contains(.,'Tasks')]").click()
    waituntil(driver, "xpath", "//mat-option[@ng-reflect-message='" + task_name + "']").click()

    # 행동 설정
    waituntil(driver, "xpath", "//span[contains(.,'Add Instruction')]").click()
    waituntil(driver, "xpath", "//span[contains(.,'Empty Instruction')]").click()
    waituntil(driver, "xpath", "//span[contains(.,'action')]").click()
    waituntil(driver, "xpath", "//span[contains(.,'move')]").click()

    # ok버튼 클릭
    waituntil(driver, "xpath", "//span[text()='Submit']").click()
    
    # 알람 클릭
    waituntil(driver, "alert")
    driver.switch_to_alert().accept()

# 웹 페이지 종료
driver.close()
