import streamlit as st

# ----------------- Konfigurasi halaman -----------------
st.set_page_config(page_title="My Concentration", page_icon="⚗", layout="centered")

# ----------------- Styling CSS -----------------
st.markdown("""
    <style>
        body {
            background-color: #fdfdff;
        }
        .title {
            color: #5f27cd;
            text-align: center;
        }
        .sub {
            text-align: center;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------- Fungsi konversi -----------------
def convert_ppm(nilai):
    return f"{nilai} mg/L"

def convert_normalitas(massa, valensi, berat_eq):
    try:
        return (massa / berat_eq) * valensi
    except:
        return "Input tidak valid"

def convert_molaritas(massa, mr, volume_ml):
    try:
        volume_l = volume_ml / 1000
        mol = massa / mr
        return mol / volume_l
    except:
        return "Input tidak valid"

# ----------------- Tampilan halaman -----------------

def halaman_utama():
    st.markdown("<h1 class='title'>Selamat Datang di My Concentration</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub'>Aplikasi ini digunakan sebagai alat pengkonversi satuan</p>", unsafe_allow_html=True)
    if st.button("Selanjutnya ➡"):
        st.session_state["halaman"] = "menu"

def halaman_menu():
    st.markdown("<h2 class='title'>📂 Menu Utama</h2>", unsafe_allow_html=True)
    menu = st.radio("Silahkan pilih menu:", ["Penjelasan Konsentrasi", "Penggunaan Aplikasi", "Aplikasi Konversi", "Tabel Periodik"])

    if menu == "Penjelasan Konsentrasi":
        halaman_penjelasan()
    elif menu == "Penggunaan Aplikasi":
        halaman_penggunaan()
    elif menu == "Aplikasi Konversi":
        halaman_konversi()
    elif menu == "Tabel Periodik":
        halaman_periodik()

def halaman_penjelasan():
    st.markdown("## 🧪 Penjelasan Konsentrasi")
    st.info("""
    *1. PPM (mg/L)*  
    Digunakan saat konsentrasi zat sangat kecil.  
    Cocok untuk: Deteksi zat dalam jumlah sangat kecil.

    *2. Normalitas (N)*  
    Digunakan dalam reaksi kimia, terutama yang melibatkan ion H⁺ atau OH⁻.  
    Cocok untuk: Perhitungan stoikiometri reaksi.

    *3. Molaritas (M)*  
    Digunakan untuk menghitung jumlah mol zat dalam 1 liter larutan.  
    Cocok untuk: titrasi, pembuatan larutan, dan stoikiometri.
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅ Kembali ke Menu", on_click=lambda: st.session_state.update({"halaman": "menu"}))
    with col2:
        st.button("🏠 Halaman Utama", on_click=lambda: st.session_state.update({"halaman": "utama"}))

def halaman_penggunaan():
    st.markdown("## 📘 Penggunaan Aplikasi")
    st.warning("""
    1. Pilih kategori konversi (PPM, Normalitas, Molaritas)  
    2. Masukkan data yang sesuai:
        - PPM: masukkan nilai
        - Normalitas: masukkan massa & valensi
        - Molaritas: masukkan massa & berat molekul (Mr)
    3. Tekan tombol KONVERSI untuk melihat hasil.
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅ Kembali ke Menu", on_click=lambda: st.session_state.update({"halaman": "menu"}))
    with col2:
        st.button("🏠 Halaman Utama", on_click=lambda: st.session_state.update({"halaman": "utama"}))

def halaman_konversi():
    st.markdown("## 🧪 Aplikasi Konversi Konsentrasi")
    pilihan = st.selectbox("Pilih jenis konversi:", ["PPM", "Normalitas", "Molaritas"])

    # ---------------- PPM ----------------
    if pilihan == "PPM":
        nilai = st.number_input("Masukkan nilai PPM (mg/L):", step=0.1)
        if st.button("Konversi"):
            st.success(f"Hasil PPM: {nilai} mg/L")

            st.markdown("### 📘 Langkah Perhitungan:")
            st.latex(r"\text{PPM} = \cfrac{\text{mg zat}}{\text{liter larutan}}")
            st.latex(rf"\text{{PPM}} = \cfrac{{{nilai}}}{{1}} = {nilai} \, \text{{mg/L}}")

    # ---------------- Normalitas ----------------
    elif pilihan == "Normalitas":
        massa = st.number_input("Masukkan massa zat (g):", step=0.01)
        berat_eq = st.number_input("Masukkan berat ekuivalen (g/mol):", step=0.01)
        valensi = st.number_input("Masukkan valensi:", step=1)
        if st.button("Konversi"):
            try:
                normalitas = (massa / berat_eq) * valensi
                st.success(f"Hasil Normalitas: {normalitas:.4f} N")

                st.markdown("### 📘 Langkah Perhitungan:")
                st.latex(r"\text{N} = \left( \cfrac{\text{massa}}{\text{berat ekuivalen}} \right) \times \text{valensi}")
                st.latex(rf"\text{{N}} = \left( \cfrac{{{massa}}}{{{berat_eq}}} \right) \times {valensi}")
                st.latex(rf"\text{{N}} = {normalitas:.4f} \, \text{{N}}")

            except:
                st.error("Terjadi kesalahan dalam perhitungan.")

    # ---------------- Molaritas ----------------
    elif pilihan == "Molaritas":
        massa = st.number_input("Masukkan massa zat (g):", step=0.01)
        mr = st.number_input("Masukkan Mr (massa molekul relatif):", step=0.01)
        volume_ml = st.number_input("Masukkan volume larutan (mL):", step=1)
        if st.button("Konversi"):
            try:
                volume_l = volume_ml / 1000
                mol = massa / mr
                molaritas = mol / volume_l

                st.success(f"Hasil Molaritas: {molaritas:.4f} M")

                st.markdown("### 📘 Langkah Perhitungan:")
                st.latex(r"\text{Mol} = \cfrac{\text{massa}}{\text{Mr}}")
                st.latex(rf"\text{{Mol}} = \cfrac{{{massa}}}{{{mr}}} = {mol:.4f} \, \text{{mol}}")
                st.latex(r"\text{M} = \cfrac{\text{mol}}{\text{volume (L)}}")
                st.latex(rf"\text{{M}} = \cfrac{{{mol:.4f}}}{{{volume_l}}} = {molaritas:.4f} \, \text{{M}}")

            except:
                st.error("Terjadi kesalahan dalam perhitungan.")

    # ---------------- Navigasi ----------------
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅ Kembali ke Menu", on_click=lambda: st.session_state.update({"halaman": "menu"}))
    with col2:
        st.button("🏠 Halaman Utama", on_click=lambda: st.session_state.update({"halaman": "utama"}))

def halaman_periodik():
    st.markdown("## 🧬 Tabel Periodik Unsur Kimia")
    st.image("https://gurubelajarku.com/wp-content/uploads/2019/12/Tabel-Periodik-Unsur-Kimia.jpg",
             caption="Sumber: gurubelajarku.com")

    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅ Kembali ke Menu", on_click=lambda: st.session_state.update({"halaman": "menu"}))
    with col2:
        st.button("🏠 Halaman Utama", on_click=lambda: st.session_state.update({"halaman": "utama"}))

# ----------------- Routing -----------------
if "halaman" not in st.session_state:
    st.session_state["halaman"] = "utama"

if st.session_state["halaman"] == "utama":
    halaman_utama()
elif st.session_state["halaman"] == "menu":
    halaman_menu()
