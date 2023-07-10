#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# sources:
# docs.streamlit.io/library/get-started

# # Introduction

# In[42]:


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

# In[43]:


import streamlit as st


# In[44]:


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


# In[45]:


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


# In[5]:


add_logo()


# ## Load Data

# In[6]:


# Format for GitHub
df = pd.read_csv('data_storage/player_batting_season.csv')

# Format for Jupyter Notebook
#df = pd.read_csv('C:/Users/b7tbu/NINEBASE/ninebase/data_storage/player_batting_season.csv')


# In[46]:


df.head()


# In[47]:


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

# In[ ]:


fig_11 = px.box(
    df.query("Season==2023"),
    y = "wRC+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_11.update_traces(marker=dict(color="darkslategrey"))

fig_11.update_layout(
    title=dict(text="wRC+", font=dict(size=24), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[41]:


fig_12 = px.box(
    df.query("Season==2023"),
    y = "Bat",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_12.update_traces(marker=dict(color="darkslategrey"))

fig_12.update_layout(
    title=dict(text="Batting WAR", font=dict(size=24), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[10]:


fig_13 = px.box(
    df.query("Season==2023"),
    y = "Pos",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_13.update_traces(marker=dict(color="darkslategrey"))

fig_13.update_layout(
    title=dict(text="Position WAR", font=dict(size=24), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# ### Row 1 - Tab 2

# In[32]:


fig_21 = px.box(
    df.query("Season==2023"),
    y = "HR",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_21.update_traces(marker=dict(color="darkslategrey"))

fig_21.update_layout(
    title=dict(text="Home Runs", font=dict(size=24), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[33]:


fig_22 = px.box(
    df.query("Season==2023"),
    y = "Soft%+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_22.update_traces(marker=dict(color="darkslategrey"))

fig_22.update_layout(
    title=dict(text="Soft Hit %+", font=dict(size=24), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[34]:


fig_23 = px.box(
    df.query("Season==2023"),
    y = "Hard%+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_23.update_traces(marker=dict(color="darkslategrey"))

fig_23.update_layout(
    title=dict(text="Hard Hit %+", font=dict(size=24), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# ### Row 1 - Tab 3

# In[15]:


fig_31 = px.box(
    df.query("Season==2023"),
    y = "Contact%",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_31.update_traces(marker=dict(color="darkslategrey"))

fig_31.update_layout(
    title=dict(text="Contact%", font=dict(size=24), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[16]:


fig_32 = px.box(
    df.query("Season==2023"),
    y = "O-Contact%",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_32.update_traces(marker=dict(color="darkslategrey"))

fig_32.update_layout(
    title=dict(text="Out of Zone Contact%", font=dict(size=24), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[17]:


fig_33 = px.box(
    df.query("Season==2023"),
    y = "Z-Contact%",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_33.update_traces(marker=dict(color="darkslategrey"))

fig_33.update_layout(
    title=dict(text="Within Zone Contact%", font=dict(size=24), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# ### Row 1 - Tab 4

# In[18]:


fig_41 = px.box(
    df.query("Season==2023"),
    y = "BB%+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_41.update_traces(marker=dict(color="darkslategrey"))

fig_41.update_layout(
    title=dict(text="Walk %+", font=dict(size=24), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[19]:


fig_42 = px.box(
    df.query("Season==2023"),
    y = "K%+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_42.update_traces(marker=dict(color="darkslategrey"))

fig_42.update_layout(
    title=dict(text="Strikeout %+", font=dict(size=24), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[20]:


fig_43 = px.box(
    df.query("Season==2023"),
    y = "O-Swing%",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_43.update_traces(marker=dict(color="darkslategrey"))

fig_43.update_layout(
    title=dict(text="Out of Zone Swing %", font=dict(size=24), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# ### Row 1 - Tab 5

# In[21]:


fig_51 = px.box(
    df.query("Season==2023"),
    y = "Pull%+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_51.update_traces(marker=dict(color="darkslategrey"))

fig_51.update_layout(
    title=dict(text="Pull %+", font=dict(size=24), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[22]:


fig_52 = px.box(
    df.query("Season==2023"),
    y = "Cent%+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_52.update_traces(marker=dict(color="darkslategrey"))

fig_52.update_layout(
    title=dict(text="Center %+", font=dict(size=24), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[31]:


fig_53 = px.box(
    df.query("Season==2023"),
    y = "Oppo%+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_53.update_traces(marker=dict(color="darkslategrey"))

fig_53.update_layout(
    title=dict(text="Oppo %+", font=dict(size=24), automargin=True, yref='paper'),
    title_font_color="darkslategrey",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# ### Row 1 - Print

# In[36]:


# Heading
st.markdown('<span style="font-family: Lato, sans-serif; font-size: 32px; color: darkslategrey; font-weight: bold;">Player Batting</span>', unsafe_allow_html=True)

# Create the tabs
tabs = st.tabs(["Summary", "Power", "Contact", "Plate Discipline", "Pull/Oppo"])

# Display the charts within the tabs
with tabs[0]:
    col1, col2, col3 = st.columns(3)
    col1.plotly_chart(fig_11, theme="streamlit", use_container_width=False)
    col2.plotly_chart(fig_12, theme="streamlit", use_container_width=False)
    col3.plotly_chart(fig_13, theme="streamlit", use_container_width=False)

with tabs[1]:
    col4, col5, col6 = st.columns(3)
    col4.plotly_chart(fig_21, theme="streamlit", use_container_width=False)
    col5.plotly_chart(fig_22, theme="streamlit", use_container_width=False)
    col6.plotly_chart(fig_23, theme="streamlit", use_container_width=False)

with tabs[2]:
    col7, col8, col9 = st.columns(3)
    col7.plotly_chart(fig_31, theme="streamlit", use_container_width=False)
    col8.plotly_chart(fig_32, theme="streamlit", use_container_width=False)
    col9.plotly_chart(fig_33, theme="streamlit", use_container_width=False)
    
with tabs[3]:
    col10, col11, col12 = st.columns(3)
    col10.plotly_chart(fig_41, theme="streamlit", use_container_width=False)
    col11.plotly_chart(fig_42, theme="streamlit", use_container_width=False)
    col12.plotly_chart(fig_43, theme="streamlit", use_container_width=False)
    
with tabs[4]:
    col13, col14, col15 = st.columns(3)
    col13.plotly_chart(fig_51, theme="streamlit", use_container_width=False)
    col14.plotly_chart(fig_52, theme="streamlit", use_container_width=False)
    col15.plotly_chart(fig_53, theme="streamlit", use_container_width=False)


# ## Row 2

# ### Raw Data

# In[25]:


from st_aggrid import AgGrid, GridOptionsBuilder, DataReturnMode, JsCode


# In[26]:


# Builds a gridOptions dictionary using a GridOptionsBuilder instance.
builder = GridOptionsBuilder.from_dataframe(df)

# Configs
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
builder.configure_column('Pos', width=100)
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
        "headerName": "Batting Summary",
        "children": [
            {"field": "Bat"},
            {"field": "Pos"},
            {"field": "WAR"},
        ]
    },
    {
        "headerName": "Power",
        "children": [
            {"field": "wRC+", "sort": "desc"},
            {"field": "Soft%+"},
            {"field": "Med%+"},
            {"field": "Hard%+"},
            {"field": "HR"},
        ]
    },
    {
        "headerName": "Contact",
        "children": [
            {"field": "BABIP+"},
            {"field": "Contact%"},
            {"field": "O-Contact%"},
            {"field": "Z-Contact%"},
        ]
    },
    {
        "headerName": "Plate Disciplline",
        "children": [
            {"field": "BB%+"},
            {"field": "K%+"},
            {"field": "Swing%"},
            {"field": "O-Swing%"},
            {"field": "Z-Swing%"},
        ]
    },
    {
        "headerName": "Pull/Oppo",
        "children": [
            {"field": "Pull%+"},
            {"field": "Cent%+"},
            {"field": "Oppo%+"},
        ]
    }
]

# Merge columnDefs with existing column definitions
grid_options = {"columnDefs": column_defs}

# Launch
go = grid_options

col1, col2 = st.columns([98, 2])

with col1:
    st.write('<span style="font-family: Lato, sans-serif; font-size: 26px; font-weight: bold; color: darkslategrey;">Raw Data</span>', unsafe_allow_html=True)
    st.text("Default Sort: wRC+")
    grid_response = AgGrid(
        df,
        gridOptions=go,
        theme="streamlit",
        height=600
    )

with col2:
    st.subheader("")


# In[27]:


st.divider()


# In[28]:


from PIL import Image

header_img = Image.open('assets/stevens_bat.jpg')

st.image(header_img)


# In[ ]:





# ### Playground

# In[ ]:


st.write("⛔ NO ENTRY ⛔ 🏗️ construction in progress...")


# In[ ]:


import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder

# ...

# Column Grouping
column_defs = [        
    {
        "headerName": "",
        "children": [
            {"field": "Name", "headerName": "Player", "pinned": 'left'},
        ],
        "headerClass": "player-group"  # CSS class for the Player group
    },
    {
        "headerName": "Player Details",
        "children": [
            {"field": "Team"},
            {"field": "Age"},
            {"field": "AB", "headerName": "At Bats"},
        ],
        "headerClass": "details-group"  # CSS class for the Player Details group
    },
    # ...
]

# Merge columnDefs with existing column definitions
grid_options = {"columnDefs": column_defs}

# CSS styles
st.markdown("""
<style>
.ag-header-group-player-group {
    background-color: #FF0000;  /* Red color for Player group */
}

.ag-header-group-details-group {
    background-color: #00FF00;  /* Green color for Player Details group */
}

/* Add more styles for other groups as needed */
</style>
""", unsafe_allow_html=True)

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





# In[ ]:




