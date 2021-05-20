#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021/5/19 11:37
@Author: Wu Kaixuan
@File  : yolo_true.py
@Desc  :
"""
import sys
import os
import glob
import xml.etree.ElementTree as ET

image_ids = open('VOCdevkit/VOC2007/ImageSets/Main/test.txt').read().strip().split()#之前生成的test.txt所在地址

if not os.path.exists("./input"):
    os.makedirs("./input")
if not os.path.exists("./input/ground-truth"):
    os.makedirs("./input/ground-truth")

for image_id in image_ids:
    with open(r"D:/dianzishangwu2020/mAP-master/input/ground-truth/"+image_id+".txt", "a") as new_f:#用于存储真实值文件所用的文件目录
        root = ET.parse("VOCdevkit/VOC2007/Annotations/"+image_id+'.xml').getroot()#数据集中xml文件所在文件夹
        for obj in root.findall('object'):
            obj_name = obj.find('name').text
            bndbox = obj.find('bndbox')
            left = bndbox.find('xmin').text
            top = bndbox.find('ymin').text
            right = bndbox.find('xmax').text
            bottom = bndbox.find('ymax').text
            new_f.write("%s %s %s %s %s\n" % (obj_name, left, top, right, bottom))
print("Conversion completed!")