#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import streamlit as st


# In[3]:


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to ninebase 👋")

st.sidebar.success("Home")

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

from pages import second_page
# Create sidebar navigation
pages = {
    "Home": Home,
    "Player Batting Season": player_batting_season,
}
selected_page = st.sidebar.selectbox("Navigation", list(pages.keys()))
if selected_page != "Home":
    pages[selected_page].app()
else:
    st.write("# Welcome to the Home Page")
    # Add content for the Home page
# Render selected page
selected_page.app()




