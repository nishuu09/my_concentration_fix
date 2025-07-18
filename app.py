import streamlit as st

st.set_page_config(page_title="Konversi Kimia", layout="centered")
st.title("⚗️ Konversi Kimia")
st.markdown("Alat bantu konversi kimia: mol, gram, partikel, volume gas.")

tab1, tab2 = st.tabs(["Mol ⇄ Gram", "Mol ⇄ Partikel"])

with tab1:
    mol = st.number_input("Masukkan jumlah mol", min_value=0.0)
    massa_molar = st.number_input("Massa molar (g/mol)", min_value=0.0)
    if st.button("Konversi ke Gram"):
        hasil = mol * massa_molar
        st.success(f"{mol} mol = {hasil} gram")

with tab2:
    mol2 = st.number_input("Mol untuk partikel", min_value=0.0, key="mol2")
    if st.button("Konversi ke Partikel"):
        hasil2 = mol2 * 6.022e23
        st.success(f"{mol2} mol = {hasil2:.2e} partikel")
