### Text_classification
![Text Classification](Img.jpeg)
## Table of Contents
- [Project Overview](#project-overview)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
- [Usage](#usage)

# project-overview
- In this projecct our goal is to build a model that can  classify which text related to which category in this we have 5 categorires.

# How we can do this project
- I can do this project by follow these steps
    - In my first step i can get the from the given link
    - Next step i can do some data preprocessing in the `jupyter notebook`.

# Data Preprocessing 
- In data preprocessing we can clean our data b/c this is a text data so we can clean the data by appling the text preprocessing technique.
    - **Following are the text preprocessing steps are**
        - Convert text into lower case.
        - Remove all the unecessary character like `pouncations` etc
        - Convert the text into token like.
            - `Example`  **i am samiullah** this could convert into **['i' ,'am','samiullah']**
        - Remove stopword.
            - Stop words are the word that is not important in the text preprocessing but in some of the context it is important
        - Apply `Steming` or `Lemitization` so that we can find the base word.
            - Like `goes` should be `go`
        - Convert the text into vector
        - After getting the vectore we can train the model.
    - **These are all the experiments that i can do in my `jupyter notebooks` i can do this project in a `Modular Coding Approcah`.

# Folder-structure
- Now i can do using `Modular Coding Approcah`.
- Here is my folder structure.

### Explanation:

- **Data/**: All the data should be present in the data folder.Raw data should be present in the raw folder that is present inside the Data folder and  process data should be present inside the process folder i-e also present inside the Data folder.

- **Notebook/**: In the Notebook folder all my experiment notebooks are present

- **models/**: After train the model we can save the best moedel inside the models folder

- **src/**:
  - **__init__.py**: Initialization file for the `src` package.
  - **utils.py**: Utility functions that might be used across the project.
  - **components/**: Contains modules related to data ingestion, data transformation, and model training.
    - **__init__.py**: Initialization file for the `components` package.
    - **data_ingestion.py**: Module used for getting the data.
    - **data_transformation.py**: Module used to apply transformation on the data.
    - **model_training.py**: Module used to train the model.
  - **pipelines/**: In this pipelines modeule we can make a pipeline for prediction.

- **setup.py**: Setup.py is used to build the project setup.

- **test_environment.py**: This file is used for testing purpose.

- **Dockerfile**: Docker file are used to containerize the project.

- **.dockerignore**: List of files and directories to be excluded when building Docker images.

- **requirements.txt**: File listing Python package dependencies for the project.

# Installation
- First you can clone them.
```python 
git clone  https://github.com/Sami606713/text_classification.git
```
- Install the `requirements.txt file`.
```python 
pip install -r requirements.txt
```

# usage
- You can run the full project by running the `test_enviroment.py` file
```python 
python test_environment.py
```
- **You can run the `streamlit web app`**
```python
streamlit run app.py
```