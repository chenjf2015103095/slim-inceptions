# -*- coding: utf-8 -*-

import os

#模型部分训练
# command='python /home/ubutnu/finilly/slim/train_image_classifier.py ' \
#   '--train_dir=/home/ubutnu/finilly/slim/satellite/train_dir ' \
#   '--dataset_name=satellite ' \
#   '--dataset_split_name=train ' \
#   '--dataset_dir=/home/ubutnu/finilly/slim/satellite/data ' \
#   '--model_name=inception_v3 ' \
#   '--checkpoint_path=/home/ubutnu/finilly/slim/satellite/pretrained/inception_v3.ckpt ' \
#   '--checkpoint_exclude_scopes=InceptionV3/Logits,InceptionV3/AuxLogits ' \
#   '--trainable_scopes=InceptionV3/Logits,InceptionV3/AuxLogits ' \
#   '--max_number_of_steps=100000 ' \
#   '--batch_size=32 ' \
#   '--learning_rate=0.001 ' \
#   '--learning_rate_decay_type=fixed ' \
#   '--save_interval_secs=300 ' \
#   '--save_summaries_secs=2 ' \
#   '--log_every_n_steps=10 ' \
#   '--optimizer=rmsprop ' \
#   '--weight_decay=0.00004 '
#
# os.system(command)

#模型重新训练
# command='python /home/ubutnu/finilly/slim/train_image_classifier.py '\
#   '--train_dir=/home/ubutnu/finilly/slim/satellite/train_dir '\
#   '--dataset_name=satellite '\
#   '--dataset_split_name=train '\
#   '--dataset_dir=/home/ubutnu/finilly/slim/satellite/data '\
#   '--model_name=inception_v3 '\
#   '--checkpoint_path=/home/ubutnu/finilly/slim/satellite/pretrained/inception_v3.ckpt '\
#   '--checkpoint_exclude_scopes=InceptionV3/Logits,InceptionV3/AuxLogits '\
#   '--max_number_of_steps=100000 '\
#   '--batch_size=32 '\
#   '--learning_rate=0.001 '\
#   '--learning_rate_decay_type=fixed '\
#   '--save_interval_secs=300 '\
#   '--save_summaries_secs=2 '\
#   '--log_every_n_steps=10 '\
#   '--optimizer=rmsprop '\
#   '--weight_decay=0.00004'
# os.system(command)



#模型评估
# command='python /home/ubutnu/finilly/slim/eval_image_classifier.py '\
#   '--checkpoint_path=/home/ubutnu/finilly/slim/satellite/train_dir '\
#   '--eval_dir=/home/ubutnu/finilly/slim/satellite/eval_dir '\
#   '--dataset_name=satellite '\
#   '--dataset_split_name=validation '\
#   '--dataset_dir=/home/ubutnu/finilly/slim/satellite/data '\
#   '--model_name=inception_v3'
#
# os.system(command)


#导出模型
# cammand='python /home/ubutnu/finilly/slim/export_inference_graph.py '\
#   '--alsologtostderr '\
#   '--model_name=inception_v3 '\
#   '--output_file=/home/ubutnu/finilly/slim/satellite/inception_v3_inf_graph.pb '\
#   '--dataset_name=satellite'
#
# os.system(cammand)


#保存模型参数
# cammand='python /home/ubutnu/finilly/freeze_graph.py '\
#   '--input_graph=/home/ubutnu/finilly/slim/satellite/inception_v3_inf_graph.pb '\
#   '--input_checkpoint=/home/ubutnu/finilly/slim/satellite/train_dir/model.ckpt-100000 '\
#   '--input_binary=true '\
#   '--output_node_names=InceptionV3/Predictions/Reshape_1 '\
#   '--output_graph=/home/ubutnu/finilly/slim/satellite/frozen_graph.pb'
#
# os.system(cammand)


#模型测试
# cammand='python /home/ubutnu/finilly/slim/classify_image_inception_v3.py '\
#   '--model_path=/home/ubutnu/finilly/slim/satellite/frozen_graph.pb '\
#   '--label_path=/home/ubutnu/finilly/slim/satellite/data/label.txt '\
#   '--image_file=/home/ubutnu/work/download_image/test01.jpg'
# os.system(cammand)