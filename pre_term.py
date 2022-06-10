# -*- coding: utf-8 -*-
"""
Created on Sat May 14 23:20:06 2022

@author: 18329
"""
import numpy as np
import pandas as pd
import pickle

import streamlit as st
from pathlib import Path

pkl_path = Path(__file__).parents[0]/ 'Pre_term.sav'
loaded_model= pickle.load(open(pkl_path,'rb'))
dataset= st.container()
with dataset:
    st.title('Pre-Term Predictions')
    st.header('20 years of responses from the National Health Interview Survey')
    st.text('In this project I investigated how maternal characteristics can cause a probability of a pre-term birth')
            
st.header('Pre_Term Dataset')
data_path= Path(__file__).parents[0]/ 'Preterm.csv'
pre_term = pd.read_csv(data_path)
st.write(pre_term.head())

st.subheader('Preterm_Distribution')
st.text('0 represent the number of birth at Full Term, while 1 represents the number of birth Preterm')

Preterm_Distribution = pd.DataFrame(pre_term['PGMOSBIRTH'].value_counts())
st.bar_chart(Preterm_Distribution)


st.header('Model Evaluation')
st.text(' !!! Input 2 for YES and 1 for NO !!!')
    
def premie_pred(input_data):
    input_np= np.array(input_data)
    input_data_reshape=input_np.reshape(1,-1)
    
    prediction= loaded_model.predict_proba(input_data_reshape)[:,1]
    return prediction
    

def main():
    def bool_to_int(YES: bool) ->int:
        if YES:
            return 2
        else:
            return 1
    original_list= ['YES','NO']
    #input data from user
    CHEBMOM = st.slider('Number of children mother has ? ', min_value=0, max_value=50)
    #CHEBMOM= st.text_input('Number of children  mother has')
    PGMECLAMP= st.selectbox('Does mother have Eclampsia ?', original_list)
    
    PGMHYPER= st.selectbox('Does mother have Hypertension', original_list)
    
    PGMEMBOL= st.selectbox('Does mother have Embolism', original_list)
    
    PGMUTI= st.selectbox('Does mother have urinary trac infection',original_list)
    
    PGMSUGUR= st.selectbox('Does mother have sugar in urine', original_list)

    PGMSUGBL = st.selectbox('Does mother have high sugar in blood ?', original_list)

    PGMDIAB =  st.selectbox('Does mother have Diabetes ?', original_list)

    PGMABNCORD= st.selectbox('Does mother have abnormal position of cord ?', original_list)

    PGMABNPLAC= st.selectbox('Does mother have abnormal position of placenta ?', original_list)

    PGMAVAGBLED= st.selectbox('Does mother have vaginal bleeding ?', original_list)

    PGMTRANQFREQ= st.selectbox('does mother take tranquilizers ?', original_list)

    PGMDRECBED= st.selectbox('Did doctor recommend bed rest ?', original_list)

    PGMWTCHANUP= st.slider('Pounds mother gained  pregnancy ?', min_value=0, max_value=75)

    BORNCONGEN= st.selectbox('Any congenital problems for child ?', original_list)

    MOMAGEATBORN= st.slider('Age of Mother ?',  min_value=13, max_value=100)
   # code for prediction
    diagnosis= ''

   #creating a button for pres
    if st.button('premie Prediction') :
        array=[CHEBMOM,PGMECLAMP,PGMHYPER,PGMEMBOL,PGMUTI,
        PGMSUGUR,PGMSUGBL,PGMDIAB,PGMABNCORD,PGMABNPLAC,PGMAVAGBLED,PGMTRANQFREQ,
        PGMDRECBED,PGMWTCHANUP,BORNCONGEN,MOMAGEATBORN]
         
        [bool_to_int(x)for x in array]
        diagnosis= premie_pred([bool_to_int(x)for x in array])

        
         
   
       
        
    st.success('The probability of you having a preemie is {}'.format(diagnosis))
    
if __name__ =='__main__':
    main()
    
    
