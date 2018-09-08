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

def readData():
    if os.path.exists('EN_word.txt'):

        with open("EN_word.txt", "r", encoding = "UTF-8-sig") as f:
            wordData = f.read()
            if wordData != "":
                data = ast.literal_eval(wordData)
                return data
            else:
                return dict()
    else:
        #with open('EN_word.txt','w',encoding = 'utf-8-sig') as f:
            return dict()

def allData():
    print(f"單字\t翻譯")
    print("==================")
    for row in data:
        print(f"{row:10}{data[row]:10}")
    print("==================")
    input("按任意鍵返回主選單")

def inputData():
    while True:
        newWord = input("請輸入新單字or按Enter返回主選單:\n")
        if newWord == "":
            break
        elif newWord in data:
            print(f"{newWord} 單字已重複")
            continue
        translation = input("請輸入翻譯:\n")
        data[newWord] = translation
        with open("EN_word.txt", "w",encoding = "UTF-8-sig") as f:
            f.write(str(data))
        print("單字已儲存")


def editData():
    while True:
        editWord = input("請輸入想修改的單字or按Enter返回主選單: \n單字: ")
        if editWord == "": break
        elif editWord not in data:
            print(f"{editWord} 單字不存在")    
        elif editWord in data:
            print("舊翻譯:", data[editWord])
            edtrans = input("請輸入修改翻譯:\n")
            if edtrans == "":
                print("請重新輸入單字")
                continue
            data[editWord] = edtrans
            with open("EN_word.txt", "w",encoding = "UTF-8-sig") as f:
                f.write(str(data))
            print("單字翻譯已修改")


    

###主程式###

import os,ast

data = dict()

data = readData()

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

print("程式已關閉") 