import streamlit as st

AVOGADRO = 6.022e23  # partikel/mol
VOLUME_STP = 22.4    # liter/mol (pada STP)

st.set_page_config(page_title="Konversi Kimia", layout="centered")
st.title("⚗️ Konversi Kimia Sederhana")

st.markdown("Konversi antara mol, gram, partikel, volume gas, dan konsentrasi.")

menu = st.selectbox("Pilih jenis konversi", [
    "Mol → Gram",
    "Gram → Mol",
    "Mol → Partikel",
    "Partikel → Mol",
    "Mol → Volume Gas (STP)",
    "Volume Gas → Mol (STP)",
    "Mol → Molaritas (M)",
    "Molaritas → Mol"
])

if menu == "Mol → Gram":
    mol = st.number_input("Masukkan jumlah mol", min_value=0.0)
    massa_molar = st.number_input("Masukkan massa molar (g/mol)", min_value=0.0)
    if st.button("Konversi"):
        hasil = mol * massa_molar
        st.success(f"{mol} mol = {hasil:.4f} gram")

elif menu == "Gram → Mol":
    gram = st.number_input("Masukkan massa (gram)", min_value=0.0)
    massa_molar = st.number_input("Masukkan massa molar (g/mol)", min_value=0.0)
    if st.button("Konversi"):
        hasil = gram / massa_molar
        st.success(f"{gram} gram = {hasil:.4f} mol")

elif menu == "Mol → Partikel":
    mol = st.number_input("Masukkan jumlah mol", min_value=0.0)
    if st.button("Konversi"):
        partikel = mol * AVOGADRO
        st.success(f"{mol} mol = {partikel:.2e} partikel")

elif menu == "Partikel → Mol":
    partikel = st.number_input("Masukkan jumlah partikel", min_value=0.0)
    if st.button("Konversi"):
        mol = partikel / AVOGADRO
        st.success(f"{partikel:.2e} partikel = {mol:.4f} mol")

elif menu == "Mol → Volume Gas (STP)":
    mol = st.number_input("Masukkan jumlah mol", min_value=0.0)
    if st.button("Konversi"):
        volume = mol * VOLUME_STP
        st.success(f"{mol} mol = {volume:.2f} L (pada STP)")

elif menu == "Volume Gas → Mol (STP)":
    volume = st.number_input("Masukkan volume gas (L)", min_value=0.0)
    if st.button("Konversi"):
        mol = volume / VOLUME_STP
        st.success(f"{volume} L = {mol:.4f} mol")

elif menu == "Mol → Molaritas (M)":
    mol = st.number_input("Masukkan mol zat", min_value=0.0)
    volume_l = st.number_input("Masukkan volume larutan (L)", min_value=0.0001)
    if st.button("Konversi"):
        M = mol / volume_l
        st.success(f"Molaritas: {M:.4f} mol/L")

elif menu == "Molaritas → Mol":
    M = st.number_input("Masukkan molaritas (mol/L)", min_value=0.0)
    volume_l = st.number_input("Masukkan volume larutan (L)", min_value=0.0)
    if st.button("Konversi"):
        mol = M * volume_l
        st.success(f"Jumlah mol: {mol:.4f} mol")
