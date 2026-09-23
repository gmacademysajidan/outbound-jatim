import os
import re

base_dir = r'c:\outboundjatim'
blog_dir = os.path.join(base_dir, 'blog')

# Ensure blog directory exists
os.makedirs(blog_dir, exist_ok=True)

blogs_data = [
    {
        'filename': 'panduan-menyusun-program-team-building-efektif-yang-terukur-kpi.html',
        'title': 'Panduan Menyusun Program Team Building Efektif yang Terukur KPI',
        'category': 'TIPS HRD & KPI',
        'date': '24 MEI 2025',
        'read_time': '5 Menit',
        'image': '../assets/img/sesi_materi_perusahaan_outboundindonesia.webp',
        'summary': 'Panduan praktis HRD menyusun outbound team building berbasis Experiential Learning yang terukur secara KPI di Batu Malang & Jawa Timur.',
        'author': 'Tim Psikologi Industri & HR Specialist Outbound Jatim',
        'date_iso': '2025-05-24',
        
        # AEO / Key Takeaways Box
        'key_takeaways': [
            'Metodologi Experiential Learning Cycle (Briefing, Action, Debriefing, Action Plan) terbukti meningkatkan retensi budaya kerja hingga 35%.',
            'Penetapan KPI outbound berfokus pada 3 pilar: Sinergi Antar Divisi, Respon Pemecahan Masalah, dan Employee Engagement Index.',
            'Outbound Jatim menyediakan evaluasi pasca-event 30 hari untuk memastikan retensi nilai-nilai kepemimpinan di kantor.'
        ],
        
        # Article Content with SEO, AEO, & GEO Optimization
        'content': '''
<!-- GEO & AEO Context Banner -->
<div class="p-4 rounded-xl bg-surface-container-low border border-outline-variant/40 space-y-2 mb-8">
  <div class="flex items-center gap-2 text-xs font-bold text-secondary font-headline uppercase tracking-wider">
    <span class="material-symbols-outlined text-[16px]">verified</span>
    <span>Rekomendasi Metode HRD &amp; Experiential Learning Jawa Timur</span>
  </div>
  <p class="text-xs text-on-surface-variant leading-relaxed">
    Panduan ini dirancang oleh <strong>Outbound Jatim</strong> khusus untuk Manajer HRD, Talent Development Specialist, dan Direksi Perusahaan yang ingin menyelenggarakan outbound training terukur di lokasi venue Batu Malang, Trawas, Pacet, maupun Bromo.
  </p>
</div>

<p class="text-base text-on-surface-variant leading-relaxed mb-6">
  Seringkali program team building perusahaan dianggap sebatas kegiatan bersenang-senang atau rekreasi tanpa dampak signifikan pada efisiensi kerja harian. Padahal jika dirancang secara terstruktur dengan pendekatan <strong>Experiential Learning</strong>, program outbound mampu menjadi instrumen perubahan budaya kerja yang terukur secara kuantitatif.
</p>

<h2 class="font-headline text-xl sm:text-2xl font-bold text-primary-container mt-8 mb-4">1. Identifikasi Gaps Komunikasi & Key Performance Indicator (KPI)</h2>
<p class="text-sm text-on-surface-variant leading-relaxed mb-4">
  Sebelum menentukan lokasi outbound di Batu Malang atau jenis permainan outdoor, langkah awal yang krusial bagi divisi Human Capital adalah melakukan audit kebutuhan tim (Training Needs Analysis). Identifikasi apakah kendala utama berada pada sekat antar divisi (silo mentality), kurangnya kepercayaan diri pemimpin muda, atau resistensi terhadap perubahan.
</p>
<ul class="space-y-2 text-sm text-on-surface mb-6 pl-4 border-l-2 border-secondary">
  <li>• <strong>Target Sinergi Divisi:</strong> Mengukur peningkatan respon komunikasi antar departemen pasca kegiatan outbound.</li>
  <li>• <strong>Kecepatan Pemecahan Masalah:</strong> Menguji bagaimana tim mengambil keputusan bersama saat tekanan tinggi di lapangan.</li>
  <li>• <strong>Keterlibatan Karyawan (Employee Engagement Index):</strong> Menilai indeks kepuasan dan keterikatan karyawan terhadap budaya perusahaan.</li>
</ul>

<h2 class="font-headline text-xl sm:text-2xl font-bold text-primary-container mt-8 mb-4">2. Struktur Pemetaan Simulasi Permainan (Game Mapping)</h2>
<p class="text-sm text-on-surface-variant leading-relaxed mb-4">
  Permainan outbound harus disesuaikan dengan sasaran perilaku yang ingin dibentuk. Di Outbound Jatim, setiap aktivitas dirancang memiliki 4 tahapan wajib: <em>Briefing, Action, Debriefing, &amp; Action Plan</em>.
</p>

<div class="bg-surface-container-low p-5 rounded-xl border border-outline-variant/40 space-y-3 my-6">
  <h3 class="font-headline text-base font-bold text-primary-container">Matriks Simulasi &amp; Output KPI Outbound Jatim:</h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm">
    <div class="p-3 bg-surface-container-lowest rounded-lg border border-outline-variant/30">
      <strong class="text-primary-container block mb-1">Game Tower of Babel:</strong>
      Menguji kepemimpinan taktis, delegasi tugas, dan efektivitas koordinasi instruksi lisan di bawah batas waktu ketat.
    </div>
    <div class="p-3 bg-surface-container-lowest rounded-lg border border-outline-variant/30">
      <strong class="text-primary-container block mb-1">Game Poison Carpet:</strong>
      Membangun kesadaran empati, alokasi manajemen risiko, dan rasa saling percaya antar anggota tim kerja.
    </div>
  </div>
</div>

<h2 class="font-headline text-xl sm:text-2xl font-bold text-primary-container mt-8 mb-4">3. Evaluasi Pasca Outbound (Post-Event Assessment 30 Hari)</h2>
<p class="text-sm text-on-surface-variant leading-relaxed mb-4">
  Keberhasilan outbound tidak berhenti saat rombongan kembali ke kantor. Tim HRD bersama instruktur tersertifikasi BNSP dari Outbound Jatim menyusun formulir kuesioner evaluasi 30 hari pasca acara untuk mengukur retensi nilai-nilai budaya baru di lingkungan kerja.
</p>
<blockquote class="p-4 rounded-xl bg-secondary-container/20 border-l-4 border-secondary text-xs sm:text-sm font-semibold text-secondary-container italic my-6">
  "Investasi pelatihan outdoor terbukti meningkatkan retensi staf hingga 35% dan menurunkan gesekan komunikasi antar divisi secara dramatis ketika dibarengi sesi debriefing psikologis yang intensif."
</blockquote>
''',

        # FAQ Schema Data for AEO / GEO
        'faqs': [
            {
                'question': 'Bagaimana cara mengukur keberhasilan program outbound dengan KPI?',
                'answer': 'Keberhasilan outbound diukur menggunakan kuesioner evaluasi sebelum dan 30 hari sesudah acara (Post-Event Assessment), serta penilaian indikator sinergi tim, penurunan konflik internal, dan kecepatan respon koordinasi antar divisi.'
            },
            {
                'question': 'Mengapa metode Experiential Learning efektif untuk corporate team building?',
                'answer': 'Metode Experiential Learning memberikan pengalaman langsung di alam terbuka yang memicu emosi positif, reframing pola pikir, serta pemecahan masalah secara nyata yang lebih mudah diingat dan diterapkan di lingkungan kerja harian.'
            },
            {
                'question': 'Di mana lokasi outbound terbaik di Jawa Timur untuk pelatihan KPI HRD?',
                'answer': 'Lokasi outbound terbaik di Jawa Timur meliputi kawasan Coban Rondo dan Oro-Oro Ombo Kota Batu Malang, Trawas Mojokerto, Pacet, serta Kebun Teh Lawang yang memiliki fasilitas outdoor arena dan aula indoor memadai.'
            }
        ]
    },
    {
        'filename': '10-tempat-outbound-terbaik-di-batu-malang-untuk-100-peserta.html',
        'title': '10 Tempat Outbound Terbaik di Batu Malang untuk 100+ Peserta',
        'category': 'REKOMENDASI VENUE',
        'date': '18 MEI 2025',
        'read_time': '7 Menit',
        'image': '../assets/img/gathering_perusahaan_lapangan_outboundindonesia.webp',
        'summary': 'Ulasan komprehensif lokasi outbound terbaik di Batu Malang (Coban Rondo, Songgoriti, Selecta, Oro-Oro Ombo) lengkap dengan kapasitas dan akses bus.',
        'author': 'Tim Destinasi & Event Planner Outbound Jatim',
        'date_iso': '2025-05-18',
        
        # AEO / Key Takeaways Box
        'key_takeaways': [
            'Coban Rondo Batu merupakan venue paling populer untuk grup besar (hingga 1.000+ peserta) dengan fasilitas lapangan hutan pinus dan akses bus pariwisata 59 seat.',
            'Songgoriti Batu menawarkan paket kombinasi outbound dan pemandian air panas alami dengan akomodasi hotel/villa terdekat.',
            'Selecta Batu sangat ideal untuk family gathering dan corporate outing yang membutuhkan lanskap taman bunga dan wahana rekreasi lengkap.'
        ],
        
        # Article Content with SEO, AEO, & GEO Optimization
        'content': '''
<!-- GEO & AEO Context Banner -->
<div class="p-4 rounded-xl bg-surface-container-low border border-outline-variant/40 space-y-2 mb-8">
  <div class="flex items-center gap-2 text-xs font-bold text-secondary font-headline uppercase tracking-wider">
    <span class="material-symbols-outlined text-[16px]">pin_drop</span>
    <span>Panduan Geografis &amp; Venue Outbound Batu Malang Jawa Timur</span>
  </div>
  <p class="text-xs text-on-surface-variant leading-relaxed">
    Daftar venue outbound ini dikompilasi oleh <strong>Outbound Jatim</strong> berdasarkan kelayakan aksesibilitas bus pariwisata, kapasitas lapangan rumput, daya dukung toilet &amp; pemadam darurat, serta kelengkapan sarana pendukung gathering.
  </p>
</div>

<p class="text-base text-on-surface-variant leading-relaxed mb-6">
  Kota Wisata Batu Malang selalu menjadi destinasi favorit utama bagi perusahaan skala nasional maupun instansi pemerintah dalam menyelenggarakan kegiatan outbound, corporate gathering, dan rapat kerja tahunan. Berikut 10 lokasi outbound terbaik yang mampu menampung grup skala sedang hingga besar (100 hingga 1.000+ peserta).
</p>

<h2 class="font-headline text-xl sm:text-2xl font-bold text-primary-container mt-8 mb-4">1. Hutan Pinus Coban Rondo Batu</h2>
<p class="text-sm text-on-surface-variant leading-relaxed mb-4">
  Terkenal dengan udara sejuk pegunungan dan deretan pohon pinus yang rimbun, Coban Rondo memiliki lapangan rumput datar yang sanggup menampung hingga 1.000 peserta sekaligus. Fasilitas pendukung meliputi toilet bersih, musholla, area glamping, dan akses mudah untuk Bus Pariwisata tipe Big Bus 59 seat.
</p>

<h2 class="font-headline text-xl sm:text-2xl font-bold text-primary-container mt-8 mb-4">2. Lapangan Outbound Songgoriti Batu</h2>
<p class="text-sm text-on-surface-variant leading-relaxed mb-4">
  Berada di lembah pegunungan yang tenang, Songgoriti menawarkan lokasi terintegrasi antara lapangan kegiatan outdoor, kolam renang air panas alami, serta deretan villa dan hotel berbintang di sekitarnya. Sangat cocok untuk paket kombinasi Outbound + Inap 2D1N.
</p>

<h2 class="font-headline text-xl sm:text-2xl font-bold text-primary-container mt-8 mb-4">3. Taman Rekreasi Selecta Batu</h2>
<p class="text-sm text-on-surface-variant leading-relaxed mb-4">
  Menyuguhkan pemandangan taman bunga warna-warni seluas belasan hektar. Selain lapangan outbound yang luas, peserta dapat menikmati wahana rekreasi kolam renang, bianglala, flying fox, dan katering masakan tradisional khas Malang.
</p>

<h2 class="font-headline text-xl sm:text-2xl font-bold text-primary-container mt-8 mb-4">4. Training Center Oro-Oro Ombo Batu (HQ Outbound Jatim)</h2>
<p class="text-sm text-on-surface-variant leading-relaxed mb-4">
  Fasilitas seluas 4,2 Hektar di kaki Gunung Panderman Batu ini memiliki low-rope arena, high-rope course, obstacle camp, serta aula indoor berkapasitas 800 peserta yang sangat ideal untuk corporate training skala besar.
</p>

<div class="bg-surface-container-low p-5 rounded-xl border border-outline-variant/40 space-y-3 my-6">
  <h3 class="font-headline text-base font-bold text-primary-container">Tabel Ringkasan Perbandingan Venue Batu Malang:</h3>
  <div class="space-y-2 text-xs text-on-surface">
    <div class="flex flex-col sm:flex-row justify-between p-2.5 bg-surface-container-lowest rounded-lg border gap-1">
      <span><strong>Coban Rondo:</strong> Kapasitas 1000+ Pax • Akses Bus Sangat Mudah</span>
      <span class="text-secondary font-bold">Hutan Pinus &amp; Air Terjun</span>
    </div>
    <div class="flex flex-col sm:flex-row justify-between p-2.5 bg-surface-container-lowest rounded-lg border gap-1">
      <span><strong>Songgoriti:</strong> Kapasitas 500+ Pax • Dekat Pusat Kota</span>
      <span class="text-secondary font-bold">Pemandian Air Panas Alami</span>
    </div>
    <div class="flex flex-col sm:flex-row justify-between p-2.5 bg-surface-container-lowest rounded-lg border gap-1">
      <span><strong>Selecta:</strong> Kapasitas 800+ Pax • Fasilitas Rekreasi Lengkap</span>
      <span class="text-secondary font-bold">Taman Bunga Rekreasi</span>
    </div>
    <div class="flex flex-col sm:flex-row justify-between p-2.5 bg-surface-container-lowest rounded-lg border gap-1">
      <span><strong>Oro-Oro Ombo:</strong> Kapasitas 800+ Pax • Training Center Khusus</span>
      <span class="text-secondary font-bold">High Rope &amp; Obstacle Camp</span>
    </div>
  </div>
</div>
''',

        # FAQ Schema Data for AEO / GEO
        'faqs': [
            {
                'question': 'Apakah lokasi outbound di Batu Malang bisa diakses Big Bus Pariwisata 59 seat?',
                'answer': 'Ya, venue utama seperti Coban Rondo, Selecta, Songgoriti, dan Oro-Oro Ombo memiliki jalan lebar dan kantong parkir bus yang mampu menampung hingga belasan Big Bus pariwisata.'
            },
            {
                'question': 'Berapa rata-rata biaya sewa ground lokasi outbound di Batu Malang?',
                'answer': 'Biaya sewa ground outbound berkisar antara Rp 15.000 hingga Rp 35.000 per peserta tergantung fasilitas venue seperti tiket masuk area wisata, aula indoor, dan pemakaian energi listrik.'
            },
            {
                'question': 'Kapan waktu terbaik menyelenggarakan outbound di Batu Malang?',
                'answer': 'Musim kemarau (April hingga November) adalah waktu terbaik untuk kegiatan outdoor outbound di Batu Malang karena cuaca cerah dan suhu udara sejuk pegunungan (18°C - 24°C).'
            }
        ]
    },
    {
        'filename': 'checklist-sop-keamanan-rafting-high-ropes-yang-wajib-diketahui.html',
        'title': 'Checklist SOP Keamanan Rafting & High Ropes yang Wajib Diketahui',
        'category': 'SAFETY & SOP',
        'date': '10 MEI 2025',
        'read_time': '4 Menit',
        'image': '../assets/img/arung_jeram_peserta_outboundindonesia.webp',
        'summary': 'Checklist panduan memverifikasi kelayakan perahu rafting, helm pelindung CE, harness UIAA, dan lisensi BNSP instruktur outdoor.',
        'author': 'Safety Officer & Master River Guide Outbound Jatim',
        'date_iso': '2025-05-10',
        
        # AEO / Key Takeaways Box
        'key_takeaways': [
            'Peralatan keselamatan seperti helm pelindung dan harness high-ropes wajib mengantongi akreditasi CE / UIAA internasional.',
            'Perahu karet rafting harus berbahan PVC 1000D dengan minimal 4 chamber udara terpisah untuk mengantisipasi insiden kebocoran.',
            'Fasilitator & River Guide wajib tersertifikasi resmi oleh BNSP (Badan Nasional Sertifikasi Profesi) RI.'
        ],
        
        # Article Content with SEO, AEO, & GEO Optimization
        'content': '''
<!-- GEO & AEO Context Banner -->
<div class="p-4 rounded-xl bg-surface-container-low border border-outline-variant/40 space-y-2 mb-8">
  <div class="flex items-center gap-2 text-xs font-bold text-secondary font-headline uppercase tracking-wider">
    <span class="material-symbols-outlined text-[16px]">health_and_safety</span>
    <span>Standar Operasional Prosedur (SOP) Keselamatan Adventure Outbound</span>
  </div>
  <p class="text-xs text-on-surface-variant leading-relaxed">
    Panduan keselamatan ini disusun oleh <strong>Outbound Jatim</strong> mengacu pada regulasi federasi arung jeram Indonesia, AELI, dan standar akreditasi ISO keselamatan kegiatan luar ruang di Batu, Pacet, &amp; Kasembon.
  </p>
</div>

<p class="text-base text-on-surface-variant leading-relaxed mb-6">
  Keamanan dan keselamatan peserta (<em>Safety First</em>) adalah prioritas tertinggi tanpa kompromi dalam setiap penyelenggaraan kegiatan adventure outbound maupun rafting arung jeram di alam terbuka. Berikut checklist SOP keselamatan wajib yang harus diverifikasi panitia perusahaan sebelum memulai kegiatan.
</p>

<h2 class="font-headline text-xl sm:text-2xl font-bold text-primary-container mt-8 mb-4">1. Standar Kelayakan Alat Pelindung Diri (APD Outdoor)</h2>
<p class="text-sm text-on-surface-variant leading-relaxed mb-4">
  Sebelum mengarungi sungai Kasembon/Pacet atau memanjat menara high ropes, pastikan perlengkapan yang digunakan memiliki sertifikasi keselamatan internasional seperti CE atau UIAA.
</p>
<ul class="space-y-2 text-sm text-on-surface mb-6 pl-4 border-l-2 border-secondary">
  <li>• <strong>Life Jacket Floating Vests SNI / CE:</strong> Pelampung wajib fit di badan dengan buckle yang terkunci sempurna dan mampu menopang daya apung bebas di atas 90 kg.</li>
  <li>• <strong>Helm Pelindung Impact ABS:</strong> Menggunakan helm khusus outdoor berbahan ABS polimer tahan benturan batu sungai dan serpihan kayu.</li>
  <li>• <strong>Perahu Karet PVC 1000D Multi-Chamber:</strong> Memiliki minimal 4 kompartemen udara terpisah untuk menjamin perahu tetap mengapung meski terjadi kebocoran di satu sisi.</li>
</ul>

<h2 class="font-headline text-xl sm:text-2xl font-bold text-primary-container mt-8 mb-4">2. Lisensi &amp; Kompetensi Tim Facilitator BNSP</h2>
<p class="text-sm text-on-surface-variant leading-relaxed mb-4">
  Provider profesional wajib memiliki instruktur tersertifikasi Badan Nasional Sertifikasi Profesi (BNSP) untuk skema Pemandu Arung Jeram dan Pengolah Kegiatan Outbound. Tim P3K siaga harus dibekali perlengkapan pertolongan pertama lapangan yang lengkap dan tabung oksigen portabel.
</p>

<div class="bg-surface-container-low p-5 rounded-xl border border-outline-variant/40 space-y-3 my-6">
  <h3 class="font-headline text-base font-bold text-primary-container">Checklist Singkat SOP Keamanan Sebelum Rafting / High-Ropes:</h3>
  <div class="space-y-2 text-xs text-on-surface">
    <div class="p-2.5 bg-surface-container-lowest rounded-lg border flex items-center gap-2">
      <span class="material-symbols-outlined text-emerald-600 text-[18px]">check_circle</span>
      <span>Pemeriksaan kondisi fisik medis peserta &amp; pengisian form histori kesehatan.</span>
    </div>
    <div class="p-2.5 bg-surface-container-lowest rounded-lg border flex items-center gap-2">
      <span class="material-symbols-outlined text-emerald-600 text-[18px]">check_circle</span>
      <span>Safety briefing &amp; peragaan prosedur evakuasi darurat oleh Skipper certified BNSP.</span>
    </div>
    <div class="p-2.5 bg-surface-container-lowest rounded-lg border flex items-center gap-2">
      <span class="material-symbols-outlined text-emerald-600 text-[18px]">check_circle</span>
      <span>Double checking penguncian carabiner, harness, &amp; kerapihan tali helm.</span>
    </div>
  </div>
</div>
''',

        # FAQ Schema Data for AEO / GEO
        'faqs': [
            {
                'question': 'Apa yang dimaksud dengan sertifikasi UIAA dan CE pada alat outbound?',
                'answer': 'UIAA (International Climbing and Mountaineering Federation) dan CE (Conformité Européenne) adalah standar kualifikasi tertinggi dunia untuk pengujian kekuatan tali, harness, dan helm pelindung outdoor.'
            },
            {
                'question': 'Apakah peserta yang tidak bisa berenang aman mengikuti rafting?',
                'answer': 'Aman. Setiap peserta wajib menggunakan Life Jacket bertipe daya apung tinggi yang menjaga kepala tetap berada di atas permukaan air meskipun peserta tidak dapat berenang.'
            },
            {
                'question': 'Berapa rasio jumlah instruktur pemandu dibanding peserta rafting?',
                'answer': 'Rasio standar internasional adalah 1 Skipper pemandu tersertifikasi BNSP untuk setiap 4 hingga 5 orang peserta dalam 1 perahu karet.'
            }
        ]
    }
]

