import streamlit as st
from api_calling import get_chat_completion

st.set_page_config(layout="wide")
st.title('FitnFit')


# ***** INPUT *****
with st.form('my_form'):
    with st.sidebar:
        # input fields for measurements
        sidecol1, sidecol2 = st.columns(2)
        with sidecol1:
            gender = st.radio(
                "Gender:",
                ('Female', 'Male'))
        with sidecol2:
            age = st.text_input('Age:', '51')

        sidecol3, sidecol4, sidecol5 = st.columns(3)
        with sidecol3:
            weight = st.text_input('Weight (kg)', '98')
        with sidecol4:
            height = st.text_input('Height (cm)', '184')
        with sidecol5:
            waist = st.text_input('Waist (cm)', '87')

        # input fields for blood test
        cholesterol = st.text_input('Cholesterol (mmol)', '4.9')
        bloodpressure = st.text_input('Blood pressure (mm Hg)', '120/81')

        # input fields for diet
        restrictions = st.radio(
            "Any food restrictions?",
            ('None', 'Pescetarian', 'Vegetarian', 'Vegan','no pork'))
        diabetic = st.checkbox('Diabetic')
        allergies = st.multiselect(
            'Any allergies',
            ['Milk', 'Eggs', 'Fish', 'Shellfish','Tree nuts', 'Peanuts', 'Wheat', 'Soybeans']
        )

        # input fields for goals
        goals = st.text_input('Goals', 'I want to lose 10 kg in 5 months')
        workouts = st.number_input('Workouts per week', 3)

    # ****** EXECUTION ******
        submitted = st.form_submit_button('Submit')
if submitted:
            


    prompt=f'''
            
            This is a detailed information of person's input to health details that would be used to build a suitable diet plan. 
            
        Gender: {gender}
        Age: {age}
        Height: {height} cm
        Weight: {weight} kg
        Waist: {waist} cm
        Cholesterol: {cholesterol} mmol
        Blood Pressure: {bloodpressure} mm Hg\
        any food restrictions: {restrictions}

        allergies:{allergies}
        goals:{goals}
        workout frequency:{workouts}
    
            
            
            '''
    
    st.write(prompt)
            
    con=get_chat_completion(f'Now you have this given info based on build a diet plan :{prompt}')
    content=con['choices'][0]['message']['content']
    st.write(content)


            
            
           





 