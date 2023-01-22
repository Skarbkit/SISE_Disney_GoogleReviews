# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time  # to simulate a real time data, time loop
import fonctions as f
import numpy as np  # np mean, np random
import pandas as pd  # 
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
from sqlalchemy import create_engine
from streamlit_option_menu import option_menu
import streamlit as st
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from pprint import pprint
#importer la librairie NLTK
import nltk
#installer "Stopwords corpus" à partir de l'onglet "CORPORA"
#nltk.download()
#chargement des posts dans une liste
import os
os.chdir(r"C:\Users\f_ati\Documents\Master2\TextMining\Projet\App\data")

#import pandas
import pandas as pd
Disneys_Hotel_NewYork = pd.read_csv("Disney_Hotel_NewYork.csv",sep=",",header=0)
Disneys_Davy_Crocket_Ranch=pd.read_csv("Disney_Davy_Crocket_Ranch.csv",sep=",",header=0)
Disney_Hotel_Cheyenne = pd.read_csv("Disney_Hotel_Cheyenne.csv",sep=",",header=0)
Disney_Hotel_Santa_Fe=pd.read_csv("Disney_Hotel_Santa_Fe.csv",sep=",",header=0)
Disney_Sequoia_Lodge=pd.read_csv("Disney_Sequoia_Lodge.csv",sep=",",header=0)
Disney_Newport_Bay_Club=pd.read_csv("Disney_Newport_Bay_Club.csv",sep=",",header=0)




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
################################################## Traitement nltk stopwords WordNetLemmatizer ################################################################################
elif choose == "Analyse Hotel":
    #nltk.download('stopwords')
    #charger les stopwords
    from nltk.corpus import stopwords
    stwf = stopwords.words('french')
   
    
    #fonction pour ne garder que le commentaire traduit
    
    
    
    
    #création d'une nouvelle colonne avce uniquement le commentaire traduit
    Disneys_Hotel_NewYork['Review Text'] = Disneys_Hotel_NewYork['Review Text'].apply(lambda x: f.find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
    Disneys_Davy_Crocket_Ranch['Review Text'] = Disneys_Davy_Crocket_Ranch['Review Text'].apply(lambda x: f.find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
    
    Disney_Hotel_Cheyenne['Review Text'] = Disney_Hotel_Cheyenne['Review Text'].apply(lambda x: f.find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
    Disney_Hotel_Santa_Fe['Review Text'] = Disney_Hotel_Santa_Fe['Review Text'].apply(lambda x: f.find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
   
    Disney_Sequoia_Lodge['Review Text'] = Disney_Sequoia_Lodge['Review Text'].apply(lambda x: f.find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
    Disney_Newport_Bay_Club['Review Text'] = Disney_Newport_Bay_Club['Review Text'].apply(lambda x: f.find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
   
    stwf = [word for word in stwf if word not in stopwords.words('french')]
    stwf.extend([word for word in stwf if (len(word) > 3)])
    stwf.extend(['zero','un','deux','trois','quatre','cinq','six','sept','huit','neuf','dix','plus','très','parc','tout','disney','disneyland','sud','si','le','nous','de','et','la','les','vous','pour','que','pas','est','il','je','des',
                 'des','une','en','dans','était','ai','ne','été','au','ils','sont','du','avec','mais','ne','qui','ce','qu','fois','avons','même','car','ma','vraiment','ou','par','ont','moins','notre','paris','chien','à',"c'est","a","cela",
                 "sur","br","sommes","j'ai","ce","y","peu","au","jour","faire","être","se","tous","'","donc","qu'il","qu'elle","n'est","d'une","c'était","votre","ça","ici","étaient"])
    #print(stwf)
    
   #WORD CLOUD POUR TOUS
   
    stopwords =stwf
    text = Disneys_Hotel_NewYork['Review Text'].str.cat(sep=' ')
    wordcloud = WordCloud(colormap='twilight',background_color='white',stopwords=stopwords).generate(text)
  
    
   #print(wordcloud)
   
    text1 = Disneys_Davy_Crocket_Ranch['Review Text'].str.cat(sep=' ')
    wordcloud1 = WordCloud(colormap='twilight',background_color='white',stopwords=stopwords).generate(text1)
  
    text2 = Disney_Hotel_Cheyenne['Review Text'].str.cat(sep=' ')
    wordcloud2 = WordCloud(colormap='twilight',background_color='white',stopwords=stopwords).generate(text2)
    text3 = Disney_Hotel_Santa_Fe['Review Text'].str.cat(sep=' ')
    wordcloud3 = WordCloud(colormap='twilight',background_color='white',stopwords=stopwords).generate(text3)
   
    text4 = Disney_Sequoia_Lodge['Review Text'].str.cat(sep=' ')
    wordcloud4 = WordCloud(colormap='twilight',background_color='white',stopwords=stopwords).generate(text4)
    text5 = Disney_Newport_Bay_Club['Review Text'].str.cat(sep=' ')
    wordcloud5 = WordCloud(colormap='twilight',background_color='white',stopwords=stopwords).generate(text5)
   
  

########################################## ANALYSE HOTEL Graphique ######################################################

    
    
        
        
        
    # Graphique Histogramme fréquence mots
    st.title("Histogramme frequence des mots")
    
    parseur = CountVectorizer(stop_words=stwf)
    X = parseur.fit_transform(Disneys_Hotel_NewYork['Review Text'].values.astype('U'))
  
    mdt = X.toarray()
    freq_mots = np.sum(mdt,axis=0)
    
    index = np.argsort(freq_mots)
    imp = {'terme':np.asarray(parseur.get_feature_names_out())[index],'freq':freq_mots[index]}
    imp1 = pd.DataFrame.from_dict(imp, orient= 'columns')
    imp2 = imp1.sort_values(by = 'freq', ascending = False)
    nbmots = np.sum(mdt,axis=0)
    print(pd.DataFrame(imp))
    f.motfreq(imp2, 10)
   
    
   
    
   
    
   
    tab1, tab2, tab3,tab4,tab5,tab6 = st.tabs(["World Cloud Disney's Hotel NewYork", "World Cloud Disneys_Davy_Crocket_Ranch","World Cloud Disney_Hotel_Cheyenne","World Cloud Disney_Hotel_Santa_Fe","World Cloud Disney_Sequoia_Lodge","World Cloud Disney_Newport_Bay_Club"])

    st.set_option('deprecation.showPyplotGlobalUse', False)
 
   
    
    with tab1:
        # Afficher le wordcloud
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot()
    with tab2:
        plt.imshow(wordcloud1, interpolation='bilinear')
        plt.axis("off")
       
        st.pyplot()
        
    with tab3:
         # Afficher le wordcloud
         plt.imshow(wordcloud2, interpolation='bilinear')
         plt.axis("off")
         st.pyplot()
    with tab4:
         plt.imshow(wordcloud3, interpolation='bilinear')
         plt.axis("off")
        
         st.pyplot()
    with tab5:
         # Afficher le wordcloud
         plt.imshow(wordcloud4, interpolation='bilinear')
         plt.axis("off")
         st.pyplot()
    with tab6:
         plt.imshow(wordcloud5, interpolation='bilinear')
         plt.axis("off")
        
         st.pyplot()
    
    
    

   
  