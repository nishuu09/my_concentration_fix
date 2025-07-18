import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.write("Input Kiri")
    st.number_input("Mol", key="mol")

with col2:
    st.write("Input Kanan")
    st.number_input("Gram", key="gram")