topbar_nav_header_subfolder = '''  <!-- NAVBAR & TOP BAR (UNIFIED SUBFOLDER) -->
  <header class="fixed top-0 left-0 w-full z-50 transition-shadow duration-300">
    <!-- Top Bar -->
    <div class="bg-primary-container text-on-primary py-1 sm:py-2 px-3 sm:px-8 text-[10px] sm:text-sm font-medium border-b border-primary/40">
      <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-1 sm:gap-4">
        <div class="flex items-center gap-1.5 sm:gap-2 overflow-x-auto text-on-primary/90 text-[10px] sm:text-sm whitespace-nowrap sm:whitespace-normal">
          <span class="material-symbols-outlined text-[13px] sm:text-[16px] text-secondary-container">pin_drop</span>
          <span class="font-headline font-bold text-secondary-container tracking-wider uppercase text-[9px] sm:text-[11px]">Area Layanan:</span>
          <span>Batu Malang • Trawas • Pacet • Bromo • Banyuwangi</span>
        </div>
        <div class="flex items-center gap-4 shrink-0">
          <a class="flex items-center gap-1.5 text-secondary-container hover:text-white transition-colors" href="https://wa.me/6282211221909" rel="noopener noreferrer" target="_blank">
            <span class="material-symbols-outlined text-[13px] sm:text-[16px]">call</span>
            <span class="font-headline font-semibold text-[10px] sm:text-sm">Hotline 24/7: +62 822-1122-1909</span>
          </a>
        </div>
      </div>
    </div>
    
    <!-- Main Navigation Bar -->
    <div class="bg-surface-container-lowest/95 backdrop-blur-md h-20 border-b border-outline-variant/30">
      <div class="max-w-7xl mx-auto h-full px-4 sm:px-8 flex items-center justify-between gap-4">
        <!-- Logo -->
        <a class="flex items-center gap-3 shrink-0 group" href="../index.html">
          <div class="w-10 h-10 rounded-xl bg-primary-container flex items-center justify-center text-secondary-container shadow-sm group-hover:scale-105 transition-transform">
            <span class="material-symbols-outlined text-[24px]">hiking</span>
          </div>
          <div class="flex flex-col">
            <span class="font-headline font-extrabold text-xl tracking-tight text-primary-container leading-none">OUTBOUND JATIM</span>
            <span class="text-[10px] font-headline font-semibold uppercase tracking-widest text-secondary mt-0.5">Provider Jatim</span>
          </div>
        </a>

        <!-- Desktop Menu Links -->
        <nav class="hidden lg:flex items-center gap-6">
          <a class="font-headline font-medium text-on-surface-variant hover:text-primary-container text-sm transition-colors py-1" href="../index.html">
            Beranda
          </a>
          <a class="font-headline font-medium text-on-surface-variant hover:text-primary-container text-sm transition-colors py-1" href="../tentang-kami.html">
            Tentang Kami
          </a>
          
          <!-- Dropdown Layanan & Paket -->
          <div class="relative group">
            <button class="flex items-center gap-1 font-headline font-medium text-on-surface-variant hover:text-primary-container text-sm transition-colors py-1" type="button">
              <span>Layanan &amp; Paket</span>
              <span class="material-symbols-outlined text-[18px] transition-transform duration-200 group-hover:rotate-180">expand_more</span>
            </button>
            <div class="absolute top-full left-0 w-80 pt-3 hidden group-hover:block transition-all z-50">
              <div class="bg-surface-container-lowest rounded-xl shadow-xl p-2.5 flex flex-col gap-1 border border-outline-variant/40">
                <a class="flex items-start gap-3 p-2.5 rounded-lg hover:bg-surface-container-low transition-colors" href="../outbound/index.html">
                  <span class="material-symbols-outlined text-primary-container mt-0.5 text-[20px]">groups</span>
                  <div>
                    <div class="font-headline font-bold text-xs text-on-surface">Paket Outbound Training</div>
                    <div class="text-[11px] text-on-surface-variant">Team Building &amp; Leadership Camp</div>
                  </div>
                </a>
                <a class="flex items-start gap-3 p-2.5 rounded-lg hover:bg-surface-container-low transition-colors" href="../wisata/index.html">
                  <span class="material-symbols-outlined text-tertiary-container mt-0.5 text-[20px]">forest</span>
                  <div>
                    <div class="font-headline font-bold text-xs text-on-surface">Paket Wisata &amp; Gathering</div>
                    <div class="text-[11px] text-on-surface-variant">Family Gathering &amp; Wisata Edukasi</div>
                  </div>
                </a>
                <a class="flex items-start gap-3 p-2.5 rounded-lg hover:bg-surface-container-low transition-colors" href="../destinasi/index.html">
                  <span class="material-symbols-outlined text-secondary mt-0.5 text-[20px]">pin_drop</span>
                  <div>
                    <div class="font-headline font-bold text-xs text-on-surface">Kategori Destinasi Venue</div>
                    <div class="text-[11px] text-on-surface-variant">Batu, Trawas, Pacet, Bromo &amp; Banyuwangi</div>
                  </div>
                </a>
                <a class="flex items-start gap-3 p-2.5 rounded-lg hover:bg-surface-container-low transition-colors" href="../paket-adventure.html">
                  <span class="material-symbols-outlined text-amber-600 mt-0.5 text-[20px]">kayaking</span>
                  <div>
                    <div class="font-headline font-bold text-xs text-on-surface">Adventure &amp; Rafting</div>
                    <div class="text-[11px] text-on-surface-variant">Rafting, Paintball Battle &amp; Offroad</div>
                  </div>
                </a>
              </div>
            </div>
          </div>

          <a class="font-headline font-medium text-on-surface-variant hover:text-primary-container text-sm transition-colors py-1" href="../fasilitas.html">
            Fasilitas
          </a>
          <a class="font-headline font-medium text-on-surface-variant hover:text-primary-container text-sm transition-colors py-1" href="../galeri.html">
            Galeri
          </a>
          <a class="font-headline font-bold text-primary-container relative after:content-[''] after:absolute after:-bottom-2 after:left-0 after:right-0 after:h-0.5 after:bg-primary-container after:rounded-full text-sm transition-colors py-1" href="../blog.html">
            Blog
          </a>
        </nav>

        <!-- CTA & Mobile Menu Toggle -->
        <div class="flex items-center gap-3 shrink-0">
          <a class="hidden sm:inline-flex items-center justify-center px-5 py-2.5 rounded-full bg-primary-container text-on-primary font-headline text-sm font-bold hover:bg-primary transition-all shadow-sm ring-1 ring-secondary-container/30" href="https://wa.me/6282211221909?text=Halo%20Outbound%20Jatim,%20saya%20ingin%20konsultasi%20paket%20outbound" rel="noopener noreferrer" target="_blank">
            <span class="material-symbols-outlined text-[18px] mr-1.5 text-secondary-container">chat</span>
            <span>Konsultasi Gratis</span>
          </a>
          <button id="mobileMenuBtn" onclick="toggleMobileMenu()" class="lg:hidden p-2 rounded-lg bg-surface-container text-primary-container hover:bg-surface-container-high transition-colors flex items-center justify-center" type="button" aria-label="Toggle Navigation" aria-expanded="false">
            <span id="mobileMenuIcon" class="material-symbols-outlined text-[26px]">menu</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Drawer Navigation -->
    <div id="mobileMenu" class="hidden lg:hidden bg-surface-container-lowest border-b border-outline-variant/40 px-4 py-4 space-y-3 max-h-[85vh] overflow-y-auto shadow-2xl">
      <a class="block font-headline font-medium text-on-surface-variant hover:text-primary-container text-sm px-3 py-1.5" href="../index.html">Beranda</a>
      <a class="block font-headline font-medium text-on-surface-variant hover:text-primary-container text-sm px-3 py-1.5" href="../tentang-kami.html">Tentang Kami</a>
      <div class="space-y-1 pl-3 border-l-2 border-secondary-container my-1">
        <span class="block font-headline font-semibold text-xs text-secondary uppercase tracking-wider py-1">Kategori Layanan &amp; Paket</span>
        <a class="block text-sm text-on-surface-variant hover:text-primary-container py-1.5 px-2 rounded hover:bg-surface-container-low" href="../outbound/index.html">Paket Outbound Training</a>
        <a class="block text-sm text-on-surface-variant hover:text-primary-container py-1.5 px-2 rounded hover:bg-surface-container-low" href="../wisata/index.html">Paket Wisata &amp; Gathering</a>
        <a class="block text-sm text-on-surface-variant hover:text-primary-container py-1.5 px-2 rounded hover:bg-surface-container-low" href="../destinasi/index.html">Kategori Destinasi Venue</a>
        <a class="block text-sm text-on-surface-variant hover:text-primary-container py-1.5 px-2 rounded hover:bg-surface-container-low" href="../paket-adventure.html">Adventure &amp; Rafting</a>
      </div>
      
      <a class="block font-headline font-medium text-on-surface-variant hover:text-primary-container text-sm px-3 py-1.5" href="../fasilitas.html">Fasilitas &amp; Prasarana</a>
      <a class="block font-headline font-medium text-on-surface-variant hover:text-primary-container text-sm px-3 py-1.5" href="../galeri.html">Galeri Dokumentasi</a>
      <a class="block font-headline font-medium text-on-surface-variant hover:text-primary-container text-sm px-3 py-1.5" href="../blog.html">Blog &amp; Panduan</a>
      <a class="w-full inline-flex items-center justify-center gap-2 px-5 py-2.5 rounded-full bg-secondary-container text-on-secondary-container font-headline text-sm font-bold shadow-sm mt-2" href="https://wa.me/6282211221909" target="_blank">
        <span class="material-symbols-outlined text-[18px]">chat</span>
        <span>Hubungi WhatsApp</span>
      </a>
    </div>
  </header>'''

