#!/usr/bin/env python
# coding: utf-8

# # ninebase Home Page

# In[2]:


import streamlit as st


# In[3]:


st.set_page_config(
    page_title="ninebase",
    page_icon="⚾",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': 'https://www.extremelycoolapp.com/help',
        'Get help': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


# In[17]:


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


# In[18]:


add_logo()


# In[21]:


# Define the layout
st.markdown(
    """
    <style>
        body {
            margin: 0;
        }

        .container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            padding: 0;
        }

        .title {
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 12px;
        }

        .description {
            font-size: 24px;
            margin-bottom: 96px;
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
        }

        .cta-button a:hover {
            background-color: #366e6e;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Render the home screen
st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown('<h1 class="title">ninebase</h1>', unsafe_allow_html=True)
st.markdown('<p class="description">identify who is hot, and who is not</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)  # Adjust the number of columns as needed

with col1:
    st.markdown('<div class="cta-button"><a href="https://ninebase.streamlit.app/player_batting_season">Batting Stats</a></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="cta-button"><a href="https://ninebase.streamlit.app/player_pitching_season">*Pitching Stats*</a></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="cta-button"><a href="https://ninebase.streamlit.app/team_stats">*Team Stats*</a></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# In[ ]:


st.write("#")


# In[ ]:


from PIL import Image

header_img = Image.open('assets/cards_at_mets.jpg')

st.image(header_img)


# In[ ]:


st.divider()

