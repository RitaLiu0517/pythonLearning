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
