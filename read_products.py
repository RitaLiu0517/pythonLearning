import os

def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f :
        for line in f :
                if '商品,價格' in line:
                    continue #跳過
                name, price = line.strip().split(",")
                products.append([name, price])
    print(products)
    return products


# def read_file(filename):
#     products = [] 
#     if os.path.isfile(filename):
#         with open(filename, 'r', encoding='utf-8') as f :  #17-23已移到上面function，所以這個只剩下檢查檔案在不在，不需要寫成一個function
#             for line in f :
#                     if '商品,價格' in line:
#                         continue #跳過
#                     name, price = line.strip().split(",")
#                     products.append([name, price])
#         print(products)
#     else:
#         print('檔案不存在')
#     return products

#使用者輸入商品及價格 
def user_input(products):      
    while True:
            name = input("請輸入商品名稱：")
            if name == 'q':
                break
            price = input("請輸入商品價格：")
            products.append([name, price])
    print(products)
    return products

#印出所有消費明細
def print_products(products):
    for product in products :
        print(product[0], "的價格是", product[1])


# #將明細寫入電腦檔案
def write_file(filename, products):
    with open(filename,'w',encoding='utf-8') as f : #'r'是讀，'W'是寫  也可以用'products.txt'，但是'products.csv'
        f.write('商品,價格\n') #加入標頭
        for product in products:
                f.write(product[0]+ ','+ product[1]+ '\n') #f.write 這段才是真正寫入檔案
    print("最後清單內：",products)


# 執行程式碼叫做main function，才能把要執行的程式放一起
def main():
    filename = 'products.csv' 
    if os.path.isfile(filename):
        print('檔案已找到，可以繼續新增')
        products = read_file(filename)
    else:
        print('檔案不存在')

    products = user_input(products)
    print_products(products)
    write_file('products.csv',products)

main()
