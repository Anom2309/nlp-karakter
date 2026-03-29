import streamlit as st
import datetime
import os
import time
import urllib.parse

# --- PENGATURAN HALAMAN ---
st.set_page_config(
    page_title="NLP Deep Analysis | Neuro Nada", 
    page_icon="🧠", 
    layout="centered"
)

# --- SIDEBAR PROMOSI ---
with st.sidebar:
    st.markdown("## 🧠 Sesi Transformasi")
    st.markdown("---")
    st.info("**Reset Pola Pikir Anda**\n\nSering merasa terhambat oleh pikiran sendiri? Mari kita lakukan kalibrasi ulang dalam sesi *Private Hypno-NLP* bersama **Ahmad Septian**.")
    st.markdown("[👉 **Amankan Jadwal Anda**](https://lynk.id/username_lu/private-hypnotherapy)")
    st.markdown("---")
    st.success("**📚 Seni Persuasi NLP**")
    st.markdown("[👉 **Akses Modul Lengkap**](https://lynk.id/username_lu/ebook-nlp)")
    st.markdown("---")
    st.caption("© 2026 Ahmad Septian")

# --- BANNER ---
if os.path.exists("banner.jpg"):
    st.image("banner.jpg", use_container_width=True)

# --- DATA ARKETIPE (TAMBAHAN) ---
nama_arketipe = {
    1: "Sang Inisiator",
    2: "Sang Penjaga",
    3: "Sang Visioner",
    4: "Sang Alchemist",
    5: "Sang Eksekutor",
    6: "Sang Harmonizer",
    7: "Sang Legacy Builder",
    8: "Sang Sovereign",
    9: "Sang Ascended"
}

deskripsi_arketipe = {
    1: "Energi memulai dan kepemimpinan.",
    2: "Energi menjaga dan kestabilan.",
    3: "Energi visi dan intuisi.",
    4: "Energi transformasi dan healing.",
    5: "Energi aksi dan eksekusi.",
    6: "Energi harmoni dan keseimbangan.",
    7: "Energi pembangunan dan legacy.",
    8: "Energi kekuasaan dan kontrol.",
    9: "Energi kesadaran dan pelepasan."
}

compatibility = {
    1: "Penjaga & Harmonizer",
    2: "Inisiator & Visioner",
    3: "Alchemist & Ascended",
    4: "Visioner & Harmonizer",
    5: "Inisiator & Sovereign",
    6: "Penjaga & Ascended",
    7: "Sovereign & Visioner",
    8: "Eksekutor & Legacy Builder",
    9: "Visioner & Harmonizer"
}

# --- DATABASE ANALISA ---
data_analisa = {
    1: {"karakter": "The Leader (Self, Towards)", "asmara": "Butuh pasangan yang menghargai independensi."},
    2: {"karakter": "The Mediator (Others)", "asmara": "Hindari pleasing berlebihan."},
    3: {"karakter": "The Communicator", "asmara": "Butuh stimulasi intelektual."},
    4: {"karakter": "The Architect", "asmara": "Butuh kepastian."},
    5: {"karakter": "The Explorer", "asmara": "Butuh freedom."},
    6: {"karakter": "The Nurturer", "asmara": "Hindari mind reading."},
    7: {"karakter": "The Analyst", "asmara": "Butuh me-time."},
    8: {"karakter": "The Strategist", "asmara": "Jangan terlalu dominan."},
    9: {"karakter": "The Humanist", "asmara": "Hindari terlalu memaklumi."}
}

# --- FUNGSI ---
def hitung_angka(tanggal):
    total = sum(int(d) for d in tanggal.strftime("%d%m%Y"))
    while total > 9:
        total = sum(int(d) for d in str(total))
    return total

# --- UI ---
st.title("🧠 NLP Deep Analysis")

nama_user = st.text_input("Nama Anda")
tgl_input = st.date_input("Tanggal Lahir")

if st.button("Mulai Analisa"):

    angka_hasil = hitung_angka(tgl_input)
    insight = data_analisa.get(angka_hasil)
    arketipe = nama_arketipe.get(angka_hasil)

    # --- HEADER ---
    st.markdown(f"# 🔮 {arketipe}")
    st.caption(deskripsi_arketipe.get(angka_hasil))

    # --- GAMBAR ---
    img = f"assets/arketipe_{angka_hasil}.png"
    if os.path.exists(img):
        st.image(img, use_container_width=True)

    # --- KARAKTER ---
    st.subheader("💡 Karakter")
    st.info(insight["karakter"])

    # --- INSIGHT EMOSIONAL ---
    st.success(f"""
    {nama_user}, arketipe Anda adalah **{arketipe}**.

    Ini bisa jadi kekuatan terbesar Anda…
    atau pola yang terus berulang tanpa sadar.
    """)

    # --- ASMARA ---
    st.subheader("❤️ Asmara")
    st.warning(insight["asmara"])

    # --- ARKETIPE SEKUNDER ---
    angka_2 = sum(int(d) for d in str(tgl_input.day))
    while angka_2 > 9:
        angka_2 = sum(int(d) for d in str(angka_2))

    st.markdown(f"### 🧬 Arketipe Sekunder: {nama_arketipe.get(angka_2)}")

    # --- COMPATIBILITY ---
    st.markdown(f"### ❤️ Cocok dengan: {compatibility.get(angka_hasil)}")

    # --- OPEN LOOP ---
    st.warning("""
    ⚠️ Ada pola tersembunyi yang belum terbuka:
    - blok rezeki
    - sabotase diri
    - siklus hubungan

    👉 buka versi lengkap
    """)

    # --- CTA ---
    st.link_button("🔓 Akses Modul Lengkap", "https://lynk.id")

    # --- DOWNLOAD ---
    st.download_button("📥 Download Hasil", f"Saya adalah {arketipe}")