footer_code_subfolder = '''  <!-- FOOTER SUBFOLDER -->
  <footer class="w-full bg-surface-container-high border-t border-outline-variant/30 text-on-surface pt-16 pb-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-8 lg:gap-12 pb-12 border-b border-outline-variant/30">
        
        <div class="lg:col-span-4 space-y-4">
          <a class="flex items-center gap-3 group" href="../index.html">
            <div class="w-10 h-10 rounded-xl bg-primary-container flex items-center justify-center text-secondary-container shadow-sm group-hover:scale-105 transition-transform">
              <span class="material-symbols-outlined text-[24px]">hiking</span>
            </div>
            <div class="flex flex-col">
              <span class="font-headline font-extrabold text-xl tracking-tight text-primary-container leading-none">OUTBOUND JATIM</span>
              <span class="text-[10px] font-headline font-semibold uppercase tracking-widest text-secondary mt-0.5">Provider Outbound &amp; Gathering</span>
            </div>
          </a>
          <p class="text-xs sm:text-sm text-on-surface-variant leading-relaxed">
            Outbound Jatim adalah provider resmi layanan outbound training, team building, corporate gathering, dan wisata adventure professional di Jawa Timur. Kami melayani lokasi Batu Malang, Trawas, Pacet, Bromo, hingga Banyuwangi dengan instruktur tersertifikasi BNSP dan standar keselamatan internasional.
          </p>
          <div class="flex flex-wrap items-center gap-2.5 pt-1">
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-surface-container-lowest text-xs font-semibold text-primary-container border border-outline-variant/30 shadow-xs">
              <span class="material-symbols-outlined text-[16px] text-secondary">verified</span>
              <span>Instruktur BNSP</span>
            </div>
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-surface-container-lowest text-xs font-semibold text-primary-container border border-outline-variant/30 shadow-xs">
              <span class="material-symbols-outlined text-[16px] text-emerald-600">health_and_safety</span>
              <span>Safety First</span>
            </div>
          </div>
        </div>

        <div class="lg:col-span-2 space-y-4">
          <h4 class="font-headline text-sm font-bold uppercase tracking-wider text-primary-container border-b-2 border-secondary/40 pb-2 inline-block">
            Navigasi Cepat
          </h4>
          <ul class="space-y-2.5 text-xs sm:text-sm text-on-surface-variant font-medium">
            <li><a class="hover:text-primary-container transition-colors flex items-center gap-1.5" href="../index.html"><span class="material-symbols-outlined text-[14px]">chevron_right</span>Beranda</a></li>
            <li><a class="hover:text-primary-container transition-colors flex items-center gap-1.5" href="../tentang-kami.html"><span class="material-symbols-outlined text-[14px]">chevron_right</span>Tentang Kami</a></li>
            <li><a class="hover:text-primary-container transition-colors flex items-center gap-1.5" href="../outbound/index.html"><span class="material-symbols-outlined text-[14px]">chevron_right</span>Layanan &amp; Paket</a></li>
            <li><a class="hover:text-primary-container transition-colors flex items-center gap-1.5" href="../destinasi/index.html"><span class="material-symbols-outlined text-[14px]">chevron_right</span>Destinasi Venue</a></li>
            <li><a class="hover:text-primary-container transition-colors flex items-center gap-1.5" href="../fasilitas.html"><span class="material-symbols-outlined text-[14px]">chevron_right</span>Fasilitas</a></li>
            <li><a class="hover:text-primary-container transition-colors flex items-center gap-1.5" href="../galeri.html"><span class="material-symbols-outlined text-[14px]">chevron_right</span>Galeri Documentation</a></li>
            <li><a class="hover:text-primary-container transition-colors flex items-center gap-1.5" href="../blog.html"><span class="material-symbols-outlined text-[14px]">chevron_right</span>Blog &amp; Artikel</a></li>
          </ul>
        </div>

        <div class="lg:col-span-3 space-y-4">
          <h4 class="font-headline text-sm font-bold uppercase tracking-wider text-primary-container border-b-2 border-secondary/40 pb-2 inline-block">
            Kategori Paket
          </h4>
          <ul class="space-y-2.5 text-xs sm:text-sm text-on-surface-variant font-medium">
            <li><a class="hover:text-primary-container transition-colors flex items-center gap-1.5" href="../outbound/index.html"><span class="material-symbols-outlined text-[14px] text-secondary">groups</span>Outbound &amp; Team Building</a></li>
            <li><a class="hover:text-primary-container transition-colors flex items-center gap-1.5" href="../wisata/index.html"><span class="material-symbols-outlined text-[14px] text-secondary">forest</span>Wisata &amp; Family Gathering</a></li>
            <li><a class="hover:text-primary-container transition-colors flex items-center gap-1.5" href="../destinasi/index.html"><span class="material-symbols-outlined text-[14px] text-secondary">pin_drop</span>Destinasi &amp; Venue Favorit</a></li>
            <li><a class="hover:text-primary-container transition-colors flex items-center gap-1.5" href="../paket-adventure.html"><span class="material-symbols-outlined text-[14px] text-secondary">kayaking</span>Adventure &amp; Rafting Tour</a></li>
          </ul>
        </div>

        <div class="lg:col-span-3 space-y-4">
          <h4 class="font-headline text-sm font-bold uppercase tracking-wider text-primary-container border-b-2 border-secondary/40 pb-2 inline-block">
            Kontak &amp; Area Operasional
          </h4>
          <ul class="space-y-3 text-xs sm:text-sm text-on-surface-variant">
            <li class="flex items-start gap-2.5">
              <span class="material-symbols-outlined text-[18px] text-primary-container shrink-0 mt-0.5">location_on</span>
              <span><strong>Kantor Operasional:</strong> Jl. Oro-Oro Ombo No. 88, Batu Malang, Jawa Timur</span>
            </li>
            <li class="flex items-start gap-2.5">
              <span class="material-symbols-outlined text-[18px] text-primary-container shrink-0 mt-0.5">call</span>
              <span><strong>Hotline WA:</strong> <a class="hover:text-primary-container transition-colors font-bold text-primary-container" href="https://wa.me/6282211221909" rel="noopener noreferrer" target="_blank">+62 822-1122-1909 (WhatsApp 24/7)</a></span>
            </li>
            <li class="flex items-start gap-2.5">
              <span class="material-symbols-outlined text-[18px] text-primary-container shrink-0 mt-0.5">mail</span>
              <span><strong>Email Resmi:</strong> info@outboundjatim.com</span>
            </li>
          </ul>
        </div>

      </div>

      <div class="pt-8 flex flex-col md:flex-row items-center justify-between gap-4 text-xs text-on-surface-variant font-medium">
        <p>© 2026 Outbound Jatim (PT. Outbound Indonesia Group). Hak Cipta Dilindungi Undang-Undang.</p>
        <div class="flex items-center gap-6">
          <span>Syarat &amp; Ketentuan</span>
          <span>Kebijakan Privasi</span>
          <span>Sitemap</span>
        </div>
      </div>
    </div>
  </footer>

  <a href="https://wa.me/6282211221909?text=Halo%20Outbound%20Jatim,%20saya%20ingin%20tanya%20detail%20artikel%20blog" target="_blank" rel="noopener noreferrer" class="fixed bottom-6 right-6 z-50 group flex items-center gap-2 bg-emerald-600 text-white p-3.5 rounded-full shadow-2xl hover:bg-emerald-500 hover:scale-105 transition-all duration-300 ring-4 ring-emerald-600/20" title="Chat WhatsApp Fast Response">
    <span class="material-symbols-outlined text-[26px]">chat</span>
    <span class="max-w-0 overflow-hidden group-hover:max-w-xs transition-all duration-500 ease-in-out whitespace-nowrap font-headline text-xs font-bold pr-1">Chat CS WhatsApp</span>
  </a>

  <button id="backToTop" onclick="scrollToTop()" class="fixed bottom-6 left-6 z-40 bg-surface-container-lowest/90 text-primary-container p-3 rounded-full shadow-lg border border-outline-variant/40 hover:bg-surface-container-high transition-all opacity-0 translate-y-10 pointer-events-none" title="Kembali ke Atas">
    <span class="material-symbols-outlined text-[20px]">arrow_upward</span>
  </button>

  <script>
    function toggleMobileMenu() {
      const menu = document.getElementById('mobileMenu');
      const icon = document.getElementById('mobileMenuIcon');
      if (menu.classList.contains('hidden')) {
        menu.classList.remove('hidden');
        icon.textContent = 'close';
      } else {
        menu.classList.add('hidden');
        icon.textContent = 'menu';
      }
    }

    window.addEventListener('scroll', () => {
      const btn = document.getElementById('backToTop');
      if (btn) {
        if (window.scrollY > 300) {
          btn.classList.remove('opacity-0', 'translate-y-10', 'pointer-events-none');
          btn.classList.add('opacity-100', 'translate-y-0');
        } else {
          btn.classList.add('opacity-0', 'translate-y-10', 'pointer-events-none');
          btn.classList.remove('opacity-100', 'translate-y-0');
        }
      }
    });

    function scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  </script>'''

