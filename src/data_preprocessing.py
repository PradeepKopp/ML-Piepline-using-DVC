import numpy as np
import pandas as pd

import os

import re
import nltk
import string 
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer

#fetch data from data/raw

train_data=pd.read_csv('./data/raw/train.csv')
test_data=pd.read_csv('./data/raw/test.csv')

#transform the data
nltk.download('wordnet')
nltk.download('stopwords')


def lemmatization(text):
    lemmatizer=WordNetLemmatizer()

    text=text.split()

    text=[lemmatizer.lemmatize(y) for y in text]

    return " " .join(text)


def remove_stop_words(text):
    stop_words=set(stopwords.words("english"))
    Text=[i for i in str(text).split() if i not in stop_words]
    return " ".join(Text)

def removing_numbers(text):
    text=''.join([i for i in text if not i.isdigit()])
    return text

def lower_case(text):
    text=text.split()
    text=[y.lower() for y in text]
    return " " .join(text)

import re

def removing_punctuations(text: str) -> str:
    # Define a regex pattern for punctuation
    pattern = r"""[!"#$%^&*()\[\]{}_+|~`:]"""  

    text = re.sub(pattern, '', text)
    text = text.replace(':', '')
    text = " ".join(text.split())
    return text.strip()

def removing_urls(text):
    url_pattern=re.compile(r'https?://\s+|www\.\s+')
    return url_pattern.sub(r'',text)

def remove_small_sentences(df):
    for i in range(len(df)):
        if len(df.text.iloc[i].split())<3:
            df.text.iloc[i]=np.nan


def normalize_text(df):
    df.content=df.content.apply(lambda content :lower_case(content))
    df.content=df.content.apply(lambda content :remove_stop_words(content))
    df.content=df.content.apply(lambda content :removing_numbers(content))
    df.content=df.content.apply(lambda content :removing_punctuations(content))
    df.content=df.content.apply(lambda content :removing_urls(content))
    df.content=df.content.apply(lambda content :lemmatization(content))
    return df 

train_processed_data=normalize_text(train_data)
test_processed_date=normalize_text(test_data)

data_path=os.path.join("data","processed")

os.makedirs(data_path)

train_processed_data.to_csv(os.path.join(data_path,"train_processed.csv"))
test_processed_date.to_csv(os.path.join(data_path,"test_processed.csv"))

