# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 15:31:00 2023

@author: f_ati
"""

import streamlit as st  # 🎈 data web app development
import numpy as np
import pandas as pd
import plotly.express as px  # interactive charts
import plotly.graph_objects as go

def motfreq(df, nbmots, title=''):
    
    height = df["freq"].head(nbmots)
    bars = df["terme"].head(nbmots)
    if title !='':
        fig = go.Figure(data=[go.Bar(x=bars, y=height)])
        fig.update_layout(xaxis_tickangle=-90,title=title)
        
    else:
        fig = go.Figure(data=[go.Bar(x=bars, y=height)])
        fig.update_layout(xaxis_tickangle=-90)
    return st.plotly_chart(fig)
    
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index(last)
        return s[start:end]
    except ValueError:
        return ""
  
def create_pie(data, values, names, title=''): 
    
    if title !='':
        
        fig = px.pie(data, values=values, names=names,title=title)
        fig.update_traces(textposition='inside', textinfo='percent+label')
    else:
        fig = px.pie(data, values=values, names=names)
        fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig
    
def create_histogram(data, colx, color, title=''):
    if title !='':
        fig = px.histogram(data, x=colx, color=color, title=title)
    else:
        fig = px.histogram(data, x=colx, color=color)
    return fig


