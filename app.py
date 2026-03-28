import streamlit as st
import datetime
import os

# --- PENGATURAN HALAMAN ---
st.set_page_config(page_title="Peta Karakter Bawah Sadar", page_icon="✨", layout="centered")

# --- SIDEBAR PROMOSI ---
with st.sidebar:
    st.markdown("## 🌟 Layanan Eksklusif")
    st.info("**🧠 Sesi Private Hypnotherapy**\n\nLepaskan mental block bersama Ahmad Septian.")
    st.markdown("[👉 Booking Jadwal](https://lynk.id/username_lu/private-hypnotherapy)")
    st.markdown("---")
    st.success("**📚 E-Book: NLP Persuasi**\n\nKuasai teknik komunikasi bawah sadar.")
    st.markdown("[👉 Download Sekarang](https://lynk.id/username_lu/ebook-nlp)")

# --- TAMPILKAN BANNER ---
if os.path.exists("banner.jpg"):
    st.image("banner.jpg", use_container_width=True)

# --- FUNGSI LOGIKA PERHITUNGAN ---
def hitung_angka(tanggal):
    tgl_str = tanggal.strftime("%d%m%Y")
    total = sum(int(digit) for digit in tgl_str)
    while total > 9: total = sum(int(digit) for digit in str(total))
    return total

def hitung_weton(tanggal):
    anchor_date = datetime.date(2000, 1, 1)
    selisih_hari = (tanggal - anchor_date).days
    hari_masehi = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    pasaran_jawa = ["Pahing", "Pon", "Wage", "Kliwon", "Legi"]
    return f"{hari_masehi[tanggal.weekday()]} {pasaran_jawa[selisih_hari % 5]}"

def hitung_zodiak(tanggal):
    d, m = tanggal.day, tanggal.month
    if (m == 3 and d >= 21) or (m == 4 and d <= 19): return "Aries"
    elif (m == 4 and d >= 20) or (m == 5 and d <= 20): return "Taurus"
    elif (m == 5 and d >= 21) or (m == 6 and d <= 20): return "Gemini"
    elif (m == 6 and d >= 21) or (m == 7 and d <= 22): return "Cancer"
    elif (m == 7 and d >= 23) or (m == 8 and d <= 22): return "Leo"
    elif (m == 8 and d >= 23) or (m == 9 and d <= 22): return "Virgo"
    elif (m == 9 and d >= 23) or (m == 10 and d <= 22): return "Libra"
    elif (m == 10 and d >= 23) or (m == 11 and d <= 21): return "Scorpio"
    elif (m == 11 and d >= 22) or (m == 12 and d <= 21): return "Sagittarius"
    elif (m == 12 and d >= 22) or (m == 1 and d <= 19): return "Capricorn"
    elif (m == 1 and d >= 20) or (m == 2 and d <= 18): return "Aquarius"
    else: return "Pisces"

# --- INTERFACE UTAMA ---
st.title("✨ Peta Karakter Bawah Sadar")
st.write("Temukan potensi tersembunyi melalui perpaduan Numerologi, Weton, dan Zodiak.")

# 1. INPUT NAMA
nama_user = st.text_input("Siapa nama lengkapmu?", placeholder="Masukkan namamu di sini...")

# 2. INPUT TANGGAL (Default ke hari ini, tapi kita kasih satpam konfirmasi)
st.write("Silakan pilih tanggal lahirmu:")
tgl_input = st.date_input(
    "Tanggal Lahir:",
    value=datetime.date.today(),
    min_value=datetime.date(1920, 1, 1),
    max_value=datetime.date.today(),
    format="DD/MM/YYYY"
)

# SATPAM KONFIRMASI (Agar klien sadar sedang input data)
sudah_input = st.checkbox("Saya sudah memastikan nama dan tanggal lahir saya benar.")

st.markdown("---")

# 3. TOMBOL ANALISA (Hanya jalan kalau checklist sudah dicentang)
if st.button("Analisa Karakter Saya Sekarang", type="primary"):
    if not nama_user:
        st.warning("⚠️ Mohon isi Nama Lengkap Anda terlebih dahulu.")
    elif not sudah_input:
        st.error("🚨 **Satpam:** Silakan centang kotak konfirmasi di atas untuk memvalidasi data Anda.")
    else:
        # Menghitung Hasil
        angka = hitung_angka(tgl_input)
        weton = hitung_weton(tgl_input)
        zodiak = hitung_zodiak(tgl_input)
        
        # Animasi Perayaan
        st.balloons()
        st.success(f"Halo **{nama_user}**, Analisa Anda telah siap!")
        
        # Menampilkan Metric (Angka, Weton, Zodiak)
        col1, col2, col3 = st.columns(3)
        col1.metric("Angka Karakter", angka)
        col2.metric("Weton Jawa", weton)
        col3.metric("Zodiak", zodiak)
        
        st.markdown("---")
        
        # Copywriting Curiosity ala NLP
        st.info(f"Kombinasi antara energi **{zodiak}** dan weton **{weton}** menciptakan pola pikiran bawah sadar yang sangat kuat. Namun, sebagai pemilik **Angka Karakter {angka}**, ada satu 'Program Mental' tersembunyi yang mungkin selama ini menghambat kesuksesanmu...")
        
        # Call to Action ke Lynk.id
        st.markdown(f"### 🔓 Buka Rahasia Penuh Potensimu, {nama_user}!")
        st.write("Dapatkan analisa video eksklusif dan panduan psikologis yang dirancang khusus untuk kombinasi unikmu ini.")
        
        # Link Dinamis (Ganti username_lu jadi username Lynk.id lu)
        url_tujuan = f"https://lynk.id/username_lu/produk-{angka}"
        st.link_button("👉 KLIK DI SINI UNTUK DOWNLOAD HASIL LENGKAP", url_tujuan, type="primary")

# --- PROFIL KREATOR ---
st.markdown("---")
st.markdown("### 👤 Tentang Kreator")
st.write("**Ahmad Septian Dwi Cahyo** adalah seorang Trainer NLP & Profesional Hipnoterapis yang mendedikasikan ilmunya untuk membantu Anda mengenali potensi pikiran bawah sadar melalui kearifan lokal dan psikologi modern.")
st.write(f"Aplikasi ini dikembangkan oleh **Ahmad Septian Dwi Cahyo**, seorang Trainer NLP & Hipnoterapis.")
