def slohi():
    tables = pandas.read_html("http://www.stockq.org/market/commodity.php")
    table = tables[7] 
    df1 =table.drop(table.index[[0,1]])
    df1.columns = ["商品","買價","漲跌","比例","台北"]
    df3 = df1["商品"].values
    df1.index =[ i for i in df3]
    df2 = df1.drop(["商品"], axis = 1)
    datas = [[data for data in df2.values]]
    #print(df2.columns, df2.index,datas)
    a = list()
    for i in df2.index:
        a.append(i)
    print(a)
    #msgtext.set("123")    
    
    #listtext.insert("end", )



def win_close():
    win.destroy()

from tkinter import ttk
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
#msgtext = tkinter.StringVar()

###元件參數
btn0 = tkinter.Button(frame1, text = "取得資料",width = 20, height = 5, command = slohi)
btn1 = tkinter.Button(frame1, text = "全部",width = 20, height = 5)
btn2 = tkinter.Button(frame1, text = "商品",width = 20, height = 5)
btn3 = tkinter.Button(frame1, text = "買價",width = 20, height = 5)
btn4 = tkinter.Button(frame1, text = "漲跌",width = 20, height = 5)
btn5 = tkinter.Button(frame1, text = "比例",width = 20, height = 5)
treetext = ttk.Treeview(frame2, columns = ["01", "02", "03", "04", "05"], show = "headings",height = 50)
treetext.column('01', width=100, anchor='center')
treetext.column('02', width=100, anchor='center')
treetext.column('03', width=100, anchor='center')
treetext.column('04', width=100, anchor='center')
treetext.column('05', width=100, anchor='center')
treetext.heading('01', text='商品')
treetext.heading('02', text='買價')
treetext.heading('03', text='漲跌')
treetext.heading('04', text='比例')
treetext.heading('05', text='台北')
#for i in range(28):
    #treetext.insert('',i,values=([s for s in a]))

#msgtext.set("取得資料")

close_btn = tkinter.Button(frame1,text="結束程式",width = 20,command=win_close, height=5)
#msg = tkinter.Message(frame2,textvariable = msgtext,font= 40)
#listtext = tkinter.Listbox(frame2, listvariable=mydata, width = 148,height = 100)

###介面配置
frame1.grid(row = 0, column = 0, sticky ="n" )
btn0.grid(row = 0, column = 0,sticky ="w")
btn1.grid(row = 1, column = 0,sticky ="w")
btn2.grid(row = 2, column = 0,sticky ="w")
btn3.grid(row = 3, column = 0,sticky ="w")
btn4.grid(row = 4, column = 0,sticky ="w")
btn5.grid(row = 5, column = 0,sticky ="w")
close_btn.grid(row = 6, column = 0,sticky ="w")

frame2.grid(row = 0, column = 1)
treetext.grid()
#msg.grid()
#listtext.grid()

win.mainloop()