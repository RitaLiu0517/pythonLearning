data =[]
count = 0 
with open('reviews.txt','r') as f:
    for line in f :
        data.append(line)
        count +=1
        if(count % 1000 == 0 ): #每一千筆印出一次讀取進度
            print(len(data)) 
print('檔案讀取完畢,共有', len(data), "筆資料")
print(data[0]) #印出第一筆留言


#算留言的平均長度
sum_len = 0
for d in data :
    sum_len += len(d) #每讀取到一筆留言的長度將它加進sum_len裡
print("留言的平均長度為" ,sum_len/len(data))
