from datetime import datetime
import os

img_list = []
folder = ""
#에러가 난 경우 캡처

def generate_folder(project_name):
    global folder
    folder = os.getcwd() + "/Test Result/" + project_name + '/' + datetime.now().strftime('%Y-%m-%d %H.%M.%S')
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

def saveimg(error_num):
    global img_list
    img_list.append("<img src='Error" + str(error_num) + ".png' width='500' height='300'>")

#result(반복 횟수, 통과한 횟수, raw_data 헤더 라인, raw_data)
def generate_result(repeat, pass_count, headers, raw_datas):
    imgs = ""

    for img in img_list:
        imgs += img

    pass_result = "성공률 : " + str(pass_count) + '/' + str(repeat) + " " + "%.2f"%(int(pass_count)/int(repeat)*100) + '%%'
    html_str = "<html><body>" + imgs + pass_result + "</body></html>"

    with open(folder + "/Test result.html", "a") as html:
        html.write(html_str)

    with open(folder + "/raw data.txt", "a") as txt:
        for header in headers:
            txt.write(header + "\t")

        for raw_data in raw_datas:
            txt.write("\n")
            for data in raw_data:
                txt.write(str(data) + "\t")