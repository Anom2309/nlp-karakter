import streamlit as st
import datetime
import os
import time

# --- PENGATURAN HALAMAN ---
st.set_page_config(page_title="Cek Program Pikiran - Ahmad Septian", page_icon="🧠", layout="centered")

# --- SIDEBAR PROMOSI (BAHASA AWAM) ---
with st.sidebar:
    st.markdown("## 🧠 Beresin Pikiran, Yuk!")
    st.markdown("---")
    st.info("**Merasa Hidup Stagnan?**\n\nMungkin ada 'virus' atau program lama di pikiranmu yang perlu di-update. Konsultasi langsung sama **Ahmad Septian** buat hapus beban mentalmu.")
    st.markdown("[👉 **Atur Jadwal Obrolan**](https://lynk.id/username_lu/private-hypnotherapy)")
    st.markdown("---")
    st.success("**📚 Cara Jago Ngomong**\n\nBelajar teknik NLP biar omonganmu gampang dituruti orang lain. Cocok buat jualan atau negosiasi.")
    st.markdown("[👉 **Ambil Materinya**](https://lynk.id/username_lu/ebook-nlp)")
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
st.title("🧠 Cek 'Program' Bawah Sadarmu")
st.write("Cari tahu pola pikiranmu lewat hitungan tanggal lahir, adat jawa (weton), dan bintang (zodiak).")
st.markdown("---")

nama_user = st.text_input("Siapa nama panggilanmu?", placeholder="Tulis namamu di sini ya...")

tgl_today = datetime.date.today()
tgl_input = st.date_input(
    "Pilih Tanggal Lahirmu:",
    value=tgl_today,
    min_value=datetime.date(1920, 1, 1),
    max_value=tgl_today,
    format="DD/MM/YYYY"
)

st.markdown("---")

# --- PROSES ANALISA ---
if st.button("Lihat Hasil Analisa", type="primary"):
    if not nama_user:
        st.error("🚨 **Maaf:** Isi namamu dulu ya biar sistem nggak bingung.")
    elif tgl_input == tgl_today:
        st.error("🚨 **Maaf:** Tanggal lahirnya diganti dulu ya, jangan pakai tanggal hari ini.")
    else:
        with st.spinner('Sedang memetakan pola pikiranmu...'):
            time.sleep(2) 
            
            angka_hasil = hitung_angka(tgl_input)
            weton_hasil = hitung_weton(tgl_input)
            zodiak_hasil = hitung_zodiak(tgl_input)
        
        st.markdown(f"### 📋 Hasil Untuk: {nama_user}")
        st.divider()
        
        c1, c2, c3 = st.columns(3)
        c1.metric("KODE PIKIRAN", angka_hasil)
        c2.metric("WETON", weton_hasil)
        c3.metric("ZODIAK", zodiak_hasil)
        
        st.markdown("---")
        
        # NARASI BAHASA AWAM
        st.write(f"Halo **{nama_user}**, sistem kami melihat kalau kamu punya pola bawaan dari **{zodiak_hasil}** dan **{weton_hasil}**.")
        
        st.info(f"**Apa artinya buat kamu?**\n\nSebagai pemilik **Kode {angka_hasil}**, pikiranmu itu ibarat HP yang punya spek tinggi tapi sering 'lemot' karena ada settingan lama yang nggak cocok. Kamu sering ngerasa pengen maju, tapi kayak ada rem tangan yang narik di belakang.")
        
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
        
        st.markdown(f"#### 🔓 Mau 'Update' Program Pikiranmu?")
        st.write(f"Khusus buat pemilik Kode {angka_hasil}, ada cara cepat buat hapus hambatan mentalmu biar hidup makin lancar.")
        
        st.link_button(f"👉 DOWNLOAD CARA UPDATE-NYA (KODE {angka_hasil})", url_tujuan, type="primary")

# --- FOOTER ---
st.markdown("---")
st.write(f"Dibuat oleh **Ahmad Septian Dwi Cahyo** - Pakar Re-Program Pikiran & Hipnoterapi.")
