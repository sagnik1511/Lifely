import base64
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import streamlit as st

def value(lst, string):
    for i in range(len(lst)):
        if lst[i] == string:
            return i
sex=['Female', 'Male']
edu=['10th pass', '12th pass/Diploma', 'Bachelors', 'Masters or Higher']
yn=['NO', 'YES']

col1, col2, col3 = st.beta_columns([10, 6, 10])
with col1:
    st.write("")
with col2:
    st.image("logo.png")
with col3:
    st.write("")
    
    
st.markdown("<h1 style='text-align: center; color:#99ffff;'>Heart Disease       Diagonistic App</h1>", unsafe_allow_html = True)
st.markdown("<h3 style='text-align: center; color:#99ffff;'>Check your cardiac health for free💝💗.</h3>", unsafe_allow_html = True)



main_bg = "blue.png"
main_bg_ext = "png"
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.header('User Input Features')



st.sidebar.markdown("""
Input your data here .
It is already set to normal values.
""")
male = st.sidebar.selectbox('Sex', ('Female', 'Male'))
age= st.sidebar.slider('Age', 5.0, 100.0, 30.0)
education = st.sidebar.selectbox('Education', ('10th pass', '12th pass/Diploma', 'Bachelors', 'Masters or Higher'))
current_smoker = st.sidebar.selectbox('Current Smoker', ('NO', 'YES'))
cigsPerDay = st.sidebar.slider('Cigarettes per Day', 0, 100, 20)
BPMeds = st.sidebar.selectbox('Takes BP medicines', ('NO', 'YES'))
prevstrk = st.sidebar.selectbox('Had any prevalent Stroke', ('NO', 'YES'))
prevhyp = st.sidebar.selectbox('Had any prevalent Hypertension', ('NO', 'YES'))
diabetes = st.sidebar.selectbox('Have diabetes', ('NO', 'YES'))
chol = st.sidebar.slider('Cholesterol (mg/dl)', 0.0, 700.0, 230.0)
highbp = st.sidebar.slider('Blood Pressure(upper value) (mmHg)', 100.0, 250.0, 120.0)
lowbp = st.sidebar.slider('Blood Pressure(Lower Value) (mmHg)', 50.0, 180.0, 80.0)
BMI = st.sidebar.slider('BMI (kg/m^2)', 15.0, 70.0, 23.0)
heart_rate = st.sidebar.slider('Heart Rate (per minute)', 30.0, 130.0, 40.0)
glucose = st.sidebar.slider('Glucose (mg/dl)', 100.0, 500.0, 110.0)

st.markdown("<h3 style='text-align: center; color:#4dffa6;'>Update your details in the sidebar</h3>", unsafe_allow_html = True)
st.markdown("<h3 style='text-align: center; color:#4dffa6;'><----</h3>", unsafe_allow_html = True)
if st.sidebar.button('Submit'):
        data = {'male': value(sex, male),
                'age': age,
                'education': value(edu, education),
                'currentSmoker': value(yn, current_smoker),
                'cigsPerDay': cigsPerDay,
                'BPMeds': value(yn, BPMeds),
                'prevalentStroke': value(yn, prevstrk),
                'prevalentHyp': value(yn, prevhyp),
                'diabetes': value(yn, diabetes),
                'totChol': chol,
                'sysBP': highbp,
                'diaBP': lowbp,
                'BMI': BMI,
                'heartRate': heart_rate,
                'glucose': glucose}
        features = pd.DataFrame(data, index=[0])

        st.markdown("<h2 style='text-align: center; color:#000066;'>Data gathered........</h2>", unsafe_allow_html = True)
        st.markdown("<h2 style='text-align: center; color:#000066;'>Processing Results........</h2>", unsafe_allow_html = True)
        # Reads in saved classification model
        load_clf = pickle.load(open('heart_disease.pkl', 'rb'))
        
        # Apply model to make predictions
        prediction = load_clf.predict(features)
        prediction_proba = load_clf.predict_proba(features).reshape(2,)
        yes = prediction_proba[1]
        no = prediction_proba[0]
        
        
        
        
        st.markdown("<h2 style='text-align: center; color:#99ffff;'><u>Prediction </u></h2>", unsafe_allow_html = True)
        pred1, pred2, pred3 = st.beta_columns([12, 6, 14])
        if prediction==0:
            st.markdown("<h1 style='text-align: center; color:#006600;'>You don't have any heart problem.</h1>", unsafe_allow_html = True)
            with pred1:
                st.write("")
            with pred2:
                st.image("smile_emo.png")
            with pred3:
                st.write("")
        else:
            st.markdown("<h1 style='text-align: center; color:#cc0000;'>Go to a doctor.You may have heart problems.</h1>", unsafe_allow_html = True)
            with pred1:
                st.write("")
            with pred2:
                st.image("amb.png")
            with pred3:
                st.write("")
        
            
        st.markdown("<h1 style='text-align: center; color:#99ffff;'><u>Prediction Probability</u></h1>", unsafe_allow_html = True)
        fig,ax=plt.subplots(figsize=(10,8))
        axes=plt.bar(['Chances of being healthy\n{} %'.format(no*100),'Chances of getting cardiac diseases\n{} %'.format(yes*100)], [no, yes])
        axes[0].set_color('g')
        axes[1].set_color('r')
        st.pyplot(fig)
        
        st.markdown("<h2>Developed with ❤ by <a style='display: block; text-align: center;' href='http://happai.epizy.com' target='_blank'>Sagnik Roy</a></h2>",unsafe_allow_html = True)


st.sidebar.markdown("""Follow me on [Kaggle](https://kaggle.com/sagnik1511) , [Instagram](https://www.instagram.com/tensored___/) , [Github](https://github.com/sagnik1511)""")
st.sidebar.markdown("""Know more about me [Sagnik Roy](http://happai.epizy.com)""")
#-----------------------------------------------------------------
