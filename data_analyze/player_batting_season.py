#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# sources:
# docs.streamlit.io/library/get-started

# In[ ]:





# # Introduction

# In[29]:


# Import Libraries
import numpy as np
import pandas as pd

pd.set_option("display.precision", 2)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
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


# In[ ]:





# In[3]:


st.set_page_config(
    page_title="9base",
    page_icon="⚾",
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

# In[37]:


from st_aggrid import AgGrid, GridUpdateMode, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder


# In[ ]:





# In[34]:


# Simplify dataframe, narrow to most insightful columns
df_short = df[['Name', 'Team', 'Age', 'AB', 'BB%+', 'K%+', 'BABIP+', 'Hard%+', 'wRC+']]


# In[68]:


#gd = GridOptionsBuilder.from_dataframe(df_short)
#gd.configure_pagination(enabled=True)
#gd.configure_default_column(groupable=True)
#gridOptions = gd.build()


# grid_table = AgGrid(df_short,
#                    gridOptions=gridOptions,
#                    fit_columns_on_grid_load=True,
#                    height='400',
#                    width='100%',
#                    theme="streamlit",
#                    update_mode=GridUpdateMode.GRID_CHANGED,
#                    reload_data=True,
#                    allow_unsafe_jscode=True,
#                    editable=False
#                    )

# In[ ]:





# In[69]:


##########################################


# from st_aggrid import AgGrid, GridOptionsBuilder
# import streamlit as st
# 
# from st_aggrid import agstyler
# from src.agstyler import PINLEFT, PRECISION_ZERO, PRECISION_ONE, PRECISION_TWO, draw_grid
# 
# formatter = {
#     'Name': ('Player', PINLEFT),
#     'Team': ('Team', {'width': 80}),
#     'Age': ('Age', {'width': 80}),
#     'AB': ('At Bats', {'width': 80}),
#     'K%+': ('K%+', {**PRECISION_ZERO,'width': 80}),
#     'BABIP+': ('BABIP+', {**PRECISION_ZERO,'width': 80}),
#     'Hard%+': ('Hard%+', {**PRECISION_ZERO,'width': 80}),
#     'wRC+': ('wRC+', {**PRECISION_ZERO,'width': 80}),
# }
# 
# row_number = st.number_input('Number of rows', min_value=0, value=20)
# data = draw_grid(
#     df.head(15),
#     formatter=formatter,
#     fit_columns=True,
#     selection='multiple',  # or 'single', or None
#     use_checkbox='True',  # or False by default
#     max_height=300
# )

# In[ ]:





# In[72]:


st.set_page_config(page_title="Player Batting", layout="wide") 
st.title("Player Batting")

# add this
gb = GridOptionsBuilder.from_dataframe(df_short)
gb.configure_pagination()
gridOptions = gb.build()

AgGrid(df_short, gridOptions=gridOptions)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




