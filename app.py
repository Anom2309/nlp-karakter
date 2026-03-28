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

# --- SIDEBAR PROMOSI ---
with st.sidebar:
    st.markdown("## 🧠 Sesi Transformasi")
    st.info("**Reset Pola Pikir Anda**\n\nMari lakukan kalibrasi ulang dalam sesi *Private Hypno-NLP* bersama **Ahmad Septian**.")
    st.markdown("[👉 **Booking Jadwal**](https://lynk.id/username_lu/private-hypnotherapy)")
    st.markdown("---")
    st.success("**📚 Seni Persuasi NLP**\n\nKuasai bahasa bawah sadar Anda.")
    st.markdown("[👉 **Akses Modul**](https://lynk.id/username_lu/ebook-nlp)")

# --- FUNGSI LOGIKA ---
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

# --- DATABASE ANALISA ---
def get_analysis(angka, nama):
    data = {
        1: ["Sang Perintis", f"Halo **{nama}**, Anda adalah pemimpin alami. Namun, hati-hati dengan *Internal Dialogue* yang terlalu keras yang memicu penundaan.", "Anda dominan. Pasangan Anda butuh *Active Listening*, bukan sekadar instruksi.", "Meminta bantuan adalah strategi *leverage*, bukan tanda lemah."],
        2: ["Sang Penyelaras", f"**{nama}**, Anda sangat intuitif. Namun, Anda sering terjebak pola *People Pleasing* hingga mengabaikan diri sendiri.", "Sangat setia, namun sering memendam emosi demi menghindari konflik.", "Keharmonisan sejati dimulai dari kejujuran pada diri sendiri."],
        3: ["Sang Ekspresif", f"**{nama}**, pikiran Anda sangat cepat dan visual. Namun, Anda sering mudah memulai hal baru tapi sulit menyelesaikannya.", "Ceria, namun kadang menutupi kegelisahan dengan candaan.", "Gunakan teknik *Chunking Down* untuk fokus pada satu misi."],
        4: ["Sang Pembangun", f"**{nama}**, Anda adalah pilar stabilitas. Namun, Anda sering stres jika menghadapi perubahan mendadak.", "Cinta bagi Anda adalah tanggung jawab nyata. Pasangan mungkin merasa Anda kurang romantis secara verbal.", "Fleksibilitas adalah kunci evolusi Anda."],
        5: ["Sang Penjelajah", f"**{nama}**, kebebasan adalah oksigen bagi Anda. Namun, rasa bosan terhadap rutinitas sering membuat hidup terasa tidak stabil.", "Penuh kejutan, namun cenderung melarikan diri jika merasa tercekik komitmen.", "Disiplin adalah jembatan menuju kebebasan yang lebih besar."],
        6: ["Sang Pelindung", f"**{nama}**, Anda merasa bertanggung jawab atas kebahagiaan orang lain. Ini sering membuat Anda lelah secara emosional.", "Sangat hangat. Hindari pola *Over-Controlling* karena rasa takut kehilangan.", "Anda tidak bisa menuang dari gelas yang kosong. Rawat diri Anda dulu."],
        7: ["Sang Pencari", f"**{nama}**, Anda pemikir dalam yang analitis. Namun, Anda sering terjebak *Overthinking* yang menghambat tindakan.", "Koneksi intelektual adalah segalanya. Tanpa itu, Anda akan merasa asing.", "Jawaban ada dalam pengalaman nyata, bukan hanya dalam pikiran."],
        8: ["Sang Eksekutif", f"**{nama}**, Anda berorientasi hasil dan kuat di bawah tekanan. Namun, Anda sering terlihat dingin karena terlalu fokus target.", "Kehadiran emosional Anda jauh lebih berharga
