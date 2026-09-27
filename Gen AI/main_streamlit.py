# Streamlit:Streamlit is a Python framework used to quickly build interactive web applications and dashboards for
# machine learning and data science projects using simple python code

import streamlit as st
import langchain_helper

st.title("Resturant Name Generator")
cuisine=st.sidebar.selectbox("pick a cuisine",("Indian","Italian","Mexican","Arabian"))

if cuisine:
    response=langchain_helper.generate_resturant_name_and_items(cuisine)
    st.header(response['resturant_name'])
    menu_items=response['items_name'].split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-",item)