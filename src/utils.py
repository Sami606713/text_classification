import pandas as pd
import numpy as np
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
        