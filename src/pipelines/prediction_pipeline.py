import pandas as pd
import numpy as np
import pickle as pkl

def load_processor():
    with open('models/processor.pkl',"rb") as f:
        processor=pkl.load(f)
    return processor

def load_model():
    with open('models/model.pkl',"rb") as f:
        model=pkl.load(f)
    return model

def label(number):
    if (number==0):
        return 'business'
    elif(number==1):
        return "entertainment"
    elif(number==2):
        return "politics"
    elif(number==3):
        return 'sport'
    elif(number==4):
        return 'tech'
    

def predict(text):
    # load the processor to convert text into vector
    processor=load_processor()
    vector=processor.transform(text)

    # load the model
    model=load_model()
    pred=model.predict(vector)

    result=label(pred)
    return result