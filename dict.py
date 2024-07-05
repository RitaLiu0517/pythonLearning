# dictionary 字典 使用{}包裝，核心概念是key-value pair 

words = {
    'ramen' : '拉麵',
    'pasta' : '義大利麵'
}

words['tea'] = '茶' #增加新的key
print(words) #{'ramen': '拉麵', 'pasta': '義大利麵', 'tea': '茶'}

# list 跟 dict 混用
p0 = {
    'name' : '麥香奶茶',
    'price' : 10
}

p1 = {
    'name' : '珍珠奶茶',
    'price' : 60
}

drinks = [p0,p1] #list
print("drinks: ", drinks) #  [{'name': '麥香奶茶', 'price': 10}, {'name': '珍珠奶茶', 'price': 60}]
print("drinks[0]['name']" , drinks[0]['name']) # 麥香奶茶
print("drinks[1]['price']" , drinks[1]['price']) #60