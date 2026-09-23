import os
import re

outbound_packages = [
    'detail-paket-executive-team-building.html',
    'detail-paket-leadership-camp.html',
    'detail-paket-fun-outbound.html',
    'detail-paket-character-building.html',
    'detail-paket-rafting-kasembon.html',
    'detail-paket-paintball-battle.html',
    'detail-paket-bromo-offroad.html',
    'detail-paket-outbound-rafting-combo.html',
]

wisata_packages = [
    'detail-paket-batu-agro-tour.html',
    'detail-paket-bromo-sunrise-culture.html',
    'detail-paket-banyuwangi-ijen-baluran.html',
    'detail-paket-custom-gathering.html',
]

topbar_nav_header_subfolder = '''  <!-- NAVBAR & TOP BAR (UNIFIED) -->
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
            <button class="flex items-center gap-1 font-headline font-bold text-primary-container relative after:content-[''] after:absolute after:-bottom-2 after:left-0 after:right-0 after:h-0.5 after:bg-primary-container after:rounded-full text-sm transition-colors py-1" type="button">
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
          <a class="font-headline font-medium text-on-surface-variant hover:text-primary-container text-sm transition-colors py-1" href="../blog.html">
            Blog
          </a>
        </nav>

        <!-- CTA & Mobile Menu Toggle -->
        <div class="flex items-center gap-3 shrink-0">
          <a class="hidden sm:inline-flex items-center justify-center px-5 py-2.5 rounded-full bg-primary-container text-on-primary font-headline text-sm font-bold hover:bg-primary transition-all shadow-sm ring-1 ring-secondary-container/30" href="https://wa.me/6282211221909?text=Halo%20Outbound%20Jatim,%20saya%20ingin%20konsultasi%20paket" rel="noopener noreferrer" target="_blank">
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

footer_code_subfolder = '''  <!-- FOOTER -->
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
            Outbound Jatim adalah provider resmi layanan outbound training, team building, corporate gathering, dan wisata adventure professional di Jawa Timur. Kami melayani lokasi Batu Malang, Trawas, Pacet, Bromo, hingga Banyuwangi dengan instruktur tersertifikasi BNSP dan standar keamanan internasional.
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

  <a href="https://wa.me/6282211221909?text=Halo%20Outbound%20Jatim,%20saya%20ingin%20tanya%20detail%20paket" target="_blank" rel="noopener noreferrer" class="fixed bottom-6 right-6 z-50 group flex items-center gap-2 bg-emerald-600 text-white p-3.5 rounded-full shadow-2xl hover:bg-emerald-500 hover:scale-105 transition-all duration-300 ring-4 ring-emerald-600/20" title="Chat WhatsApp Fast Response">
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

