#!/usr/bin/env python
# coding: utf-8

# # ninebase Home Page

# In[25]:


import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

def set_page_configuration():
    st.set_page_config(
        page_title="ninebase",
        page_icon="⚾",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Report a bug': 'https://www.extremelycoolapp.com/help',
            'Get help': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an *extremely* cool app!"
        }
    )

def show_sidebar_pages():
    pages = [
        Page("Home.py", "Home"),
        Section("Player"),
            Page("pages/Player/player_batting_season.py", "Batting"),
            Page("pages/Player/player_pitching_season.py", "Pitching"),
        Section("Team"),
        Section("References"),
            Page("pages/References/Data_Dictionary.py"),
    ]
    
    show_pages(pages)


# In[3]:


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


# In[4]:


add_logo()


# In[ ]:


import streamlit as st
from datetime import datetime

def countdown_to_playoffs():
    # Get the current date
    now = datetime.now().date()

    # Set the target date as October 3rd
    target_date = datetime(now.year, 10, 3).date()

    # Calculate the remaining days
    remaining_days = (target_date - now).days

    # Customize the countdown style
    countdown_style = f"<p style='text-align: right; color: #164f5e; font-size: 18px; padding: 0; margin: 0;'>Days until playoffs: <span style='font-size: 32px;'>{remaining_days}</span></p>"

    # Display the countdown
    st.markdown(countdown_style, unsafe_allow_html=True)


# In[10]:


st.markdown(
    """
    <style>
        body {
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: flex-start;
            height: 100vh;
            margin: 0;
        }

        .title {
            font-size: 46px;
            font-weight: bold;
            margin-bottom: 12px;
            font-family: Lato, sans-serif;
            color: #164f5e;
        }

        .description {
            font-size: 24px;
            margin-bottom: 96px;
            font-family: Lato, sans-serif;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# In[7]:


st.markdown("")
st.markdown("")
st.markdown("")


# In[8]:


from PIL import Image

header_img = Image.open('assets/cards_at_mets.jpg')


# In[ ]:


col1, col2, col3 = st.columns([2, 6, 2])

with col1:
    st.write("#")

with col2:
    col2_content = st.container()
    with col2_content:
        st.image('assets/cards_at_mets.jpg')
        st.divider()

with col3:
    st.write("#")

