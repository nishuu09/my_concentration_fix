import streamlit as st

st.sidebar.title("🔍 Navigasi")
menu = st.sidebar.radio("Pilih halaman:", ["Beranda", "Konversi", "Tentang"])

if menu == "Beranda":
    st.title("MY CALCULATOR")
    st.write("Aplikasi Pengkonversi Konsentrasi Kimia")
elif menu == "Konversi":
    st.write("Silakan konversi data kimia.")
elif menu == "Tentang":
    st.write("Aplikasi ini dibuat untuk praktikum kimia.")

#===========================================================================================
