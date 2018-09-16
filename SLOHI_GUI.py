def slohi():
    tables = pandas.read_html("http://www.stockq.org/market/commodity.php")
    table = tables[7] 
    df1 =table.drop(table.index[[0,1]])
    df1.columns = ["商品","買價","漲跌","比例","台北"]
    df3 = df1["商品"].values
    df1.index =[ i for i in df3]
    df2 = df1.drop(["商品"], axis = 1)
    #print(df2)
    msgtext.set(df2)    
    
    #listtext.insert("end", )



def win_close():
    win.destroy()

import pandas,html5lib
import tkinter

###主視窗
win = tkinter.Tk()
win.geometry("800x600")
win.title("原物料行情")
###其他視窗
frame1 = tkinter.Frame(win)
frame2 = tkinter.Frame(win)
###變數容器
mydata = tkinter.StringVar()
msgtext = tkinter.StringVar()
###元件參數
btn0 = tkinter.Button(frame1, text = "取得資料",width = 20, command = slohi)
btn1 = tkinter.Button(frame1, text = "全部",width = 20)
btn2 = tkinter.Button(frame1, text = "商品",width = 20)
btn3 = tkinter.Button(frame1, text = "買價",width = 20)
btn4 = tkinter.Button(frame1, text = "漲跌",width = 20)
btn5 = tkinter.Button(frame1, text = "比例",width = 20)

msg = tkinter.Message(frame2,textvariable = msgtext,font= 40)
msgtext.set("取得資料")

close_btn = tkinter.Button(frame1,text="結束程式",width = 20,command=win_close)

#listtext = tkinter.Listbox(frame2, listvariable=mydata, width = 148,height = 100)

###介面配置
frame1.grid(row = 0, column = 0)
btn0.grid(row = 0, column = 0,sticky ="en")
btn1.grid(row = 0, column = 1,sticky ="en")
btn2.grid(row = 0, column = 2,sticky ="en")
btn3.grid(row = 0, column = 3,sticky ="en")
btn4.grid(row = 0, column = 4,sticky ="en")
btn5.grid(row = 0, column = 5,sticky ="en")

close_btn.grid(row = 0, column = 6,sticky ="en")
frame2.grid(row = 1, column = 0)
msg.grid()
#listtext.grid()

win.mainloop()