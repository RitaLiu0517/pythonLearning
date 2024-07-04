# def is_leap(year):
#     if year % 4 != 0:
#         return("西元" + str(year) + "年為平年")
#     elif year % 4 == 0 and year % 100 != 0:
#         return("西元"+ str(year) + "年為閏年")
#     elif year % 100 == 0 and year % 400 != 0:
#         return("西元"+ str(year) +"年為平年")
#     elif year % 400 == 0 and year % 3200 != 0:
#         return("西元"+ str(year) +"年為閏年")
 
    
# userInput = int(input('請輸入西元年:'))
# print(is_leap(userInput))


def sum_of_list(numbers):
    return sum(numbers)

print( sum_of_list([1, 2, 3]))