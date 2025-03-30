from tensorflow import keras
import tensorflow as tf
from tensorflow.keras import layers
import numpy as np

tf.config.set_visible_devices([], 'GPU')


def load_model():
    model = tf.keras.models.load_model('./models/vgg16_complete_model.h5')
    if model is None:
        return False
    print("Model loaded")
    print(model.summary())
    print(model.get_weights()[-1].shape)
    print(model.get_weights()[-2].shape)
    print(model.get_weights()[-3].shape)
    print(model.get_weights()[-4].shape)

    return model


def preprocess_image(image_path, model):
    pred_labels = ["Normal", "Pneumonia", "Covid-19"]
    layer1 = tf.keras.layers.Rescaling(scale=1. / 255)
    img1 = tf.keras.utils.load_img(image_path, target_size=(224, 224))
    x = tf.expand_dims(layer1(img1), 0)
    pred_prob = model.predict(x)
    pred = np.argmax(pred_prob, axis=1)
    pred_index = int(pred[0])
    return {
        "prediction":pred_labels[pred_index]
    }
