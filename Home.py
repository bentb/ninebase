#!/usr/bin/env python
# coding: utf-8

# # ninebase Home Page

# In[ ]:





# In[7]:


import streamlit as st


# In[8]:


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.sidebar.success("Select a page above")


# In[13]:


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://i.imgur.com/nuEg4fJ.png);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "ninebase";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


# In[10]:


add_logo()


# In[11]:


st.write("Home Page 👋")


# In[ ]:




