#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
 基于Flask的简单web服务测试代码
-------------------------------------------------
"""
from flask import  Flask,  jsonify,redirect, url_for, render_template, request
import time
import random
import os
import numpy as np
from PIL import Image
import response_info as res

from classify import run_inference_on_image_copy
from setting import *
app = Flask(__name__)

def inference(file_name):
    try:
        model_path = Model_path
        label_path = Label_path
        image_file = Image_file
        predictions = run_inference_on_image_copy(model_path, label_path, image_file, file_name, num_top_predictions1=1)

    except Exception as ex:
        print(ex)
        return ""

    return predictions

@app.route("/", methods=['get'])
def test():
    return render_template('glass.html')


@app.route("/upload", methods=['post'])
def upload():
    log_file = None
    message = ''
    try:
        recognition_id = '{0}_{1}'.format(int(round(time.time() * 1000)), random.randint(10000, 99999))
        print(recognition_id)
        params = request.form
        files = request.files
        if len(files) == 0:
            res.business('001', '上传图片失败.')
        img = files['fileUpload']
        
        download_path = SAVEPATH
        download_path += recognition_id
        log_file = os.path.join(download_path, 'log.txt')
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        save_path = os.path.join(download_path, '1.jpg')

        img.save(save_path)

        if not os.path.exists(save_path):
            res.business('001', '上传图片失败.')

        score= inference(save_path)

        if score==0:
            # return render_template('upload_ok_wrong.html', userinput=result_html, val1=time.time())
            # with open(log_path, 'a+') as f:
            #     f.write('问题图片\r\n')
            pass
        else:
            print(score)
            return res.business('000', str(score))

    finally:
        if log_file is not None:
            with open(log_file, 'a+') as f:
                f.write(str(score) + '\n')
                f.write(message)


if __name__ == '__main__':
    #host = '192.168.120.26'
    #port='8080'
    app.run(host=HOST, port=PORT, debug=False, threaded=False)