# 1. Generate individual blog detail pages INSIDE blog/ folder
for article in blogs_data:
    filepath = os.path.join(blog_dir, article['filename'])
    canonical_url = f"https://outboundjatim.com/blog/{article['filename']}"
    
    # Remove old root-level legacy blog detail file if present
    old_root_filepath = os.path.join(base_dir, article['filename'])
    if os.path.exists(old_root_filepath):
        try:
            os.remove(old_root_filepath)
            print(f"Removed legacy root file: {old_root_filepath}")
        except Exception as e:
            pass

    # Related articles HTML generator with matching photo cards
    related_html = ""
    for rel in blogs_data:
        if rel['filename'] != article['filename']:
            related_html += f'''
            <a href="{rel['filename']}" class="group bg-surface-container-lowest rounded-2xl overflow-hidden border border-outline-variant/40 hover:shadow-lg transition-all flex flex-col sm:flex-row items-stretch">
              <div class="relative w-full sm:w-2/5 h-44 sm:h-auto overflow-hidden shrink-0 bg-surface-container-high">
                <img src="{rel['image']}" alt="{rel['title']}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy"/>
                <span class="absolute top-2.5 left-2.5 px-2.5 py-0.5 rounded-full bg-primary-container/90 backdrop-blur-md text-on-primary text-[9px] font-headline font-bold uppercase tracking-wider">{rel['category']}</span>
              </div>
              <div class="p-4 sm:p-5 flex flex-col justify-between flex-1 space-y-2">
                <div class="space-y-1.5">
                  <div class="flex items-center gap-2 text-[10px] text-secondary font-headline font-bold uppercase">
                    <span>{rel['date']}</span>
                    <span>• {rel['read_time']}</span>
                  </div>
                  <h4 class="font-headline text-sm font-bold text-primary-container group-hover:text-primary transition-colors leading-snug line-clamp-2">{rel['title']}</h4>
                  <p class="text-xs text-on-surface-variant line-clamp-2">{rel['summary']}</p>
                </div>
                <div class="pt-2 flex items-center justify-between border-t border-surface-container">
                  <span class="text-[11px] text-on-surface-variant font-medium">Artikel Terkait</span>
                  <span class="text-xs text-primary-container font-bold group-hover:underline inline-flex items-center gap-1">
                    <span>Baca Selengkapnya</span>
                    <span class="material-symbols-outlined text-[14px]">arrow_forward</span>
                  </span>
                </div>
              </div>
            </a>'''

    # Key Takeaways HTML for AEO
    takeaways_items = "".join([f'<li class="flex items-start gap-2"><span class="material-symbols-outlined text-secondary text-[16px] shrink-0 mt-0.5">check_circle</span><span>{item}</span></li>' for item in article['key_takeaways']])

    # FAQ HTML for AEO & GEO
    faq_html = ""
    faq_schemas = []
    for faq in article['faqs']:
        faq_html += f'''
        <div class="p-4 rounded-xl bg-surface-container-lowest border border-outline-variant/30 space-y-1.5">
          <h4 class="font-headline text-sm font-bold text-primary-container flex items-center gap-2">
            <span class="material-symbols-outlined text-secondary text-[18px]">help</span>
            <span>{faq['question']}</span>
          </h4>
          <p class="text-xs text-on-surface-variant leading-relaxed pl-6">
            {faq['answer']}
          </p>
        </div>'''
        faq_schemas.append({
            "@type": "Question",
            "name": faq['question'],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq['answer']
            }
        })

    import json
    faq_ld_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_schemas
    }, ensure_ascii=False, indent=2)

    article_ld_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": article['title'],
        "description": article['summary'],
        "image": f"https://outboundjatim.com/{article['image'].replace('../', '')}",
        "author": {
            "@type": "Organization",
            "name": article['author'],
            "url": "https://outboundjatim.com"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Outbound Jatim",
            "logo": {
                "@type": "ImageObject",
                "url": "https://outboundjatim.com/assets/img/logo.png"
            }
        },
        "datePublished": article['date_iso'],
        "dateModified": article['date_iso'],
        "mainEntityOfPage": canonical_url
    }, ensure_ascii=False, indent=2)

    detail_html = f'''<!DOCTYPE html>
<html class="scroll-smooth" lang="id">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>{article['title']} - Outbound Jatim</title>
  <meta name="description" content="{article['summary']}"/>
  <link rel="canonical" href="{canonical_url}"/>
  
  <!-- SEO & Open Graph Meta Tags -->
  <meta property="og:title" content="{article['title']} - Outbound Jatim"/>
  <meta property="og:description" content="{article['summary']}"/>
  <meta property="og:image" content="https://outboundjatim.com/{article['image'].replace('../', '')}"/>
  <meta property="og:url" content="{canonical_url}"/>
  <meta property="og:type" content="article"/>
  
  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com" rel="preconnect"/>
  <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Plus+Jakarta+Sans:wght@500;600;700;800&amp;display=swap" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet"/>
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
  <script id="tailwind-config">
    tailwind.config = {{
      darkMode: "class",
      theme: {{
        extend: {{
          colors: {{
            "primary-container": "#4a0e17",
            "on-primary": "#ffffff",
            "on-primary-container": "#ca7379",
            "primary": "#2a0006",
            "secondary-container": "#fdc268",
            "on-secondary-container": "#764e00",
            "secondary": "#805600",
            "tertiary-container": "#002931",
            "on-tertiary-container": "#6e919b",
            "background": "#fff8f7",
            "on-background": "#201a1b",
            "surface": "#fff8f7",
            "on-surface": "#201a1b",
            "surface-container-lowest": "#ffffff",
            "surface-container-low": "#fef1f2",
            "surface-container": "#f8ebec",
            "surface-container-high": "#f2e5e6",
            "on-surface-variant": "#544343",
            "outline-variant": "#d9c1c1"
          }},
          fontFamily: {{
            headline: ["Plus Jakarta Sans", "sans-serif"],
            body: ["Inter", "sans-serif"]
          }}
        }}
      }}
    }};
  </script>
  <style>
    .material-symbols-outlined {{
      font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    }}
  </style>

  <!-- Schema JSON (SEO, AEO & GEO Structured Data) -->
  <script type="application/ld+json">
  {article_ld_json}
  </script>

  <script type="application/ld+json">
  {faq_ld_json}
  </script>
  <!-- Favicon -->
  <link rel="icon" type="image/webp" href="../assets/img/favicon-removebg-preview.webp"/>
  <link rel="apple-touch-icon" href="../assets/img/favicon-removebg-preview.webp"/>
</head>
<body class="bg-background font-body text-on-surface antialiased flex flex-col min-h-screen">

{topbar_nav_header_subfolder}

  <!-- MAIN CONTENT -->
  <main class="w-full pt-32 sm:pt-28 flex-1">
    
    <!-- Top Breadcrumb Section -->
    <section class="w-full bg-surface-container-low py-4 px-4 sm:px-8 border-b border-outline-variant/30">
      <div class="max-w-4xl mx-auto flex items-center justify-between text-xs sm:text-sm text-on-surface-variant">
        <nav aria-label="Breadcrumb" class="flex items-center gap-2 overflow-x-auto">
          <a class="hover:text-primary-container transition-colors shrink-0" href="../index.html">Beranda</a>
          <span class="material-symbols-outlined text-[14px] shrink-0">chevron_right</span>
          <a class="hover:text-primary-container transition-colors shrink-0" href="../blog.html">Blog &amp; Panduan</a>
          <span class="material-symbols-outlined text-[14px] shrink-0">chevron_right</span>
          <span class="text-primary-container font-bold truncate max-w-xs sm:max-w-md">{article['title']}</span>
        </nav>
      </div>
    </section>

    <!-- Blog Header Banner -->
    <section class="w-full py-10 px-4 sm:px-8 bg-surface border-b border-outline-variant/30">
      <div class="max-w-4xl mx-auto space-y-4">
        <div class="flex flex-wrap items-center gap-3">
          <span class="px-3 py-1 rounded-full bg-secondary-container/30 text-on-secondary-container font-headline text-xs font-bold uppercase tracking-wider">
            {article['category']}
          </span>
          <span class="text-xs text-on-surface-variant font-medium">• {article['date']}</span>
          <span class="text-xs text-on-surface-variant font-medium">• Waktu Baca: {article['read_time']}</span>
          <span class="text-xs text-secondary font-bold uppercase tracking-wider">• Author: {article['author']}</span>
        </div>
        <h1 class="font-headline text-2xl sm:text-4xl font-extrabold text-primary-container leading-tight">
          {article['title']}
        </h1>
        <p class="text-sm sm:text-base text-on-surface-variant leading-relaxed">
          {article['summary']}
        </p>

        <!-- Image Banner -->
        <div class="relative w-full h-64 sm:h-96 rounded-2xl overflow-hidden shadow-lg border border-outline-variant/40 mt-4">
          <img src="{article['image']}" alt="{article['title']}" class="w-full h-full object-cover" loading="eager"/>
        </div>
      </div>
    </section>

    <!-- Main Article Body & CTA Sidebar -->
    <section class="w-full py-12 px-4 sm:px-8 bg-surface">
      <div class="max-w-4xl mx-auto space-y-10">
        
        <!-- AEO Key Takeaways Box -->
        <div class="p-6 rounded-2xl bg-secondary-container/20 border-2 border-secondary/40 space-y-3">
          <div class="flex items-center gap-2 text-primary-container font-headline text-sm font-bold uppercase tracking-wider">
            <span class="material-symbols-outlined text-secondary text-[20px]">lightbulb</span>
            <span>Key Takeaways / Ringkasan Cepat Artikel (AEO &amp; GEO)</span>
          </div>
          <ul class="space-y-2 text-xs sm:text-sm text-on-surface-variant font-medium">
            {takeaways_items}
          </ul>
        </div>

        <!-- Article Body -->
        <article class="prose max-w-none space-y-6">
          {article['content']}
        </article>

        <!-- FAQ Section (AEO Direct Answers & GEO Citations) -->
        <div class="pt-6 border-t border-outline-variant/30 space-y-4">
          <div class="flex items-center gap-2 text-primary-container font-headline text-lg font-bold">
            <span class="material-symbols-outlined text-secondary text-[22px]">quiz</span>
            <h3>Pertanyaan Sering Diajukan (FAQ - Answer Engine Optimization):</h3>
          </div>
          <div class="space-y-3">
            {faq_html}
          </div>
        </div>

        <!-- CTA Box -->
        <div class="p-6 sm:p-8 rounded-2xl bg-primary-container text-on-primary shadow-xl space-y-4 text-center sm:text-left flex flex-col sm:flex-row items-center justify-between gap-6">
          <div class="space-y-2">
            <h3 class="font-headline text-xl font-bold text-white">Butuh Konsultasi Program Outbound Perusahaan?</h3>
            <p class="text-xs sm:text-sm text-surface-container-high leading-relaxed max-w-xl">
              Tim profesional Outbound Jatim siap mendesain modul kegiatan, estimasi RAB, dan survey lokasi sesuai anggaran instansi Anda di Batu Malang, Trawas, Pacet, Bromo &amp; Banyuwangi.
            </p>
          </div>
          <a class="px-6 py-3.5 rounded-full bg-emerald-600 text-white font-headline text-xs sm:text-sm font-bold shadow-lg hover:bg-emerald-500 transition-all shrink-0 flex items-center gap-2" href="https://wa.me/6282211221909?text=Halo%20Outbound%20Jatim,%20saya%20tertarik%20konsultasi%20setelah%20membaca%20artikel%20{article['title']}" target="_blank">
            <span class="material-symbols-outlined text-[18px]">chat</span>
            <span>Konsultasi WA Gratis</span>
          </a>
        </div>

        <!-- Related Articles Grid -->
        <div class="pt-8 border-t border-outline-variant/30 space-y-4">
          <h3 class="font-headline text-lg font-bold text-primary-container">Artikel Terkait Lainnya:</h3>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {related_html}
          </div>
        </div>

      </div>
    </section>

  </main>

{footer_code_subfolder}

</body>
</html>'''

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(detail_html)
    print(f"Generated blog detail page in blog/: {filepath}")

