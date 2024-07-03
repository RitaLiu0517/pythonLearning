import random

r = random.randint(1,100) #1-100數
print(r)
while True :
    num = int(input("請輸入1-100的數字： "))
    if num > r :
        print ("數字太大囉")
    elif num < r :
        print("數字太小囉")
    else :
        print("終於猜對囉")
        break






