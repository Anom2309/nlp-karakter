import streamlit as st
import datetime
import os
import time

# --- PENGATURAN HALAMAN ---
st.set_page_config(page_title="NLP Deep Analysis - Ahmad Septian", page_icon="🧠", layout="centered")

# --- SIDEBAR PROMOSI (NLP FOCUS) ---
with st.sidebar:
    st.markdown("## 🧠 NLP Mastery")
    st.markdown("---")
    st.info("**Re-Program Your Mind!**\n\nJangan biarkan *Limiting Beliefs* menghambatmu. Temukan struktur internal pikiranmu melalui sesi *Private Hypno-NLP* bersama **Ahmad Septian**.")
    st.markdown("[👉 **Install Program Sukses**](https://lynk.id/username_lu/private-hypnotherapy)")
    st.markdown("---")
    st.success("**📚 E-Book: NLP Persuasi**\n\nKuasai *Language Patterns* untuk meng-install gagasan ke pikiran bawah sadar orang lain.")
    st.markdown("[👉 **Download Modul**](https://lynk.id/username_lu/ebook-nlp)")
    st.markdown("---")
    st.caption("© 2026 Ahmad Septian Dwi Cahyo")

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
st.title("🧠 Neuro-Linguistic Programming (NLP) Analysis")
st.write("Membedah struktur pengalaman subjektif melalui penggabungan *Deep Numerology* dan kearifan lokal.")
st.markdown("---")

nama_user = st.text_input("Siapa nama lengkapmu?", placeholder="Identifikasi diri Anda...")

tgl_today = datetime.date.today()
tgl_input = st.date_input(
    "Tanggal Kelahiran (Data Input):",
    value=tgl_today,
    min_value=datetime.date(1920, 1, 1),
    max_value=tgl_today,
    format="DD/MM/YYYY"
)

st.markdown("---")

# --- PROSES ANALISA ---
if st.button("Mulai Pemetaan Bawah Sadar", type="primary"):
    if not nama_user:
        st.error("🚨 **Error:** Input nama diperlukan untuk pemetaan Meta-Program.")
    elif tgl_input == tgl_today:
        st.error("🚨 **Error:** Input tanggal lahir diperlukan untuk sinkronisasi data.")
    else:
        with st.spinner('Menganalisa Meta-Program & Struktur Pikiran...'):
            time.sleep(2) 
            
            angka_hasil = hitung_angka(tgl_input)
            weton_hasil = hitung_weton(tgl_input)
            zodiak_hasil = hitung_zodiak(tgl_input)
        
        st.markdown(f"### 📋 Mapping Result: {nama_user}")
        st.divider()
        
        c1, c2, c3 = st.columns(3)
        c1.metric("KODE PROGRAM", angka_hasil)
        c2.metric("VAR WETON", weton_hasil)
        c3.metric("VAR ZODIAK", zodiak_hasil)
        
        st.markdown("---")
        
        # NARASI FULL NLP
        st.write(f"Berdasarkan analisa **Neuro-Linguistic**, Anda memiliki pola frekuensi dominan yang dipengaruhi oleh energi **{zodiak_hasil}** dan **{weton_hasil}** sebagai filter eksternal.")
        
        st.info(f"**Analisa NLP untuk {nama_user}:**\n\nSebagai pemilik **Angka Karakter {angka_hasil}**, struktur *Representational System* Anda cenderung memiliki pola unik yang jika tidak dikalibrasi dengan benar dapat menciptakan *Mental Block*. Terdapat ketidakselarasan antara *State* emosi dan *Behavior* yang sering Anda tampilkan.")
        
        # DATABASE LINK
        link_produk = {
            1: "https://lynk.id/username_lu/produk-angka-1",
            2: "https://lynk.id/username_lu/produk-angka-2",
            3: "https://lynk.id/username_lu/produk-angka-3",
            4: "https://lynk.id/username_lu/produk-angka-4",
            5: "https://lynk.id/username_lu/produk-angka-5",
            6: "https://lynk.id/username_lu/produk-angka-6",
            7: "https://lynk.id/username_lu/produk-angka-7",
            8: "https://lynk.id/username_lu/produk-angka-8",
            9: "https://lynk.id/username_lu/produk-angka-9"
        }
        
        url_tujuan = link_produk.get(angka_hasil, "https://lynk.id/username_lu")
        
        st.markdown(f"#### 🔓 Lakukan Reframing Sekarang, {nama_user}!")
        st.write(f"Akses data lengkap untuk memprogram ulang *Submodalitas* pikiran Anda dan menghapus *Limiting Beliefs* khusus untuk pemilik Angka {angka_hasil}.")
        
        st.link_button(f"👉 DOWNLOAD MODUL RE-PROGRAMMING (ANGKA {angka_hasil})", url_tujuan, type="primary")

# --- FOOTER ---
st.markdown("---")
st.write(f"Developed by **Ahmad Septian Dwi Cahyo** - Certified NLP Trainer & Hypnotherapist.")
