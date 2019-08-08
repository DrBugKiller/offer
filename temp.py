# -*- coding: utf-8 -*-
# @Time    : 2019/7/31 21:50
# @Author  : DrMa
import tensorflow as tf

a=tf.constant([[1,2,3],[4,5,6]],dtype=tf.float32)
a1=tf.nn.softmax(a,axis=-1)
b=tf.nn.top_k(a1, 2)

with tf.Session()as sess:
    A=sess.run(a)
    A1=sess.run(a1)
    B=sess.run(b)
    print('a:   ',A,'\n','a1:   ',A1,'\n','b:   ',B)