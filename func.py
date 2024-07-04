# function
# function是用來收納程式碼，並減少重複

def wash():
    print('加洗衣精')
    print('加水')
    print('旋轉')
    print('脫水')

wash() #加洗衣精 加水 旋轉 脫水

#加入參數
def wash(dry):
    print('加洗衣精')
    print('加水')
    print('旋轉')
    print('脫水')
    if dry:
        print('烘衣')

wash(True) #加洗衣精 加水 旋轉 脫水 烘衣
wash(False) #加洗衣精 加水 旋轉 脫水

#參數可以給預設值
def wash(dry=False, water=8): #dry預設（false）
    print('加洗衣精')
    print('加水', water,'分滿')  #下面呼叫有給值，會印出加水10分滿'
    print('旋轉')
    print('脫水')
    if dry:
        print('烘衣')
    
wash() #加洗衣精 加水 旋轉 脫水
wash(water=10) #加洗衣精 加水 旋轉 脫水 

#有return才能把運行結果存下來
def add(x, y):
    # print(x + y)
    return(x + y)
result = add(3, 4)
print(result) #7



def average(numbers):
    avg = sum(numbers) / len(numbers)
    return avg

a = average([1,2,3]) 
print(a)#執行結果2

#簡化
def average(numbers):
    return sum(numbers) / len(numbers)

print(average([1,2,3])) #執行結果2    
