#!/usr/bin/env python
# coding: utf-8

# # ninebase Home Page

# In[10]:


import streamlit as st


# In[11]:


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


# In[12]:


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


# In[13]:


add_logo()


# In[14]:


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
    countdown_style = f"<p style='text-align: right; color: darkslategrey; font-size: 18px; padding: 0; margin: 0;'>Days until playoffs:</p>"
    remaining_days_style = f"<p style='text-align: right; color: darkslategrey; font-size: 32px; padding: 0; margin: 0;'>{remaining_days}</p>"

    # Display the countdown
    st.markdown(countdown_style, unsafe_allow_html=True)
    st.markdown(remaining_days_style, unsafe_allow_html=True)

# Run the countdown function
countdown_to_playoffs()


# In[15]:


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
            color: darkslategrey;
        }

        .description {
            font-size: 24px;
            margin-bottom: 96px;
            font-family: Lato, sans-serif;
        }

        .cta-button {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-bottom: 24px;
        }

        .cta-button a {
            color: white;
            display: block;
            text-align: center;
            padding: 12px 24px;
            border-radius: 8px;
            background-color: darkslategrey;
            text-decoration: none;
            transition: background-color 0.3s;
            font-family: Lato, sans-serif;
            font-size: 16px;
            font-weight: bold;
        }

        .cta-button a:hover {
            background-color: #366e6e;
        }
    </style>
    """,
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns([1, 5, 1])

with col1:
    st.write("#")

with col2:
    st.markdown('<div class="title">ninebase</div>', unsafe_allow_html=True)
    st.markdown('<p class="description">identify who is hot, and who is not</p>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="display: flex; justify-content: center;">', unsafe_allow_html=True)
        st.markdown('<div class="cta-button" style="margin-right: 12px;"><a href="https://ninebase.streamlit.app/player_batting_season">Batting Stats</a></div>', unsafe_allow_html=True)
        st.markdown('<div class="cta-button" style="margin-right: 12px;"><a href="https://ninebase.streamlit.app/player_pitching_season">*Pitching Stats*</a></div>', unsafe_allow_html=True)
        st.markdown('<div class="cta-button"><a href="https://ninebase.streamlit.app/team_stats">*Team Stats*</a></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("Content of the current page goes here.")
    st.image('assets/cards_at_mets.jpg')

    st.divider()

with col3:
    st.write("#")


# In[16]:


st.write("#")


# In[17]:


from PIL import Image

header_img = Image.open('assets/cards_at_mets.jpg')

st.image(header_img)


# In[18]:


st.divider()


# In[ ]:




