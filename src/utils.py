import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.corpus import stopwords
import re
import logging
logging.basicConfig(level=logging.INFO)


def get_data():
    try:
        logging.info("Reading the data")

        df=pd.read_csv('given_data/BBC News Train.csv') 

        logging.info("Reading data successfully")
        print(df.head(2))
        return df 
    except Exception as e:
        logging.info("File not found")
        return "File not found"
    

def text_preprocess(text):
    """
    1- Convert text into lower case
    2- Remove unecessary char
    3- Convert text into token
    4- Limitization
    5- Convert text into vector
    """
    # Lower Case
    text=text.lower()
    
    # Remove unecessary char
    new_text=re.sub(r"[^a-zA-Z0-9\s\$\£\.\,]"," ",text)
    
    # Convert text into token
    token=word_tokenize(new_text)
    
    # remove stop word
    new_text=[word for word in token if word not in set(stopwords.words("english"))]
    
    # Apply limitization
    limitizer=WordNetLemmatizer()
    new_text=[limitizer.lemmatize(word) for word in new_text]
    
    
    return " ".join(new_text)

if __name__=="__main__":
    print(text_preprocess("SAMI<><>?||)"))