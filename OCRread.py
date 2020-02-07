import numpy as np
import cv2
# from keras import layers
# from keras.layers import Input, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D
# from keras.layers import AveragePooling2D, MaxPooling2D, Dropout, GlobalMaxPooling2D, GlobalAveragePooling2D
# from keras.models import Model, Sequential
# from keras.preprocessing import image
# from keras.utils import layer_utils
# from keras.utils.data_utils import get_file
# from keras.applications.imagenet_utils import preprocess_input
# from keras.utils.vis_utils import model_to_dot
# from keras.utils import plot_model
# import random
# import keras.backend as K
# K.set_image_data_format('channels_last')
import keras
from keras.models import model_from_json

X_train=[]
X_test=[]
Y_train=[]
Y_test=[]

 
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")
 
# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])




X_test=[]
Y_test=[]

img=cv2.imread('X:\\Coding\\Python\\OCRreader\\Data\\EnglishFnt\\EnglishFnt\\English\\Fnt\\Sample059\\img059-00011.png')
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img=cv2.resize(img,None,fx=0.25,fy=0.25,interpolation=cv2.INTER_CUBIC)
X_test.append(img)

X_test=np.asarray(X_test) 
temp=np.zeros(36)
Y_test.append(temp)
Y_test=np.asarray(Y_test)

img_rows, img_cols = 32, 32
input_shape = (img_rows, img_cols, 1)
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)

X_test = X_test.astype('float32')
X_test /= 255

num_classes = 36
print ("number of test examples = " + str(X_test.shape[0]))
print ("X_test shape: " + str(X_test.shape))
print ("Y_test shape: " + str(Y_test.shape))

score = loaded_model.evaluate(X_test, Y_test, verbose=0)
print(loaded_model.metrics_names, score)
print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))
result = loaded_model.predict(X_test, batch_size=1)
resultfinal = result[0]
print(result)
print('result ', resultfinal,resultfinal.argmax(), resultfinal[resultfinal.argmax()])
for i in result:
    print(i)

# result = loaded_model.predict(test_image, batch_size=1)
# print(result)



# score = loaded_model.evaluate(X, Y, verbose=0)
# print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))


# from keras.models import load_model
# from keras.preprocessing import image
# import numpy as np


# import numpy as np
# import cv2
# from keras import layers
# from keras.layers import Input, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D
# from keras.layers import AveragePooling2D, MaxPooling2D, Dropout, GlobalMaxPooling2D, GlobalAveragePooling2D
# from keras.models import Model, Sequential
# from keras.preprocessing import image
# from keras.utils import layer_utils
# from keras.utils.data_utils import get_file
# from keras.applications.imagenet_utils import preprocess_input
# from keras.utils.vis_utils import model_to_dot
# from keras.utils import plot_model
# import random
# import keras.backend as K
# K.set_image_data_format('channels_last')
# import keras
# from keras.models import model_from_json
# from keras.models import load_model


# def create_model():
#     model = Sequential()
#     model.add(Conv2D(32, kernel_size=(3, 3),
#                     activation='relu',
#                     input_shape=input_shape))
#     model.add(Conv2D(64, (3, 3), activation='relu'))
#     model.add(Conv2D(128, (3, 3), activation='relu'))
#     model.add(MaxPooling2D(pool_size=(2, 2)))
#     model.add(Dropout(0.25))
#     model.add(Flatten())
#     model.add(Dense(128, activation='relu'))
#     model.add(Dropout(0.5))
#     model.add(Dense(num_classes, activation='softmax'))
#     return model


# def load_trained_model(weights_path):
#    model = create_model()
#    model.load_weights(weights_path)

# def dass():

#     model = load_model('X:\\Coding\\Python\\OCRreader\\model.h5')
#     img_width, img_height = 32, 32
#     # Get test image ready
#     test_image = image.load_img('X:\\Coding\\Python\\OCRreader\\Data\\EnglishFnt\\EnglishFnt\\English\\Fnt\\Sample006\\img006-00004.png', target_size=(img_width, img_height))
#     test_image = image.img_to_array(test_image)
#     test_image = np.expand_dims(test_image, axis=0)

#     test_image = test_image.reshape(img_width, img_height*3)    # Ambiguity!
#     # Should this instead be: test_image.reshape(img_width, img_height, 3) ??

#     result = model.predict(test_image, batch_size=1)
#     print(result)

#     #load_trained_model("modelTest.h5")

# dass()
# # later...
 
# # # load json and create model
# json_file = open('model.json', 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# loaded_model = model_from_json(loaded_model_json)
# # load weights into new model
# loaded_model.load_weights("modelTest.h5")
# print("Loaded model from disk")
 
# # evaluate loaded model on test data
# loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
# score = loaded_model.evaluate(X, Y, verbose=0)
# print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))

