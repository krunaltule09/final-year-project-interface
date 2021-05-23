
from tensorflow import keras
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import cv2
import numpy as np
from keras.preprocessing.sequence import pad_sequences
import json
from keras.applications import ResNet50
from keras.models import Model

incept_model = ResNet50(include_top=True)

last = incept_model.layers[-2].output
modele = Model(inputs=incept_model.input, outputs=last)


model = keras.models.load_model('model.h5')

MAX_LEN = 34

with open("data_file.json", "r") as read_file:
    new_dict = json.load(read_file)

type(new_dict)
inv_dict = {v: k for k, v in new_dict.items()}


def getImage(path):
    test_img = cv2.imread(path)
    test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)

    test_img = cv2.resize(test_img, (224, 224))

    test_img = np.reshape(test_img, (1, 224, 224, 3))

    return test_img


def getCaption(path):
    test_feature = modele.predict(getImage(path)).reshape(1, 2048)
    # print(test_feature)
    test_img_path = path
    test_img = cv2.imread(test_img_path)
    test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)
    text_inp = ['startofseq']
    count = 0
    caption = ''
    while count < 25:
        count += 1

        encoded = []
        for i in text_inp:
            encoded.append(new_dict[i])
            # print(i,new_dict[i])

        encoded = [encoded]

        encoded = pad_sequences(encoded, padding='post',
                                truncating='post', maxlen=MAX_LEN)

        prediction = np.argmax(model.predict([test_feature, encoded]))
        # print(prediction)

        sampled_word = inv_dict[prediction]

        if sampled_word == 'endofseq':
            break
        caption = caption + ' ' + sampled_word

        text_inp.append(sampled_word)

    return caption
