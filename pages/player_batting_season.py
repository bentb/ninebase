#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# sources:
# docs.streamlit.io/library/get-started

# # Introduction

# In[2]:


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

# In[3]:


import streamlit as st


# In[4]:


st.set_page_config(
    page_title="Player Batting",
    page_icon="⚾",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': 'https://www.extremelycoolapp.com/help',
        'Get help': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


# In[ ]:


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://i.imgur.com/OBQbrzX.png);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


# In[ ]:


add_logo()


# ## Load Data

# In[9]:


# Format for GitHub
df = pd.read_csv('data_storage/player_batting_season.csv')

# Format for Jupyter Notebook
#df = pd.read_csv('C:/Users/b7tbu/NINEBASE/ninebase/data_storage/player_batting_season.csv')


# In[12]:


df.head()


# In[7]:


import plotly.express as px


# ### Row 1 - Scatter Plot 1

# In[10]:


fig_1 = px.scatter(
    df.query("Season==2023"),
    x = "Hard%+",
    y = "BABIP+",
    hover_name = "Name",
    log_x = True,
    size_max = 60,
)


# ### Row 1 - Scatter Plot 2

# In[13]:


fig_2 = px.scatter(
    df.query("Season==2023"),
    x = "BB%+",
    y = "K%+",
    hover_name = "Name",
    log_x = True,
    size_max = 60,
)


# ### Row 1 - Print

# In[12]:


# Create the tabs
tab1, tab2 = st.tabs(["Hard Hit vs. BABIP", "Walks vs Strikeouts"])

# Display the charts within the tabs
with tab1:
    st.plotly_chart(fig_1, height=1000, width=1000, theme="streamlit", use_container_width=False)

with tab2:
    st.plotly_chart(fig_2, height=1000, width=1000, theme="streamlit", use_container_width=False)


# ## Row 2

# ### Row - Raw Data

# In[22]:


from st_aggrid import AgGrid, GridOptionsBuilder, DataReturnMode, JsCode


# In[23]:


# Simplify dataframe, narrow to most insightful columns
df_short = df[['Name', 'Team', 'Age', 'AB', 'BB%+', 'K%+', 'BABIP+', 'Hard%+', 'wRC+']]


# In[24]:


# Builds a gridOptions dictionary using a GridOptionsBuilder instance.
builder = GridOptionsBuilder.from_dataframe(df_short)
builder.configure_side_bar(filters_panel=True, columns_panel=True)

# Columns

builder.configure_column("Name", header_name="Player", width=150, editable=False)
builder.configure_column("Team", width=100, enableRowGroup=True)
builder.configure_column("Age", width=100)
builder.configure_column("AB", width=100)
builder.configure_column("BB%+", width=100)
builder.configure_column('K%+', width=100)
builder.configure_column('BABIP+', width=100)
builder.configure_column('Hard%+', width=100)
builder.configure_column("wRC+", width=100, sort='desc')

# Launch
go = builder.build()


# ### Row 2 - Print

# In[20]:


st.subheader("Raw Data")
grid_response = AgGrid(
    df_short,
    gridOptions=go,
    theme="streamlit",
    height=450
)


# 

# In[21]:





# In[ ]:





# In[ ]:




