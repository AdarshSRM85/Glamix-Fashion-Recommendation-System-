import tensorflow as tf
from keras.applications.resnet50 import ResNet50, preprocess_input
from keras.layers import GlobalMaxPooling2D
from tensorflow import keras
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import GlobalMaxPooling2D
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import MaxPooling2D 
import cv2
import numpy as np
from numpy.linalg import norm
import pickle
from sklearn.neighbors import NearestNeighbors

feature_list=np.array(pickle.load(open("featurevector.pkl", "rb")))
filename=pickle.load(open("filename.pkl", "rb"))

model=ResNet50(weights='imagenet',include_top=False, input_shape=(224,224,3))
model.trainable=False

model=Sequential([
    model,
    GlobalMaxPooling2D()
])
model.summary()

#def extract_feature(img_path, model):
img=cv2.imread("1636.jpg")
img=cv2.resize(img, (224,224))
img=np.array(img)
expand_img=np.expand_dims(img, axis=0)
pre_img=preprocess_input(expand_img)
result=model.predict(pre_img).flatten()
normalized=result/norm(result)
    #return normalized

neighbors=NearestNeighbors(n_neighbors=6, algorithm="brute", metric="euclidean")
neighbors.fit(feature_list)


distance, indices = neighbors.kneighbors([normalized])
print(indices)

for file in indices[0][1:6]:
    #print(filename[file], end="\t")
    imgName=cv2.imread(filename[file])
    cv2.imshow("Frame",  cv2.resize(imgName, (480,480)))
    cv2.waitKey(0)
    

