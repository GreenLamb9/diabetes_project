import streamlit as st
import pandas as pd
import pickle
import sklearn as sk
from sk.datasets import load_diabetes



# (streamlit run app.py) to run the app

st.title('This app is to predict the glucose level in the blood of a dibaetic patient')

model_lr = pickle.load(open('model_lr.pkl', 'rb'))
model_en = pickle.load(open('model_en.pkl', 'rb'))
model_ridge = pickle.load(open('model_ridge.pkl', 'rb'))

# load the dataset
diab=load_diabetes()
X = pd.DataFrame(diab.data, columns=diab.feature_names)


# user data
user_input={}

for col in X.columns:
    user_input[col]=st.slider(col, X[col].min(), X[col].max())

df=pd.DataFrame(user_input, index=[0])

st.write(df)

models={'Linear Regression': model_lr, 'Elastic Net': model_en, 'Ridge': model_ridge}

selected_model = st.selectbox('Select a model',('Linear Regression', 'Ridge', 'Elastic Net') )

if st.button('Predict'):
    prediction = models[selected_model].predict(df)[0]
    st.write(f'The predicted glucose level is: {prediction}')






