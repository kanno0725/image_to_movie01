# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:03:06 2020
@author: kanno
https://theailearner.com/2018/10/15/creating-video-from-images-using-opencv-python/
"""
from glob import glob
import cv2
#import numpy as np
 
img_array = []
for filename in glob('*.JPG')[5001:10000]:
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter('project2.avi',cv2.VideoWriter_fourcc(*'DIVX'), 1, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
    print(i)
out.release()

