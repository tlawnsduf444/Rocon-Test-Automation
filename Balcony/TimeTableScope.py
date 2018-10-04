from selenium import webdriver
from webwait import waituntil
from datetime import datetime
import random
import os

# 만들어질 Preset 갯수, 로봇 , 태스크 이름
repeat = 100
result = []
pass_count = 0
img_list = []
imgs = ''

hightimetable = ["0:00", "1:00", "2:00", "3:00", "4:00", "5:00", "6:00", "7:00", "8:00", "9:00", "10:00", "11:00", "12:00",
             "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "24:00"]
bottomtimtable = ["12am","1am","2am","3am","4am","5am","6am","7am","8am","9am","10am", "11am", "12pm",
                  "1pm","2pm","3pm","4pm","5pm","6pm","7pm","8pm","9pm","10pm", "11pm"]

# 폴더 생성
folder = "C:/Users/tlawn/OneDrive/바탕 화면/Rocon Test Automation/Balcony/Test Result/TimeTableScope/" + datetime.now().strftime('%H%M%S')

if not os.path.exists(folder):
    os.makedirs(folder)

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

waituntil(driver, "xpath", "//span[contains(.,'arrow_downward')]")
timebuttons = driver.find_elements_by_css_selector(".mat-raised-button")

for i in range(repeat):
    time = random.randrange(0, 4)
    timebuttons[time].click()
    realhigh = driver.find_elements_by_css_selector(".text")
    realbottom = driver.find_elements_by_css_selector(".fc-axis.fc-time.fc-widget-content")
    try:
        is_bottom_ok_min = realbottom[0].text
        is_bottom_ok_max = realbottom[-2].text

        is_high_ok_min = realhigh[1].text
        is_high_ok_max = realhigh[3].text

        result.append([is_bottom_ok_min, is_high_ok_min, is_bottom_ok_max, is_high_ok_max])
        if bottomtimtable.index(is_bottom_ok_min) == hightimetable.index(is_high_ok_min):
            if bottomtimtable.index(is_bottom_ok_max) == hightimetable.index(is_high_ok_max)-1:
                pass_count += 1
    except:
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

with open(folder + "/raw data.txt", "a") as html:
    html.write("TopMin" + "\t" + "BotMin" + "\t" + "TopMax" + "\t"  "BotMax" + "\t" )
    for r in result:
        html.write("\n")
        for l in r:
            html.write(str(l) + "\t")

#시간 초기화
"""while timetext[1].text != "0:00":
    buttons[0].click()

while timetext[3].text != "24:00":
    buttons[3].click()"""
