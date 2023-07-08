#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# sources:
# docs.streamlit.io/library/get-started

# In[ ]:





# # Introduction

# In[27]:


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

# In[28]:


import streamlit as st


# In[ ]:





# In[52]:


st.set_page_config(
    page_title="9base",
    page_icon="⚾",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': 'https://www.extremelycoolapp.com/help',
        'Get help': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


# In[53]:


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

# In[37]:


# Format for GitHub
df = pd.read_csv('data_storage/player_batting_season.csv')

# Format for Jupyter Notebook
#df = pd.read_csv('C:/Users/b7tbu/NINEBASE/ninebase/data_storage/player_batting_season.csv')


# In[38]:


df.head()


# ## Scatter Chart

# In[39]:


import plotly.express as px


# In[40]:


fig = px.scatter(
    df.query("Season==2023"),
    x = "wRC+",
    y = "Hard%+",
    color = "Team",
    hover_name = "Name",
    log_x = True,
    size_max = 60,
)


# In[41]:


#st.plotly_chart(fig, theme="streamlit", use_container_width = True)


# ## Filters

# In[42]:


# calculate min/max/mean for slider
min_AB = df['AB'].min()
max_AB = df['AB'].max()
mean_AB = df['AB'].mean()

# float em
min_AB = float(min_AB)
max_AB = float(max_AB)
mean_AB = float(mean_AB)


# In[43]:


# slider

ab_slider = st.slider('At Bat Range', min_AB, max_AB, (mean_AB, max_AB))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[44]:


## Sidebar


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Columns

# In[45]:


col1, col2 = st.columns([2,1])


# In[46]:


col1.subheader("Scatter Chart")
col1.plotly_chart(fig, theme="streamlit", use_container_width = True)

col2.subheader("Filters")
col2.write(ab_slider)


# In[ ]:





# In[ ]:





# ## Raw Data Display

# In[47]:


from st_aggrid import AgGrid, GridOptionsBuilder, DataReturnMode, JsCode


# In[48]:


# Simplify dataframe, narrow to most insightful columns
df_short = df[['Name', 'Team', 'Age', 'AB', 'BB%+', 'K%+', 'BABIP+', 'Hard%+', 'wRC+']]


# In[71]:


#builds a gridOptions dictionary using a GridOptionsBuilder instance.
builder = GridOptionsBuilder.from_dataframe(df_short)
builder.configure_column("Name", header_name="First", editable=False)
builder.configure_pagination(enabled=True, paginationAutoPageSize=True, paginationPageSize=100)
builder.configure_side_bar(filters_panel=True, columns_panel=True)
builder.configure_column("Team", width=100, enableRowGroup=True)
builder.configure_column("Age", width=100)
builder.configure_column("AB", width=100)
builder.configure_column("BB%+", width=100)
builder.configure_column('K%+', width=100)
builder.configure_column('BABIP+', width=100)
builder.configure_column('Hard%+', width=100)
builder.configure_column("wRC+", width=100, sort='des')
go = builder.build()


# In[72]:


#uses the gridOptions dictionary to configure AgGrid behavior.
AgGrid(df_short, gridOptions=go, height=1000)


# In[ ]:





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





# In[ ]:





# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




