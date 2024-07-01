import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import PorterStemmer,WordNetLemmatizer
from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score,confusion_matrix,classification_report
from sklearn.model_selection import train_test_split,cross_val_score
from nltk.corpus import stopwords
import re
import pickle as pkl
import json
import logging
logging.basicConfig(level=logging.INFO)

def save_report(file_path,json_file):
    with open(file_path,"w") as f:
        json.dump(json_file, f, indent=4)

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

def save_file(path,obj):
    with open(path,"wb")as f:
        pkl.dump(obj, f)

def evulate_model(actual,pred):
    result={
        "accuracy":accuracy_score(actual,pred),
        "precession":precision_score(actual,pred,average='macro'),
        "recall":recall_score(actual,pred,average='macro'),
        "f1_score":f1_score(actual,pred,average='macro'),
        # "Classification_report":classification_report(actual,pred),
        # "confussion_metrics":confusion_matrix(actual,pred)
    }

    return result

def train_model(x_train,y_train,x_test,y_test,models:dict):
    final_result={}

    for model_name,model in models.items():
        print(model)
        # fit the model
        logging.info("fit the model")
        model.fit(x_train,y_train)

        # prediction
        logging.info("predict the model")
        y_pred=model.predict(x_test)
        
        logging.info("Cross_validation of training data")
        train_score=cross_val_score(model,x_train,y_train,cv=5,scoring='accuracy').mean()

        logging.info("Cross_validation of test data")
        test_score=cross_val_score(model,x_test,y_test,cv=5,scoring='accuracy').mean()

        logging.info(f"Report of the model {model_name}")
        curr_model_result=evulate_model(actual=y_test,pred=y_pred)
        final_result[model_name]={
            "model":model,
            "Report":curr_model_result,
            "train_score": train_score,
            "test_score": test_score
        }

    best_model_name=best_model(final_result)
    return final_result,best_model_name


def best_model(results:dict):
    sorted_data=dict(sorted(results.items(), key=lambda item: item[1]['Report']['accuracy'],reverse=True))
    best_model_name = list(sorted_data.keys())[0]
    print(list(sorted_data.keys()))
    print(f"Best model: {best_model_name}")
    return best_model_name

# if __name__=="__main__":
#     print(text_preprocess("SAMI<><>?||)"))