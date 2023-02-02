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
#Parc
Disneyland_Paris=pd.read_csv(r"data\Disneyland_Paris.csv",sep=",",header=0)
Parc_Walt_Disney_Studios=pd.read_csv(r"data\Parc_Walt_Disney_Studios.csv",sep=",",header=0)


Disneys_Hotel_NewYork['type']="Hotel_NewYork"
Disneys_Davy_Crocket_Ranch['type']="Davy_Crocket_Ranch"
Disney_Hotel_Cheyenne['type']="Hotel_Cheyenne"
Disney_Hotel_Santa_Fe['type']="Hotel_Santa_Fe"
Disney_Sequoia_Lodge['type']="Sequoia_Lodge"
Disney_Newport_Bay_Club['type']="Newport_Bay_Club"

Disneyland_Paris['type']="Disneyland_Paris"
Parc_Walt_Disney_Studios['type']="Parc_Walt_Disney_Studios"

# merge files
dataHotel = pd.concat( [Disneys_Hotel_NewYork,Disneys_Davy_Crocket_Ranch,Disney_Hotel_Cheyenne,Disney_Hotel_Santa_Fe,Disney_Sequoia_Lodge,Disney_Newport_Bay_Club], axis=0,
            join="outer",
            ignore_index=True,
            keys=None,
            levels=None,
            names=None,
            verify_integrity=False,
            copy=True)
print(dataHotel)


