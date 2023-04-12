# link - "https://jayprakash15-web-app-largest-number-app-pwehw6.streamlit.app/"
# Use "pip show package_name" to get version package to write in requirements.txt file OR
# open terminal in pycharm and run "pip freeze > requirements.txt"
# To run streamlit use this in terminal "streamlit run app.py"
import streamlit as st
#import pandas as pd
#from sklearn import datasets
#from sklearn.ensemble import RandomForestClassifier
#import pickle5

st.write("""

# Finding Largest Number among given 3 Numbers

""")


st.header('User Input Parameters')
def user_input_features():
    Num1 = st.number_input("Type 1st Number ")
    Num2 = st.number_input("Type 2nd Number ")
    Num3 = st.number_input("Type 3rd Number ")
    
    #data = {'Number_1': Num1, 'Number_2': Num2, 'Number_3': Num3}
    #Numbers = pd.DataFrame(data, index=[0])
    return [Num1,Num2,Num3]

Numbers = user_input_features()

#st.subheader('Largest Number among 3 is ')
st.write('## Largest Number among 3 is : ', max(Numbers))
