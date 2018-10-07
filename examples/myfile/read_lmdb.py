import caffe
import lmdb
import numpy as np
import cv2
from caffe.proto import caffe_pb2

lmdb_env = lmdb.open('img_train_lmdb')
lmdb_txn = lmdb_env.begin()
lmdb_cursor = lmdb_txn.cursor()
datum = caffe_pb2.Datum()

for key, value in lmdb_cursor:
    datum.ParseFromString(value)

    label = datum.label
    data = caffe.io.datum_to_array(datum)

    #CxHxW to HxWxC in cv2
    image = np.transpose(data, (1,2,0))
    cv2.imshow('cv2', image)
    cv2.waitKey(1)
    print('{},{}'.format(key, label))
