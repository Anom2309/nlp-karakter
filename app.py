import streamlit as st
import datetime
import os
import time

# --- PENGATURAN HALAMAN ---
st.set_page_config(
    page_title="NLP Deep Analysis | Ahmad Septian", 
    page_icon="🧠", 
    layout="centered"
)

# --- CUSTOM CSS (GOLD THEME) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1c1e26; border: 1px solid #d4af37; padding: 15px; border-radius: 10px; }
    .stButton>button { width: 100%; background-color: #d4af37; color: black; font-weight: bold; border-radius: 5px; border: none; height: 50px; }
    .stButton>button:hover { background-color: #b8962e; color: white; }
    </style>
    """, unsafe_allow_stdio=True)

# --- SIDEBAR PROMOSI ---
with st.sidebar:
    st.markdown("## 🧠 Sesi Transformasi")
    st.markdown("---")
    st.info("**Reset Pola Pikir Anda**\n\nSering merasa terhambat oleh pikiran sendiri? Mari lakukan kalibrasi ulang dalam sesi *Private Hypno-NLP* bersama **Ahmad Septian**.")
    st.markdown("[👉 **Booking Jadwal Konsultasi**](https://lynk.id/username_lu/private-hypnotherapy)")
    st.markdown("---")
    st.success("**📚 Seni Persuasi NLP**\n\nKuasai bahasa bawah sadar untuk meningkatkan pengaruh Anda.")
    st.markdown("[👉 **Akses Modul Lengkap**](https://lynk.id/username_lu/ebook-nlp)")
    st.caption("© 2026 Ahmad Septian Dwi Cahyo")

# --- BANNER ---
if os.path.exists("banner.jpg"):
    st.image("banner.jpg", use_container_width=True)

# --- LOGIKA PERHITUNGAN ---
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

# --- DATABASE ANALISA MENDALAM ---
def get_deep_analysis(angka, nama):
    data = {
        1: {
            "title": "Sang Perintis (The Initiator)",
            "karakter": f"Halo **{nama}**, Anda memiliki instalasi mental seorang pemimpin. Namun, seringkali *Internal Dialogue* Anda terlalu keras, menuntut kesempurnaan yang memicu penundaan (*procrastination*).",
            "asmara": "Anda dominan dan protektif. Tantangan NLP Anda adalah belajar *Active Listening*. Pasangan butuh didengarkan, bukan sekadar diberi instruksi.",
            "insight": "Meminta bantuan bukan tanda lemah, tapi strategi *leverage* untuk melompat lebih tinggi."
        },
        2: {
            "title": "Sang Penyelaras (The Harmonizer)",
            "karakter": f"**{nama}**, Anda memiliki intuisi tajat untuk membaca perasaan orang lain. Namun, Anda sering terjebak dalam pola *People Pleasing* hingga mengabaikan diri sendiri.",
            "asmara": "Sangat setia, namun sering memendam emosi demi menghindari konflik. Ini bisa menjadi bom waktu bagi kedekatan emosional Anda.",
            "insight": "Keharmonisan sejati dimulai dari kejujuran pada diri sendiri. Belajarlah menetapkan *Boundaries*."
        },
        3: {
            "title": "Sang Ekspresif (The Communicator)",
            "karakter": f"Pikiran Anda, **{nama}**, bekerja sangat cepat secara visual. Namun, Anda sering mengalami *Shiny Object Syndrome*—mudah memulai tapi sulit menyelesaikan.",
            "asmara": "Pasangan yang ceria, namun kadang menutupi kegelisahan dengan candaan sehingga pasangan sulit menyentuh sisi terdalam Anda.",
            "insight": "Gunakan teknik *Chunking Down* untuk menyelesaikan satu misi besar hingga tuntas."
        },
        4: {
            "title": "Sang Pembangun (The Architect)",
            "karakter": f"**{nama}**, Anda adalah pilar stabilitas. Namun, pola pikir prosedural ini membuat Anda stres jika menghadapi perubahan mendadak.",
            "asmara": "Cinta bagi Anda adalah tanggung jawab nyata. Pasangan mungkin merasa Anda kurang romantis secara verbal karena fokus pada bukti tindakan.",
            "insight": "Fleksibilitas adalah kunci evolusi. Terima ketidakpastian sebagai bagian dari keindahan hidup."
        },
        5: {
            "title": "Sang Penjelajah (The Visionary)",
            "karakter": f"Kebebasan adalah oksigen bagi Anda, **{nama}**. Tantangannya adalah rasa bosan ekstrem terhadap rutinitas yang membuat hidup terasa tidak stabil.",
            "asmara": "Penuh kejutan, namun cenderung melarikan diri secara emosional jika merasa 'tercekik' oleh komitmen yang terlalu kaku.",
            "insight": "Disiplin adalah jembatan menuju kebebasan yang lebih besar. Temukan satu fokus yang layak diperjuangkan."
        },
        6: {
            "title": "Sang Pelindung (The N
