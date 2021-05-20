#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021/5/19 11:58
@Author: Wu Kaixuan
@File  : extract_picture.py
@Desc  :
"""
import sys
source_path = " "
dst_path = " "

import sys
import re
from PIL import Image
# f1 = open('E:\CODE\TX\dir.txt','r')
# f2 = open('E:\CODE\TX\dir.txt','w+')
# for line in f1.readlines():
#    if re.findall(' 1',line): #查找“空格1”的行 每行的格式000005 -1\n 000007
#       f2.write(line)#把查找到的行写入f2.
# f1.close()
# f2.close()
# data = []
data = []
for line in open("D:/dianzishangwu2020/yolov4-tiny-keras-master/VOCdevkit/VOC2007/ImageSets/Main/test.txt", "r"):  # 设置文件对象并读取每一行文件
    data.append(line)
for a in data:
    #  print(a)
    # line3=line2[:-4] #读取每行去掉后四位的数#
    im = Image.open('D:/dianzishangwu2020/yolov4-tiny-keras-master/VOCdevkit/VOC2007/JPEGImages/{}.jpg'.format(a[:-1]))  # 打开改路径下的line3记录的的文件名
    im.save('D:/dianzishangwu2020/mAP-master/input/images-optional/{}.jpg'.format(a[:-1]))  # 把文件夹中指定的文件名称的图片另存到该路径下
