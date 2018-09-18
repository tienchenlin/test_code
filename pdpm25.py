import tkinter
from tkinter import ttk
import pandas

citylist = list()
sitelist = list()
listradio = list()

def rbcity():
    global sitelist,listradio
    sitelist.clear()
    for r in listradio:
        r.destroy()

    n = 0
    for c in data3["county"]:
        if c == city.get():
            sitelist.append(data.iloc[n][3])                        
        n += 1
    sitemake()
    rbsite()
    
def sitemake():
    global sitelist,listradio
    for s1 in sitelist:
        rbtn2 = tkinter.Radiobutton(frame2, text = s1, value =s1, variable = site,command = rbsite)
        
        listradio.append(rbtn2)
        if s1 == sitelist[0]:
            rbtn2.select()
        rbtn2.pack(side = "left")    

def rbsite():
    n = 0
    for s in data3.iloc[0:,1]:
        if s == site.get():
            try:
                pm = int(data3.iloc[n][0])
                if pandas.isna(pm):
                    retext.set(s + "站的PM2.5目前無資料")
                else:
                    if  pm  <=  35:
                        gradel = "低"
                    elif pm <= 53:
                        gradel = "中"
                    elif pm <= 70:
                        gradel = "高"
                    else:
                        gradel = "非常高"
                    retext.set(s + "站的PM2.5為:" + str(pm) + "等級為:" + gradel)
                break
            
            except:
                retext.set(s + "站的PM2.5目前無資料")            
        n += 1


def redata():
    global data
    data = pandas.read_json("https://opendata.epa.gov.tw/api/v1/\
ATM00625?%24skip=0&%24top=1000&%24format=json")
    retime.set("更新時間:" + uptime)
    rbsite()

###資料分析###
data = pandas.read_json("https://opendata.epa.gov.tw/api/v1/\
ATM00625?%24skip=0&%24top=1000&%24format=json")
data2 = data.drop("ItemUnit",axis =1)
data3 = data2.drop("DataCreationDate", axis =1)

uptime = data.iloc[0][0]

for c in data3["county"]:
    if c not in citylist:
        citylist.append(c)

count = 0
for r in data3["county"]:
    if (r == citylist[0]):
        sitelist.append(data.iloc[count][3])
    count += 1
    
###測試輸出###
#print(data3.iloc[0:,1])
###主視窗###
win = tkinter.Tk()
win.geometry("640x270")
win.title("PM2.5實時監測")
win.resizable(False,False)

###副視窗###
frame1 = tkinter.Frame(win)
frame2 = tkinter.Frame(win)

###變數容器###
city = tkinter.StringVar()
site = tkinter.StringVar()
retext = tkinter.StringVar()
retime = tkinter.StringVar()

###元件參數
label1 = tkinter.Label(win, text = "縣市", font = ("思源黑體", 16),fg = "blue")
label2 = tkinter.Label(win, text = "監測站", font = ("思源黑體", 16),fg = "blue")
for i in range(3):
    for j in range(8):
        n = i * 8 + j
        if n < len(citylist):
            city1 = citylist[n]
            rbtn1 = tkinter.Radiobutton(frame1,text =city1, value =city1, variable =city, command =rbcity)
            rbtn1.grid(row = i, column = j)
            if n == 0:
                rbtn1.select()
sitemake()
rbsite()

btn1 = tkinter.Button(win, text = "更新資料", font = ("思源黑體", 16),command = redata)
label3 = tkinter.Label(win, textvariable = retext, fg = "red")
label4 = tkinter.Label(win, textvariable = retime)

###介面配置###
label1.pack(pady = 6)
frame1.pack()
label2.pack(pady = 6)
frame2.pack()
btn1.pack()
label3.pack(pady = 6)
label4.pack(pady = 6)




win.mainloop()
