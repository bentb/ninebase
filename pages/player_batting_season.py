#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# sources:
# docs.streamlit.io/library/get-started

# # Introduction

# In[16]:


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

# In[17]:


import streamlit as st


# In[18]:


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


# In[19]:


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
            [data-testid="stSidebarNav"]::before {
                content: "Navigation Menu";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 26px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


# In[20]:


add_logo()


# ## Load Data

# In[21]:


# Format for GitHub
df = pd.read_csv('data_storage/player_batting_season.csv')

# Format for Jupyter Notebook
#df = pd.read_csv('C:/Users/b7tbu/NINEBASE/ninebase/data_storage/player_batting_season.csv')


# In[22]:


df.head()


# In[31]:


import plotly.express as px
import statsmodels.api as sm


# ### Row 1 - Scatter Plot 1

# In[39]:


fig_1 = px.scatter(
    df.query("Season==2023"),
    title="Hard%+ vs. BABIP+",
    x = "Hard%+",
    y = "BABIP+",
    hover_name = "Name",
    log_x = True,
    trendline = "ols",
    size_max = 60,
    height = 750,
    width = 750,
)


# In[46]:


fig_3 = px.scatter(df, x='Hard%+', y='BABIP+')

fig_3.update_layout(
    title = "Hard%+ vs 'BABIP+",
    xaxis_title = "Hard Hit%+",
    yaxis_title = "BABIP+",
    barmode = 'group',
    showlegend = True,
    legend_title = 'Legend',
    template = 'plotly_dark'
)


# In[43]:





# ### Row 1 - Scatter Plot 2

# In[33]:


fig_2 = px.scatter(
    df.query("Season==2023"),
    title="BB%+ vs. K%+",
    x = "BB%+",
    y = "K%+",
    hover_name = "Name",
    log_x = True,
    trendline = "ols",
    size_max = 60,
    height = 750,
    width = 750,
)


# ### Row 1 - Print

# In[47]:


# Subheader
st.subheader('Player Batting')

# Create the tabs
tab1, tab2, tab3 = st.tabs(["Hard Hit vs. BABIP", "Walks vs Strikeouts", "Tab 3"])

# Display the charts within the tabs
with tab1:
    st.plotly_chart(fig_1, theme="streamlit", use_container_width=False)

with tab2:
    st.plotly_chart(fig_2, theme="streamlit", use_container_width=False)
    
with tab3:
    st.plotly_chart(fig_3)


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


col1, col2, = st.columns([0.75, 0.25])

with col1:
    st.subheader("Raw Data")
    grid_response = AgGrid(
        df_short,
        gridOptions=go,
        theme="streamlit",
        height=600
    )
    
with col2:
    st.subheader("")


# 

# In[21]:





# In[ ]:





# In[ ]:




