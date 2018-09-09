###功能函數###

def mune():
    os.system("cls")
    
    print("單字卡系統")
    print("==================")
    print("1. 新增單字")
    print("2. 全部內容")
    print("3. 修改翻譯")
    print("0. 結束系統")
    print("==================")
    print(os.getcwd())

def allData():

    cursor = conn.execute('select * from table01')
    print(f"單字\t翻譯")
    print("==================")
    for row in cursor:
        print(f"{row[0]:10}{row[1]:10}")
    print("==================")
    input("按任意鍵返回主選單")

def inputData():
    while True:
        newWord = input("請輸入新單字or按Enter返回主選單:\n")
        if newWord == "": break
        sqlstr = f"select * from table01 where word='{newWord}'"
        cursor = conn.execute(sqlstr)
        row = cursor.fetchone()
        print(row)
        if not row==None:
            print(f"{newWord} 單字已重複")
            continue
        translation = input("請輸入翻譯:\n")
        sqlstr = f'insert into table01 values("{newWord}","{translation}")'
        conn.execute(sqlstr)
        conn.commit()
        print("單字已儲存")


def editData():
    while True:
        editWord = input("請輸入想修改的單字or按Enter返回主選單: \n單字: ")
        if editWord == "": break
        sqlstr = f"select * from table01 where word = '{editWord}'"
        cursor = conn.execute(sqlstr)
        row = cursor.fetchone()
        if row == None:
            print(f"{editWord} 單字不存在")    
        elif editWord in row:
            print("舊翻譯:", row[1])
            edtrans = input("請輸入修改翻譯:\n")
            sqlstr = f"update table01 set trans='{edtrans}' where word = '{editWord}'"
            conn.execute(sqlstr)
            conn.commit()
            if edtrans == "":
                print("請重新輸入單字")
                continue
            print("單字翻譯已修改")


    

###主程式###

import os,sqlite3

os.getcwd()
os.chdir('D:\\git_work\\word_system')

conn = sqlite3.connect('D:\\git_work\\word_system\\en_totw.sqlite')
#cur =conn.cursor()
while True:
    try:
        mune()

        option = int(input("請輸入你的選擇: "))

        if option == 1:
            inputData()
        elif option == 2:
            allData()
        elif option == 3:
            editData()
        else:
            break
    except:
        break

conn.close()

print("程式已關閉") 