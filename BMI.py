
height = float(input("請輸入你的身高： "))
weight = float(input("請輸入你的體重： "))
bmi = weight / (height/100)**2

print("你的BMI: " , bmi)

if (bmi >= 35) :
    print("重度肥胖")
elif(30 <= bmi < 35 ) :
    print("中度肥胖")
elif(27 <= bmi < 30 ) :
    print("輕度肥胖")
elif(24 <= bmi < 27 ) :
    print("過重")
else :
    print("過輕")



