import streamlit as st
import pandas as pd
from src.pipelines.prediction_pipeline import predict

# Set the title of the app
st.title("Welcome to Text Classification App")
st.header("Text should be in the following categories:")

col1, col2, col3 = st.columns(3)

with col1:
    pass

with col2: 
    st.write("""
        1. **Business** 2. **Entertainment** 3. **Politics** 4. **Sport** 5. **Tech**
    """)
with col3:
    pass

# Take user input
st.subheader("Enter your text below:")
user_text = st.text_area("")

if(st.button("Classify")):
    df=pd.DataFrame({
        "Text":user_text
    },index=[0])

    pred=predict(df)
    st.text(user_text,)
    col1,col2,col3=st.columns(3)

    with col1:
        pass
    with col2:
        st.success(pred)
    with col3:
        pass