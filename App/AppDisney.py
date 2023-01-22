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

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
#importer la librairie NLTK
import nltk
#installer "Stopwords corpus" à partir de l'onglet "CORPORA"
#nltk.download()
#chargement des posts dans une liste
import os
os.chdir(r"C:\Users\f_ati\Documents\Master2\TextMining\Projet\App\data")

#import pandas
import pandas as pd
disneys_Hotel_NewYork = pd.read_csv("Disney_Hotel_NewYork.csv",sep=",",header=0)
Disneys_Davy_Crocket_Ranch=pd.read_csv("Disney_Davy_Crocket_Ranch.csv",sep=",",header=0)




#engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/test')
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
    
############################################# HOME ##################################################################################
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
    
################################################## DATA #####################################################################################
elif choose == "Data":
    
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Databases Park and Hotel </p>', unsafe_allow_html=True)

        

    #query = "SELECT * FROM test"
    #df = pd.read_sql(query, con=engine)
    #st.dataframe(df)
################################################## ANALYSE PARC #################################################################################  
elif choose == "Analyse Parc":
    st.write("# Google Review Analyzer 🎆🪄 ")
    #Import of the 'sitereview' table 
    
    #query_ReviewText_park = "SELECT ReviewText,RewiewVisite FROM sitereview "
    #ReviewText = pd.read_sql(query_ReviewText_park, con=engine)
    #ReviewText["COMMENTAIRE"] = ReviewText["COMMENTAIRE"].astype(str)
    #st.write(ReviewText)
################################################## ANALYSE HOTEL Traitement nltk stopwords ################################################################################
elif choose == "Analyse Hotel":
    #nltk.download('stopwords')
    #charger les stopwords
    from nltk.corpus import stopwords
    stwf = stopwords.words('french')
  
    #fonction pour ne garder que le commentaire traduit
    def find_between( s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index(last)
            return s[start:end]
        except ValueError:
            return ""
    
    
    
    #création d'une nouvelle colonne avce uniquement le commentaire traduit
    disneys_Hotel_NewYork['Review Text'] = disneys_Hotel_NewYork['Review Text'].apply(lambda x: find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
    Disneys_Davy_Crocket_Ranch['Review Text'] = Disneys_Davy_Crocket_Ranch['Review Text'].apply(lambda x: find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
    
    stwf = [word for word in stwf if word not in stopwords.words('french')]
    stwf.extend([word for word in stwf if (len(word) > 3)])
    stwf.extend(['zero','un','deux','trois','quatre','cinq','six','sept','huit','neuf','dix','plus','très','parc','tout','disney','disneyland','sud','si','le','nous','de','et','la','les','vous','pour','que','pas','est','il','je','des',
                 'des','une','en','dans','était','ai','ne','été','au','ils','sont','du','avec','mais','ne','qui','ce','qu','fois','avons','même','car','ma','vraiment','ou','par','ont','moins','notre','paris','chien','à',"c'est","a","cela",
                 "sur","br","sommes","j'ai","ce","y","peu","au","jour","faire","être","se","tous","'","donc","qu'il","qu'elle","n'est","d'une","c'était","votre","ça","ici","étaient"])
    #print(stwf)
    


########################################## PLOT ######################################################




    row1_1, row1_2 = st.columns((1,1))
    tab1, tab2 = st.tabs(["World Cloud Disney's Hotel NewYork", "  Disneys_Davy_Crocket_Ranch World Cloud "])

    st.set_option('deprecation.showPyplotGlobalUse', False)
    #WORD CLOUD POUR TOUS
    text = disneys_Hotel_NewYork['Review Text'].str.cat(sep=' ')
    stopwords =stwf
    wordcloud = WordCloud(colormap='twilight',background_color='white',stopwords=stopwords).generate(text)
    text1 = Disneys_Davy_Crocket_Ranch['Review Text'].str.cat(sep=' ')
    wordcloud1 = WordCloud(colormap='twilight',background_color='white',stopwords=stopwords).generate(text1)
    # Afficher le wordcloud
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    #plt.show()
    with tab1:
       
        st.pyplot()
    with tab2:
        plt.imshow(wordcloud1, interpolation='bilinear')
        plt.axis("off")
       
        st.pyplot()
    
    

    
    
    
    
    
    
  