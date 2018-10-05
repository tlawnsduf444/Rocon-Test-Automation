from selenium import webdriver
from webwait import waituntil
from datetime import datetime, timedelta
import random
from Result_generator import saveimg, generate_result, generate_folder

# 오늘의 날짜, 반복 횟수
repeat = 100
today = datetime.now()
pass_count = 0
folder = generate_folder("DayTable")
result = []

# 이전, 다음
daybutton = [".fc-icon.fc-icon-left-single-arrow", ".fc-icon.fc-icon-right-single-arrow"]

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

# 랜덤으로 날짜 바꿈
for i in range(repeat):
    randay = random.randrange(0, 2)
    waituntil(driver, "css", daybutton[randay]).click()
    if randay == 0:
        today = today + timedelta(days=-1)
    elif randay == 1:
        today = today + timedelta(days=1)

    if int(today.strftime('%d')) < 10:
        realtoday = today.strftime('%B ') + today.strftime('%d, ')[1:] + today.strftime('%Y') + today.strftime('%A')
    else:
        realtoday = today.strftime('%B ') + today.strftime('%d, ') + today.strftime('%Y') + today.strftime('%A')

    balcony_day = waituntil(driver, "css", ".fc-left").text + waituntil(driver, "css", ".fc-day-header.fc-widget-header").text
    result.append([realtoday, balcony_day])
    if realtoday == balcony_day:
        pass_count += 1
    else:
        driver.save_screenshot(folder + "/Error" + str(i) + ".png")
        saveimg(i)

# 웹 페이지 종료
driver.close()
generate_result(repeat, pass_count, ["realtoday", "balconytoday"], result)
# 오늘로 가기
# waituntil(driver, "xpath", "//button[contains(.,'today')]").click()
