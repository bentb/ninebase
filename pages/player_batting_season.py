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
                background-image: url(https://i.imgur.com/sLSMBYJ.png);
                background-repeat: no-repeat;
                padding-top: 40px;
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


# ### Row 1 - Plot 1 (outdated)

# fig_1 = px.scatter(
#     df.query("Season==2023"),
#     title="Hard%+ vs. BABIP+",
#     x = "Hard%+",
#     y = "BABIP+",
#     hover_name = "Name",
#     log_x = True,
#     trendline = "ols",
#     size_max = 60,
#     height = 750,
#     width = 750,
# )

# ### Row 1 - Tab 1

# In[118]:


fig_11 = px.box(
    df.query("Season==2023"),
    y = "Hard%+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_11.update_layout(
    title=dict(text="Hard Hit %+", font=dict(size=26), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[119]:


fig_12 = px.box(
    df.query("Season==2023"),
    y = "HR",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_12.update_layout(
    title=dict(text="Home Runs", font=dict(size=26), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[120]:


fig_13 = px.box(
    df.query("Season==2023"),
    y = "wRC+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_13.update_layout(
    title=dict(text="wRC+", font=dict(size=26), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[ ]:


fig_14 = px.box(
    df.query("Season==2023"),
    y = "wRC+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_14.update_layout(
    title=dict(text="wRC+", font=dict(size=26), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# ### Row 1 - Tab 2

# In[121]:


fig_21 = px.box(
    df.query("Season==2023"),
    y = "BB%+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_21.update_layout(
    title=dict(text="Walk %+", font=dict(size=26), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[122]:


fig_22 = px.box(
    df.query("Season==2023"),
    y = "K%+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_22.update_layout(
    title=dict(text="Strikeout %+", font=dict(size=26), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[123]:


fig_23 = px.box(
    df.query("Season==2023"),
    y = "O-Swing%",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_23.update_layout(
    title=dict(text="Out of Zone Swing %+", font=dict(size=26), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# ### Row 1 - Print

# In[72]:


# Subheader
st.subheader('Player Batting')

# Create the tabs
tabs = st.tabs(["Power", "Plate Discipline", "Clutch"])

# Display the charts within the tabs
with tabs[0]:
    col1, col2, col3, col4 = st.columns(4)
    col1.plotly_chart(fig_11, theme="streamlit", use_container_width=False)
    col2.plotly_chart(fig_12, theme="streamlit", use_container_width=False)
    col3.plotly_chart(fig_13, theme="streamlit", use_container_width=False)
    col4.plotly_chart(fig_14, theme="streamlit", use_container_width=False)

with tabs[1]:
    col4, col5, col6 = st.columns(3)
    col4.plotly_chart(fig_21, theme="streamlit", use_container_width=False)
    col5.plotly_chart(fig_22, theme="streamlit", use_container_width=False)
    col6.plotly_chart(fig_23, theme="streamlit", use_container_width=False)


# ## Row 2

# ### Row - Raw Data

# In[74]:


from st_aggrid import AgGrid, GridOptionsBuilder, DataReturnMode, JsCode


# # Simplify dataframe, narrow to most insightful columns
# df_short = df[['Name', 'Team', 'Age', 'AB', 'BB%+', 'K%+', 'BABIP+', 'Hard%+', 'wRC+']]

# # Builds a gridOptions dictionary using a GridOptionsBuilder instance.
# builder = GridOptionsBuilder.from_dataframe(df_short)
# builder.configure_side_bar(filters_panel=True, columns_panel=True)
# 
# # Columns
# 
# builder.configure_column("Name", header_name="Player", width=150, editable=False)
# builder.configure_column("Team", width=100, enableRowGroup=True)
# builder.configure_column("Age", width=100)
# builder.configure_column("AB", width=100)
# builder.configure_column("BB%+", width=100)
# builder.configure_column('K%+', width=100)
# builder.configure_column('BABIP+', width=100)
# builder.configure_column('Hard%+', width=100)
# builder.configure_column("wRC+", width=100, sort='desc')
# 
# # Launch
# go = builder.build()

# ### Row 2 - Print

# col1, col2, = st.columns([0.75, 0.25])
# 
# with col1:
#     st.subheader("Raw Data")
#     grid_response = AgGrid(
#         df_short,
#         gridOptions=go,
#         theme="streamlit",
#         height=600
#     )
#     
# with col2:
#     st.subheader("")

# In[ ]:


st.divider()


# In[ ]:





# ### Playground

# In[ ]:





# In[92]:


# Builds a gridOptions dictionary using a GridOptionsBuilder instance.
builder = GridOptionsBuilder.from_dataframe(df)
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

# Column Grouping
column_defs = [        
    {
        "headerName": "",
        "children": [
            {"field": "Name", "headerName": "Player", "pinned": 'left'},
        ]
    },
    {
        "headerName": "Player Details",
        "children": [
            {"field": "Team"},
            {"field": "Age"},
            {"field": "AB", "headerName": "At Bats"},
        ]
    },
    {
        "headerName": "Power",
        "children": [
            {"field": "Hard%+"},
            {"field": "HR"},
            {"field": "BABIP+"},
            {"field": "Hard%+"},
            {"field": "wRC+"},
        ]
    },
    {
        "headerName": "Plate Disciplline",
        "children": [
            {"field": "BB%+"},
            {"field": "K%+"},
        ]
    }
]

# Merge columnDefs with existing column definitions
grid_options = {"columnDefs": column_defs}

# Launch
go = grid_options

col1, col2 = st.columns([0.75, 0.25])

with col1:
    st.subheader("Raw Data")
    grid_response = AgGrid(
        df,
        gridOptions=go,
        theme="streamlit",
        height=600
    )

with col2:
    st.subheader("")


# In[ ]:




