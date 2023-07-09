#!/usr/bin/env python
# coding: utf-8

# # ninebase Home Page

# In[7]:


import streamlit as st


# In[8]:


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


# In[13]:


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://i.imgur.com/sLSMBYJ.png);
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


# In[10]:


add_logo()


# In[15]:


from PIL import Image

header_img = Image.open('assets/cards_at_mets.jpg')

st.image(header_img)


# In[11]:


st.header('ninebase')


# In[ ]:


st.subheader('Use the Navigation Menu to browse reports')


# In[ ]:


st.divider()

