from selenium import webdriver
from webwait import waituntil
from datetime import datetime, timedelta
from time import sleep
import random
import os

# 폴더 생성
folder = "C:/Users/tlawn/OneDrive/바탕 화면/Rocon Test Automation/Balcony/Test Result/DayTable/" + datetime.now().strftime('%H%M%S')
if not os.path.exists(folder):
    os.makedirs(folder)

# 오늘의 날짜, 반복 횟수
repeat = 100
today = datetime.now()
pass_count = 0
img_list = []
imgs = ''

# 이전, 다음
daybutton = [".fc-icon.fc-icon-left-single-arrow",".fc-icon.fc-icon-right-single-arrow"]

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
        realtoday = today.strftime('%B ') + today.strftime('%d, ')[1:] + today.strftime('%Y')
    else:
        realtoday = today.strftime('%B ') + today.strftime('%d, ') + today.strftime('%Y')

    if realtoday == waituntil(driver, "css", ".fc-left").text:
        pass_count += 1
    else:
        driver.save_screenshot(folder + "/Error" + str(i) + ".png")
        img_list.append("<img src='Error" + str(i) + ".png' width='500' height='300'>")

# 웹 페이지 종료
driver.close()

for img in img_list:
    imgs += img

pass_result = "성공률 : " + str(pass_count) + '/' + str(repeat) + " " + "%.2f"%(int(pass_count)/int(repeat)*100) + '%%'
html_str = "<html><body>" + imgs + pass_result + "</body></html>"

with open(folder + "/Test result.html", "a") as html:
    html.write(html_str)

#오늘로 가기
#waituntil(driver, "xpath", "//button[contains(.,'today')]").click()