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


#chargement des posts dans une liste
import os
os.chdir(r"C:\Users\f_ati\Documents\Master2\TextMining\Projet\App")

#Importations csv
#Hotel
Disneys_Hotel_NewYork = pd.read_csv(r"data\Disney_Hotel_NewYork.csv",sep=",",header=0)
Disneys_Davy_Crocket_Ranch=pd.read_csv(r"data\Disney_Davy_Crocket_Ranch.csv",sep=",",header=0)
Disney_Hotel_Cheyenne = pd.read_csv(r"data\Disney_Hotel_Cheyenne.csv",sep=",",header=0)
Disney_Hotel_Santa_Fe=pd.read_csv(r"data\Disney_Hotel_Santa_Fe.csv",sep=",",header=0)
Disney_Sequoia_Lodge=pd.read_csv(r"data\Disney_Sequoia_Lodge.csv",sep=",",header=0)
Disney_Newport_Bay_Club=pd.read_csv(r"data\Disney_Newport_Bay_Club.csv",sep=",",header=0)

Disneys_Hotel_NewYork['type']="Hotel_NewYork"
Disneys_Davy_Crocket_Ranch['type']="Davy_Crocket_Ranch"
Disney_Hotel_Cheyenne['type']="Hotel_Cheyenne"
Disney_Hotel_Santa_Fe['type']="Hotel_Santa_Fe"
Disney_Sequoia_Lodge['type']="Sequoia_Lodge"
Disney_Newport_Bay_Club['type']="Newport_Bay_Club"

# merge files
dataHotel = pd.concat( [Disneys_Hotel_NewYork,Disneys_Davy_Crocket_Ranch,Disney_Hotel_Cheyenne,Disney_Hotel_Santa_Fe,Disney_Sequoia_Lodge,Disney_Newport_Bay_Club], axis=0,
            join="outer",
            ignore_index=True,
            keys=None,
            levels=None,
            names=None,
            verify_integrity=False,
            copy=True,)
print(dataHotel)

#Parc
Disneyland_Paris=pd.read_csv(r"data\Disneyland_Paris.csv",sep=",",header=0)
Parc_Walt_Disney_Studios=pd.read_csv(r"data\Parc_Walt_Disney_Studios.csv",sep=",",header=0)

#fonction pour ne garder que le commentaire traduit
    
#création d'une nouvelle colonne avce uniquement le commentaire traduit

