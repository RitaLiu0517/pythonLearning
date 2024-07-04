# 記帳程式

products = [] #大清單，裝所有商品
while True:
        name = input("請輸入商品名稱：")
        if name == 'q':
            break

        price = input("請輸入商品價格：")
        # p = [] #製作小清單，裡面裝著每一個商品跟價格
        # p.append(name)
        # p.append(price)

        # 10-12 可寫成
        # p = [name, price]
        # products.append(p) #最後將小清單加入大清單
        
        #又可將15-16改寫成
        products.append([name, price])

print(products)

#列出每個清單，使用for loop
for product in products:
      print(product[0], "的價格是", product[1])

#將明細寫入電腦檔案
with open('products.csv','w',encoding='utf-8') as f : #'r'是讀，'W'是寫  也可以用'products.txt'，但是'products.csv'
      f.write('商品,價格\n') #加入標頭
      for product in products:
            f.write(product[0]+ ','+ product[1]+ '\n') #f.write 這段才是真正寫入檔案


# 練習寫入檔案
# 假設有一些整數裝在data清單裡，你想要一行一行的把這些數字寫到test.txt檔去，請寫出這樣的程式碼

# data = [1, 3, 5, 7, 9] # 清單中裝著一些整數

# with open('test.txt','w') as f :
#       for d in data :
#             f.write(data + "\n")

