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