packages_data = [
    {
        'filename': 'detail-paket-executive-team-building.html',
        'folder': 'outbound',
        'title': 'Executive Team Building Batu',
        'category': 'OUTBOUND & TEAM BUILDING',
        'subtitle': 'Paket Outbound Team Building Fullday di Coban Rondo & Songgoriti Batu',
        'price': 175000,
        'venue': 'Coban Rondo / Songgoriti Batu Malang',
        'capacity': '30 - 500+ Pax',
        'duration': '1 Day Fullday (08.00 - 15.00 WIB)',
        'description': 'Program simulasi outdoor interaktif berfokus pada penguatan sinergi tim, komunikasi efektif antar divisi, adaptabilitas kepemimpinan taktis, dan pemecahan masalah kelompok dengan pendekatan Experiential Learning oleh fasilitator BNSP.',
        'gallery': {
            'main_img': '../assets/img/tos_tantangan_tim_outboundindonesia.webp',
            'main_title': 'Simulasi Team Building Executive',
            'thumbs': [
                ('../assets/img/tim_building_perusahaan_outboundindonesia.webp', 'Sinergi Tim'),
                ('../assets/img/sesi_materi_perusahaan_outboundindonesia.webp', 'Evaluasi BNSP'),
                ('../assets/img/gathering_perusahaan_lapangan_outboundindonesia.webp', 'Simulasi Outdoor')
            ]
        },
        'includes': [
            'Modul Experiential Learning + Master Trainer BNSP',
            'Sewa Lapangan Rumput & Perizinan Lokasi Outbound',
            'Peralatan Game Equipment & Property Lengkap',
            'Sound System Outdoor & Megaphone Trainer',
            'Makan Siang Prasmanan Khas Batu & Welcome Drink',
            'Air Mineral Botol 600ml Selama Acara',
            'Banner / Spanduk Welcome 4x1 Meter Custom',
            'Tim Medis Siaga & Kotak P3K Standar Outdoor'
        ],
        'rundown': [
            ('08.00 - 08.30', 'Kedatangan & Registrasi', 'Penyambutan peserta di lokasi, pembagian ID tag, welcome drink & snack tradisional.'),
            ('08.30 - 10.00', 'Ice Breaking & Grouping', 'Peleburan kekakuan antar divisi, fun energizer, pembentukan kelompok, yel-yel tim.'),
            ('10.00 - 12.00', 'Synergy & Leadership Games', 'Simulasi tantangan kelompok (Spider Web, Poison Carpet, Transfer Tower).'),
            ('12.00 - 13.00', 'Ishoma (Istirahat & Prasmanan)', 'Makan siang prasmanan khas masakan Batu & waktu istirahat.'),
            ('13.00 - 15.00', 'Final Mission & Debriefing', 'Simulasi gabungan seluruh tim (Tower of Babel) & refleksi komitmen kerja.')
        ],
        'wa_msg': 'Halo Outbound Jatim, saya ingin konsultasi dan pesan Paket Executive Team Building Batu (Rp 175.000/pax)'
    },
    {
        'filename': 'detail-paket-leadership-camp.html',
        'folder': 'outbound',
        'title': 'Leadership Camp & Glamping Trawas',
        'category': 'LEADERSHIP & RETREAT',
        'subtitle': 'Paket Inap Villa / Tenda Glamping 2D1N & Motivasi Keakraban Trawas',
        'price': 385000,
        'venue': 'Villa / Tenda Glamping Trawas Mojokerto',
        'capacity': '20 - 300+ Pax',
        'duration': '2 Days 1 Night',
        'description': 'Pengalaman menginap di villa atau tenda glamping udara sejuk Trawas diselingi malam keakraban api unggun, motivasi kepemimpinan malam hari, dan outbound team building intensif hari ke-2.',
        'gallery': {
            'main_img': '../assets/img/sesi_materi_perusahaan_outboundindonesia.webp',
            'main_title': 'Sesi Motivasi & Leadership Camp',
            'thumbs': [
                ('../assets/img/tos_tantangan_tim_outboundindonesia.webp', 'Tantangan Tim'),
                ('../assets/img/tenda_camping_matahari_terbit_outboundindonesia.webp', 'Glamping Camp'),
                ('../assets/img/barbekyu_sate_daging_outboundindonesia.webp', 'Malam Keakraban')
            ]
        },
        'includes': [
            'Akomodasi Villa Eksklusif / Tenda Glamping Trawas',
            '3x Makan (Prasmanan/BBQ) & 2x Coffee Break',
            'Acara Malam Keakraban & Api Unggun + Sound System',
            'Program Outbound Team Building Hari Ke-2',
            'Fasilitator & Motivator BNSP Certified',
            'Air Mineral Botol & Snack Pendamping',
            'Banner Acara Custom 4x1 Meter',
            'Tim Medis & Asuransi Kegiatan Outdoor'
        ],
        'rundown': [
            ('Hari 1 - 14.00', 'Check-in Villa / Glamping', 'Pembagian kamar/tenda, istirahat dan nikmati welcome drink.'),
            ('Hari 1 - 16.00', 'Fun Energizer Sore', 'Permainan ringan untuk mengakrabkan seluruh peserta.'),
            ('Hari 1 - 19.00', 'Malam Keakraban & Api Unggun', 'Gala dinner / BBQ, motivasi kepemimpinan malam, dan api unggun.'),
            ('Hari 2 - 06.00', 'Senam Pagi & Sarapan', 'Olahraga ringan dan makan pagi sehat bersama.'),
            ('Hari 2 - 08.00', 'Outbound Training Intensif', 'Simulasi kepemimpinan dan kerjasama tim di arena terbuka.'),
            ('Hari 2 - 12.00', 'Check-out & Penutupan', 'Makan siang, pembagian foto kenang-kenangan dan perjalanan pulang.')
        ],
        'wa_msg': 'Halo Outbound Jatim, saya ingin konsultasi dan pesan Paket Leadership Camp Trawas (Rp 385.000/pax)'
    },
    {
        'filename': 'detail-paket-fun-outbound.html',
        'folder': 'outbound',
        'title': 'Fun Outbound & Recreational Games',
        'category': 'RECREATIONAL OUTBOUND',
        'subtitle': 'Program Fun Games Rekreasi Ringan & Refreshing Karyawan',
        'price': 135000,
        'venue': 'Taman Rekreasi Selecta / Coban Rondo Batu',
        'capacity': '40 - 1000+ Pax',
        'duration': 'Halfday / Fullday (3 - 5 Jam)',
        'description': 'Program permainan rekreasi ringan dan gembira yang dirancang khusus untuk melepas penat kerja, membangun keakraban santai, dan menghibur seluruh jajaran staf serta keluarga.',
        'gallery': {
            'main_img': '../assets/img/es_breaking_grup_perusahaan_outboundindonesia.webp',
            'main_title': 'Fun Outbound Ceria',
            'thumbs': [
                ('../assets/img/profesional_tertawa_kegiatan_outboundindonesia.webp', 'Ice Breaking'),
                ('../assets/img/gathering_perusahaan_lapangan_outboundindonesia.webp', 'Games Lapangan'),
                ('../assets/img/siswa_bermain_game_lapangan_outboundindonesia.webp', 'Synergy Games')
            ]
        },
        'includes': [
            'Master Games Master & Game Crew Ceria',
            'Peralatan Fun Games Warna-warni Lengkap',
            'Sound System Outdoor Portable',
            'Makan Siang Box / Prasmanan',
            'Welcome Snack & Es Kelapa Muda',
            'Banner Foto Bersama 3x1 Meter',
            'P3K Standar & Air Mineral Refill'
        ],
        'rundown': [
            ('08.30 - 09.00', 'Gathering & Opening Ceria', 'Pembukaan oleh MC / Master Games & pemanasan gembira.'),
            ('09.00 - 10.30', 'Fun Games & Competition', 'Lomba antar kelompok (Estafet Air, Bakiak Raksasa, Voli Plastik).'),
            ('10.30 - 11.30', 'Final Game & Pembagian Hadiah', 'Permainan penutup bersama seluruh peserta & penyerahan doorprize.'),
            ('11.30 - 13.00', 'Makan Siang & Acara Bebas', 'Makan siang bersama dan menikmati wahana rekreasi lokasi.')
        ],
        'wa_msg': 'Halo Outbound Jatim, saya ingin konsultasi dan pesan Paket Fun Outbound (Rp 135.000/pax)'
    },
    {
        'filename': 'detail-paket-character-building.html',
        'folder': 'outbound',
        'title': 'Character & Capacity Building',
        'category': 'DEVELOPMENT PROGRAM',
        'subtitle': 'Pelatihan Karakter, Kedisiplinan & Etos Kerja Profesional',
        'price': 225000,
        'venue': 'Pusdiklat / Hutan Pinus Trawas Pacet',
        'capacity': '30 - 300 Pax',
        'duration': '1 - 2 Days',
        'description': 'Program pengembangan karakter berbasis mental tangguh, disiplin tinggi, integritas personal, dan loyalitas organisasi yang dipandu oleh instruktur senior dan praktisi psikologi lapangan.',
        'gallery': {
            'main_img': '../assets/img/siswa_bermain_game_lapangan_outboundindonesia.webp',
            'main_title': 'Pelatihan Karakter & Disiplin',
            'thumbs': [
                ('../assets/img/siswa_sorak_perkemahan_outboundindonesia.webp', 'Semangat Tim'),
                ('../assets/img/es_breaking_grup_perusahaan_outboundindonesia.webp', 'Kekompakan'),
                ('../assets/img/tos_tantangan_tim_outboundindonesia.webp', 'Mentoring Lapangan')
            ]
        },
        'includes': [
            'Modul Pembentukan Karakter & Etos Kerja',
            'Instruktur Kedisiplinan & Tim Fasilitator Psikologi',
            'Seragam Kaos Outbound & Topi Custom',
            'Peralatan Simulasi Ketahanan Mental',
            'Konsumsi Makan Siang Prasmanan & Coffee Break',
            'Sertifikat Keikutsertaan Peserta',
            'Dokumentasi Foto & Video High Quality'
        ],
        'rundown': [
            ('07.30 - 08.00', 'Upacara Pembukaan & Apel Pagi', 'Penyerahan peserta kepada tim instruktur & penanaman komitmen.'),
            ('08.00 - 10.30', 'Discipline & Focus Training', 'Simulasi konsentrasi, baris-berbaris dinamika, dan ketaatan instruksi.'),
            ('10.30 - 12.00', 'Problem Solving Challenge', 'Tantangan pemecahan masalah rumit dengan batas waktu ketat.'),
            ('12.00 - 13.00', 'Ishoma & Pembinaan Mental', 'Makan siang teratur & evaluasi perilaku bersama.'),
            ('13.00 - 15.30', 'Commitment Building & Debriefing', 'Perumusan janji komitmen kerja & pembaretan/penutupan simbolis.')
        ],
        'wa_msg': 'Halo Outbound Jatim, saya ingin konsultasi Paket Character Building (Rp 225.000/pax)'
    },
    {
        'filename': 'detail-paket-rafting-kasembon.html',
        'folder': 'outbound',
        'title': 'White Water Rafting Kasembon Malang',
        'category': 'ADVENTURE & RAFTING',
        'subtitle': 'Pengarungan Sungai Kasembon 7.5 KM dengan 12+ Jeram Menantang',
        'price': 215000,
        'venue': 'Kasembon Rafting, Malang Barat',
        'capacity': '15 - 300+ Pax',
        'duration': 'Halfday (2 - 3 Jam di Sungai)',
        'description': 'Petualangan mengarungi kesegaran arus Sungai Kasembon Malang sepanjang 7.5 KM. Diapit pemandangan tebing sawah yang indah, air terjun alami, dan jeram grade III yang memicu adrenalin namun aman.',
        'gallery': {
            'main_img': '../assets/img/arung_jeram_peserta_outboundindonesia.webp',
            'main_title': 'Arung Jeram Kasembon Malang',
            'thumbs': [
                ('../assets/img/rafting_keluarga_sungai_outboundindonesia.webp', 'Pengarungan Jeram'),
                ('../assets/img/barbekyu_sate_daging_outboundindonesia.webp', 'Makan Prasmanan'),
                ('../assets/img/restoran_interior_lembah_outboundindonesia.webp', 'Basecamp Resto')
            ]
        },
        'includes': [
            'Perahu Karet, Dayung, Helm, & Life Jacket Standar SNI',
            'Guide / Skipper Bersertifikat & Tim Rescue Siaga',
            'Pengangkut Perahu & Transport Lokal',
            'Welcome Drink, Snack Warm & Kelapa Muda Segar',
            'Makan Siang Prasmanan Masakan Desa Kasembon',
            'Asuransi Jiwa Pengarungan Rafting',
            'Fasilitas Kamar Mandi Bilas & Loker Penyimpanan'
        ],
        'rundown': [
            ('08.30 - 09.00', 'Registrasi & Safety Briefing', 'Fiting helm & pelampung, serta instruksi keselamatan oleh kepala skipper.'),
            ('09.00 - 09.15', 'Simulasi Dayung', 'Latihan cara mendayung dan merunduk di perahu.'),
            ('09.15 - 11.30', 'Pengarungan Sungai Kasembon', 'Mengarungi jeram seru, stopover di air terjun & kelapa muda.'),
            ('11.30 - 13.00', 'Bilas & Makan Siang Prasmanan', 'Mandi di ruang bilas dan menikmati hidangan prasmanan hangat.')
        ],
        'wa_msg': 'Halo Outbound Jatim, saya ingin booking Paket Rafting Kasembon (Rp 215.000/pax)'
    },
    {
        'filename': 'detail-paket-paintball-battle.html',
        'folder': 'outbound',
        'title': 'Paintball Battle Wargame Simulation',
        'category': 'TACTICAL ADVENTURE',
        'subtitle': 'Simulasi Tempur Taktis di Arena Hutan Pinus dengan Senapan Gas Tippmann',
        'price': 150000,
        'venue': 'Hutan Pinus Coban Rondo / Songgoriti / Trawas',
        'capacity': '20 - 200 Pax',
        'duration': '2 - 3 Jam Match',
        'description': 'Uji taktik, keberanian, dan komunikasi tim melalui wargame paintball profesional. Menggunakan senjata Tippmann US, pelindung goggle helm, seragam loreng komando, dan skenario pertempuran memikat.',
        'gallery': {
            'main_img': '../assets/img/paintball_outboundindonesia.webp',
            'main_title': 'Simulasi Tempur Paintball',
            'thumbs': [
                ('../assets/img/flying_fox_outboundindonesia.webp', 'Flying Fox'),
                ('../assets/img/pos_p3k_taman_outboundindonesia.webp', 'Safety Post'),
                ('../assets/img/tos_tantangan_tim_outboundindonesia.webp', 'Taktik Tim')
            ]
        },
        'includes': [
            'Senjata Paintball Semi-Otomatis Gas CO2',
            '50 Butir Peluru Cat Per Peserta',
            'Masker Pelindung Wajah / Goggle Full Face',
            'Seragam Loreng Komando Protect Body',
            'Wasit / Marshal Arena & Safety Instructor',
            'Sewa Arena Pertempuran Hutan Pinus',
            'Air Mineral Botol 600ml & P3K Siaga'
        ],
        'rundown': [
            ('09.00 - 09.30', 'Tactical Briefing & Gear Up', 'Penjelasan aturan main, pemakaian masker goggle & seragam loreng.'),
            ('09.30 - 10.15', 'Round 1: Elimination Battle', 'Skenario perebutan benteng musuh dan eliminasi total lawan.'),
            ('10.15 - 11.00', 'Round 2: Capture The Flag', 'Misi taktis merebut bendera utama di tengah hutan pinus.'),
            ('11.00 - 11.30', 'Debriefing & Pengumuman Juara', 'Evaluasi taktik kerjasama dan foto komando bersama.')
        ],
        'wa_msg': 'Halo Outbound Jatim, saya ingin pesan Paket Paintball Battle (Rp 150.000/pax)'
    },
    {
        'filename': 'detail-paket-bromo-offroad.html',
        'folder': 'outbound',
        'title': 'Bromo Offroad Jeep 4x4 Expedition',
        'category': 'ADVENTURE TOUR',
        'subtitle': 'Jelajah 5 Destinasi Ikonik Bromo Menggunakan Jeep Hardtop Toyota Land Cruiser',
        'price': 450000,
        'venue': 'Kawasan Taman Nasional Bromo Tengger Semeru',
        'capacity': '12 - 200+ Pax (6 Pax per Jeep)',
        'duration': 'Midnight Expedition (00.00 - 12.00 WIB)',
        'description': 'Menembus lautan pasir Bromo di malam hari, menyaksikan matahari terbit tercantik di Penanjakan 1 Bromo, dilanjutkan eksplorasi Kawah Aktif, Pasir Berbisik, dan Savana Bukit Teletubbies.',
        'gallery': {
            'main_img': '../assets/img/tenda_camping_matahari_terbit_outboundindonesia.webp',
            'main_title': 'Sunrise & Jeep Expedition Bromo',
            'thumbs': [
                ('../assets/img/background.webp', 'Lautan Pasir'),
                ('../assets/img/barbekyu_sate_daging_outboundindonesia.webp', 'Sarapan Warm'),
                ('../assets/img/hotel_mewah_eksterior_outboundindonesia.webp', 'Transit Hotel')
            ]
        },
        'includes': [
            'Sewa Jeep Toyota Land Cruiser 4x4 + Driver Pengalaman',
            'Tiket Masuk Tamu Nusantara Taman Nasional Bromo',
            'Spot Penanjakan 1 / Kingkong Hill Sunrise',
            'Eksplorasi Kawah Bromo & Pura Luhur Poten',
            'Spot Pasir Berbisik & Savana Bukit Teletubbies',
            'Sarapan Hangat di Area Resto Bromo',
            'Driver Guide & Masker Debu Bromo'
        ],
        'rundown': [
            ('00.30 - 02.30', 'Penjemputan & Perjalanan ke Bromo', 'Meeting point Malang/Probolinggo, perjalanan naik Jeep 4x4.'),
            ('03.30 - 06.00', 'Sunrise View Penanjakan 1', 'Menikmati keindahan Bromo Sunrise & golden hour panorama.'),
            ('06.30 - 08.30', 'Lautan Pasir & Kawah Bromo', 'Trekking/naik kuda ke bibir Kawah Bromo & Pura Poten.'),
            ('08.30 - 10.30', 'Pasir Berbisik & Bukit Teletubbies', 'Sesi foto estetis di bukit hijau savana Bromo.'),
            ('10.30 - 12.00', 'Sarapan & Kembali ke Meeting Point', 'Makan pagi dan pengantaran kembali ke titik awal.')
        ],
        'wa_msg': 'Halo Outbound Jatim, saya ingin tanya Paket Bromo Offroad Jeep (Rp 450.000/pax)'
    },
    {
        'filename': 'detail-paket-outbound-rafting-combo.html',
        'folder': 'outbound',
        'title': 'Combo Outbound Training + Rafting Batu',
        'category': 'COMBO ADVENTURE',
        'subtitle': 'Paket Super Lengkap: Team Building Pagi + Rafting Seru Siang Hari',
        'price': 325000,
        'venue': 'Coban Rondo & Sungai Kasembon / Pujon',
        'capacity': '20 - 300 Pax',
        'duration': '1 Full Day Adventure (08.00 - 16.30 WIB)',
        'description': 'Kombinasi sempurna untuk perusahaan yang menginginkan penguatan kekompakan tim lewat Outbound Training di pagi hari, lalu memuncak pada pengarungan jeram rafting seru di siang hari.',
        'gallery': {
            'main_img': '../assets/img/arung_jeram_peserta_outboundindonesia.webp',
            'main_title': 'Combo Outbound & Rafting Adventure',
            'thumbs': [
                ('../assets/img/tim_building_perusahaan_outboundindonesia.webp', 'Team Building'),
                ('../assets/img/rafting_keluarga_sungai_outboundindonesia.webp', 'Rafting Seru'),
                ('../assets/img/es_breaking_grup_perusahaan_outboundindonesia.webp', 'Ice Breaking')
            ]
        },
        'includes': [
            'Sesi Outbound Team Building + Trainer BNSP',
            'Paket Rafting Kasembon 7.5 KM + Perlengkapan SNI',
            'Peralatan Game Equipment Outbound & Sound System',
            'Makan Siang Prasmanan + Welcome Drink',
            'Snack Warm & Kelapa Muda Segar di Rafting',
            'Dokumentasi Foto Lapangan & Banner Acara',
            'Asuransi Jiwa & Tim P3K Siaga'
        ],
        'rundown': [
            ('08.00 - 08.30', 'Registrasi & Opening', 'Penyambutan dan ice breaking pembuka di lapangan outbound.'),
            ('08.30 - 11.30', 'Outbound Team Building Games', 'Simulasi kekompakan, problem solving, dan sinergi kelompok.'),
            ('11.30 - 12.30', 'Ishoma & Transisi ke Basecamp Rafting', 'Makan siang prasmanan dan perjalanan singkat ke basecamp.'),
            ('12.30 - 15.30', 'Pengarungan Rafting Arus Sungai', 'Sensasi jeram menantang dan kesegaran air alam Batu Kasembon.'),
            ('15.30 - 16.30', 'Bilas, Kelapa Muda & Penutupan', 'Bilas bersih, nikmati kelapa muda segar, dan sesi penutupan.')
        ],
        'wa_msg': 'Halo Outbound Jatim, saya ingin konsultasi Paket Combo Outbound + Rafting (Rp 325.000/pax)'
    },
    {
        'filename': 'detail-paket-batu-agro-tour.html',
        'folder': 'wisata',
        'title': 'Family Gathering & Tour Rekreasi Batu 2D1N',
        'category': 'WISATA & FAMILY GATHERING',
        'subtitle': 'Paket Inap Hotel Bintang 3 Batu, Petik Apel, Museum Angkut & Fun Games',
        'price': 650000,
        'venue': 'Kota Wisata Batu (Hotel Bintang 3 + Destinasi Hit)',
        'capacity': '30 - 500+ Pax',
        'duration': '2 Days 1 Night',
        'description': 'Paket liburan kebersamaan keluarga dan karyawan dengan mengunjungi destinasi unggulan Kota Batu: Wisata Petik Apel Mandiri, Museum Angkut, Coban Rondo, diselingi program Fun Gathering Ceria.',
        'gallery': {
            'main_img': '../assets/img/wisatawan_kebun_teh_outboundindonesia.webp',
            'main_title': 'Tour Kebun & Rekreasi Batu',
            'thumbs': [
                ('../assets/img/hotel_mewah_eksterior_outboundindonesia.webp', 'Hotel Resort'),
                ('../assets/img/restoran_interior_lembah_outboundindonesia.webp', 'Kuliner Lembah'),
                ('../assets/img/pusat_oleh_oleh_outboundindonesia.webp', 'Pusat Oleh-Oleh')
            ]
        },
        'includes': [
            'Menginap 1 Malam di Hotel Bintang 3 Batu (Twin Share)',
            'Tiket Masuk Wisata Petik Apel Kebun Kota Batu',
            'Tiket Masuk Museum Angkut / Jatim Park',
            'Program Fun Gathering & Game Rekreasi Keluarga',
            '4x Makan Prasmanan Khas Jawa Timur & 1x Snack',
            'Bus Pariwisata AC Executive / HiAce Luxury',
            'Tour Leader Profesional & Banner Acara Custom'
        ],
        'rundown': [
            ('Hari 1 - 09.00', 'Penjemputan & Wisata Petik Apel', 'Penjemputan rombongan, langsung menuju kebun apel Batu.'),
            ('Hari 1 - 12.00', 'Makan Siang Prasmanan & Check-in', 'Makan siang kuliner Batu & proses check-in hotel.'),
            ('Hari 1 - 15.00', 'Wisata Museum Angkut', 'Eksplorasi zona angkutan dunia dan pertunjukan spektakuler.'),
            ('Hari 1 - 19.00', 'Gala Dinner Gathering', 'Makan malam kebersamaan, hiburan musik & ramah tamah.'),
            ('Hari 2 - 08.00', 'Fun Games Gathering di Taman', 'Permainan keakraban ringan seluruh keluarga.'),
            ('Hari 2 - 12.00', 'Belanja Oleh-oleh & Kepulangan', 'Pusat oleh-oleh khas Batu dan pengantaran pulang.')
        ],
        'wa_msg': 'Halo Outbound Jatim, saya ingin pesan Paket Gathering Batu 2D1N (Rp 650.000/pax)'
    },
    {
        'filename': 'detail-paket-bromo-sunrise-culture.html',
        'folder': 'wisata',
        'title': 'Wisata Midnight Jeep Bromo & Sunrise Gathering',
        'category': 'WISATA NATURE & CULTURE',
        'subtitle': 'Petualangan Bromo Midnight, Sunrise Penanjakan 1 & Makan Pagi Bromo',
        'price': 450000,
        'venue': 'Bromo Tengger & Tosari Pasuruan / Probolinggo',
        'capacity': '20 - 300 Pax',
        'duration': 'Midnight Tour (12 Jam)',
        'description': 'Paket perjalanan wisata Bromo malam hari untuk menyaksikan fenomena keindahan matahari terbit Bromo yang mendunia, keunikan budaya suku Tengger, dan keajaiban pasir berbisik.',
        'gallery': {
            'main_img': '../assets/img/tenda_camping_matahari_terbit_outboundindonesia.webp',
            'main_title': 'Sunrise Penanjakan & Jeep Bromo',
            'thumbs': [
                ('../assets/img/background.webp', 'Lautan Pasir'),
                ('../assets/img/hotel_mewah_eksterior_outboundindonesia.webp', 'Resto Transit'),
                ('../assets/img/barbekyu_sate_daging_outboundindonesia.webp', 'Sarapan Warm')
            ]
        },
        'includes': [
            'Sewa Jeep 4x4 Toyota Hardtop Selama di Bromo',
            'Tiket Masuk Kawasan TNBTS Bromo Lengkap',
            'Pendampingan Guide Lokal Bromo',
            'Sarapan Pagi Buffet Hangat di Bromo Resto',
            'Masker Pelindung & Air Mineral',
            'Banner Foto Rombongan Custom',
            'Dokumentasi Foto Selama di Spot Bromo'
        ],
        'rundown': [
            ('23.30 - 00.30', 'Meeting Point & Registrasi', 'Kumpul di titik temu Malang / Pasuruan / Probolinggo.'),
            ('01.00 - 03.30', 'Perjalanan Jeep ke Penanjakan 1', 'Perjalanan seru membelah kegelapan lautan pasir.'),
            ('03.30 - 06.00', 'Golden Sunrise Bromo Panorama', 'Menikmati keindahan sunrise dan pemandangan Gunung Batok & Semeru.'),
            ('06.30 - 09.00', 'Trekking Kawah & Bukit Teletubbies', 'Spot foto Pasir Berbisik, Savana, dan Kawah Bromo.'),
            ('09.30 - 11.30', 'Sarapan Resto & Pengantaran Pulang', 'Makan pagi hangat dan kembali ke meeting point.')
        ],
        'wa_msg': 'Halo Outbound Jatim, saya ingin booking Paket Wisata Bromo Midnight (Rp 450.000/pax)'
    },
    {
        'filename': 'detail-paket-banyuwangi-ijen-baluran.html',
        'folder': 'wisata',
        'title': 'Exotic East Java: Ijen Blue Fire & Baluran 3D2N',
        'category': 'EKSOTIS BANYUWANGI',
        'subtitle': 'Midnight Trekking Kawah Ijen Blue Fire, Savana Bekol Baluran & Hutan Djawatan',
        'price': 1250000,
        'venue': 'Banyuwangi (Kawah Ijen, Baluran, De Djawatan)',
        'capacity': '15 - 150 Pax',
        'duration': '3 Days 2 Nights',
        'description': 'Eksplorasi mahakarya alam Jawa Timur paling timur: menyaksikan keajaiban dunia Blue Fire Kawah Ijen, serasa di Afrika pada Savana Bekol Baluran, dan suasana magis Lord of the Rings Hutan De Djawatan.',
        'gallery': {
            'main_img': '../assets/img/wisatawan_kebun_teh_outboundindonesia.webp',
            'main_title': 'Wisata Eksotis Ijen & Baluran Banyuwangi',
            'thumbs': [
                ('../assets/img/hotel_mewah_eksterior_outboundindonesia.webp', 'Hotel Resort'),
                ('../assets/img/restoran_interior_lembah_outboundindonesia.webp', 'Kuliner khas'),
                ('../assets/img/barbekyu_sate_daging_outboundindonesia.webp', 'Seafood Beach BBQ')
            ]
        },
        'includes': [
            'Penginapan Hotel Bintang 3 / Resort Banyuwangi 2 Malam',
            'Transportasi Bus AC Executive / HiAce Commuter',
            'Masker Gas Respirator SNI untuk Trekking Ijen',
            'Local Guide Kawah Ijen & Taman Nasional Baluran',
            'Tiket Masuk Seluruh Destinasi Wisata Banyuwangi',
            'Makan 7x Prasmanan Kuliner Khas Banyuwangi (Nasi Tempong)',
            'Air Mineral, Snack & Asuransi Wisata'
        ],
        'rundown': [
            ('Hari 1', 'Kedatangan & De Djawatan Benculuk', 'Tiba di Banyuwangi, foto di De Djawatan & Sunset Pantai Boom.'),
            ('Hari 2 - 00.30', 'Midnight Trekking Blue Fire Ijen', 'Perjalanan ke Pos Paltuding & mendaki ke Kawah Ijen.'),
            ('Hari 2 - 08.00', 'Kembali ke Hotel & Istirahat', 'Sarapan pagi dan istirahat santai di resort.'),
            ('Hari 2 - 14.00', 'Wisata Savana Bekol Baluran', 'Jelajah Savana Bekol, Pantai Bama & hutan mangrove Baluran.'),
            ('Hari 3', 'Oleh-oleh Khas Banyuwangi & Transfer Out', 'Pusat oleh-oleh khas Banyuwangi & pengantaran ke Bandara/Stasiun.')
        ],
        'wa_msg': 'Halo Outbound Jatim, saya ingin konsultasi Paket Banyuwangi Ijen Baluran (Rp 1.250.000/pax)'
    },
    {
        'filename': 'detail-paket-custom-gathering.html',
        'folder': 'wisata',
        'title': 'Custom Event, Gathering & Conference Package',
        'category': 'CUSTOM EVENT CORPORATE',
        'subtitle': 'Rancangan Acara Sesuai Anggaran, Tema Khusus, Venue Hotel / Resort & Artis',
        'price': 285000,
        'venue': 'Batu Malang / Trawas / Pacet / Bromo / Banyuwangi',
        'capacity': '30 - 2000+ Pax',
        'duration': 'Flexible (1 - 4 Days)',
        'description': 'Kami siap merancang acara khusus sesuai kebutuhan instansi/perusahaan Anda. Mulai dari konsep Gala Dinner, Raker/Rapat Kerja, Awarding Night, Panggung Hiburan Artis, hingga Outbound Tematik.',
        'gallery': {
            'main_img': '../assets/img/gathering_perusahaan_lapangan_outboundindonesia.webp',
            'main_title': 'Custom Corporate Event & Gathering',
            'thumbs': [
                ('../assets/img/tenda_camping_matahari_terbit_outboundindonesia.webp', 'Nature Camp'),
                ('../assets/img/kolam_air_panas_pegunungan_outboundindonesia.webp', 'Hot Spring Resort'),
                ('../assets/img/barbekyu_sate_daging_outboundindonesia.webp', 'Gala Dinner')
            ]
        },
        'includes': [
            'Perencanaan Konsep Acara Custom & Creative Proposal',
            'Pemilihan Venue Hotel / Resort / Outdoor Arena',
            'Lighting Stage, Panggung, & Sound System Rigging',
            'MC Event Profesional, Artis / Entertainment Support',
            'Vendor Catering Custom (Barbeque, Seafood, Traditional)',
            'Tim Production Crew & Event Director Berpengalaman',
            'Dokumentasi Drone 4K & Multicam Video Production'
        ],
        'rundown': [
            ('Fleksibel', 'Konsultasi Konsep & Rundown', 'Diskusi kebutuhan tema, durasi, target acara, dan alokasi budget.'),
            ('Fleksibel', 'Survey Lokasi & Presentasi RAB', 'Tim kami menyajikan pilihan venue terbaik dan simulasi biaya transparan.'),
            ('Fleksibel', 'Eksekusi Event & Pendampingan', 'Tim EO Outbound Jatim mengeksekusi seluruh kelancaran acara dari awal hingga penutupan.')
        ],
        'wa_msg': 'Halo Outbound Jatim, saya ingin diskusi penawaran Custom Gathering Event'
    }
]

