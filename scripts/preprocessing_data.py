"""
    clean raw data of the tweet csv before sending to the BERT model
    """

from posixpath import split
import pandas as pd
import re
import numpy as np
import os
import glob
import csv
import urllib.request
from transformers import AutoTokenizer
import string


MODEL = f"cardiffnlp/twitter-roberta-base-hate"
tokenizer = AutoTokenizer.from_pretrained(MODEL)

def load_csv(path=''):
    """
        Import the DataFrame and made the preprocessing. First column will be
        the user ID and second column text of the tweet (named by 'text').
        ATTENTION IL FAUDRA BIEN METTRE A JOUR LE NOM DU CSV
        """

    ##PATH universel
    path = os.path.join(os.path.dirname(__file__), "../sexist_speech_recognition/raw_data")  #data_complet.csv
    df = pd.read_csv(path)
    return df['text']

def cleaning(sentence):
    """
        This function make a basic cleaning of the new_X_text by removing
        http, whitespaces, lowercase.
        """
    # Basic cleaning
    sentence = re.sub(r'http[^ ]+', '', sentence, flags=re.MULTILINE)
    sentence = sentence.strip() ## remove whitespaces
    sentence = sentence.lower() ## lowercase
    sentence = ''.join(char for char in sentence if not char.isdigit()) ## remove numbers

    # Advanced cleaning
    for punctuation in string.punctuation:
        sentence = sentence.replace(punctuation, '') ## remove punctuation

    return sentence

def token(df,tokenizer):
    """
        This function tokenise the new_X_text
        """
    tokens_test= tokenizer(list(df[0]), return_tensors='tf', truncation=True, padding=True,max_length=150)
    X_tokenize = tokens_test.data

    return X_tokenize


def full_preproc():
    """
        This function made the full preprocessing and tokenize before returning X_token
        """
    twt = load_csv()
    sentences = []
    for i in twt:
        sentences.append(cleaning(i))

    df = pd.DataFrame(sentences)
    X_token = token(df, tokenizer)
    return X_token




X = full_preproc()
print(X)
