# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yandongwei
   Date：          2018-12-19 下午2:33
   Description :
   
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""
# coding=utf-8
import os
import sys

import importlib

importlib.reload(sys)

from flask import Flask, request, redirect, url_for
import uuid

import tensorflow as tf
# from classify_image_inception_v3 import run_inference_on_image

from slim.classify_image_inception_v3_copy import run_inference_on_image_copy

ALLOWED_EXTENSIONS = set(['jpg', 'JPG', 'jpeg', 'JPEG', 'png'])

FLAGS = tf.app.flags.FLAGS

"""Namespace(image_file='test_image.jpg', 
		label_path='data_prepare/pic/label.txt',
		model_path='slim/satellite/frozen_graph.pb', 
		num_top_predictions=5)"""

tf.app.flags.DEFINE_string('model_path', '/home/ubutnu/work/my_data/slim/satellite/frozen_graph.pb', """*****, """)
tf.app.flags.DEFINE_string('label_path', '/home/ubutnu/work/my_data/slim/satellite/data/labels.txt', '')
tf.app.flags.DEFINE_string('upload_folder', '/home/ubutnu/work/download_image/', '')
tf.app.flags.DEFINE_integer('num_top_predictions', 5,
                            """Display this many predictions.""")
tf.app.flags.DEFINE_integer('port', '8080',
                            'server with port,if no port, use deault port 80')

tf.app.flags.DEFINE_boolean('debug', True, '')

UPLOAD_FOLDER = FLAGS.upload_folder

app = Flask(__name__)
app._static_folder = UPLOAD_FOLDER


def allowed_files(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def rename_filename(old_file_name):
    basename = os.path.basename(old_file_name)
    name, ext = os.path.splitext(basename)
    new_name = str(uuid.uuid1()) + ext
    return new_name


def inference(file_name):
    try:
        model_path = '//home/ubutnu/work/my_data/slim/satellite/frozen_graph.pb'
        label_path = '/home/ubutnu/work/my_data/slim/satellite/data/label.txt'
        image_file = '/home/ubutnu/work/download_image/'
        predictions, score = run_inference_on_image_copy(model_path, label_path, image_file, file_name, num_top_predictions1=1)
        # print('##################')
        # print(score)
        # print(type(predictions))
        # print(predictions)
    except Exception as ex:
        print(ex)
        return ""
    # new_url = '/static/%s' % os.path.basename(file_name)
    # image_tag = '<img src="%s"></img><p>'
    # new_tag = image_tag % new_url
    # format_string = ''
    # for node_id, human_name in zip(top_k, top_names):
    #     score = predictions[node_id]
    #     format_string += '%s (score:%.5f)<BR>' % (human_name, score)
    # ret_string = new_tag + format_string + '<BR>'
    # return ret_string
    return predictions



@app.route("/test", methods=['GET', 'POST'])
def root():
    result = """ 
    <!doctype html> 
    <title>临时测试用</title> 
    <h1>来一张照片吧</h1> 
    <form action="" method=post enctype=multipart/form-data> 
      <p><input type=file name=file value='选择图片'> 
         <input type=submit value='上传'> 
    </form> 
    <p>%s</p> 
    """ % "<br>"
    if request.method == 'POST':
        file = request.files['file']
        old_file_name = file.filename
        if file and allowed_files(old_file_name):
            filename = rename_filename(old_file_name)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            type_name = 'N/A'
            print('file saved to %s' % file_path)
            out_html = inference(file_path)
            return result + out_html
    return result


if __name__ == "__main__":
    # set_flags(FLAGS)
    print('listening on port %d' % FLAGS.port)
    app.run(host='192.168.120.240', port=FLAGS.port, debug=FLAGS.debug, threaded=True)
