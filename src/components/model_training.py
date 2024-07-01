from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB,GaussianNB
from src.utils import train_model
from src.utils import save_file
import numpy as np
import os
import logging
logging.basicConfig(level=logging.INFO)

def inisiate_model_training(train_array,test_array):
    model_path=os.path.join("models","model.pkl")

    logging.info("Saperate the input and output feature")

    # x_train
    x_train_transform=train_array[:,:-1]
    print("X_train_trans",x_train_transform.shape)

    # y_train
    y_train=train_array[:,-1]
    print("y_train",y_train.shape)
    # print(y_train)

    # x_test
    x_test_transform=test_array[:,:-1]
    print("X_test_trans",x_test_transform.shape)

    # y_test
    y_test=test_array[:,-1]
    print("y_test",y_test.shape)
    # print(y_test)

    models={
        "LR":LogisticRegression(),
        "RandomForest":RandomForestClassifier(),
        "Adaboost":AdaBoostClassifier(),
        "DecessionTree":DecisionTreeClassifier(),
        "Multi_Naivabiase":MultinomialNB(),
        "Gussian Naivebiase":GaussianNB(),
        "Burnalli NaiveBiase":BernoulliNB()
    }

    logging.info("Evulating the models")
    report,model_name=train_model(x_train=x_train_transform,y_train=y_train,x_test=x_test_transform,y_test=y_test,models=models)
    
    print(report[model_name]['model'])
    
    best_model=report[model_name]['model']
    logging.info("Save the best model")
    save_file(model_path,best_model)

# if __name__ =="__main__":
#     train_array=np.load('Data/procrss/train_array.npy')
#     test_array=np.load('Data/procrss/test_array.npy')

#     inisiate_model_training(train_array=train_array,test_array=test_array)