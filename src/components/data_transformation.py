import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from src.utils import text_preprocess,save_file
import os
import logging
logging.basicConfig(level=logging.INFO)


def inisiate_data_transformation(train_path,test_path):
    try:
        # set the path where we can store the processor
        logging.info("Setting the path where we can store process files")
        procssor_path=os.path.join("models",'processor.pkl')
        train_array_path = os.path.join("Data", "train_array.npy")
        test_array_path = os.path.join("Data", "test_array.npy")

        logging.info("Readind train and test file")
        train_df=pd.read_csv(train_path)
        test_df=pd.read_csv(test_path)

        logging.info("Saperate the input and output columns")
        x_train=train_df[['Text']]
        x_test=test_df[['Text']]

        y_train=train_df['Category']
        y_test=test_df['Category']

        # print("x_train",x_train.shape)
        # print("x_test",x_test.shape)
        print("y_train",y_train)
        # print("y_test",y_test.shape)
        # Build a pipe line
        # logging.info("Building Encoding Pipelines")
        # pipe=Pipeline(steps=[
        #     ('convert_text_vector',TfidfVectorizer(max_features=1000,preprocessor=text_preprocess))
        # ])

        # # build a transformer
        # logging.info("Building Transformer")
        # transfomer=ColumnTransformer(transformers=[
        #     ("tranform",pipe,'Text')
        # ],remainder='passthrough')

        # # Build the final pipeline
        # logging.info("Building Final pipelines")
        # final=Pipeline(steps=[
        #     ('process',transfomer)
        # ])

        # # apply transfomation on train and test data
        # logging.info("Apply transfomation on train and test data")
        # x_train_transform=final.fit_transform(x_train)
        # x_test_transform=final.transform(x_test)
        # # print(x_train_transform.shape)
        # # concat the transform data and target data
        # logging.info("Concat the train data with target col")
        # train_array=np.hstack([x_train_transform,y_train.values.reshape(-1,1)])

        # logging.info("Concat the test data with target col")
        # test_array=np.hstack([x_test_transform,y_test.values.reshape(-1,1)])

        # # save processor
        # logging.info(f"Saving the processor in this location {procssor_path}")
        # save_file(path=procssor_path,obj=final)

        # # save the train and test array
        # logging.info("Saving train and test array")
        # np.save(train_array_path, train_array)
        # np.save(test_array_path, test_array)


        # return [
        #     train_array,
        #     test_array
        # ]

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return e
