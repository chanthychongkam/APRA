import streamlit as st

st.title("Project Archie - APRA POC")
st.write('Hello Archie version 3')

with st.sidebar:
    vABN= st.text_input(label='Please provide your ABN')
