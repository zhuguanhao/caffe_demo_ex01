import numpy as np
import matplotlib.pyplot as plt

caffe_root= "/home/zhuguanhao/caffe"
import sys
sys.path.insert(0,caffe_root+'python')
import caffe

MODEL_FILE = '/home/zhuguanhao/caffe/examples/myfile/deploy.prototxt' #
PRETRAINED = '/home/zhuguanhao/caffe/examples/myfile/minemodel/solver_iter_500.caffemodel'# already trained model # solver_iter_500.caffemodel
IMAGE_FILE = '/home/zhuguanhao/caffe/data/re/test/614.jpg' # 

import os
if not os.path.isfile(PRETRAINED):
    print("Downloading pre-trained CaffeNet model")

caffe.set_mode_cpu()
net = caffe.Classifier(MODEL_FILE,PRETRAINED,mean = np.load('examples/myfile/mean.npy').mean(1).mean(1),channel_swap=(2,1,0),raw_scale=255,image_dims=(256,256))#limit martix of the input image

input_image = caffe.io.load_image(IMAGE_FILE)
plt.imshow(input_image)
plt.show()


prediction = net.predict([input_image]) # 
print 'prediction class:',prediction[0].shape
plt.plot(prediction[0]) # 
plt.show() 
print 'predicted class',prediction[0].argmax()

print net.predict([input_image])

input_oversampled = caffe.io.oversample([caffe.io.resize_image(input_image,net.image_dims)],net.crop_dims)

caffe_input = np.asarray([net.transformer.preprocess('data',in_) for in_ in input_oversampled])

print net.forward(data = caffe_input)

