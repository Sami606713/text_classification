from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer


def inisiate_model_training(train_process_path,test_process_path):
    # saperate the input and output column
    train_df=pd.read_csv(train_process_path)
    test_df=pd.read_csv(test_process_path)

    x_train=train_df[['Text']]
    x_test=test_df[['Text']]

    y_train=train_df['Category']
    y_test=test_df['Category']

    # Build a pipe line
    pipe=Pipeline(steps=[
        ('convert_text_vector',TfidfVectorizer(max_features=1000))
    ])

    # build a transformer
    transfomer=ColumnTransformer(transformers=[
        ("tranform",pie,'Text')
    ],remainder='passthrough')

    # Build the final pipeline
    final=Pipeline(steps=[
        ('process',transfomer),
        ("")
    ])


