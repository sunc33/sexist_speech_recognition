"""Use the pre-trained BERT model and make a predict with the tweet_csv"""

import pandas as pd
import numpy as np
import os
import glob
import csv
import urllib.request
import tensorflow as tf

from transformers import TFAutoModel
from transformers import AutoTokenizer
from tensorflow.keras import layers
from tensorflow.keras import metrics
from tensorflow import keras
from keras.models import load_model

def init_model():

  model_pre_train = TFAutoModel.from_pretrained('cardiffnlp/twitter-roberta-base-hate')

  input_ids = tf.keras.layers.Input(shape=(150),dtype='int32')              ## VOIR LES PARAMS
  input_attention_mask = tf.keras.layers.Input(shape=(150),dtype='int32')   ## VOIR LES PARAMS

  backbone_output = model_pre_train({'input_ids':input_ids,
                            'attention_mask':input_attention_mask})[1]

  model_pre_train.trainable=False         ## pour ne pas réentrainer les poids

  output = tf.keras.layers.Dense(1,activation='sigmoid')(backbone_output)  ## Dernière couche Dense

  model_ok = tf.keras.Model(inputs={'input_ids':input_ids,
                            'attention_mask':input_attention_mask},outputs=output)

  model_ok.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy',metrics.Precision(),metrics.Recall()])

  return model_ok


def load_trained_model():
    """
        initialise the model with the trained weights
        """
    path = os.path.join(os.path.dirname(__file__), "../sexist_speech_recognition/model/weightsfile.h5")

    model_testing = init_model()
    model_tuned = model_testing.load_weights(path)

    return model_tuned

 def pred_with_load_model(model_tuned, tweet_preproc):
    """
        make a prediction with the tweet_csv with our the saved model loaded
        """
    prediction = model_tuned.predict(tweet_preproc)
    return prediction
