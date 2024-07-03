driving = input("你有開過車嗎？ ")
if driving != '有' and driving != '沒有' :
    print("只能輸入 有/沒有")
    raise SystemExit

age = int(input("請輸入你的年齡： "))
if(driving == '有'):
    if (age >= 18) :
        print("快帶家人出門玩!!")
    else :
        print("你犯法了")
elif(driving == '沒有'):
     if (age >= 18) :
        print("可以考照了")
     else :
        print("再過幾年考駕照")