# 2. Update blog.html to link to blog/filename.html
blog_page_filepath = os.path.join(base_dir, 'blog.html')

cards_html = ""
for article in blogs_data:
    cards_html += f'''
          <!-- Article Card -->
          <article class="blog-card group bg-surface-container-lowest rounded-2xl overflow-hidden shadow-sm hover:shadow-lg transition-all border border-outline-variant/40 flex flex-col justify-between" data-title="{article['title']}" data-category="{article['category']}" data-desc="{article['summary']}">
            <div class="relative w-full h-48 overflow-hidden bg-surface-container-high">
              <img src="{article['image'].replace('../', '')}" alt="{article['title']}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy"/>
              <span class="absolute top-3 left-3 px-3 py-1 rounded-full bg-primary-container/90 backdrop-blur-md text-on-primary text-[10px] font-headline font-bold uppercase tracking-wider">{article['category']}</span>
            </div>
            <div class="p-6 flex flex-col justify-between flex-1 space-y-4">
              <div class="space-y-3">
                <div class="flex items-center justify-between text-xs text-secondary font-headline font-bold uppercase">
                  <span>{article['date']}</span>
                  <span>Baca {article['read_time']}</span>
                </div>
                <h3 class="font-headline text-lg font-bold text-primary-container">
                  <a href="blog/{article['filename']}" class="hover:text-primary transition-colors">{article['title']}</a>
                </h3>
                <p class="text-xs text-on-surface-variant line-clamp-3">{article['summary']}</p>
              </div>
              <div class="pt-3 border-t border-surface-container flex items-center justify-between">
                <span class="text-xs text-on-surface-variant font-medium">Artikel Outbound</span>
                <a class="text-xs font-bold text-primary-container hover:underline flex items-center gap-1" href="blog/{article['filename']}">
                  <span>Baca Selengkapnya</span>
                  <span class="material-symbols-outlined text-[14px]">arrow_forward</span>
                </a>
              </div>
            </div>
          </article>'''

