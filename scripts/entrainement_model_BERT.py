"""Module pour entrainer le model BERT"""

import pandas as pd
import numpy as np
import csv
import urllib.request
import tensorflow as tf

from transformers import TFAutoModel
from transformers import AutoTokenizer

from tensorflow.keras import metrics


"""Import du DataFrame et création du train et du test"""

##PATH u#niversel
path = '../sexist_speech_recognition/raw_data/data_complet.csv'
df = pd.read_csv(path)

##Création du X et y
X = df[['text']]
y = df['label']

#On shuffle le data set avant de faire le split
shuffled = df.sample(frac=1, random_state=1).reset_index()

#On fait le split du data-set en 70% de 0 et 30% de 1.
#Cela permet que le model se train sur suffisament de tweet sexiste
df_0 = shuffled[shuffled['label'] == 0]
df_1 = shuffled[shuffled['label'] == 1]

train_set = df_0.head(7952).append(df_1.head(3458))
test_set = df_0.tail(5000).append(df_1.tail(864))

train_set = train_set.sample(frac=1, random_state=1)
test_set = test_set.sample(frac=1, random_state=1)

X_train = train_set[['text']]
y_train = train_set['label']

X_test = test_set[['text']]
y_test = test_set['label']

"""Création du model BERT"""
# Tasks:
# emoji, emotion, hate, irony, offensive, sentiment
# stance/abortion, stance/atheism, stance/climate, stance/feminist, stance/hillary

task='hate'
MODEL = f"cardiffnlp/twitter-roberta-base-{task}"

tokenizer = AutoTokenizer.from_pretrained(MODEL)

# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

# download label mapping
labels=[]
mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"
with urllib.request.urlopen(mapping_link) as f:
    html = f.read().decode('utf-8').split("\n")
    csvreader = csv.reader(html, delimiter='\t')
labels = [row[1] for row in csvreader if len(row) > 1]

#TF
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

model_testing = init_model()

print(model_testing.summary())

## tokeniser X_train
tokens= tokenizer(list(X_train['text']), return_tensors='tf', truncation=True, padding=True,max_length=150)

X_train_tokenize = tokens.data

history = model_testing.fit(X_train_tokenize, y_train, validation_split = 0.2, batch_size=32, epochs=20, verbose=1)
