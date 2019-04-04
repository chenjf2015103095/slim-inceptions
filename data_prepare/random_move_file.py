# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       陈剑锋
   Date：         2019-03-15 下午1:19
   Description :  Dream it possible!
   
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import collections
import tensorflow as tf

import os
import random
import shutil

def moveFile(fileDir):
    pathDir=os.listdir(fileDir)
    filenumber=len(pathDir)
    print(filenumber)
    rate=0.1     #自定义抽取图片的比例，比如说100张抽取10张，那就是0.1
    picknumber=int(filenumber*rate)  #按照rate比例从文件夹中抽取一定数量的图片
    sample=random.sample(pathDir,picknumber)#随机选取picknumber数量的样本
    print(sample)
    for name in sample:
        shutil.move(fileDir+name,tarDir+name)
    return




if __name__=='__main__':
    fileDir='/home/ubutnu/finilly/data_prepare/pic/train/damage/' #原图片文件夹路径
    tarDir='/home/ubutnu/finilly/data_prepare/pic/validation/damage/'#移到新的文件夹路径
    moveFile(fileDir)


























