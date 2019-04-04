# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yandongwei
   Date：          2018-12-24 下午1:27
   Description :
   
-------------------------------------------------
   Change Activity:
 v-------------------------------------------------
"""

import os
import data_convert

data_convert.convert('pic/')

#制作tfrecord数据集
# command='python /home/ubutnu/finilly/data_prepare/data_convert.py -t pic/  \
#   --train-shards=2 \
#   --validation-shards=2 \
#   --num-threads=2 \
#   --dataset-name=satellite '
#
# os.system(command)