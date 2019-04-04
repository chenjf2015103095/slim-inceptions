# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yandongwei
   Date：          2018-12-24 下午1:11
   Description :
   
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""


#这个工程文件是用来生成tfrecord数据的，可以方便tensorflow读取数据
# coding:utf-8
from __future__ import absolute_import
import argparse
import os
import logging
# from src.tfrecord import main
import tfrecord


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--tensorflow-data-dir', default='pic/')
    parser.add_argument('--train-shards', default=2, type=int)
    parser.add_argument('--validation-shards', default=2, type=int)
    parser.add_argument('--num-threads', default=2, type=int)
    parser.add_argument('--dataset-name', default='satellite', type=str)
    return parser.parse_args()

def convert(tensorflow_data_dir,train_shards=2,validation_shards=2,
            num_threads=2,dataset_name='satellite'):
    args = parse_args()
    args.tensorflow_dir = tensorflow_data_dir
    args.train_shards = train_shards
    args.validation_shards = validation_shards
    args.num_threads = num_threads
    args.dataset_name = dataset_name
    args.train_directory = os.path.join(args.tensorflow_dir, 'train')
    args.validation_directory = os.path.join(args.tensorflow_dir, 'validation')
    args.output_directory = args.tensorflow_dir
    args.labels_file = os.path.join(args.tensorflow_dir, 'label.txt')
    if os.path.exists(args.labels_file) is False:
        logging.warning('Can\'t find label.txt. Now create it.')
        all_entries = os.listdir(args.train_directory)
        dirnames = []
        for entry in all_entries:
            if os.path.isdir(os.path.join(args.train_directory, entry)):
                dirnames.append(entry)
        with open(args.labels_file, 'w') as f:
            for dirname in dirnames:
                f.write(dirname + '\n')
    tfrecord.main(args)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    args = parse_args()
    args.tensorflow_dir = args.tensorflow_data_dir
    args.train_directory = os.path.join(args.tensorflow_dir, 'train')
    args.validation_directory = os.path.join(args.tensorflow_dir, 'validation')
    args.output_directory = args.tensorflow_dir
    args.labels_file = os.path.join(args.tensorflow_dir, 'label.txt')
    if os.path.exists(args.labels_file) is False:
        logging.warning('Can\'t find label.txt. Now create it.')
        all_entries = os.listdir(args.train_directory)
        dirnames = []
        for entry in all_entries:
            if os.path.isdir(os.path.join(args.train_directory, entry)):
                dirnames.append(entry)
        with open(args.labels_file, 'w') as f:
            for dirname in dirnames:
                f.write(dirname + '\n')
    tfrecord.main(args)
