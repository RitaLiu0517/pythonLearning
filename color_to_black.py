from PIL import Image
import os

# http://www.sharejs.com

for file in os.listdir('orig'):
    if file.endswith('.jpg'):
        image_file = Image.open(os.path.join('orig',file)) #使用os.path.join()方法連接，中間用逗號隔開，使用join方法不需要在路徑加上“/”
        image_file = image_file.convert('L') #將圖片轉換成黑白
        image_file.save(os.path.join('result' , file[:-4]+'_grey.png'))  #file[:-4] 去掉原檔名的.jpg