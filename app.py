import streamlit as st

# Konstanta
AVOGADRO = 6.022e23  # Partikel/mol
VOLUME_STP = 22.4    # Liter/mol (STP)

# Konfigurasi aplikasi
st.set_page_config(page_title="Konversi Kimia", layout="centered")
st.sidebar.title("🔬 Navigasi")
halaman = st.sidebar.radio("Pilih Halaman:", ["Penjelasan", "Konversi", "Informasi"])

# =========================
# HALAMAN 1: PENJELASAN
# =========================
if halaman == "Penjelasan":
    st.title("🧪 Penjelasan Konversi Kimia")
    st.markdown("""
    Aplikasi ini membantu kamu menghitung **konversi satuan dalam kimia**, khususnya:

    - Mol ↔ Gram
    - Mol ↔ Partikel
    - Mol ↔ Volume Gas (STP)

    **Kenapa ini penting?**
    - Dalam stoikiometri, kita sering mengubah antar satuan untuk memahami reaksi kimia.
    - Misalnya: menghitung berapa gram H₂O yang terbentuk dari 2 mol H₂.

    💡 Cocok untuk siswa SMA, mahasiswa, atau praktikum laboratorium kimia dasar.
    """)

# =========================
# HALAMAN 2: KONVERSI
# =========================
elif halaman == "Konversi":
    st.title("⚗️ Halaman Konversi Kimia")

    konversi = st.selectbox("Pilih jenis konversi:", [
        "Mol → Gram",
        "Gram → Mol",
        "Mol → Partikel",
        "Partikel → Mol",
        "Mol → Volume Gas (STP)",
        "Volume Gas → Mol (STP)"
    ])

    st.divider()

    if konversi == "Mol → Gram":
        mol = st.number_input("Masukkan jumlah mol", min_value=0.0)
        massa_molar = st.number_input("Massa molar (g/mol)", min_value=0.0)
        if st.button("Hitung"):
            gram = mol * massa_molar
            st.success(f"{mol} mol = {gram:.4f} gram")

    elif konversi == "Gram → Mol":
        gram = st.number_input("Masukkan massa (gram)", min_value=0.0)
        massa_molar = st.number_input("Massa molar (g/mol)", min_value=0.0)
        if st.button("Hitung"):
            mol = gram / massa_molar
            st.success(f"{gram} gram = {mol:.4f} mol")

    elif konversi == "Mol → Partikel":
        mol = st.number_input("Masukkan mol", min_value=0.0)
        if st.button("Hitung"):
            partikel = mol * AVOGADRO
            st.success(f"{mol} mol = {partikel:.2e} partikel")

    elif konversi == "Partikel → Mol":
        partikel = st.number_input("Masukkan jumlah partikel", min_value=0.0)
        if st.button("Hitung"):
            mol = partikel / AVOGADRO
            st.success(f"{partikel:.2e} partikel = {mol:.4f} mol")

    elif konversi == "Mol → Volume Gas (STP)":
        mol = st.number_input("Masukkan mol", min_value=0.0)
        if st.button("Hitung"):
            volume = mol * VOLUME_STP
            st.success(f"{mol} mol = {volume:.2f} liter (pada STP)")

    elif konversi == "Volume Gas → Mol (STP)":
        volume = st.number_input("Masukkan volume gas (liter)", min_value=0.0)
        if st.button("Hitung"):
            mol = volume / VOLUME_STP
            st.success(f"{volume} liter = {mol:.4f} mol")

# =========================
# HALAMAN 3: INFORMASI
# =========================
elif halaman == "Informasi":
    st.title("📘 Informasi Aplikasi")

    st.markdown("""
    **Aplikasi Konversi Kimia** ini dibuat untuk mendukung pembelajaran kimia interaktif berbasis web menggunakan Streamlit.

    **Fitur Utama:**
    - Konversi mol ke satuan lain
    - Antarmuka sederhana dan edukatif
    - Dapat dijalankan di web tanpa instalasi berat

    **Teknologi:**
    - Python
    - Streamlit
    - GitHub (jika di-deploy)

    **Kontak Pengembang:**
    - Nama: *[Isi Namamu]*
    - Email: *email@example.com*
    - GitHub: [github.com/username](https://github.com/username)
    """)

    st.image("https://upload.wikimedia.org/wikipedia/commons/3/38/Periodic_table_large.png", caption="Tabel Periodik Unsur", use_column_width=True)


    
#===========================================================================================
