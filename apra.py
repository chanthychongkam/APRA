import streamlit as st

st.title("Project Archie - APRA POC")
st.write('Hello Archie version 3')

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
