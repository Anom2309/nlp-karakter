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
    .stButton>button { width: 100%; background-color: #d4af37; color: black; font-weight: bold; border-radius: 5px; border: none; }
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

# --- DATABASE ANALISA MENDALAM (ULTIMATE VERSION) ---
def get_deep_analysis(angka, nama):
    data = {
        1: {
            "title": "Sang Perintis (The Initiator)",
            "karakter": f"Halo **{nama}**, Anda memiliki instalasi mental seorang pemimpin. Anda didesain untuk membuka jalan. Namun, seringkali *Internal Dialogue* Anda terlalu keras, menuntut kesempurnaan yang justru memicu penundaan (*procrastination*). Anda tidak malas, Anda hanya terlalu takut jika hasilnya tidak sempurna.",
            "asmara": "Anda dominan dan protektif. Tantangan NLP Anda adalah belajar *Active Listening*. Pasangan Anda butuh merasa didengarkan sebagai subjek, bukan sekadar diberi instruksi atau solusi cepat.",
            "insight": "Anda sering merasa 'sendirian di puncak'. Reframing: Meminta bantuan bukan tanda lemah, tapi strategi *leverage* untuk melompat lebih tinggi."
        },
        2: {
            "title": "Sang Penyelaras (The Harmonizer)",
            "karakter": f"**{nama}**, Anda memiliki intuisi tajam untuk membaca perasaan orang lain. Anda adalah lem yang menyatukan tim. Namun, Anda sering terjebak dalam pola *People Pleasing*—sulit berkata 'tidak' hingga mengabaikan kebutuhan diri sendiri.",
            "asmara": "Anda sangat setia, namun sering memendam emosi demi menghindari konflik. Ini bisa menjadi bom waktu yang merusak kedekatan emosional jika tidak dikomunikasikan.",
            "insight": "Keharmonisan sejati dimulai dari kejujuran pada diri sendiri. Belajarlah untuk menetapkan *Boundaries* (batasan) yang sehat."
        },
        3: {
            "title": "Sang Ekspresif (The Communicator)",
            "karakter": f"Pikiran Anda, **{nama}**, bekerja dengan kecepatan tinggi dalam bentuk visual. Anda kreatif dan penuh ide. Namun, Anda sering mengalami *Shiny Object Syndrome*—mudah memulai hal baru tapi sulit menyelesaikannya.",
            "asmara": "Anda adalah pasangan yang ceria. Tantangannya adalah kedalaman. Kadang Anda menutupi kegelisahan dengan candaan, sehingga pasangan sulit menyentuh sisi terdalam Anda.",
            "insight": "Fokus adalah kekuatan Anda yang tersembunyi. Berlatihlah teknik *Chunking Down* untuk menyelesaikan satu misi besar hingga tuntas."
        },
        4: {
            "title": "Sang Pembangun (The Architect)",
            "karakter": f"**{nama}**, Anda adalah pilar stabilitas. Anda mencintai struktur, data, dan kepastian. Namun, pola pikir prosedural ini membuat Anda stres jika menghadapi perubahan mendadak atau ketidakpastian.",
            "asmara": "Cinta bagi Anda adalah tanggung jawab nyata. Pasangan mungkin merasa Anda kurang romantis secara verbal, karena Anda lebih fokus pada bukti tindakan (*Acts of Service*).",
            "insight": "Fleksibilitas adalah kunci evolusi Anda. Belajarlah menerima bahwa ketidakpastian adalah bagian dari keindahan hidup."
        },
        5: {
            "title": "Sang Penjelajah (The Visionary)",
            "karakter": f"Kebebasan adalah oksigen bagi Anda, **{nama}**. Anda cepat belajar dan mudah beradaptasi. Tantangannya adalah rasa bosan yang ekstrem terhadap rutinitas, yang sering membuat hidup Anda terasa tidak stabil.",
            "asmara": "Sangat menarik dan penuh kejutan. Namun, Anda cenderung melarikan diri secara emosional jika merasa 'tercekik' oleh komitmen atau aturan yang terlalu kaku.",
            "insight": "Disiplin bukan penjara, melainkan jembatan menuju kebebasan yang lebih besar. Temukan fokus utama yang layak Anda perjuangkan."
        },
        6: {
            "title": "Sang Pelindung (The Nurturer)",
            "karakter": f"**{nama}**, Anda memiliki energi pengasuh yang besar. Anda merasa bertanggung jawab atas kebahagiaan orang di sekitar Anda. Namun, ini sering membuat Anda lelah secara emosional karena memikul beban yang bukan milik Anda.",
            "asmara": "Sangat hangat dan berorientasi keluarga. Tantangan NLP-nya: Hindari pola *Over-Controlling* (terlalu mengatur) yang lahir dari rasa takut kehilangan atau takut mereka celaka.",
            "insight": "Anda tidak bisa menuang dari gelas yang kosong. Rawatlah diri Anda terlebih dahulu sebelum merawat dunia."
        },
        7: {
            "title": "Sang Pencari (The Analyst)",
            "karakter": f"**{nama}**, Anda adalah pemikir dalam yang skeptis dan analitis. Anda butuh waktu menyendiri untuk memproses informasi. Namun, Anda sering terjebak dalam *Overthinking* yang menghambat pengambilan tindakan nyata.",
            "asmara": "Koneksi intelektual adalah segalanya bagi Anda. Jika tidak ada diskusi yang mendalam, Anda akan merasa asing bahkan saat sedang bersama pasangan.",
            "insight": "Jawaban yang Anda cari seringkali ada dalam pengalaman, bukan dalam pemikiran. Keluarlah dari 'gua' pikiran Anda dan mulai bertindak."
        },
        8: {
            "title": "Sang Eksekutif (The Strategist)",
            "karakter": f"**{nama}**, Anda memiliki ambisi besar dan orientasi pada hasil. Anda mampu memimpin di bawah tekanan. Namun, seringkali Anda terlihat dingin atau terlalu otoriter karena terlalu fokus pada target.",
            "asmara": "Anda ingin memberikan segalanya secara material. Namun, ingatlah bahwa kehadiran emosional Anda jauh lebih berharga daripada fasilitas yang Anda berikan.",
            "insight": "Kekuatan sejati adalah kelembutan yang terkendali. Belajarlah untuk mengapresiasi proses, bukan hanya hasil akhir."
        },
        9: {
            "title": "Sang Humanis (The Philanthropist)",
            "karakter": f"Visi Anda melampaui diri sendiri, **{nama}**. Anda penuh empati dan idealis. Namun, Anda sering merasa kecewa atau terluka jika realitas dunia tidak sejalan dengan standar moral tinggi yang Anda pegang.",
            "asmara": "Anda mencintai tanpa syarat dan sangat pemaaf. Bahayanya, Anda sering mengizinkan orang yang salah menetap terlalu lama dalam hidup Anda hanya karena rasa iba.",
            "insight": "Tegaskan batasan Anda. Membantu orang lain tidak boleh menghancurkan diri Anda sendiri. Anda berhak untuk bahagia."
        }
    }
    return data.get(angka)

# --- INTERFACE UTAMA ---
st.title("🧠 NLP Deep Analysis")
st.subheader("Mapping Your Internal Program")
st.write("Gunakan data kelahiran Anda sebagai filter untuk memetakan program pikiran bawah sadar.")
st.markdown("---")

nama_user = st.text_input("Siapa nama lengkap Anda?", placeholder="Input Nama Anda...")

tgl_today = datetime.date.today()
tgl_input = st.date_input(
    "Data Input (Tanggal Lahir):",
    value=tgl_today,
    min_value=datetime.date(1920, 1, 1),
    max_value=tgl_today,
    format="DD/MM/YYYY"
)

st.markdown("---")

if st.button("Mulai Pemetaan Internal", type="primary"):
    if not nama_user:
        st.error("🚨 **Peringatan:** Nama diperlukan untuk kalibrasi pola pikiran.")
    elif tgl_input == tgl_today:
        st.error("🚨 **Peringatan:** Mohon pilih tanggal lahir Anda yang benar.")
    else:
        with st.spinner('Menganalisa Meta-Program & Struktur Pikiran...'):
            time.sleep(2) 
            
            angka_hasil = hitung_angka(tgl_input)
            weton_hasil = hitung_weton(tgl_input)
            zodiak_hasil = hitung_zodiak(tgl_input)
            detail = get_deep_analysis(angka_hasil, nama_user)
        
        # --- HASIL UTAMA ---
        st.markdown(f"### 📋 Laporan Pemetaan: {nama_user}")
        st.divider()
        
        col1, col2, col3 = st.columns(3)
        col1.metric("KODE PROGRAM", angka_hasil)
        col2.metric("ENERGI WETON", weton_hasil)
        col3.metric("POLA ZODIAK", zodiak_hasil)
        
        st.markdown("---")
        
        # --- PENJELASAN MENDALAM ---
        st.header(f"✨ {detail['title']}")
        
        st.subheader("💡 Struktur Karakter & Mental")
        st.info(detail['karakter'])
        
        st.subheader("❤️ Dinamika Hubungan & Asmara")
        st.warning(detail['asmara'])
        
        st.subheader("🔍 Deep Insight (NLP Perspective)")
        st.success(detail['insight'])
        
        # --- CTA ---
        st.markdown("---")
        st.markdown(f"#### 🔓 Ingin Memprogram Ulang Hidup Anda, {nama_user}?")
        st.write(f"Khusus pemilik **Kode {angka_hasil}**, saya telah menyiapkan modul transformasi khusus untuk menghapus *Mental Block* Anda secara permanen.")
        
        url_tujuan = f"https://lynk.id/username_lu/produk-angka-{angka_hasil}"
        st.link_button(f"👉 DOWNLOAD MODUL TRANSFORMASI ANGKA {angka_hasil}", url_tujuan, type="primary")

        # --- FAQ ---
        st.markdown("---")
        with st.expander("❓ Pertanyaan Sering Diajukan (FAQ)"):
            st.write("**Apakah ini ramalan?** Bukan. Ini adalah pemetaan pola perilaku berdasarkan kecenderungan psikologis yang dikemas dalam kerangka NLP.")
            st.write("**Kenapa hasilnya terasa sangat akurat?** Karena kami menggunakan gabungan filter data personal yang membentuk struktur pengalaman subjektif Anda.")

        # --- DISCLAIMER ---
        with st.expander("⚖️ Disclaimer & Batasan Layanan"):
            st.caption("Hasil analisa ini bertujuan untuk edukasi dan refleksi diri. Ahmad Septian tidak bertanggung jawab atas keputusan pribadi pengguna. Untuk hasil maksimal, disarankan mengikuti sesi konsultasi privat.")

# --- FOOTER ---
st.markdown("---")
st.write(f"Developed by **Ahmad Septian Dwi Cahyo** - Certified NLP Trainer & Professional Hypnotherapist.")