dataParc = pd.concat([Disneyland_Paris,Parc_Walt_Disney_Studios],axis=0,
            join="outer",
            ignore_index=True,
            keys=None,
            levels=None,
            names=None,
            verify_integrity=False,
            copy=True )

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
             'des','une','en','dans','était','ai','ne','été','au','ils','sont','du','avec','mais','ne','qui','ce','qu','fois','avons','petit','plus','même','car','ma','vraiment','hôtel','ou','par','ont','chambres','moins','notre','paris','chien','à',"c'est","a","cela",
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
    
    # Create a list of options for the dropdown menu
    options = dataHotel['type'].unique()
    st.sidebar.title("Filtres : ")
  
    # Create a dropdown menu
    selected_option = st.selectbox("Select Hotel to filter:", options)
  
    # Filter the DataFrame based on the selected option
    filtered = dataHotel[dataHotel['type'] == selected_option]
    
    filtered['Review Text'] = filtered['Review Text'].apply(lambda x: f.find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
    
    
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
        st.markdown('<p class="font">Databases Hotel </p>', unsafe_allow_html=True)
       
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        
        # Display the filtered DataFrame
        st.dataframe(filtered)
        st.markdown('<p class="font">Databases Park </p>', unsafe_allow_html=True)
        # Create a list of options for the dropdown menu
        optionsParc = dataParc['type'].unique()
        
        # Create a dropdown menu
        selected_option1 = st.selectbox("Select Parc to filter by:", optionsParc)
        
        # Filter the DataFrame based on the selected option
        filtered_df1 = dataParc[dataParc['type'] == selected_option1]
        dataParc['Review Text'] = dataParc['Review Text'].apply(lambda x: f.find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
        

       
        st.dataframe(filtered_df1)


################################################## ANALYSE PARC #################################################################################  
elif choose == "Analyse Parc":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Analyses des Parcs  </p>', unsafe_allow_html=True)
    # Create a list of options for the dropdown menu
    optionsParc = dataParc['type'].unique()
    
    # Create a dropdown menu
    selected_option = st.selectbox("Select Parc to filter by:", optionsParc)
    
    # Filter the DataFrame based on the selected option
    filtered_df = dataParc[dataParc['type'] == selected_option]
    filtered_df['Review Text'] = filtered_df['Review Text'].apply(lambda x: f.find_between(str(x), "(Traduit par Google)" ,"(Avis d'origine)"))
    

    
    #création d'une nouvelle colonne avce uniquement le commentaire traduit

    text6 = filtered_df['Review Text'].str.cat(sep=' ')
    wordcloud1 = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black', colormap='Set2', collocations=False,stopwords=stopwords).generate(text6)
   
    
######################################################### Graphique ###########################################################"
    


    



    # Graphique Histogramme fréquence mots
    
    
    if selected_option=="Disneyland_Paris":
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
        f.motfreq(imp2, 10,title="Histogramme frequence des mots: Disneyland Paris")
        fig=f.create_histogram(Disneyland_Paris, colx="Review Rate", color ="Review Rate",title="Repartiton des notes")
        st.plotly_chart(fig, use_container_width=True)
    elif selected_option=="Parc_Walt_Disney_Studios":
        parseur = CountVectorizer(stop_words=stwf)
        X = parseur.fit_transform(Parc_Walt_Disney_Studios['Review Text'].values.astype('U'))
      
        mdt = X.toarray()
        freq_mots = np.sum(mdt,axis=0)
        
        index = np.argsort(freq_mots)
        imp = {'terme':np.asarray(parseur.get_feature_names_out())[index],'freq':freq_mots[index]}
        imp1 = pd.DataFrame.from_dict(imp, orient= 'columns')
        imp2 = imp1.sort_values(by = 'freq', ascending = False)
        nbmots = np.sum(mdt,axis=0)
        print(pd.DataFrame(imp))
        f.motfreq(imp2, 10,title="Histogramme frequence des mots: Parc Walt Disney Studios")
        fig=f.create_histogram(Parc_Walt_Disney_Studios, colx="Review Rate", color ="Review Rate",title="Repartiton des notes")
        st.plotly_chart(fig, use_container_width=True)
    
   # Graphique Histogramme des sentiments
   
    Disneyland_Paris['Review Visite'] = pd.to_datetime(Disneyland_Paris['Review Visite'],format='%m/%Y', errors='coerce')
    Disneyland_Paris['month'] = Disneyland_Paris['Review Visite'].dt.month
    Parc_Walt_Disney_Studios['Review Visite'] = pd.to_datetime(Parc_Walt_Disney_Studios['Review Visite'],format='%m/%Y', errors='coerce')
    Parc_Walt_Disney_Studios['month'] = Parc_Walt_Disney_Studios['Review Visite'].dt.month
   
   
       
    tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
   
    senti_list = []
    if selected_option=="Disneyland_Paris":
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
       
        #fig=f.create_histogram(Disneyland_Paris,colx="month",color="sentiment",title="Repartiton par sentiments Disneyland Paris")
        fig=f.create_pie(Disneyland_Paris, values="month", names="sentiment",title="Repartiton par sentiments Disneyland Paris")
        st.plotly_chart(fig, use_container_width=True)
        
        
    elif selected_option=="Parc_Walt_Disney_Studios":
        for i in Parc_Walt_Disney_Studios["Review Text"]:
           vs = tb(i).sentiment[0]
           if (vs > 0):
               senti_list.append('Positive')
           elif (vs < 0):
               senti_list.append('Negative')
           else:
               senti_list.append('Neutral')
       
        Parc_Walt_Disney_Studios["sentiment"]=senti_list
        Parc_Walt_Disney_Studios["sentiment"]=Parc_Walt_Disney_Studios["sentiment"].astype('category')
       
        #fig=f.create_histogram(Parc_Walt_Disney_Studios,colx="month",color="sentiment",title="Repartiton par sentiments Parc Walt Disney Studios")
        fig=f.create_pie(Parc_Walt_Disney_Studios, values="month", names="sentiment",title="Repartiton par sentiments Parc_Walt_Disney_Studios")
        st.plotly_chart(fig, use_container_width=True)
    

    
    
    
            
   

    st.set_option('deprecation.showPyplotGlobalUse', False)

     # Afficher le wordcloud
    if selected_option=="Disneyland_Paris":
        # Afficher le wordcloud
        plt.imshow(wordcloud1, interpolation='bilinear')
        plt.axis("off")
        
        st.pyplot()
        
    elif selected_option=="Parc_Walt_Disney_Studios":
        plt.imshow(wordcloud1, interpolation='bilinear')
        plt.axis("off")
        
        st.pyplot()
  
    #Import of the 'sitereview' table 
    
    #query_ReviewText_park = "SELECT ReviewText,RewiewVisite FROM sitereview "
    #ReviewText = pd.read_sql(query_ReviewText_park, con=engine)
    #ReviewText["COMMENTAIRE"] = ReviewText["COMMENTAIRE"].astype(str)
    #st.write(ReviewText)
################################################## ANALYSE HOTEL Graphique ################################################################################
elif choose == "Analyse Hotel":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Analyses des Hotles  </p>', unsafe_allow_html=True)
    
  
############################################## graphique #####################################"""""""    
    # Graphique Histogramme fréquence mots
  
    
    parseur = CountVectorizer(stop_words=stwf)
    #print(pd.DataFrame(imp))
    if selected_option=="Hotel_NewYork":
        X = parseur.fit_transform(filtered['Review Text'].values.astype('U'))
        mdt = X.toarray()
        freq_mots = np.sum(mdt,axis=0)
        
        index = np.argsort(freq_mots)
        imp = {'terme':np.asarray(parseur.get_feature_names_out())[index],'freq':freq_mots[index]}
        imp1 = pd.DataFrame.from_dict(imp, orient= 'columns')
        imp2 = imp1.sort_values(by = 'freq', ascending = False)
        nbmots = np.sum(mdt,axis=0)
        f.motfreq(imp2, 10,title="Histogramme frequence des mots")
        fig=f.create_histogram(filtered, colx="Review Rate", color ="Review Rate",title="Repartiton des notes")
        st.plotly_chart(fig, use_container_width=True)
    elif selected_option=="Davy_Crocket_Ranch":
         X = parseur.fit_transform(Disneys_Davy_Crocket_Ranch['Review Text'].values.astype('U'))
         mdt = X.toarray()
         freq_mots = np.sum(mdt,axis=0)
         
         index = np.argsort(freq_mots)
         imp = {'terme':np.asarray(parseur.get_feature_names_out())[index],'freq':freq_mots[index]}
         imp1 = pd.DataFrame.from_dict(imp, orient= 'columns')
         imp2 = imp1.sort_values(by = 'freq', ascending = False)
         nbmots = np.sum(mdt,axis=0)
         f.motfreq(imp2, 10,title="Histogramme frequence des mots")
         fig=f.create_histogram(Disneys_Davy_Crocket_Ranch, colx="Review Rate", color ="Review Rate",title="Repartiton des notes")
         st.plotly_chart(fig, use_container_width=True)
    elif selected_option=="Hotel_Cheyenne":
         X = parseur.fit_transform(Disney_Hotel_Cheyenne['Review Text'].values.astype('U'))
         mdt = X.toarray()
         freq_mots = np.sum(mdt,axis=0)
         
         index = np.argsort(freq_mots)
         imp = {'terme':np.asarray(parseur.get_feature_names_out())[index],'freq':freq_mots[index]}
         imp1 = pd.DataFrame.from_dict(imp, orient= 'columns')
         imp2 = imp1.sort_values(by = 'freq', ascending = False)
         nbmots = np.sum(mdt,axis=0)
         f.motfreq(imp2, 10,title="Histogramme frequence des mots")
         fig=f.create_histogram(Disney_Hotel_Cheyenne, colx="Review Rate", color ="Review Rate",title="Repartiton des notes")
         st.plotly_chart(fig, use_container_width=True)
    elif selected_option=="Hotel_Santa_Fe":
         X = parseur.fit_transform(Disney_Hotel_Santa_Fe['Review Text'].values.astype('U'))
         mdt = X.toarray()
         freq_mots = np.sum(mdt,axis=0)
         
         index = np.argsort(freq_mots)
         imp = {'terme':np.asarray(parseur.get_feature_names_out())[index],'freq':freq_mots[index]}
         imp1 = pd.DataFrame.from_dict(imp, orient= 'columns')
         imp2 = imp1.sort_values(by = 'freq', ascending = False)
         nbmots = np.sum(mdt,axis=0)
         f.motfreq(imp2, 10,title="Histogramme frequence des mots")
         fig=f.create_histogram(Disney_Hotel_Santa_Fe, colx="Review Rate", color ="Review Rate",title="Repartiton des notes")
         st.plotly_chart(fig, use_container_width=True)
    elif selected_option=="Sequoia_Lodge":
         X = parseur.fit_transform(Disney_Sequoia_Lodge['Review Text'].values.astype('U'))
         mdt = X.toarray()
         freq_mots = np.sum(mdt,axis=0)
         
         index = np.argsort(freq_mots)
         imp = {'terme':np.asarray(parseur.get_feature_names_out())[index],'freq':freq_mots[index]}
         imp1 = pd.DataFrame.from_dict(imp, orient= 'columns')
         imp2 = imp1.sort_values(by = 'freq', ascending = False)
         nbmots = np.sum(mdt,axis=0)
         f.motfreq(imp2, 10,title="Histogramme frequence des mots")
         fig=f.create_histogram(Disney_Sequoia_Lodge, colx="Review Rate", color ="Review Rate",title="Repartiton des notes")
         st.plotly_chart(fig, use_container_width=True)
    elif selected_option=="Newport_Bay_Club":
         X = parseur.fit_transform(Disney_Newport_Bay_Club['Review Text'].values.astype('U'))
         mdt = X.toarray()
         freq_mots = np.sum(mdt,axis=0)
         
         index = np.argsort(freq_mots)
         imp = {'terme':np.asarray(parseur.get_feature_names_out())[index],'freq':freq_mots[index]}
         imp1 = pd.DataFrame.from_dict(imp, orient= 'columns')
         imp2 = imp1.sort_values(by = 'freq', ascending = False)
         nbmots = np.sum(mdt,axis=0)
         f.motfreq(imp2, 10,title="Histogramme frequence des mots")
         fig=f.create_histogram(Disney_Newport_Bay_Club, colx="Review Rate", color ="Review Rate",title="Repartiton des notes")
         st.plotly_chart(fig, use_container_width=True)
    # Graphique Histogramme des sentiments
    
    
    

    
 
    if selected_option=="Hotel_NewYork":
        Disneys_Hotel_NewYork['Review Visite'] = pd.to_datetime(Disneys_Hotel_NewYork['Review Visite'],format='%m/%Y', errors='coerce')
        Disneys_Hotel_NewYork['month'] = Disneys_Hotel_NewYork['Review Visite'].dt.month
        
        
            
        tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
        
        senti_list = []
        
        for i in Disneys_Hotel_NewYork["Review Text"]:
            vs = tb(i).sentiment[0]
            if (vs > 0):
                senti_list.append('Positive')
            elif (vs < 0):
                senti_list.append('Negative')
            else:
                senti_list.append('Neutral')
        
        Disneys_Hotel_NewYork["sentiment"]=senti_list
        Disneys_Hotel_NewYork["sentiment"]=Disneys_Hotel_NewYork["sentiment"].astype('category')
        fig=f.create_pie(Disneys_Hotel_NewYork,values="month",names="sentiment",title="Repartiton par sentiments Hotel NewYork")
        st.plotly_chart(fig, use_container_width=True)
    
        fig2=f.create_pie(Disneys_Hotel_NewYork,values="month",names="Review Voyage Type",title="Repartion par titre Hotel NewYork")
        st.plotly_chart(fig2, use_container_width=True)

    elif selected_option=="Davy_Crocket_Ranch":
        Disneys_Davy_Crocket_Ranch['Review Visite'] = pd.to_datetime(Disneys_Davy_Crocket_Ranch['Review Visite'],format='%m/%Y', errors='coerce')
        Disneys_Davy_Crocket_Ranch['month'] = Disneys_Davy_Crocket_Ranch['Review Visite'].dt.month
        
        
            
        tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
        
        senti_list = []
        
        for i in Disneys_Davy_Crocket_Ranch["Review Text"]:
            vs = tb(i).sentiment[0]
            if (vs > 0):
                senti_list.append('Positive')
            elif (vs < 0):
                senti_list.append('Negative')
            else:
                senti_list.append('Neutral')
        
        Disneys_Davy_Crocket_Ranch["sentiment"]=senti_list
        Disneys_Davy_Crocket_Ranch["sentiment"]=Disneys_Davy_Crocket_Ranch["sentiment"].astype('category')
        fig=f.create_pie(Disneys_Davy_Crocket_Ranch,values="month",names="sentiment",title="Repartiton par sentiments Hotel NewYork")
        st.plotly_chart(fig, use_container_width=True)
    
        fig2=f.create_pie(Disneys_Davy_Crocket_Ranch,values="month",names="Review Voyage Type",title="Repartion par titre Hotel NewYork")
        st.plotly_chart(fig2, use_container_width=True)
    
    elif selected_option=="Hotel_Cheyenne":
        Disney_Hotel_Cheyenne['Review Visite'] = pd.to_datetime(Disney_Hotel_Cheyenne['Review Visite'],format='%m/%Y', errors='coerce')
        Disney_Hotel_Cheyenne['month'] = Disney_Hotel_Cheyenne['Review Visite'].dt.month
        
        
            
        tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
        
        senti_list = []
        
        for i in Disney_Hotel_Cheyenne["Review Text"]:
            vs = tb(i).sentiment[0]
            if (vs > 0):
                senti_list.append('Positive')
            elif (vs < 0):
                senti_list.append('Negative')
            else:
                senti_list.append('Neutral')
        
        Disney_Hotel_Cheyenne["sentiment"]=senti_list
        Disney_Hotel_Cheyenne["sentiment"]=Disney_Hotel_Cheyenne["sentiment"].astype('category')
        fig=f.create_pie(Disney_Hotel_Cheyenne,values="month",names="sentiment",title="Repartiton par sentiments Hotel NewYork")
        st.plotly_chart(fig, use_container_width=True)
    
        fig2=f.create_pie(Disney_Hotel_Cheyenne,values="month",names="Review Voyage Type",title="Repartion par titre Hotel NewYork")
        st.plotly_chart(fig2, use_container_width=True)
        
    elif selected_option=="Hotel_Santa_Fe":
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
       
        fig=f.create_pie(Disney_Hotel_Santa_Fe,values="month",names="sentiment",title="Repartiton par sentiments Hotel NewYork")
        st.plotly_chart(fig, use_container_width=True)
    
        fig2=f.create_pie(Disney_Hotel_Santa_Fe,values="month",names="Review Voyage Type",title="Repartion par titre Hotel NewYork")
        st.plotly_chart(fig2, use_container_width=True) 
        
   
    
    
   #WORD CLOUD POUR TOUS
   
    stopwords =stwf
    text = filtered['Review Text'].str.cat(sep=' ')
    wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black', colormap='Set2', collocations=False,stopwords=stopwords).generate(text)
    
 
    # Graphique Histogramme fréquence mots
   
  
    st.set_option('deprecation.showPyplotGlobalUse', False)
 

    
    if selected_option=="Hotel_NewYork":
        # Afficher le wordcloud
        
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.xticks([])
        plt.yticks([])
       
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
         plt.title("Nuage de mots ")
         st.pyplot()
    elif selected_option=="Newport_Bay_Club":
         plt.imshow(wordcloud, interpolation='bilinear',)
         plt.axis("off")
        
         st.pyplot()
    
    
    

   
  