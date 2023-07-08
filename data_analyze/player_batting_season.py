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


# In[ ]:


st.set_page_config(
    page_title="Hello",
    page_icon="⚾",
)

st.write("# Welcome to ninebase 👋")

st.sidebar.success("Sidebar Success?")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)


# ## Load Data

# In[37]:


# Format for GitHub
df = pd.read_csv('data_storage/player_batting_season.csv')

# Format for Jupyter Notebook
#df = pd.read_csv('C:/Users/b7tbu/NINEBASE/ninebase/data_storage/player_batting_season.csv')


# In[134]:


df.head()


# # Page 1

# In[135]:


import plotly.express as px


# ### Page 1/Row 1 - Scatter Plot 1

# In[136]:


fig_1 = px.scatter(
    df.query("Season==2023"),
    x = "Hard%+",
    y = "BABIP+",
    hover_name = "Name",
    log_x = True,
    size_max = 60,
)


# ### Page 1/Row 1 - Scatter Plot 2

# In[137]:


fig_2 = px.scatter(
    df.query("Season==2023"),
    x = "BB%+",
    y = "K%+",
    hover_name = "Name",
    log_x = True,
    size_max = 60,
)


# ### Page 1/Row 1 - Columns 1/2

# In[138]:


# Create the columns
col1, col2 = st.columns(2)

# Create the tabs within col1
with col1:
    # Create the tabs
    tab1, tab2 = st.tabs(["Hard Hit vs. BABIP", "Walks vs Strikeouts"])
    
    # Display the charts within the tabs
    with tab1:
        st.plotly_chart(fig_1, theme="streamlit", use_container_width=True)
    
    with tab2:
        st.plotly_chart(fig_2, theme="streamlit", use_container_width=True)
        
with col2:
    st.write("Hello World, column 2 here")


# ## Page 1/Row 2

# ### Raw Data

# In[139]:


from st_aggrid import AgGrid, GridOptionsBuilder, DataReturnMode, JsCode


# In[140]:


# Simplify dataframe, narrow to most insightful columns
df_short = df[['Name', 'Team', 'Age', 'AB', 'BB%+', 'K%+', 'BABIP+', 'Hard%+', 'wRC+']]


# In[141]:


# Builds a gridOptions dictionary using a GridOptionsBuilder instance.
builder = GridOptionsBuilder.from_dataframe(df_short)
builder.configure_pagination(enabled=True, paginationAutoPageSize=True, paginationPageSize=100)
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
builder.configure_column("wRC+", width=100)

# Launch
go = builder.build()


# ### Page 1/Row 2 - Columns

# In[142]:


# Create Streamlit columns
col3, col4 = st.columns([1, 1])

# Set the CSS styles for column widths and heights
col3_html = col3.markdown("")
col4_html = col4.markdown("")

# Generate the HTML code for CSS styling
col3_css = "<style>div[data-testid='stHorizontalBlock'] > div{width: 100% !important;}</style>"
col4_css = "<style>div[data-testid='stHorizontalBlock'] > div{width: 100% !important;}</style>"
col3_height_css = f"<style>.st-cc{{height: 500px !important;}}</style>"  # Set the desired height
col4_height_css = f"<style>.st-cc{{height: 800px !important;}}</style>"  # Set the desired height


# Set the HTML content of the columns
col3_html.markdown(col3_css, unsafe_allow_html=True)
col4_html.markdown(col4_css, unsafe_allow_html=True)

with col3:
    st.subheader("Raw Data")
    grid_response = AgGrid(
        df_short,
        gridOptions=go,
        theme="streamlit",
        height=470
    )

# Set the HTML content of the height styling
col3_html.markdown(col3_height_css, unsafe_allow_html=True)

with col4:
    st.write("Other content goes here")
    col4_html.markdown(col4_height_css, unsafe_allow_html=True)


# In[ ]:





# 

# # Page 2

# ### Page 2/Row 1

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




