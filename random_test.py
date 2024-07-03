import random

start = int(input("請決定隨機數字的開始值： "))
end = int(input("請決定隨機數字的結束值： "))

r = random.randint(start,end) 
print(r)
count = 0

while True :
    count += 1 
    num = int(input("請輸入數字： "))
    if num > r :
        print ("數字太大囉")
    elif num < r :
        print("數字太小囉")
    else :
        print("終於猜對囉，共猜了" , count ,"次")
        break






