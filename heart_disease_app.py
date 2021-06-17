## Lifely


"""
Base64 is used to overlay 
the images as background,etc.
Matplotlib is used to 
visualize the prediction.
Numpy has been used to set the dataset
from input features and further data manipulations.
Pandas has been used to 
form the dataframes.
Pickleshare has been used to 
load the pretrained random-forest model.
Streamlit is used for deploying 
and connecting backedn with frontend.
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
import matplotlib.pyplot as plt

"""  
This function value has been used to encode the user input.
Those encoded values are further moved into prediction dataset.
"""


def value(lst,string):
    for i in range(len(lst)):
        if lst[i]==string:
	@@ -13,6 +44,19 @@ def value(lst,string):
edu=['10th pass','12th pass/Diploma','Bachelors','Masters or Higher']
yn=['NO','YES']

"""
Interface 
The instreface widgets are developed
by streamlit organisation.
Streamlit , a high level library to 
connect with web has various widgtes
which can be used to build GUI on
web and also connect with backend.
"""


col1, col2, col3 = st.beta_columns([10,6,10])
with col1:
    st.write("")
	@@ -41,7 +85,8 @@ def value(lst,string):
)
st.sidebar.header('User Input Features')

""" These are the entry widgets which are going
to take the input features  """

st.sidebar.markdown("""
Input your data here .
	@@ -65,6 +110,13 @@ def value(lst,string):

st.markdown("<h3 style='text-align: center; color:#4dffa6;'>Update your details in the sidebar</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color:#4dffa6;'><----</h3>", unsafe_allow_html=True)

"""  after clicking submit , 
the input data forms a one liner
dataset(dataset with 1 row) ,
then the saved model predict and 
outputs as follows"""

if st.sidebar.button('Submit'):
        data = {'male':value(sex,male),
                'age':age,
	@@ -129,4 +181,4 @@ def value(lst,string):

st.sidebar.markdown("""Follow me on [Kaggle](https://kaggle.com/sagnik1511) , [Instagram](https://www.instagram.com/tensored___/) , [Github](https://github.com/sagnik1511)""")
st.sidebar.markdown("""Know more about me [Sagnik Roy](http://happai.epizy.com)""")
#-----------------------------------------------------------------
