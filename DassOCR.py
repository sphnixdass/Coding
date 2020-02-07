#https://machinelearningmastery.com/save-load-keras-deep-learning-models/
#https://github.com/lazyoracle/OCR/blob/master/OCR.ipynb

import numpy as np
import cv2
from keras import layers
from keras.layers import Input, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D
from keras.layers import AveragePooling2D, MaxPooling2D, Dropout, GlobalMaxPooling2D, GlobalAveragePooling2D
from keras.models import Model, Sequential
from keras.preprocessing import image
from keras.utils import layer_utils
from keras.utils.data_utils import get_file
from keras.applications.imagenet_utils import preprocess_input
from keras.utils.vis_utils import model_to_dot
from keras.utils import plot_model
import random
import keras.backend as K
K.set_image_data_format('channels_last')
import keras
from keras.models import model_from_json

X_train=[]
X_test=[]
Y_train=[]
Y_test=[]

for i in range(1,63):
#for i in range(29,30):
    s="%03d"%i
    directory="X:\\Coding\\Python\\OCRreader\\Data\\EnglishFnt\\EnglishFnt\\English\\Fnt\\Sample"+s
    for j in range(1,1017):
        s2="%05d"%j
        img_name=directory+"/img"+s+"-"+s2+".png"
        img=cv2.imread(img_name)
        img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img=cv2.GaussianBlur(img, (5,5), 0)
        img=cv2.adaptiveThreshold(imgBlurred,                           # input image
                                      255,                                  # make pixels that pass the threshold full white
                                      cv2.ADAPTIVE_THRESH_GAUSSIAN_C,       # use gaussian rather than mean, seems to give better results
                                      cv2.THRESH_BINARY_INV,                # invert so foreground will be white, background will be black
                                      11,                                   # size of a pixel neighborhood used to calculate threshold value
                                      2)       
        img=cv2.resize(img,None,fx=0.25,fy=0.25,interpolation=cv2.INTER_CUBIC)
        if j<=762:
            X_train.append(img)
        else:
            X_test.append(img)

X_train=np.asarray(X_train)
X_test=np.asarray(X_test) 
for i in range(0,36):
    for k in range(1016):
        temp=np.zeros(36)
        temp[i]=1
        if k<762:
            Y_train.append(temp)
        else:
            Y_test.append(temp)
Y_train=np.asarray(Y_train)
Y_test=np.asarray(Y_test)

img_rows, img_cols = 32, 32
input_shape = (img_rows, img_cols, 1)
X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

num_classes = 36
print ("number of training examples = " + str(X_train.shape[0]))
print ("number of test examples = " + str(X_test.shape[0]))
print ("X_train shape: " + str(X_train.shape))
print ("Y_train shape: " + str(Y_train.shape))
print ("X_test shape: " + str(X_test.shape))
print ("Y_test shape: " + str(Y_test.shape))

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

epochs = 10
batch_size = 128

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

model.fit(X_train, Y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(X_test, Y_test))
score = model.evaluate(X_test, Y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")


# later...
 
# # load json and create model
# json_file = open('model.json', 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# loaded_model = model_from_json(loaded_model_json)
# # load weights into new model
# loaded_model.load_weights("model.h5")
# print("Loaded model from disk")
 
# # evaluate loaded model on test data
# loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
# score = loaded_model.evaluate(X, Y, verbose=0)
# print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))

print("working ...")