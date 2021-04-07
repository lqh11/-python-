import os
from PIL import Image
from collections import Counter

def walkFile(file):
    for root, dirs, files in os.walk(file):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        return files

imgs = walkFile("F:\python_works\\test\\")      #得到路径文件夹下的图片名称集合
imgs_added = []
white_lists = []

for i in imgs:
    imgs_added.append(Image.open('F:\python_works\\test\\'+i))

for i in range(len(imgs_added)):
    t = Counter(list(imgs_added[i].getdata())).most_common(1)[0][0]     #得到出现次数最多的像素颜色
    num = Counter(list(imgs_added[i].getdata())).most_common(1)[0][1]   #得到出现的次数
    #print(len(imgs_added[i].getdata()))  测试图片的结果为：2073600
    if num / 2073600 > 0.9 and t == (255, 255, 255, 255):   #筛选空白比例占90%以上的图片
        white_lists.append(imgs[i])

print(white_lists)