# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:17:25 2021

@author: serhan
"""

import os 

imgDir = 'test_images\\'

train_file = 'images_list.txt'
train = open(train_file, "w+")


for imgName in os.listdir(imgDir):
    if imgName.split(".")[1] != "txt":
        train.write("data/barcode/test_images/" + imgName + '\n')
train.close()