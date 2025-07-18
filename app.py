import streamlit as st

st.sidebar.title("🔍 Navigasi")
menu = st.sidebar.radio("Pilih halaman:", ["Beranda", "Konversi", "Tentang"])

if menu == "Beranda":   
    st.write("Ini adalah halaman utama.")
    
elif menu == "Konversi":
    st.write("Silakan konversi data kimia.")
    st.set_page_config(page_title="Konversi Konsentrasi Kimia", layout="centered")
st.title("⚗️ Konversi Konsentrasi Kimia")

menu = st.selectbox("Pilih jenis konversi", [
    "Mol → Molaritas (M)",
    "Molaritas (M) → Mol",
    "Mol → ppm (mg/L)",
    "ppm (mg/L) → Mol",
    "Mol → % Massa",
    "% Massa → Mol"
])

if menu == "Mol → Molaritas (M)":
    mol = st.number_input("Jumlah mol", min_value=0.0)
    volume_l = st.number_input("Volume larutan (L)", min_value=0.0001)
    if st.button("Hitung"):
        M = mol / volume_l
        st.success(f"Molaritas: {M:.4f} mol/L")

elif menu == "Molaritas (M) → Mol":
    M = st.number_input("Molaritas (mol/L)", min_value=0.0)
    volume_l = st.number_input("Volume larutan (L)", min_value=0.0)
    if st.button("Hitung"):
        mol = M * volume_l
        st.success(f"Jumlah mol: {mol:.4f} mol")

elif menu == "Mol → ppm (mg/L)":
    mol = st.number_input("Jumlah mol", min_value=0.0)
    massa_molar = st.number_input("Massa molar (g/mol)", min_value=0.0)
    volume_l = st.number_input("Volume larutan (L)", min_value=0.0001)
    if st.button("Hitung"):
        gram = mol * massa_molar
        mg = gram * 1000
        ppm = mg / volume_l
        st.success(f"{mol} mol = {ppm:.2f} ppm (mg/L)")

elif menu == "ppm (mg/L) → Mol":
    ppm = st.number_input("Konsentrasi ppm (mg/L)", min_value=0.0)
    massa_molar = st.number_input("Massa molar (g/mol)", min_value=0.0)
    volume_l = st.number_input("Volume larutan (L)", min_value=0.0)
    if st.button("Hitung"):
        gram = ppm * volume_l / 1000
        mol = gram / massa_molar
        st.success(f"{ppm} ppm = {mol:.6f} mol")

elif menu == "Mol → % Massa":
    mol = st.number_input("Jumlah mol zat terlarut", min_value=0.0)
    massa_molar = st.number_input("Massa molar zat (g/mol)", min_value=0.0)
    massa_total = st.number_input("Total massa larutan (g)", min_value=0.0)
    if st.button("Hitung"):
        massa_zat = mol * massa_molar
        persen = (massa_zat / massa_total) * 100
        st.success(f"Persen massa: {persen:.2f} %")

elif menu == "% Massa → Mol":
    persen = st.number_input("Persen massa zat (%)", min_value=0.0)
    massa_total = st.number_input("Total massa larutan (g)", min_value=0.0)
    massa_molar = st.number_input("Massa molar zat (g/mol)", min_value=0.0)
    if st.button("Hitung"):
        massa_zat = persen / 100 * massa_total
        mol = massa_zat / massa_molar
        st.success(f"Jumlah mol: {mol:.4f} mol")
        
elif menu == "Tentang":
    st.write("Aplikasi ini dibuat untuk praktikum kimia.")

    
#===========================================================================================
