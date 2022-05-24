# -*- coding: utf-8 -*-
"""
Created on Sat May 14 23:20:06 2022

@author: 18329
"""
import numpy as np
import pickle
import streamlit as st
pickle_in= open('Claf.pkl','rb')
claf=pickle.load(pickle_in)
dataset= st.container()
with dataset:
    st.title('Pre-Term Predictions')
    st.header('20 years of responses from the National Health Interview Survey')
    st.text('Investigated how maternal characteristics during pregnancy affected birth outcomes')

    
def premie_pred(input_data):
    input_np= np.array(input_data)
    input_data_reshape=input_np.reshape(1,-1)
    
    prediction= claf.predict_proba(input_data_reshape)
    return prediction
    

def main():

    
    #input data from user
    CHEBMOM= st.text_input('Number of children  mother has','Type Here')
    PGMECLAMP= st.text_input('Does mother have Eclampsia','Type Here')
    PGMHYPER= st.text_input('Does mother have Hpertension','Type Here')
    PGMEMBOL= st.text_input('Does mother have Embolism','Type Here')
    PGMUTI= st.text_input('Does mother have Urinary tract infection','Type Here')
    PGMSUGUR= st.text_input('Does mother have Sugar in urine','Type Here')
    PGMSUGBL = st.text_input("Does mother have high sugar in blood",'Type Here')
    PGMDIAB =  st.text_input('Does mother have Diates','Type Here')
    PGMABNCORD= st.text_input('Does mother have abnormal position of cord','Type Here')
    PGMABNPLAC= st.text_input('Does mother have abnormal position of placenta','Type Here')
    PGMAVAGBLED= st.text_input('Does mother have vaginal bleeding','Type Here')
    PGMTRANQFREQ= st.text_input('does mother take tranquilizers','Type Here')
    PGMDRECBED= st.text_input('Did doctore recommend bed rest','Type Here')
    PGMWTCHANUP= st.text_input('Pounds mother gained  pregnancy','Type Here')
    BORNCONGEN= st.text_input('Any congenital problems for child','Type Here')
    MOMAGEATBORN= st.text_input('Age of Mother','Type Here')
   # code for prediction
    diagnosis= ''

   #creating a button for pres
    if st.button('premie Prediction') :
        diagnosis= premie_pred([CHEBMOM,PGMECLAMP,PGMHYPER,PGMEMBOL,PGMUTI,
        PGMSUGUR,PGMSUGBL,PGMDIAB,PGMABNCORD,PGMABNPLAC,PGMAVAGBLED,PGMTRANQFREQ,
        PGMDRECBED,PGMWTCHANUP,BORNCONGEN,MOMAGEATBORN])
       
        
    st.success('The probability of you having a preemie is {}'.format(diagnosis))
    
if __name__ =='__main__':
    main()