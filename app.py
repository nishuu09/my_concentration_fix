import streamlit as st

st.sidebar.title("🔍 Navigasi")
menu = st.sidebar.radio("Pilih halaman:", ["Beranda", "Konversi", "Tentang"])

if menu == "Beranda":
    st.write("Oke")
elif menu == "Konversi":
    st.write("Silakan konversi data kimia.")
elif menu == "Tentang":
    st.write("Aplikasi ini dibuat untuk praktikum kimia.")

import pandas as pd

st.write(1234)
st.write(
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )
)
