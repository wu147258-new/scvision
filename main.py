import shutil
import os
from PIL import Image
'''
txt_path:txt的文件地址，里面存放的是所要复制的文件名，但这个文件名不包含文件地址
mat_path：所要复制的mat文件的文件地址
out_path:复制的目标地址

'''
txt_path="C:\\Users\\HP\\Desktop\\path.txt"
mat_path="C:\\Users\\HP\\Desktop\\image"
out_path="C:\\Users\\HP\\Desktop\\out"
new_image_path="C:\\Users\\HP\\Desktop\\newimage" #重新保存后的文件
path_list=[]

for image_path in os.listdir(mat_path): #重新保存并重命名
    path=os.path.join(mat_path,image_path)
    image = Image.open(path)
    new_path=image_path.split("_")[0]
    image.save('C:\\Users\\HP\\Desktop\\newimage\\%s.png' %(new_path))

with open(txt_path,'r') as f:
    for line in f.readlines():
        line = line.strip('\n')  #去掉列表中每一个元素的换行符
        line = line + '.png'
        path_list.append(line)

for i in path_list:
    one_path = os.path.join(new_image_path,i)
    shutil.copy(one_path,out_path)
