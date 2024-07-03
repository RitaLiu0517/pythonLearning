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



#清單篩選，少於100字的印出
new =[]

for d in data :
    if(len(d)<100):
        new.append(d) #少於字數100的留言加入新清單內
        
print ('共印出',len(new),'筆資料字數少於100')
print(new[0])


#清單篩選，有good字的留言印出
good =[]
for d in data:
    if 'good' in d:
        good.append(d)
print("一共有",len(good),'筆留言提到good')
print(good[0])


#速寫
good = [d for d in data if 'good' in d] #33-38的速寫 
# d in data 如果有good,就將程式中最前面的d加入


bad = ['bad' in d for d in data] #for d in data 找有bad的判斷是在用true/false寫出
#原寫法
bad = []
for d in data: 
    bad.append('bad' in d) #('bad' in d)是判斷式