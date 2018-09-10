def butCheck():  
    textvar.set('更新完畢')
    url ='https://www.cwb.gov.tw/V7/forecast/taiwan/inc/UVI/Hualien_County.htm?_=\
    1536423242592'
    html = requests.get(url)
    html.encoding = 'UTF-8'
    soup = BeautifulSoup(html.text,'html.parser')

    data1 = soup.select('#forecast0')
    data2 = data1[0].find_all(['th','td'])

    for i in range(8):
        tkdata[data2[i].text] = data2[i+8].text
    
    for i in tkdata:
        text = (f'{i},{tkdata[i]}')
        var.append(text)

    for i in var:
        box.insert('end', i)
    box.insert(0,'花蓮縣')
    box.insert(1,'日期=====體感溫度')
    box.delete(2)

def hw_close():
    win.destroy()
    
import tkinter
import requests,hashlib
from bs4 import BeautifulSoup

tkdata = dict()
var = list()

###主視窗
win = tkinter.Tk()
win.geometry('400x300')
win.title('花蓮一周溫度')
win.resizable(False, False) #關閉最大化


###變數容器
btntext = tkinter.StringVar()
btnclose = tkinter.StringVar()
boxvar = tkinter.StringVar()
textvar = tkinter.StringVar()

###元件參數
button1 = tkinter.Button(win, textvariable = btntext , command = butCheck)
btntext.set('取得資料')
button2 = tkinter.Button(win, textvariable = btnclose , command = hw_close)
btnclose.set('結束程式')
hw_data = tkinter.Label(win, textvariable = textvar,  height= 5, width= 10 )
textvar.set('請更新資料')
box = tkinter.Listbox(win, listvariable = boxvar)

###介面配置
button1.pack(side="left", padx= 20)
button2.pack(side="right", padx= 20)
hw_data.pack()
box.pack()


win.mainloop()