blog_search_and_grid_section = f'''
    <!-- Search Bar Section (ONLY SEARCH FITUR) -->
    <div class="max-w-7xl mx-auto px-4 sm:px-8 -mt-6 relative z-20">
      <div class="bg-surface-container-lowest p-4 sm:p-6 rounded-2xl shadow-lg border border-outline-variant/40 max-w-2xl mx-auto">
        
        <!-- Search Input -->
        <div class="relative w-full">
          <span class="material-symbols-outlined absolute left-3.5 top-1/2 -translate-y-1/2 text-on-surface-variant text-[20px]">search</span>
          <input type="text" id="blogSearchInput" onkeyup="filterBlogs()" placeholder="Cari artikel blog..." class="w-full pl-11 pr-10 py-3 rounded-xl bg-surface-container-low border border-outline-variant/40 text-xs sm:text-sm text-on-surface focus:outline-none focus:ring-2 focus:ring-primary-container font-medium">
          <button id="clearSearchBtn" onclick="clearSearch()" class="hidden absolute right-3 top-1/2 -translate-y-1/2 text-on-surface-variant hover:text-primary-container">
            <span class="material-symbols-outlined text-[18px]">close</span>
          </button>
        </div>

      </div>
    </div>

    <!-- Blog Articles Showcase Grid (3 Articles) -->
    <section class="w-full py-12 px-4 sm:px-8 bg-surface">
      <div class="max-w-7xl mx-auto flex flex-col gap-8">
        
        <!-- Articles Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6" id="blogCardsGrid">
{cards_html}
        </div>

        <!-- No Results Found State -->
        <div id="noResultsMessage" class="hidden text-center py-16 space-y-3 bg-surface-container-lowest rounded-2xl border border-outline-variant/30">
          <span class="material-symbols-outlined text-[48px] text-on-surface-variant">search_off</span>
          <h3 class="font-headline text-lg font-bold text-primary-container">Artikel Tidak Ditemukan</h3>
          <p class="text-xs text-on-surface-variant">Coba kata kunci pencarian lain.</p>
          <button onclick="clearSearch()" class="inline-flex items-center gap-1.5 px-4 py-2 rounded-full bg-primary-container text-on-primary text-xs font-bold hover:bg-primary transition-all shadow-sm">
            <span>Reset Pencarian</span>
          </button>
        </div>

      </div>
    </section>

    <!-- Live Search Script -->
    <script>
      function filterBlogs() {{
        const query = document.getElementById('blogSearchInput').value.toLowerCase().trim();
        const clearBtn = document.getElementById('clearSearchBtn');
        const cards = document.querySelectorAll('.blog-card');
        let visibleCount = 0;

        if (query.length > 0) {{
          clearBtn.classList.remove('hidden');
        }} else {{
          clearBtn.classList.add('hidden');
        }}

        cards.forEach(card => {{
          const title = card.getAttribute('data-title').toLowerCase();
          const category = card.getAttribute('data-category').toLowerCase();
          const desc = card.getAttribute('data-desc').toLowerCase();

          const matchesSearch = query === '' || title.includes(query) || category.includes(query) || desc.includes(query);

          if (matchesSearch) {{
            card.style.display = 'flex';
            visibleCount++;
          }} else {{
            card.style.display = 'none';
          }}
        }});

        const noResults = document.getElementById('noResultsMessage');
        if (noResults) {{
          if (visibleCount === 0) {{
            noResults.classList.remove('hidden');
          }} else {{
            noResults.classList.add('hidden');
          }}
        }}
      }}

      function clearSearch() {{
        document.getElementById('blogSearchInput').value = '';
        filterBlogs();
      }}
    </script>'''

with open(blog_page_filepath, 'r', encoding='utf-8') as f:
    blog_content = f.read()

search_section_pattern = r'<!-- Search (?:Bar Section|& Filter Bar Section).*?<!-- Live Search (?:& Category Filtering |)Script -->\s*<script>.*?</script>'
if re.search(search_section_pattern, blog_content, flags=re.DOTALL):
    updated_blog_content = re.sub(search_section_pattern, blog_search_and_grid_section, blog_content, flags=re.DOTALL)
else:
    old_section_pattern = r'<!-- Blog Articles Showcase -->\s*<section class="w-full py-16 px-4 sm:px-8 bg-surface">.*?</section>'
    updated_blog_content = re.sub(old_section_pattern, blog_search_and_grid_section, blog_content, flags=re.DOTALL)

with open(blog_page_filepath, 'w', encoding='utf-8') as f:
    f.write(updated_blog_content)

print("Successfully updated generate_blogs.py, generated detail pages in blog/, and updated blog.html!")
