# 讀取檔案

data = []
with open('food.txt','r') as f : # f為自命名 file
    for line in f : # line自命名，一次讀取一行
        data.append(line.strip())  # strip： 去/n

#with 當程式離開第六行後，會自動close
print(data)



data = []
with open('test.txt' , 'r') as f:
    for line in f:
        data.append(line.sptip())
