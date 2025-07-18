import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Input Kiri")
    st.number_input("Mol", key="mol")

with col2:
    st.write("Input Kanan")
    st.number_input("Gram", key="gram")

with col3:
    st.write("Input Paling Kanan")
    st.number_input("Kg", key="kg")
