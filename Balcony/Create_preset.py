from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 만들어질 Preset 갯수
how_many_create = 100

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

# 프리셋 만들기
for i in range(how_many_create):
    driver.find_element_by_xpath("//mat-icon[text()='playlist_add']").click()
    # 특수문자 + 띄어쓰기 + 영어 + 한글 + + 탭 + 숫자(번호)
    driver.find_element_by_id("mat-input-0").send_keys("@ A한\t" + i)
    driver.find_element_by_xpath("//span[text()='AUTO']").click()
    driver.find_element_by_xpath("//span[text()='"+ +"']").click()


# 웹 페이지 종료
driver.close()