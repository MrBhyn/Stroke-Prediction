
import streamlit as st
import sklearn
import pickle
import base64

def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = set_background("strksdbr1.png")
img1 = set_background("strkbg1.jpg")
css = f"""
<style>
.stApp {{
    background-image: url("data:image/png;base64,{img1}");
    background-size: cover;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
 
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stSidebar"] {{
text-align: center;
}}
</style>
"""
st.markdown(css, unsafe_allow_html=True)


st.title('Stroke Incident Prediction')
st.sidebar.header("ABOUT")
st.sidebar.write("Stroke Incident Prediction is a machine-learning application that attempts to predict human vulnerability to stroke. The application imports it's Random Forest model from the Stroke dataset retrieved from Centers for Disease Control and Prevention 2015 Behavioral Risk Factor Surveillance System Survey Data and Documentation.")
st.sidebar.write("The SIP(Stroke Incident Protection) does not aim to replace human health care provided inside healthcare facilities but instead spreads awareness to people of the danger and causes of stroke. This machine's prediction should not replace a doctor's opinion or be an excuse for health negligence.")

name = st.sidebar.text_input("Name")
with open('strkmodel2.pkl', 'rb') as f:
    model = pickle.load(f)

if name:
    st.header(f"Welcome, {name}")
sexopt = {
    "----": 3,
    "Female": 1,
    "Male": 0    
}
Sexmenu = st.selectbox("Select your sex:", list(sexopt.keys()))
Sex = sexopt[Sexmenu]
age= st.number_input("Enter age:", step=1)
weight = st.number_input("Enter Weight:(kg) ", step=1, value = 0)
height = st.number_input("Enter Height:(cm)", step=1, value= 1)
hinmeters = height/100
hsquared = hinmeters**2
bmi = weight / hsquared
if bmi:
    st.write(f"You BMI is {bmi}")



workopt = {
    "Never Worked": 0,
    "Child": 1,
    "Government Job": 2,
    "Self-employed": 3,
    "Private": 4    
}
workmenu = st.selectbox("What is your work type?", list(workopt.keys()))
work = workopt[workmenu]


resopt = {
    "Rural": 0,
    "Urban": 1,   
}
resmenu = st.selectbox("What is your residence?", list(resopt.keys()))
residence = resopt[resmenu]



st.write("Check if it applies to you")

hyptoggle= st.checkbox("Hypertension")
hypertension = 1 if hyptoggle else 0

hearttoggle= st.checkbox("Had Heart Disease")
heart = 1 if hearttoggle else 0

marriedtoggle= st.checkbox("Been in a marriage")
married = 1 if marriedtoggle else 0

smoketoggle= st.checkbox("Tried smoking")
smoke = 1 if smoketoggle else 0

if st.button("Predict"):
    prediction = model.predict([[Sex,age,hypertension,heart,married,work,residence,bmi,smoke]])
    if prediction == 0:
        st.success("No Stroke Hazard.")
    else:
        st.warning("Stroke is imminent.")
