#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# sources:
# docs.streamlit.io/library/get-started

# In[ ]:





# # Introduction

# In[1]:


# Import Libraries
import numpy as np
import pandas as pd

pd.set_option("display.precision", 2)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 200)
pd.set_option('display.float_format', lambda x: '%.5f' % x)
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

import plotly.figure_factory as ff


# ## Streamlit

# In[2]:


import streamlit as st


# In[25]:


from PIL import Image

#github format 
image = Image.open('images/9base_white.png')
#jupyter notebook format
#image = Image.open(r'C:/Users/b7tbu/NINEBASE/ninebase/images/9base_white.png')

st.image(image)


# In[3]:


st.set_page_config(
    page_title="9base",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


# In[19]:


#from st_pages import Page, Section, show_pages, add_page_title

##⚾🥇

#add_page_title() # By default this also adds indentation

## Specify what pages should be shown in the sidebar, and what their titles and icons should be
#show_pages(
#    [
#        Section("14 Day", icon="🥇"),
#        Section("Season", icon="♂️"),
#        Page("player_batting_season.py", "Player Batting", "🏠"),
#    ]
#)


# In[ ]:





# In[ ]:





# ## Load Data

# In[4]:


# Format for GitHub
df = pd.read_csv('data_storage/player_batting_season.csv')

# Format for Jupyter Notebook
#df = pd.read_csv('C:/Users/b7tbu/NINEBASE/ninebase/data_storage/player_batting_season.csv')


# In[6]:


df.head()


# ## Scatter Chart

# In[7]:


import plotly.express as px


# In[8]:


fig = px.scatter(
    df.query("Season==2023"),
    x = "wRC+",
    y = "Hard%+",
    color = "Team",
    hover_name = "Name",
    log_x = True,
    size_max = 60,
)


# In[9]:


#st.plotly_chart(fig, theme="streamlit", use_container_width = True)


# ## Filters

# In[10]:


# calculate min/max/mean for slider
min_AB = df['AB'].min()
max_AB = df['AB'].max()
mean_AB = df['AB'].mean()

# float em
min_AB = float(min_AB)
max_AB = float(max_AB)
mean_AB = float(mean_AB)


# In[11]:


# slider

ab_slider = st.slider('At Bat Range', min_AB, max_AB, (mean_AB, max_AB))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[12]:


## Sidebar


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Columns

# In[13]:


col1, col2 = st.columns([2,1])


# In[14]:


col1.subheader("Scatter Chart")
col1.plotly_chart(fig, theme="streamlit", use_container_width = True)

col2.subheader("Filters")
col2.write(ab_slider)


# In[ ]:





# In[ ]:





# ## Raw Data Section

# In[15]:


from st_aggrid import AgGrid


# In[20]:


st.divider()
st.subheader('Data')
AgGrid(df)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




