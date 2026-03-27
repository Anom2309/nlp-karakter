import streamlit as st
from datetime import date
import urllib.parse

# Konfigurasi Tampilan
st.set_page_config(page_title="Persona-NLP Analis", page_icon="🧠", layout="centered")

# Visual Estetik
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f4f7f6;
    }
    .main .block-container {
        background-color: white;
        padding: 3rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #2e7d32;
        color: white;
        font-weight: bold;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧠 Persona-NLP Analis")
st.markdown("**Temukan Struktur Pikiran & Potensimu di Balik Tanggal Lahir**")
st.write("---")

# Input Data
nama = st.text_input("Siapa nama kamu?", placeholder="Ketik namamu di sini...")
tgl_lahir = st.date_input("Kapan kamu lahir?", min_value=date(1930, 1, 1), max_value=date.today())

def hitung_life_path(tgl):
    # Mengambil angka dari tanggal
    digits = "".join(filter(str.isdigit, str(tgl)))
    total = sum(int(d) for d in digits)
    while total > 9 and total not in [11, 22, 33]:
        total = sum(int(d) for d in str(total))
    return total

if st.button("Analisa Karakter Saya Sekarang"):
    lp = hitung_life_path(tgl_lahir)
    
    # Database Narasi Deep NLP
    database = {
        1: {"inti": "🌟 Sang Inisiator Mandiri (The Pioneer)", "pola": "Pikiranmu beroperasi dengan 'Internal Frame of Reference' yang sangat kuat. Kamu adalah arsitek sekaligus pengemudi bagi hidupmu sendiri. Otakmu memproses informasi secara mandiri; jika sebuah arahan tidak masuk akal secara logis bagimu, kamu tidak akan tunduk begitu saja. Kamu melihat jalan saat orang lain melihat tembok.", "emosi": "Kamu memiliki daya dorong dan kompetisi yang tinggi. Namun, di balik ketangguhan itu, kamu sering merasa kesepian di puncak. Standar tinggimu membuatmu lelah karena merasa harus memikul dan menyelesaikan semuanya sendirian.", "saran": "Delegasi bukanlah bentuk kelemahan atau kehilangan kendali. Reframe (bingkai ulang) pikiranmu: mendelegasikan tugas adalah cara terbaik untuk meluaskan pengaruh dan menghemat energimu untuk hal yang jauh lebih besar."},
        2: {"inti": "🤝 Sang Penyelaras Harmoni (The Peacemaker)", "pola": "Kamu memiliki radar 'External Frame' yang sangat sensitif. Tanpa disadari, matamu mampu menangkap micro-expression (perubahan wajah kecil) dan nuansa emosi di suatu ruangan yang dilewatkan oleh 90% orang. Kamu adalah jembatan yang menghubungkan berbagai perbedaan karakter.", "emosi": "Empatimu adalah kekuatan sekaligus kelemahanmu. Kamu sering menyerap emosi orang lain bagai spons, membuatmu mudah lelah secara mental (burnout) saat berada di lingkungan yang toxic. Kedamaian adalah harga mati bagimu.", "saran": "Mulailah berlatih 'Ego State' proteksi diri. Berkata 'TIDAK' pada orang lain seringkali berarti berkata 'IYA' pada kewarasanmu sendiri. Menjaga batas diri (boundaries) adalah cara terbaik agar kamu bisa menolong orang lain dengan tulus."},
        3: {"inti": "🎨 Sang Komunikator Kreatif (The Catalyst)", "pola": "Dalam NLP, kamu adalah tipe 'Options'. Otakmu menolak kekakuan prosedur dan beroperasi bagai pabrik ide yang tidak pernah tidur. Kamu memproses dunia melalui ekspresi, suara, dan warna. Kamu melihat setiap masalah dari sudut pandang yang sama sekali out-of-the-box.", "emosi": "Kamu memiliki energi yang memancar dan mudah membuat orang lain nyaman. Namun, emosimu bisa naik-turun (rollercoaster) secara drastis jika ruang gerak dan ide-idemu dibungkam atau tidak mendapat apresiasi.", "saran": "Ide yang brilian tanpa eksekusi hanyalah hiasan pikiran. Buatlah 'Jangkar' (Anchor) kedisiplinan. Jangan melompat ke ide baru sebelum ide yang lama selesai kamu wujudkan menjadi karya nyata."},
        4: {"inti": "🏗️ Sang Arsitek Struktur (The Builder)", "pola": "Pikiranmu berakar kuat pada 'Procedures' dan 'Detail-Oriented'. Kamu merasa aman dan produktif ketika ada sistem, jadwal, dan kejelasan arah. Kamu mampu mengurai benang kusut menjadi langkah-langkah logis yang mudah diikuti oleh siapapun.", "emosi": "Kamu adalah sosok yang sangat setia, stabil, dan menjadi tempat bersandar banyak orang. Tantangan terbesarmu muncul saat menghadapi perubahan mendadak atau situasi yang serba abu-abu; hal itu bisa memicu kecemasan di dalam dirimu.", "saran": "Latihlah fleksibilitas pikiranmu. Ingatlah bahwa tidak semua hal di dunia ini bisa dikontrol. Berikan sedikit ruang kosong dalam rencanamu untuk menyambut kejutan dan keajaiban yang tidak terduga."},
        5: {"inti": "🦅 Sang Penjelajah Kebebasan (The Explorer)", "pola": "Oksigen bagi otakmu adalah 'Variasi'. Kamu memiliki Meta Program yang mencari perbedaan (Difference), sehingga kamu sangat cepat beradaptasi di lingkungan baru. Rutinitas yang berulang-ulang akan terasa seperti penjara bagi pikiranmu.", "emosi": "Antusiasmemu sangat magnetis. Kamu hidup untuk pengalaman, bukan sekadar kepemilikan. Namun, kebosanan adalah musuh terbesarmu, seringkali membuatmu meninggalkan proyek atau hubungan penting tepat sebelum membuahkan hasil.", "saran": "Pahami paradoks ini: 'Kebebasan sejati justru lahir dari kedisiplinan'. Jika kamu bisa bertahan sedikit lebih lama dan mengelola rasa bosanmu, petualanganmu akan menghasilkan mahakarya yang melegenda."},
        6: {"inti": "❤️ Sang Penjaga & Pengayom (The Nurturer)", "pola": "Filter utamamu adalah 'Others' (Fokus pada orang lain). Kamu memiliki insting alami untuk merawat, melindungi, dan memastikan harmoni di sekitarmu berjalan baik. Kamu membaca dunia melalui rasa tanggung jawab terhadap kelompok atau keluargamu.", "emosi": "Hatimu sangat luas dan penuh kasih. Sisi buta-nya (blind spot), kamu sering merasa bersalah jika mendahulukan diri sendiri. Terkadang kamu memendam kekecewaan mendalam ketika pengorbananmu dianggap angin lalu oleh orang lain.", "saran": "Hukum alam mengatakan: Kamu tidak bisa menuangkan air dari teko yang kosong. Merawat diri sendiri (self-love) bukanlah sebuah keegoisan, melainkan prasyarat agar kamu bisa terus menjadi pengayom yang tangguh."},
        7: {"inti": "🔍 Sang Pencari Kedalaman (The Analyst)", "pola": "Otakmu adalah mesin pemroses data yang sangat mendalam. Kamu tidak mudah menelan informasi dari permukaan. Pola pikirmu reflektif dan analitis; kamu selalu mencari 'Mengapa' di balik setiap kejadian. Kesendirian adalah caramu mengisi ulang baterai pikiran.", "emosi": "Kamu tampak tenang, misterius, dan rasional dari luar, namun memiliki lautan pemikiran yang bergemuruh di dalam. Kamu sangat berhati-hati dalam memberikan kepercayaan kepada orang baru.", "saran": "Awas jebakan 'Analysis Paralysis' (lumpuh karena terlalu banyak mikir). Terkadang, jawaban yang kamu cari dengan keras di dalam kepala, justru baru akan ditemukan ketika kamu mulai melangkah dan bertindak."},
        8: {"inti": "👑 Sang Pengelola Kekuatan (The Executive)", "pola": "Sistem berpikirmu adalah 'Result-Oriented' dengan kemampuan 'Global Chunking' (melihat gambaran besar). Kamu secara instingtif tahu cara mengorganisir sumber daya, waktu, dan orang lain untuk mencapai target yang rasanya mustahil bagi orang biasa.", "emosi": "Tangguh, berwibawa, dan dominan. Namun, ambisimu yang menyala-nyala sering membuatmu lupa untuk berhenti sejenak, bernapas, dan merayakan kemenangan-kemenangan kecil dalam hidup.", "saran": "Kekuasaan yang besar menuntut kerendahan hati yang jauh lebih besar. Seimbangkan orientasi hasilmu dengan sentuhan humanis. Nikmati prosesnya, karena puncak gunung hanyalah tempat singgah, bukan tempat menetap."},
        9: {"inti": "🌍 Sang Humanis Global (The Philanthropist)", "pola": "Pikiranmu beroperasi di level idealisme tinggi. Kamu tidak memikirkan keuntungan ego sektoral, melainkan dampak universal. Kamu digerakkan oleh nilai-nilai kemanusiaan, keadilan, dan keinginan kuat untuk meninggalkan warisan (legacy) yang baik di dunia.", "emosi": "Kapasitas memaafkanmu sangat luar biasa. Namun, karena kamu melihat dunia melalui kacamata idealisme, kamu sangat rentan mengalami patah hati atau sinis ketika melihat realita dunia yang kejam dan tidak adil.", "saran": "Jangan biarkan visi besarmu membuatmu mengabaikan sekitarmu. Perubahan dunia yang masif tidak dimulai dari panggung besar, melainkan dari senyuman dan bantuan kecil yang kamu berikan pada orang di sebelahmu hari ini."},
        11: {"inti": "⚡ Sang Visioner Intuitif (The Illuminator)", "pola": "Kamu dikaruniai 'High Sensory Acuity' yang di atas rata-rata. Kamu memproses informasi bukan sekadar lewat logika (conscious mind), tapi lewat sinyal intuitif dan vibrasi (subconscious). Kamu sering 'tahu' akan suatu hal tanpa bisa menjelaskan logikanya.", "emosi": "Energi mentalmu sangat intens dan inspiratif. Seringkali kamu merasa 'berbeda', terasing, atau seperti alien yang sedang mengobservasi manusia lain. Lingkungan yang negatif bisa menguras energimu dengan sangat cepat.", "saran": "Intuisimu adalah anugerah, gunakan untuk membimbing, bukan menghakimi. Temukan 'Jangkar' (grounding) di dunia nyata—seperti olahraga atau rutinitas harian—agar pikiranmu tidak melayang terlalu jauh tanpa pijakan."},
        22: {"inti": "🏛️ Sang Pembangun Utama (The Master Builder)", "pola": "Ini adalah kombinasi langka: Kamu memiliki visi setinggi langit (seperti angka 11) namun dikawinkan dengan kemampuan eksekusi yang sangat membumi dan terstruktur (seperti angka 4). Otakmu merancang blueprint masa depan secara detail.", "emosi": "Kamu terlihat sangat solid dan tak tergoyahkan. Namun, di dalam, kamu menanggung beban tekanan yang luar biasa berat karena merasa bertanggung jawab untuk mewujudkan hal-hal raksasa dalam hidupmu dan hidup orang lain.", "saran": "Kendalikan ekspektasimu. Ingatlah bahwa membangun gedung pencakar langit membutuhkan fondasi waktu yang lama. Istirahatlah. Kesehatan fisik dan mentalmu adalah aset paling berharga dari semua proyek besarmu."}
    }
    
    res = database.get(lp, {
        "inti": "✨ Karakter Dinamis",
        "pola": "Memiliki kombinasi energi yang unik dan dinamis.",
        "emosi": "Adaptif terhadap lingkungan.",
        "saran": "Teruslah bereksplorasi dengan potensi dirimu."
    })

    if not nama:
        nama = "Kawan"

    # Output Display
    st.success(f"Halo **{nama}**, hasil pemetaan pikiranmu adalah:")
    st.markdown(f"### **1. Inti Karakter: {res['inti']}**")
    st.write(f"**2. Pola Pikiran:** {res['pola']}")
    st.write(f"**3. Dinamika Emosi:** {res['emosi']}")
    st.info(f"💡 **Saran Pengembangan:** {res['saran']}")
    
    st.write("---")
    
    # Bagian Tombol WhatsApp (LEAD MAGNET)
    st.subheader("Bongkar Potensi Aslimu Lebih Dalam 🚀")
    st.write(f"Hasil di atas baru menyentuh 10% dari program pikiran bawah sadarmu. Ingin melepaskan *mental block* atau memaksimalkan kekuatan **{res['inti']}** secara privat?")
    
    # JANGAN LUPA GANTI NOMOR DI BAWAH INI BRO
    nomor_wa = "6281234567890" 
    
    pesan_wa = f"Halo Coach Ahmad, saya {nama}. Saya baru saja mencoba Persona-NLP Analis dan hasilnya adalah {res['inti']}. Saya ingin konsultasi lebih lanjut tentang sesi coaching/hipnoterapi."
    pesan_encoded = urllib.parse.quote(pesan_wa)
    link_wa = f"https://wa.me/{nomor_wa}?text={pesan_encoded}"

    st.markdown(f'<a href="{link_wa}" target="_blank" style="background-color:#25D366;color:white;padding:12px 20px;border-radius:10px;text-decoration:none;font-weight:bold;display:block;text-align:center;font-size:16px;">💬 KLIK UNTUK KONSULTASI VIA WHATSAPP</a>', unsafe_allow_html=True)

    st.write("")
    st.caption("Analisis ini bersifat reflektif berdasarkan pendekatan Neuro-Linguistic Programming & Numerologi Dasar.")
