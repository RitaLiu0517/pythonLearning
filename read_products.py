import os

products = [] 
if os.path.isfile('product.csv'):
    with open('products.csv', 'r', encoding='utf-8') as f :
        for line in f :
                if '商品,價格' in line:
                    continue #跳過
                name, price = line.strip().split(",")
                products.append([name, price])
    print(products)
else:
      print('檔案不存在')

#使用者輸入商品及價格       
while True:
        name = input("請輸入商品名稱：")
        if name == 'q':
            break
        price = input("請輸入商品價格：")
        products.append([name, price])
print(products)

# #將明細寫入電腦檔案
with open('products.csv','w',encoding='utf-8') as f : #'r'是讀，'W'是寫  也可以用'products.txt'，但是'products.csv'
      f.write('商品,價格\n') #加入標頭
      for product in products:
            f.write(product[0]+ ','+ product[1]+ '\n') #f.write 這段才是真正寫入檔案
print("最後清單內：",products)