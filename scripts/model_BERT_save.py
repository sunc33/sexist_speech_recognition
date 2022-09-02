"""Module pour utiliser le model BERT pré-entrainé"""

import pandas as pd
import numpy as np
import csv
import urllib.request
import tensorflow as tf

from transformers import TFAutoModel
from transformers import AutoTokenizer

from tensorflow.keras import metrics
