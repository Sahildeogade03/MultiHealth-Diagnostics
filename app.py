import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Set page configuration
st.set_page_config(page_title="MultiHealth Diagnostics", layout="wide", page_icon="🧑‍⚕️")

with open("diabetes.pkl", "rb") as file:
    model_d = pickle.load(file)

with open("heart.pkl", "rb") as file:
    model_h = pickle.load(file)

with open("lung_cancer.pkl", "rb") as file:
    model_l = pickle.load(file)

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction','Heart Disease Prediction','Lung Cancer Prediction'],
                           menu_icon='hospital-fill',icons=['activity', 'heart', 'lungs'], default_index=0)
    

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value (60 - 120+)')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value (0 - 99)')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value (00.0 - 99.9)')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value (0.000 - 0.999)')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = model_d.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)
	
# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Age')

    with col2:
        Sex = st.text_input('Sex')

    with col3:
        ChestPainType = st.text_input('Chest Pain types')

    with col1:
        RestingBP = st.text_input('Resting Blood Pressure')

    with col2:
        Cholesterol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        FastingBS = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        RestingECG = st.text_input('Resting Electrocardiographic results')

    with col2:
        MaxHR = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')


    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS	,RestingECG	,MaxHR,exang,oldpeak,slope]

        user_input = [float(x) for x in user_input]

        heart_prediction = model_h.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

#lung cancer prediction 
if selected == "Lung Cancer Prediction":
    
    # page title
    st.title('Lung Cancer Prediction')

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        Gender = st.selectbox('Gender', options=['Male', 'Female'])
    
    with col2:
        Age = st.text_input('Age', 25)
    
    with col3:
        Smoking = st.selectbox('Smoking', options=['YES', 'NO'])
    
    with col4:
        YellowFingers = st.selectbox('Yellow fingers', options=['YES', 'NO'])
    
    with col1:
        Anxiety = st.selectbox('Anxiety', options=['YES', 'NO'])
    
    with col2:
        PeerPressure = st.selectbox('Peer Pressure', options=['YES', 'NO'])
    
    with col3:
        ChronicDisease = st.selectbox('Chronic Disease', options=['YES', 'NO'])
    
    with col4:
        Fatigue = st.selectbox('Fatigue', options=['YES', 'NO'])
    
    with col1:
        Allergy = st.selectbox('Allergy', options=['YES', 'NO'])
    
    with col2:
        Wheezing = st.selectbox('Wheezing', options=['YES', 'NO'])
    
    with col3:
        Alcohol = st.selectbox('Alcohol', options=['YES', 'NO'])
    
    with col4:
        Coughing = st.selectbox('Coughing', options=['YES', 'NO'])
    
    with col1:
        ShortnessOfBreath = st.selectbox('Shortness of Breath', options=['YES', 'NO'])
    
    with col2:
        SwallowingDifficulty = st.selectbox('Swallowing Difficulty', options=['YES', 'NO'])
    
    with col3:
        ChestPain = st.selectbox('Chest Pain', options=['YES', 'NO'])
    
    # Code for Prediction
    lung_cancer_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Lung Cancer Test Result'):
        try:
            # Converting inputs to numeric values
            user_input = [
                1 if Gender == 'Male' else 0,  # Mapping Gender to numeric value
                int(Age),
                2 if Smoking == 'YES' else 1,
                2 if YellowFingers == 'YES' else 1,
                2 if Anxiety == 'YES' else 1,
                2 if PeerPressure == 'YES' else 1,
                2 if ChronicDisease == 'YES' else 1,
                2 if Fatigue == 'YES' else 1,
                2 if Allergy == 'YES' else 1,
                2 if Wheezing == 'YES' else 1,
                2 if Alcohol == 'YES' else 1,
                2 if Coughing == 'YES' else 1,
                2 if ShortnessOfBreath == 'YES' else 1,
                2 if SwallowingDifficulty == 'YES' else 1,
                2 if ChestPain == 'YES' else 1
            ]
            
            # Making prediction
            lung_cancer_prediction = model_l.predict([user_input])
            
            if lung_cancer_prediction[0] == 1:
                lung_cancer_diagnosis = 'The person is having lung cancer'
            else:
                lung_cancer_diagnosis = 'The person does not have lung cancer'
        
        except Exception as e:
            st.error(f"Error making prediction: {e}")
    
    st.success(lung_cancer_diagnosis)
