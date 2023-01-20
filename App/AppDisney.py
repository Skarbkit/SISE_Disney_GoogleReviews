# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # 
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
from sqlalchemy import create_engine
from streamlit_option_menu import option_menu
import streamlit as st






with st.sidebar:
    choose = option_menu("App Disney", ["Home", "Analyse Parc", "Analyse Hotel", "Data"],
                         icons=['house', 'kanban', 'kanban', 'book'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )
    

if choose == "Home":
    st.write("# Google Review Analyzer 🎆🪄 ")

    st.image('disney.png',width=600)




    names = ['Fatimetou HAIDARA', 'Louison PAPAZIAN','Florian RICARD',  'Kenan REYNAUD']

    # Use st.write to print the names one by one
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Contributors:</p>', unsafe_allow_html=True)  
 
    for name in names:
        st.write(name)   
    
    
elif choose == "Data":
    
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Databases Park and Hotel </p>', unsafe_allow_html=True)

        engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/test')


    #query = "SELECT * FROM test"
    #df = pd.read_sql(query, con=engine)
    #st.dataframe(df)


 