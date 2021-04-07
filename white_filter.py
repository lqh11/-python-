import os
from PIL import Image
from collections import Counter

def walkFile(file):
    for root, dirs, files in os.walk(file):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        return files

imgs = walkFile("F:\\python_works\\Filter_blank_bg\\test\\image\\")      #得到路径文件夹下的图片名称集合
white_lists = []

for i in range(len(imgs)):
    print(i+1)
    op = Image.open('F:\\python_works\\Filter_blank_bg\\test\\image\\'+imgs[i])
    t = Counter(list(op.getdata())).most_common(1)[0][0]     #得到出现次数最多的像素颜色
    num = Counter(list(op.getdata())).most_common(1)[0][1]   #得到出现的次数
    num_all = len(op.getdata())
    if num / num_all > 0.9 and t == (255, 255, 255, 255):   #筛选空白比例占90%以上的图片
        print(imgs[i])
        white_lists.append(imgs[i])
    op.close()

print(white_lists)
