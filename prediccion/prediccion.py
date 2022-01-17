import numpy as np
from keras.preprocessing.image import load_img,img_to_array
from keras.models import load_model

from tensorflow.keras.utils import to_categorical


longitud,altura=100,100
modelo='./modelo/modelo.h5'
pesos='./modelo/pesos.h5'

cnn=load_model(modelo)

cnn.load_weights=pesos

def predict(file):
    x=load_img(file,target_size=(longitud,altura))
    x=img_to_array(x)
    x=np.expand_dims(x,axis=0)
    arreglo=cnn.predict(x)  ##[1,0,0]
    print(arreglo)
    resultado=arreglo[0]
    print(resultado)
    respuesta=np.argmax(resultado)
    print(respuesta)

predict("./modelo/imagen1.jpg")