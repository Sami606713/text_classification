from src.components.data_ingestion import insiate_data_ingestion
from src.components.data_transformation import inisiate_data_transformation
from src.components.model_training import inisiate_model_training

import numpy as np

if __name__=="__main__":
    # Inisiate Data ingestion
    train_path,test_path=insiate_data_ingestion()

    # inisiate data transformation
    train_array,test_array=inisiate_data_transformation(train_path=train_path,test_path=test_path)
    
    # inisiate model training
    inisiate_model_training(train_array=train_array,test_array=test_array)

    # train_array=np.load('Data/procrss/train_array.npy')
    # test_array=np.load('Data/procrss/test_array.npy')

    # inisiate_model_training(train_array=train_array,test_array=test_array)