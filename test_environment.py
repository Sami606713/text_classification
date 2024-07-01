from src.components.data_ingestion import insiate_data_ingestion
from src.components.data_transformation import inisiate_data_transformation



if __name__=="__main__":
    # Inisiate Data ingestion
    train_path,test_path=insiate_data_ingestion()

    # inisiate data transformation
    train_array,test_array=inisiate_data_transformation(train_path=train_path,test_path=test_path)
    