base_dir = r'c:\outboundjatim'

# 1. Generate 12 detail package files inside their target folders
for pkg in packages_data:
    target_folder = os.path.join(base_dir, pkg['folder'])
    os.makedirs(target_folder, exist_ok=True)
    
    target_filepath = os.path.join(target_folder, pkg['filename'])
    root_filepath = os.path.join(base_dir, pkg['filename'])

    calc_price_str = f"{pkg['price']:,}".replace(',', '.')
    
    inc_html = ""
    for inc in pkg['includes']:
        inc_html += f'''              <div class="flex items-start gap-2">
                <span class="material-symbols-outlined text-secondary text-[18px] shrink-0">check_circle</span>
                <span>{inc}</span>
              </div>\n'''
              
    rundown_html = ""
    for time_slot, title, desc in pkg['rundown']:
        rundown_html += f'''              <div class="flex gap-4 p-3 rounded-xl bg-surface-container-low border-l-4 border-primary-container">
                <span class="font-headline font-bold text-primary-container w-28 shrink-0">{time_slot}</span>
                <div>
                  <h4 class="font-bold text-on-surface">{title}</h4>
                  <p class="text-on-surface-variant text-xs">{desc}</p>
                </div>
              </div>\n'''

    # Disclaimer Note required by user:
    disclaimer_text = "*Harga tertera masih bersifat estimasi dan tidak mengikat. Silakan hubungi admin via WhatsApp untuk memastikan harga pasti."
    
    disclaimer_box_html = f'''
              <div class="p-3 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-800 dark:text-amber-300 text-xs font-semibold leading-relaxed mt-2">
                <span>{disclaimer_text}</span>
              </div>'''

    disclaimer_calc_html = f'''
            <div class="mt-3 p-3 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-900 dark:text-amber-200 text-[11px] font-semibold leading-relaxed text-center">
              <span>{disclaimer_text}</span>
            </div>'''

    gallery = pkg.get('gallery', None)
    photo_gallery_html = ""
    if gallery:
        main_img = gallery['main_img']
        main_title = gallery['main_title']
        thumbs = gallery['thumbs']
        
        thumbs_html = ""
        for t_img, t_lbl in thumbs:
            thumbs_html += f'''              <div class="h-28 rounded-xl overflow-hidden bg-surface-container border border-outline-variant/30 group relative shadow-xs">
                <img src="{t_img}" alt="{t_lbl}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-300"/>
                <span class="absolute bottom-1 left-1 right-1 bg-black/50 text-white text-[10px] text-center rounded py-0.5 font-semibold backdrop-blur-sm">{t_lbl}</span>
              </div>\n'''
              
        photo_gallery_html = f'''          <!-- CARD GAMBAR / PHOTO GALLERY -->
          <div class="space-y-4">
            <div class="w-full h-80 sm:h-96 rounded-2xl overflow-hidden bg-surface-container-high border border-outline-variant/40 relative shadow-lg group">
              <img src="{main_img}" alt="{pkg['title']}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"/>
              <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"></div>
              <span class="absolute bottom-4 left-4 text-white text-xs sm:text-sm font-headline font-bold bg-primary-container/80 px-3 py-1 rounded-full backdrop-blur-sm">{main_title}</span>
            </div>
            
            <div class="grid grid-cols-3 gap-4">
{thumbs_html}            </div>
          </div>'''

    content = f'''<!DOCTYPE html>
<html class="scroll-smooth" lang="id">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>Detail {pkg['title']} - Outbound Jatim</title>
  <meta name="description" content="Detail paket {pkg['title']} di {pkg['venue']}. Lengkap dengan fasilitas, rundown kegiatan, simulasi biaya, dan pemesanan proposal resmi."/>
  
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
</head>
<body class="bg-background font-body text-on-surface antialiased flex flex-col min-h-screen">

{topbar_nav_header_subfolder}

  <!-- MAIN CONTENT CONTAINER -->
  <main class="w-full pt-32 sm:pt-28 flex-1">
    
    <!-- Top Breadcrumb Section -->
    <section class="w-full bg-surface-container-low py-4 px-4 sm:px-8 border-b border-outline-variant/30">
      <div class="max-w-7xl mx-auto flex items-center justify-between text-xs sm:text-sm text-on-surface-variant">
        <nav aria-label="Breadcrumb" class="flex items-center gap-2">
          <a class="hover:text-primary-container transition-colors" href="../index.html">Beranda</a>
          <span class="material-symbols-outlined text-[14px]">chevron_right</span>
          <a class="hover:text-primary-container transition-colors" href="../paket.html">Katalog Paket</a>
          <span class="material-symbols-outlined text-[14px]">chevron_right</span>
          <span class="text-primary-container font-bold">Detail {pkg['title']}</span>
        </nav>
        <span class="hidden sm:inline-block font-headline text-xs text-secondary uppercase font-bold">Respon Cepat WA 24/7</span>
      </div>
    </section>

    <!-- Main Content Area: Left Details + Right Simulator Calculator -->
    <section class="w-full py-12 px-4 sm:px-8 bg-surface">
      <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        <!-- Left 7 Columns: Package Info & Itinerary -->
        <div class="lg:col-span-7 space-y-8">
          
          <!-- Package Header Card -->
          <div class="bg-surface-container-lowest p-6 rounded-2xl shadow-sm border border-outline-variant/40 space-y-4">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-secondary-container/30 text-on-secondary-container font-headline text-xs font-bold uppercase">
              <span class="material-symbols-outlined text-[16px]">verified</span>
              <span>{pkg['category']}</span>
            </div>
            
            <h1 class="font-headline text-2xl sm:text-3xl font-extrabold text-primary-container leading-tight">
              {pkg['title']}
            </h1>
            <p class="text-xs sm:text-sm font-semibold text-secondary">{pkg['subtitle']}</p>
            
            <div class="flex flex-wrap items-center gap-4 text-xs font-semibold text-on-surface-variant pt-2 border-t border-surface-container">
              <span class="flex items-center gap-1.5"><span class="material-symbols-outlined text-secondary text-[18px]">location_on</span> Venue: {pkg['venue']}</span>
              <span class="flex items-center gap-1.5"><span class="material-symbols-outlined text-secondary text-[18px]">group</span> Kapasitas: {pkg['capacity']}</span>
              <span class="flex items-center gap-1.5"><span class="material-symbols-outlined text-secondary text-[18px]">timer</span> Durasi: {pkg['duration']}</span>
            </div>
            
            <p class="text-sm text-on-surface-variant leading-relaxed pt-2">
              {pkg['description']}
            </p>

            {disclaimer_box_html}
          </div>

          {photo_gallery_html}

          <!-- Fast Highlights Checklist -->
          <div class="bg-surface-container-low p-6 rounded-2xl border border-outline-variant/40 space-y-4">
            <h3 class="font-headline text-base font-bold text-primary-container">Fasilitas &amp; Inklusi Paket yang Termasuk:</h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm text-on-surface">
{inc_html}
            </div>
          </div>

          <!-- Itinerary Breakdown -->
          <div class="bg-surface-container-lowest p-6 rounded-2xl shadow-sm border border-outline-variant/40 space-y-4">
            <h3 class="font-headline text-lg font-bold text-primary-container">Estimasi Rundown &amp; Itinerary Kegiatan:</h3>
            
            <div class="space-y-4 text-xs sm:text-sm">
{rundown_html}
            </div>
          </div>

        </div>

        <!-- Right 5 Columns: Interactive Price & Quote Calculator Form -->
        <div class="lg:col-span-5 sticky top-28 space-y-6">
          
          <div class="bg-surface-container-lowest p-6 rounded-2xl shadow-lg border-2 border-secondary-container/60 space-y-5">
            <div class="flex items-center justify-between pb-3 border-b border-surface-container">
              <div>
                <span class="font-headline text-[10px] text-secondary font-bold uppercase tracking-wider block">ESTIMASI SIMULASI BIAYA</span>
                <h3 class="font-headline text-lg font-bold text-primary-container">Hitung Proposal {pkg['title']}</h3>
              </div>
              <span class="material-symbols-outlined text-secondary text-[28px]">calculate</span>
            </div>

            <form class="space-y-4 text-xs sm:text-sm" onsubmit="event.preventDefault(); sendWhatsAppProposal();">
              <div>
                <label class="font-headline font-bold text-on-surface block mb-1">Nama Perusahaan / Instansi</label>
                <input required class="w-full bg-surface-container-low rounded-xl px-4 py-2.5 text-on-surface border border-outline-variant/40" id="calcCompany" placeholder="Contoh: PT. Bank Central Asia / Instansi" type="text">
              </div>

              <div>
                <label class="font-headline font-bold text-on-surface block mb-1">Jumlah Peserta (Pax)</label>
                <input required min="5" value="50" oninput="calculateTotal()" class="w-full bg-surface-container-low rounded-xl px-4 py-2.5 text-on-surface border border-outline-variant/40 font-headline font-bold text-primary-container" id="calcPax" type="number">
              </div>

              <div>
                <label class="font-headline font-bold text-on-surface block mb-1">Tarif Dasar Per Pax</label>
                <div class="w-full bg-surface-container-low rounded-xl px-4 py-2.5 text-primary-container font-headline font-bold border border-outline-variant/40">
                  Rp {calc_price_str} / pax
                </div>
              </div>

              <div class="p-4 rounded-xl bg-surface-container-low space-y-2 border border-surface-container">
                <div class="flex justify-between text-xs text-on-surface-variant">
                  <span>Tarif per Pax:</span>
                  <span class="font-bold text-on-surface" id="displayUnitPrice">Rp {calc_price_str}</span>
                </div>
                <div class="flex justify-between text-xs text-on-surface-variant">
                  <span>Jumlah Peserta:</span>
                  <span class="font-bold text-on-surface" id="displayPaxCount">50 Pax</span>
                </div>
                <div class="pt-2 border-t border-outline-variant/40 flex justify-between items-baseline">
                  <span class="font-headline font-bold text-primary-container text-xs sm:text-sm">ESTIMASI TOTAL:</span>
                  <span class="font-headline font-extrabold text-xl text-primary-container" id="displayTotalPrice">Rp 0</span>
                </div>
              </div>

              <button class="w-full py-3.5 px-6 rounded-full bg-emerald-600 text-white font-headline text-sm font-bold shadow-md hover:bg-emerald-500 transition-all flex items-center justify-center gap-2" type="submit">
                <span class="material-symbols-outlined text-[20px]">send</span>
                <span>Booking via WhatsApp Formal</span>
              </button>
            </form>

            <div class="text-[11px] text-on-surface-variant text-center pt-2">
              <span class="flex items-center justify-center gap-1"><span class="material-symbols-outlined text-[14px] text-emerald-600">lock</span> Proposal PDF resmi &amp; penawaran khusus dikirim ke WhatsApp Anda.</span>
            </div>

            {disclaimer_calc_html}
          </div>

          <div class="bg-surface-container-low p-5 rounded-2xl border border-outline-variant/30 text-center space-y-3">
            <div class="font-headline text-xs font-bold text-primary-container uppercase">Punya Permintaan Khusus / Custom?</div>
            <p class="text-xs text-on-surface-variant">Butuh penyesuaian rundown, tambahan hiburan, artis, atau pilihan lokasi venue lain?</p>
            <a href="https://wa.me/6282211221909?text={pkg['wa_msg']}" target="_blank" class="inline-flex items-center justify-center gap-2 px-5 py-2.5 rounded-full bg-primary-container text-on-primary font-headline text-xs font-bold hover:bg-primary transition-all shadow-sm w-full">
              <span class="material-symbols-outlined text-[16px]">chat</span>
              <span>Diskusi Custom via WA</span>
            </a>
          </div>

        </div>
      </div>
    </section>

  </main>

{footer_code_subfolder}

  <script>
    const unitPrice = {pkg['price']};
    
    function calculateTotal() {{
      const paxInput = document.getElementById('calcPax');
      let pax = parseInt(paxInput.value) || 0;
      if (pax < 1) pax = 1;
      
      const total = pax * unitPrice;
      
      document.getElementById('displayPaxCount').textContent = pax + ' Pax';
      document.getElementById('displayTotalPrice').textContent = 'Rp ' + total.toLocaleString('id-ID');
    }}

    function sendWhatsAppProposal() {{
      const company = document.getElementById('calcCompany').value || 'Instansi';
      const pax = document.getElementById('calcPax').value || '50';
      const total = (parseInt(pax) * unitPrice).toLocaleString('id-ID');
      
      const text = `Halo Outbound Jatim, saya ingin mengajukan proposal resmi untuk:\\n` +
                   `- Nama Paket: {pkg['title']}\\n` +
                   `- Perusahaan/Instansi: ${{company}}\\n` +
                   `- Estimasi Peserta: ${{pax}} Pax\\n` +
                   `- Estimasi Total Biaya: Rp ${{total}}\\n\\n` +
                   `Mohon dikirimkan proposal penawaran resmi dalam format PDF. Terima kasih.`;
                   
      const url = `https://wa.me/6282211221909?text=${{encodeURIComponent(text)}}`;
      window.open(url, '_blank');
    }}

    document.addEventListener('DOMContentLoaded', calculateTotal);
  </script>
</body>
</html>'''

    with open(target_filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved: {target_filepath}")
    
    # Remove duplicate file from root if it exists
    if os.path.exists(root_filepath):
        os.remove(root_filepath)
        print(f"Removed old root file: {root_filepath}")


# 2. Update catalog files with new detail page links
catalog_files = [
    ('index.html', 'root'),
    ('paket.html', 'root'),
    ('paket-adventure.html', 'root'),
    ('paket-gathering.html', 'root'),
    ('outbound/index.html', 'outbound'),
    ('wisata/index.html', 'wisata')
]

for file_rel, context in catalog_files:
    full_path = os.path.join(base_dir, file_rel.replace('/', os.sep))
    if not os.path.exists(full_path):
        continue
        
    with open(full_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace links for outbound packages
    for filename in outbound_packages:
        if context == 'root':
            target_href = f'outbound/{filename}'
        elif context == 'outbound':
            target_href = filename
        elif context == 'wisata':
            target_href = f'../outbound/{filename}'
            
        # Match any previous variation of href
        html = re.sub(r'href=["\'](?:\.\.\/|\.\.\/outbound\/|\.\.\/wisata\/|outbound\/|wisata\/)?' + re.escape(filename) + r'["\']',
                      f'href="{target_href}"', html)

    # Replace links for wisata packages
    for filename in wisata_packages:
        if context == 'root':
            target_href = f'wisata/{filename}'
        elif context == 'wisata':
            target_href = filename
        elif context == 'outbound':
            target_href = f'../wisata/{filename}'
            
        html = re.sub(r'href=["\'](?:\.\.\/|\.\.\/outbound\/|\.\.\/wisata\/|outbound\/|wisata\/)?' + re.escape(filename) + r'["\']',
                      f'href="{target_href}"', html)

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated catalog links in: {full_path}")

print("All package detail files successfully moved, disclaimer added, and catalog links updated!")
