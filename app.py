import streamlit as st

st.sidebar.title("🔍 Navigasi")
menu = st.sidebar.radio("Pilih halaman:", ["Beranda", "Konversi", "Tentang"])

if menu == "Beranda":
    st.write("Oke")
elif menu == "Konversi":
    st.write("Silakan konversi data kimia.")
elif menu == "Tentang":
    st.write("Aplikasi ini dibuat untuk praktikum kimia.")

#===========================================================================================
st.title("MY CALCULATOR")