Disneys_Hotel_NewYork['Review Text'] = Disneys_Hotel_NewYork['Review Text'].apply(lambda x: f.find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
Disneys_Davy_Crocket_Ranch['Review Text'] = Disneys_Davy_Crocket_Ranch['Review Text'].apply(lambda x: f.find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
    
Disney_Hotel_Cheyenne['Review Text'] = Disney_Hotel_Cheyenne['Review Text'].apply(lambda x: f.find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
Disney_Hotel_Santa_Fe['Review Text'] = Disney_Hotel_Santa_Fe['Review Text'].apply(lambda x: f.find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
   
Disney_Sequoia_Lodge['Review Text'] = Disney_Sequoia_Lodge['Review Text'].apply(lambda x: f.find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
Disney_Newport_Bay_Club['Review Text'] = Disney_Newport_Bay_Club['Review Text'].apply(lambda x: f.find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
Disneyland_Paris['Review Text'] = Disneyland_Paris['Review Text'].apply(lambda x: f.find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
Parc_Walt_Disney_Studios['Review Text'] = Parc_Walt_Disney_Studios['Review Text'].apply(lambda x: f.find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
      

from nltk.corpus import stopwords
stwf = stopwords.words('french')

stwf = [word for word in stwf if word not in stopwords.words('french')]
stwf.extend([word for word in stwf if (len(word) > 3)])
stwf.extend(['zero','un','deux','trois','quatre','cinq','six','sept','huit','neuf','dix','plus','très','parc','tout','disney','disneyland','sud','si','le','nous','de','et','la','les','vous','pour','que','pas','est','il','je','des',
             'des','une','en','dans','était','ai','ne','été','au','ils','sont','du','avec','mais','ne','qui','ce','qu','fois','avons','petit','plus','même','car','ma','vraiment','ou','par','ont','chambres','moins','notre','paris','chien','à',"c'est","a","cela",
             "sur","br","sommes","j'ai","ce","y","peu","au","jour","faire","être","se","tous","'","donc","qu'il","qu'elle","l'hôtel","n'est","d'une","c'était","votre","ça","ici","étaient"])

stopwords =stwf
############################################ Filtre #############################################################





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

    st.image(r'data\disney.png',width=600)




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
        # Create a list of options for the dropdown menu
        options = dataHotel['type'].unique()

        # Create a dropdown menu
        selected_option = st.selectbox("Select Hotel to filter by:", options)

        # Filter the DataFrame based on the selected option
        filtered_df = dataHotel[dataHotel['type'] == selected_option]
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Databases Hotel </p>', unsafe_allow_html=True)

        # Display the filtered DataFrame
        st.dataframe(filtered_df)


################################################## ANALYSE PARC #################################################################################  
elif choose == "Analyse Parc":
    st.write("# Google Review Analyzer 🎆🪄 ")
    
    
   
    #création d'une nouvelle colonne avce uniquement le commentaire traduit

    text6 = Disneyland_Paris['Review Text'].str.cat(sep=' ')
    wordcloud6 = WordCloud(colormap='twilight',background_color='white',stopwords=stopwords).generate(text6)
    text7 = Parc_Walt_Disney_Studios['Review Text'].str.cat(sep=' ')
    wordcloud7 = WordCloud(colormap='twilight',background_color='white',stopwords=stopwords).generate(text7)
    
    # Graphique Histogramme fréquence mots
    st.title("Histogramme frequence des mots")
    
    parseur = CountVectorizer(stop_words=stwf)
    X = parseur.fit_transform(Disneyland_Paris['Review Text'].values.astype('U'))
  
    mdt = X.toarray()
    freq_mots = np.sum(mdt,axis=0)
    
    index = np.argsort(freq_mots)
    imp = {'terme':np.asarray(parseur.get_feature_names_out())[index],'freq':freq_mots[index]}
    imp1 = pd.DataFrame.from_dict(imp, orient= 'columns')
    imp2 = imp1.sort_values(by = 'freq', ascending = False)
    nbmots = np.sum(mdt,axis=0)
    print(pd.DataFrame(imp))
    f.motfreq(imp2, 10)
   
    
   
    
   # Graphique Histogramme des sentiments
   
    Disneyland_Paris['Review Visite'] = pd.to_datetime(Disneyland_Paris['Review Visite'],format='%m/%Y', errors='coerce')
    Disneyland_Paris['month'] = Disneyland_Paris['Review Visite'].dt.month
   
   
       
    tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
   
    senti_list = []
    for i in Disneyland_Paris["Review Text"]:
       vs = tb(i).sentiment[0]
       if (vs > 0):
           senti_list.append('Positive')
       elif (vs < 0):
           senti_list.append('Negative')
       else:
           senti_list.append('Neutral')
   
    Disneyland_Paris["sentiment"]=senti_list
    Disneyland_Paris["sentiment"]=Disneyland_Paris["sentiment"].astype('category')
   

    
    fig=f.create_histogram(Disneyland_Paris,colx="month",color="sentiment",title="Repartiton par sentiments")
    st.plotly_chart(fig, use_container_width=True)
    

    
    
    
    
    
    tab1, tab2 = st.tabs(["World Cloud Disneyland Paris", "World Cloud Parc_Walt_Disney_Studios"])

    st.set_option('deprecation.showPyplotGlobalUse', False)


    
    with tab1:
        # Afficher le wordcloud
        plt.imshow(wordcloud6, interpolation='bilinear')
        plt.axis("off")
        st.pyplot()
    with tab2:
        plt.imshow(wordcloud7, interpolation='bilinear')
        plt.axis("off")
       
        st.pyplot()
    #Import of the 'sitereview' table 
    
    #query_ReviewText_park = "SELECT ReviewText,RewiewVisite FROM sitereview "
    #ReviewText = pd.read_sql(query_ReviewText_park, con=engine)
    #ReviewText["COMMENTAIRE"] = ReviewText["COMMENTAIRE"].astype(str)
    #st.write(ReviewText)
################################################## ANALYSE HOTEL Graphique ################################################################################
elif choose == "Analyse Hotel":
    
    # Create a list of options for the dropdown menu
    options = dataHotel['type'].unique()

    # Create a dropdown menu
    selected_option = st.selectbox("Select Hotel to filter by:", options)

    # Filter the DataFrame based on the selected option
    filtered_df = dataHotel[dataHotel['type'] == selected_option]
    
    dataHotel['Review Text'] = dataHotel['Review Text'].apply(lambda x: f.find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
    
    
    # Graphique Histogramme fréquence mots
  
    
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
    
    
   
    # Graphique Histogramme des sentiments
    
    Disney_Hotel_Santa_Fe['Review Visite'] = pd.to_datetime(Disney_Hotel_Santa_Fe['Review Visite'],format='%m/%Y', errors='coerce')
    Disney_Hotel_Santa_Fe['month'] = Disney_Hotel_Santa_Fe['Review Visite'].dt.month
    
    
        
    tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    
    senti_list = []
    for i in Disney_Hotel_Santa_Fe["Review Text"]:
        vs = tb(i).sentiment[0]
        if (vs > 0):
            senti_list.append('Positive')
        elif (vs < 0):
            senti_list.append('Negative')
        else:
            senti_list.append('Neutral')
    
    Disney_Hotel_Santa_Fe["sentiment"]=senti_list
    Disney_Hotel_Santa_Fe["sentiment"]=Disney_Hotel_Santa_Fe["sentiment"].astype('category')
    

    
 
    
    fig=f.create_histogram(Disney_Hotel_Santa_Fe,colx="month",color="sentiment",title="Repartiton par sentiments")
    st.plotly_chart(fig, use_container_width=True)
    
    fig2=f.create_histogram(Disney_Hotel_Santa_Fe,colx="month",color="Review Voyage Type",title="Repartion par titre")
    st.plotly_chart(fig2, use_container_width=True)
    
    
    
    
    
    
    
    
   #WORD CLOUD POUR TOUS
   
    stopwords =stwf
    text = dataHotel['Review Text'].str.cat(sep=' ')
    wordcloud = WordCloud(colormap='twilight',background_color='white',stopwords=stopwords).generate(text)
    
 
    # Graphique Histogramme fréquence mots
   
    #tab1, tab2, tab3,tab4,tab5,tab6 = st.tabs(["World Cloud Disney's Hotel NewYork", "World Cloud Disneys_Davy_Crocket_Ranch","World Cloud Disney_Hotel_Cheyenne","World Cloud Disney_Hotel_Santa_Fe","World Cloud Disney_Sequoia_Lodge","World Cloud Disney_Newport_Bay_Club"])

    st.set_option('deprecation.showPyplotGlobalUse', False)
 

    
    if selected_option=="Hotel_NewYork":
        # Afficher le wordcloud
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot()
    elif selected_option=="Davy_Crocket_Ranch":
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
       
        st.pyplot()
        
    elif selected_option=="Hotel_Cheyenne":
         # Afficher le wordcloud
         plt.imshow(wordcloud, interpolation='bilinear')
         plt.axis("off")
         st.pyplot()
    elif selected_option=="Hotel_Santa_Fe":
         plt.imshow(wordcloud, interpolation='bilinear')
         plt.axis("off")
        
         st.pyplot()
    elif selected_option=="Sequoia_Lodge":
         # Afficher le wordcloud
         plt.imshow(wordcloud, interpolation='bilinear')
         plt.axis("off")
         st.pyplot()
    elif selected_option=="Newport_Bay_Club":
         plt.imshow(wordcloud, interpolation='bilinear')
         plt.axis("off")
        
         st.pyplot()
    
    
    

   
  