import random

r = random.randint(1,100) #1-100數
print(r)
count = 0

while True :
    count += 1 
    num = int(input("請輸入1-100的數字： "))
    if num > r :
        print ("數字太大囉")
    elif num < r :
        print("數字太小囉")
    else :
        print("終於猜對囉，共猜了" , count ,"次")
        break






