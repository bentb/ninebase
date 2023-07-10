#!/usr/bin/env python
# coding: utf-8

# # ninebase Home Page

# In[2]:


import streamlit as st


# In[3]:


st.set_page_config(
    page_title="ninebase",
    page_icon="👋",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': 'https://www.extremelycoolapp.com/help',
        'Get help': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


# In[4]:


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


# In[6]:


from PIL import Image

header_img = Image.open('assets/cards_at_mets.jpg')

st.image(header_img)


# In[9]:


# Define the layout
st.markdown(
    """
    <style>
        .container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .title {
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 24px;
        }

        .description {
            font-size: 24px;
            margin-bottom: 48px;
        }

        .cta-button {
            font-size: 20px;
            padding: 12px 24px;
            border-radius: 8px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            transition: background-color 0.3s;
        }

        .cta-button:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Render the home screen
st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown('<h1 class="title">ninebase</h1>', unsafe_allow_html=True)
st.markdown('<p class="description">identify who is hot, and who is not</p>', unsafe_allow_html=True)
st.markdown('<a href="https://ninebase.streamlit.app/player_batting_season" class="cta-button">Batting Stats</a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# In[10]:


st.divider()


# In[ ]:





# In[ ]:




