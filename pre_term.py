# -*- coding: utf-8 -*-
"""
Created on Sat May 14 23:20:06 2022

@author: 18329
"""

import streamlit as st
dataset= st.beta_container()
with dataset:
    st.title('Pre-Term Predictions')
    st.header('20 years of responses from the National Health Interview Survey')
    st.text('Investigated how maternal characteristics during pregnancy affected birth outcomes')
    