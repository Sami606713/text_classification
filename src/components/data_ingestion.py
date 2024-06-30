import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from src.utils import get_data
import os
import logging
logging.basicConfig(level=logging.INFO)


def insiate_data_ingestion():
    try:
        # Set the path where we can save the data
        raw_path=os.path.join("Data/raw","raw.csv")
        train_path=os.path.join("Data/raw","train.csv")
        test_path=os.path.join("Data/raw","test.csv")
        
        # Get the data
        df=get_data()

        df.drop(columns=['ArticleId'],inplace=True)

        logging.info("Splitig the data")
        train_data,test_data=train_test_split(df,test_size=0.2,random_state=43)

        logging.info("Saving all the data")

        logging.info(f"Raw data save in this path {raw_path}")
        df.to_csv(raw_path,index=False)

        logging.info(f"train data save in this path {train_path}")
        train_data.to_csv(train_path,index=False)
        
        logging.info(f"test data save in this path {test_path}")
        test_data.to_csv(test_path,index=False)

        return [
            train_path,
            test_path
        ]
        
    except Exception as e:
        logging.info(e)