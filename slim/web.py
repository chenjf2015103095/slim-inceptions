# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yandongwei
   Date：          2018-12-19 下午3:21
   Description :
   
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""
import os
import sys

import importlib

importlib.reload(sys)
from bottle import route, run, request, static_file

import uuid

import tensorflow as tf
from classify_image_inception_v3_copy import run_inference_on_image_copy


@route("/infer_img", method='POST')
def infer_img():
    img = request.files.get('image')
    if img is None:
        return "not found image"
    file_path = '/home/ubutnu/work/download_image/test01.jpg'
    if os.path.exists(file_path):
        os.remove(file_path)
    img.save(file_path)
    if not os.path.exists(file_path):
        return "save image failed"
    import eval_single_img
    num_top_predictions = 5
    model_path = '/home/ubutnu/work/my_data/slim/satellite/frozen_graph.pb'
    label_path = '/home/ubutnu/work/my_data/slim/satellite/data/label.txt'
    image_size = 299
    output_node_name = 'InceptionV3/Predictions/Reshape_1'
    result = eval_single_img.infer(file_path, model_path, label_path,
                                   image_size, num_top_predictions, output_node_name)
    print(result)
    return result


def inference(file_name):
    try:
        model_path = '/home/ubutnu/work/my_data/slim/satellite/frozen_graph.pb'
        label_path = '/home/ubutnu/work/my_data/slim/satellite/data/label.txt'
        image_file = '/home/ubutnu/work/download_image/'
        predictions, score = run_inference_on_image_copy(model_path, label_path, image_file, file_name, num_top_predictions1=1)
        # print(predictions)
        # print(score)
    except Exception as ex:
        # print(ex)
        return ""
    # new_url = '/static/%s' % os.path.basename(file_name)
    # image_tag = '<img src="%s"></img><p>'
    # new_tag = image_tag % new_url
    # format_string = ''
    # for node_id, human_name in zip(top_k, top_names):
    #     score = predictions[node_id]
    #     format_string += '%s (score:%.5f)<BR>' % (human_name, score)
    # ret_string = new_tag + format_string + '<BR>'

    return predictions


# web接口服务

@route("/infer", method='POST')
def infer_img():
    img = request.files.get('image')
    if img is None:
        return "not found image"

    file_path = '/home/ubutnu/work/download_image/test01.jpg'
    if os.path.exists(file_path):
        os.remove(file_path)
    img.save(file_path)
    if not os.path.exists(file_path):
        return "save image failed"
    return inference(file_path)


@route("/test", method='GET')
def test():
    return 'server is running'


if __name__ == '__main__':
    run(host='192.168.120.240', port='8081')
