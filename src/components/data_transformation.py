import pandas as pd
import numpy as np
from src.utils import text_preprocess
import os
import logging
logging.basicConfig(level=logging.INFO)


def inisiate_data_transformation(train_path,test_path):
    try:
        # set the path where we can store the proceess data
        train_process_path=os.path.join("Data/procrss","train_process.csv")
        test_process_path=os.path.join("Data/procrss","test_process.csv")

        train_df=pd.read_csv(train_path)
        test_df=pd.read_csv(test_path)

        logging.info("Apply the text cleaning fun on train data")
        train_df['Text']=train_df['Text'].apply(text_preprocess)
        logging.info("train data clean successfull")

        logging.info("Apply the text cleaning fun on test data")
        test_df['Text']=test_df['Text'].apply(text_preprocess)
        logging.info("test data clean successfull")
        

        logging.info("save the clean data in prcess_data folder")

        logging.info(f"Train df save in this location {train_process_path}")
        train_df.to_csv(train_process_path,index=False)

        logging.info(f"Test df save in this location {test_process_path}")
        test_df.to_csv(test_process_path,index=False)
        
        return [
            train_process_path,
            test_process_path
        ]

    except Exception as e:
        logging.info(e)
        return e