def find_max(a_list):
    if not a_list : #如果是空的，直接回傳0
        return 0
    max_num = a_list[0] # 先宣告一個變數出來儲存"目前看過的最大數"，先設成清單中的第一個東西
    for num in a_list:
        if num > max_num: # 如果此數字比目前最大數還大
            max_num = num # 那就把目前最大數變成此數字
    return max_num

print(find_max([1, 2, 3]))
print(find_max([1, -1, -5])) 
print(find_max([]))