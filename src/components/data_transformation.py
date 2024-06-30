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
        procssor_path=os.path.join("models",'processor.pkl')

        train_df=pd.read_csv(train_path)
        test_df=pd.read_csv(test_path)

        x_train=train_df[['Text']]
        x_test=test_df[['Text']]

        y_train=train_df['Category']
        y_test=test_df['Category']

        # Build a pipe line
        pipe=Pipeline(steps=[
            ('convert_text_vector',TfidfVectorizer(max_features=1000,preprocessor=text_preprocess))
        ])

        # build a transformer
        transfomer=ColumnTransformer(transformers=[
            ("tranform",pie,'Text')
        ],remainder='passthrough')

        # Build the final pipeline
        final=Pipeline(steps=[
            ('process',transfomer)
        ])

        x_train_transform=final.fit_transform(x_train)
        x_test_transform=final.transform(x_test)

        # concat the transform data and target data
        train_array=np.c_[x_train_transform, y_train.values.reshape(-1, 1)]
        test_array=np.c_[x_test_transform,y_test.values.reshape(-1,1)]

        # save processor
        save_file(path=procssor_path,obj=final)

        return [
            train_array,
            test_array
        ]

    except Exception as e:
        logging.info(e)
        return e