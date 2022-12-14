from model_BERT_save import *
from preprocessing_data import *

# preprocessing_data
MODEL = f"cardiffnlp/twitter-roberta-base-hate"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
path = os.path.join(os.path.dirname(__file__),"../sexist_speech_recognition/raw_data/Test_Sexist_tweet.csv")  #data_complet.csv
data_preproc = full_preproc(path)
print(data_preproc)

# model_BERT_save
model = load_trained_model()
threshold = 0.66
prediction = pred_with_load_model(model, data_preproc)
print(f'Resultats de prediction = ', prediction)
prediction_threshold = predicator(prediction,threshold)
print(f'Resultats de prediction avec threshold de 0,66 = ', prediction_threshold)
