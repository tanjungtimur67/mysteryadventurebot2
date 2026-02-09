import time
import random
from enum import Enum

class BusKoridor(Enum):
    """Enum untuk 14 koridor Transjakarta"""
    K1 = ("🔵 Koridor 1", "Blok M - Kota", ["Blok M", "Senayan", "Istora", "Sudirman", "Kota"])
    K2 = ("🟢 Koridor 2", "Monas - Pulo Gadung", ["Monas", "Cikini", "Pasar Baru", "Pulogadung"])
    K3 = ("🟠 Koridor 3", "Monas - Kalideres", ["Monas", "Kwitang", "Pasar Baru", "Harmoni", "Kalideres"])
    K4 = ("🟡 Koridor 4", "Pulo Gadung - Galunggung", ["Pulogadung", "Sunter", "Galunggung"])
    K5 = ("🔴 Koridor 5", "Kampung Melayu - Ancol", ["Kampung Melayu", "Senen", "Penjaringan", "Ancol"])
    K6 = ("🟣 Koridor 6", "Ragunan - Galunggung", ["Ragunan", "Fatmawati", "Pancoran", "Galunggung"])
    K7 = ("🟤 Koridor 7", "Kampung Melayu - Kampung Rambutan", ["Kampung Melayu", "Pancoran", "Kampung Rambutan"])
    K8 = ("🔵 Koridor 8", "Lebak Bulus - Pasar Baru", ["Lebak Bulus", "Fatmawati", "Blok M", "Sudirman", "Pasar Baru"])
    K9 = ("🟢 Koridor 9", "Pluit - Pinang Ranti", ["Pluit", "Penjaringan", "Tanjung Priok", "Pinang Ranti"])
    K10 = ("🟠 Koridor 10", "PGC - Tanjung Priok", ["PGC", "Cakung", "Ancol", "Tanjung Priok"])
    K11 = ("🟡 Koridor 11", "Kampung Melayu - Pulo Gebang", ["Kampung Melayu", "Pulo Gebang"])
    K12 = ("🔴 Koridor 12", "Pluit - Tanjung Priok", ["Pluit", "Kota", "Tanjung Priok"])
    K13 = ("🟣 Koridor 13", "Puri Beta - Tegal Mampang", ["Puri Beta", "Blok M", "Pancoran", "Tegal Mampang"])
    K14 = ("🟤 Koridor 14", "JIS - Senen", ["Jakarta Int. Stadium", "Blok M", "Senen"])

class Lokasi(Enum):
    """Enum untuk lokasi umum dalam game"""
    STASIUN = "Stasiun Sentral"
    JALAN_UTAMA = "Jalan Utama"
    TERMINAL = "Terminal Pusat"
    PASAR = "Pasar Tradisional"
    TAMAN = "Taman Hiburan"
    PABRIK = "Pabrik Suku Cadang"
    BENGKEL = "Bengkel Hitam"
    KANTOR_PUSAT = "Kantor Pusat Transjakarta"
    ISTANA_JAHAT = "Istana Raja Jahat Bus"

class Sidekick(Enum):
    """Enum untuk karakter sidekick dari berbagai koridor"""
    # Mapping: (nama_sidekick, deskripsi, koridor_asal, emoji)
    SOPIR_K4 = ("👨 Sopir dari K4", "Master navigasi Pulo Gadung - Galunggung", "K4", "🟡")
    SOPIR_K7 = ("👨 Sopir dari K7", "Ahli rute Kampung Melayu - Kampung Rambutan", "K7", "🟤")
    GADIS_K2 = ("👩 Gadis dari K2", "Expert customer service Monas - Pulo Gadung", "K2", "🟢")
    GADIS_K5 = ("👩 Gadis dari K5", "Profesional Kampung Melayu - Ancol", "K5", "🔴")
    MEKANIK_K9 = ("🔧 Mekanik dari K9", "Ahli perbaikan mesin Pluit - Pinang Ranti", "K9", "🟢")
    MEKANIK_K12 = ("🔧 Mekanik dari K12", "Teknisi berpengalaman Pluit - Tanjung Priok", "K12", "🔴")
    MUSISI_K3 = ("🎵 Musisi dari K3", "Penghibur rute Monas - Kalideres", "K3", "🟠")
    MUSISI_K13 = ("🎵 Musisi dari K13", "Penyanyi legendaris Puri Beta - Tegal Mampang", "K13", "🟣")

class Karakter:
    """Kelas untuk menyimpan data karakter pemain"""
    def __init__(self, nama, koridor):
        self.nama = nama
        self.koridor = koridor
        self.emoji_koridor = koridor.value[0]
        self.desc_koridor = koridor.value[1]
        self.halte_koridor = koridor.value[2]
        self.hp = 100
        self.max_hp = 100
        self.energi = 100
        self.max_energi = 100
        self.uang = 5000
        self.level = 1
        self.exp = 0
        self.exp_untuk_level_up = 100
        self.misi_selesai = 0
        self.misi_dikunci = set()
        self.inventory = []
        self.sidekick = None
        self.stats = {
            "kecepatan": 50,
            "ketahanan": 50,
            "kerajinan": 50,
            "kecerdasan": 50
        }

    def tampilkan_status(self):
        """Menampilkan status karakter"""
        print("\n" + "="*60)
        print(f"🚌 STATUS {self.nama.upper()}")
        print("="*60)
        print(f"Koridor: {self.emoji_koridor} {self.desc_koridor}")
        print(f"Rute: {' → '.join(self.halte_koridor)}")
        print(f"Level: {self.level}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Energi: {self.energi}/{self.max_energi}")
        print(f"Uang: Rp{self.uang:,}")
        print(f"Misi Selesai: {self.misi_selesai}/22")
        print(f"EXP: {self.exp}/{self.exp_untuk_level_up}")
        
        if self.sidekick:
            print(f"\n👥 Sidekick: {self.sidekick.value[0]}")
            print(f"   Deskripsi: {self.sidekick.value[1]}")
            print(f"   Dari Koridor: {self.sidekick.value[2]}")
        
        print("\nStats:")
        for stat, nilai in self.stats.items():
            print(f"  {stat.capitalize()}: {nilai}")
        if self.inventory:
            print(f"\nInventory: {', '.join(self.inventory)}")
        print("="*60 + "\n")

class Game:
    """Kelas utama untuk menjalankan game dengan loop permainan"""
    def __init__(self):
        self.karakter = None
        self.lokasi_sekarang = Lokasi.STASIUN
        self.misi_aktif = None
        self.dialog_index = 0
        self.game_aktif = True

    def dialog(self, pembicara, teks, delay=0.02):
        """Menampilkan dialog dengan delay untuk efek typing"""
        print(f"\n💬 {pembicara}: ", end="", flush=True)
        for char in teks:
            print(char, end="", flush=True)
            time.sleep(delay)
        print("\n")

    def pilihan(self, opsi_dict):
        """Menampilkan pilihan dan mendapatkan input dari pemain"""
        print("Pilihan:")
        for key, value in opsi_dict.items():
            print(f"  {key}. {value}")
        while True:
            try:
                pilihan = input("\nPilihan Anda (masukkan nomor): ").strip()
                if pilihan in opsi_dict:
                    return pilihan
                else:
                    print("❌ Pilihan tidak valid!")
            except:
                print("❌ Input tidak valid!")

    def intro_game(self):
        """Pengenalan game"""
        print("\n" + "🎮"*25)
        print("\n        🚌 PETUALANGAN BUS TRANSJAKARTA 🚌")
        print("              Misi Menyelamatkan Dunia")
        print("\n" + "🎮"*25 + "\n")
        
        self.dialog("Narator", "Selamat datang di dunia Transjakarta yang penuh misteri...")
        self.dialog("Narator", "Sebuah kekuatan jahat telah menguasai jaringan transportasi kita.")
        self.dialog("Narator", "Hanya satu bus yang dapat menyelamatkan kota ini dari kehancuran!")
        time.sleep(1)

    def pilih_karakter(self):
        """Pemilihan karakter bus berdasarkan koridor"""
        print("\n📋 PILIH KORIDOR BUS ANDA (14 Pilihan):")
        print("="*70)
        
        koridor_options = {
            "1": BusKoridor.K1,
            "2": BusKoridor.K2,
            "3": BusKoridor.K3,
            "4": BusKoridor.K4,
            "5": BusKoridor.K5,
            "6": BusKoridor.K6,
            "7": BusKoridor.K7,
            "8": BusKoridor.K8,
            "9": BusKoridor.K9,
            "10": BusKoridor.K10,
            "11": BusKoridor.K11,
            "12": BusKoridor.K12,
            "13": BusKoridor.K13,
            "14": BusKoridor.K14,
        }
        
        for key, koridor in koridor_options.items():
            desc = koridor.value
            print(f"{key:>2s}. {desc[0]} - {desc[1]}")
        
        pilihan_bus = self.pilihan(koridor_options)
        koridor_terpilih = koridor_options[pilihan_bus]
        
        print(f"\n✅ Anda memilih: {koridor_terpilih.value[0]} - {koridor_terpilih.value[1]}")
        
        nama = input("\nSiapa nama bus Anda? ").strip()
        if not nama:
            nama = "Bus Pemberani"
        
        self.karakter = Karakter(nama, koridor_terpilih)
        self.sesuaikan_stats_karakter(koridor_terpilih)
        
        self.dialog(nama, f"Saya adalah bus dari {koridor_terpilih.value[1]}! Siap untuk menyelamatkan kota!")
        time.sleep(1)

    def sesuaikan_stats_karakter(self, koridor):
        """Sesuaikan stats karakter berdasarkan koridor"""
        stats_base = {
            BusKoridor.K1: {"kecepatan": 75, "ketahanan": 60},
            BusKoridor.K2: {"kecepatan": 70, "ketahanan": 65},
            BusKoridor.K3: {"kecepatan": 65, "ketahanan": 70},
            BusKoridor.K4: {"kecepatan": 60, "ketahanan": 75},
            BusKoridor.K5: {"kecepatan": 72, "ketahanan": 62},
            BusKoridor.K6: {"kecepatan": 68, "ketahanan": 68},
            BusKoridor.K7: {"kecepatan": 70, "ketahanan": 65},
            BusKoridor.K8: {"kecepatan": 65, "ketahanan": 70},
            BusKoridor.K9: {"kecepatan": 72, "ketahanan": 62},
            BusKoridor.K10: {"kecepatan": 68, "ketahanan": 68},
            BusKoridor.K11: {"kecepatan": 70, "ketahanan": 65},
            BusKoridor.K12: {"kecepatan": 75, "ketahanan": 60},
            BusKoridor.K13: {"kecepatan": 65, "ketahanan": 72},
            BusKoridor.K14: {"kecepatan": 70, "ketahanan": 68},
        }
        
        if koridor in stats_base:
            for stat, nilai in stats_base[koridor].items():
                self.karakter.stats[stat] = nilai
        else:
            for stat in self.karakter.stats:
                self.karakter.stats[stat] = 65

    def tampilkan_map(self):
        """Menampilkan peta game yang disesuaikan dengan koridor"""
        print("\n" + "🗺️ "*30)
        print("\n🚌 PETA PETUALANGAN - " + self.karakter.emoji_koridor + " " + self.karakter.desc_koridor)
        print("="*70)
        
        # Map dinamis berdasarkan koridor
        halte_peta = " → ".join(self.karakter.halte_koridor)
        
        peta = f"""
        ┌─────────────────────────────────────────────────────────┐
        │  RUTE ANDA: {halte_peta:<45} │
        ├─────────────────────────────────────────────────────────┤
        │                                                         │
        │  🏛️ KANTOR PUSAT ────────────── 🏭 PABRIK            │
        │      │  Koordinasi                  │                 │
        │      │  Misi Harian                 │                 │
        │      │                              │                 │
        │  🛠️ BENGKEL HITAM ──────────── 🎪 TAMAN HIBURAN      │
        │      │ Perbaikan                    │                 │
        │      │ Upgrade                      │                 │
        │      │        🌆 JALAN UTAMA       │                 │
        │      │             │                │                 │
        │  🚉 STASIUN ANDA ──────── 🏪 PASAR TRADISIONAL       │
        │  (Titik Awal Rute)              │                 │
        │      │                             │                 │
        │      └─────── 🚐 TERMINAL PUSAT   │                 │
        │                    │                                 │
        │              🌳 HUTAN MISTERI                        │
        │                    │                                 │
        │             👑 ISTANA RAJA JAHAT BUS                │
        │                                                     │
        └─────────────────────────────────────────────────────┘
        
        Lokasi Saat Ini: {self.lokasi_sekarang.value}
        """
        
        print(peta)
        print("="*70)
        print("Ketik 'peta' untuk melihat peta, 'status' untuk lihat status,")
        print("'jelajahi' untuk melihat lokasi yang tersedia, 'inventori' untuk lihat item.")
        print("="*70 + "\n")

    def main_menu(self):
        """Menu utama game dengan loop"""
        while self.game_aktif and self.karakter.misi_selesai < 21:
            print("\n" + "="*60)
            print(f"📍 Lokasi: {self.lokasi_sekarang.value}")
            print(f"🚌 Bus: {self.karakter.emoji_koridor} {self.karakter.desc_koridor}")
            print(f"Misi Selesai: {self.karakter.misi_selesai}/22")
            if self.karakter.sidekick:
                print(f"👥 Sidekick: {self.karakter.sidekick.value[0]}")
            print("="*60)
            print("\n📋 OPSI UTAMA:")
            print("1. Jelajahi lokasi")
            print("2. Lihat status")
            print("3. Lihat peta")
            print("4. Lihat inventori")
            print("5. Istirahat (isi energi)")
            print("6. Keluar game")
            
            pilihan = input("\nPilihan Anda: ").strip()
            
            if pilihan == "1":
                self.jelajahi_lokasi()
            elif pilihan == "2":
                self.karakter.tampilkan_status()
            elif pilihan == "3":
                self.tampilkan_map()
            elif pilihan == "4":
                self.lihat_inventori()
            elif pilihan == "5":
                self.istirahat()
            elif pilihan == "6":
                self.dialog("Narator", "Terima kasih telah bermain! Sampai jumpa!")
                self.game_aktif = False
            else:
                print("❌ Pilihan tidak valid!")
        
        # Cek jika misi selesai
        if self.game_aktif and self.karakter.misi_selesai >= 21:
            print("\n" + "="*60)
            print("🎉 ANDA TELAH MENYELESAIKAN SEMUA MISI! 🎉")
            print("="*60)

    def jelajahi_lokasi(self):
        """Menu jelajahi lokasi"""
        print("\n" + "="*60)
        print("🚌 LOKASI YANG DAPAT DIJELAJAHI:")
        print("="*60)
        
        lokasi_dict = {
            "1": Lokasi.STASIUN,
            "2": Lokasi.JALAN_UTAMA,
            "3": Lokasi.TERMINAL,
            "4": Lokasi.PASAR,
            "5": Lokasi.TAMAN,
            "6": Lokasi.PABRIK,
            "7": Lokasi.BENGKEL,
            "8": Lokasi.KANTOR_PUSAT,
            "0": None
        }
        
        for key, loc in lokasi_dict.items():
            if loc:
                print(f"{key}. Menuju {loc.value}")
            else:
                print(f"{key}. Kembali ke menu utama")
        
        pilihan = input("\nPilihan Anda: ").strip()
        
        if pilihan in lokasi_dict and lokasi_dict[pilihan]:
            self.lokasi_sekarang = lokasi_dict[pilihan]
            self.ke_lokasi()
        elif pilihan != "0":
            print("❌ Pilihan tidak valid!")

    def ke_lokasi(self):
        """Masuk ke lokasi dan tampilkan aktivitas"""
        self.dialog("Narator", f"Anda sekarang berada di {self.lokasi_sekarang.value}...")
        time.sleep(1)
        
        aktivitas = self.get_aktivitas_lokasi()
        
        print("\n" + "="*60)
        print(f"📍 {self.lokasi_sekarang.value}")
        print("="*60)
        
        if not aktivitas:
            print("Tidak ada aktivitas di lokasi ini saat ini.")
            return
        
        print("\nAktivitas yang tersedia:")
        
        for key, aktiv in aktivitas.items():
            status = " [SELESAI]" if int(aktiv['id'].split("_")[1]) in self.karakter.misi_dikunci else ""
            print(f"{key}. {aktiv['nama']}{status}")
        
        print("0. Kembali")
        
        pilihan = input("\nPilihan Anda: ").strip()
        
        if pilihan in aktivitas:
            misi = aktivitas[pilihan]
            self.mulai_misi(misi)
        elif pilihan != "0":
            print("❌ Pilihan tidak valid!")

    def get_aktivitas_lokasi(self):
        """Dapatkan aktivitas berdasarkan lokasi"""
        aktivitas = {}
        
        if self.lokasi_sekarang == Lokasi.STASIUN:
            aktivitas = {
                "1": {"nama": "Misi Angkut Penumpang (Pekerjaan)", "id": "misi_1", "tipe": "pekerjaan"},
                "2": {"nama": "Temui Bus Teman (Spesial)", "id": "misi_19", "tipe": "spesial"},
            }
        elif self.lokasi_sekarang == Lokasi.JALAN_UTAMA:
            aktivitas = {
                "1": {"nama": "Misi Perjalanan Malam (Pekerjaan)", "id": "misi_2", "tipe": "pekerjaan"},
                "2": {"nama": "Pertarungan dengan Pengganggu (Pertarungan)", "id": "misi_5", "tipe": "pertarungan"},
            }
        elif self.lokasi_sekarang == Lokasi.TERMINAL:
            aktivitas = {
                "1": {"nama": "Misi Kedatangan Penumpang (Pekerjaan)", "id": "misi_3", "tipe": "pekerjaan"},
                "2": {"nama": "Minigame Parkir (Minigame)", "id": "misi_15", "tipe": "minigame"},
            }
        elif self.lokasi_sekarang == Lokasi.PASAR:
            aktivitas = {
                "1": {"nama": "Misi Rute Pasar Ramai (Pekerjaan)", "id": "misi_4", "tipe": "pekerjaan"},
                "2": {"nama": "Pertarungan Pedagang Nakal (Pertarungan)", "id": "misi_6", "tipe": "pertarungan"},
            }
        elif self.lokasi_sekarang == Lokasi.TAMAN:
            aktivitas = {
                "1": {"nama": "Misi Rute Wisata (Pekerjaan)", "id": "misi_7", "tipe": "pekerjaan"},
                "2": {"nama": "Minigame Permainan Keseimbangan (Minigame)", "id": "misi_16", "tipe": "minigame"},
            }
        elif self.lokasi_sekarang == Lokasi.PABRIK:
            aktivitas = {
                "1": {"nama": "Misi Pengiriman Suku Cadang (Pekerjaan)", "id": "misi_8", "tipe": "pekerjaan"},
                "2": {"nama": "Temui Bus Legendaris (Spesial)", "id": "misi_20", "tipe": "spesial"},
            }
        elif self.lokasi_sekarang == Lokasi.BENGKEL:
            aktivitas = {
                "1": {"nama": "Misi Perbaikan Mesin (Pekerjaan)", "id": "misi_9", "tipe": "pekerjaan"},
                "2": {"nama": "Pertarungan Mekanik Bengis (Pertarungan)", "id": "misi_11", "tipe": "pertarungan"},
            }
        elif self.lokasi_sekarang == Lokasi.KANTOR_PUSAT:
            aktivitas = {
                "1": {"nama": "Misi Laporan Harian (Pekerjaan)", "id": "misi_10", "tipe": "pekerjaan"},
                "2": {"nama": "Minigame Teka-teki Direktur (Minigame)", "id": "misi_17", "tipe": "minigame"},
                "3": {"nama": "Temui Bus Paling Kuat (Spesial)", "id": "misi_21", "tipe": "spesial"},
                "4": {"nama": "Cari Sidekick (Misi Spesial)", "id": "misi_22", "tipe": "spesial"},
            }
        
        return aktivitas

    def mulai_misi(self, misi):
        """Mulai misi yang dipilih"""
        misi_id = misi["id"]
        misi_num = int(misi_id.split("_")[1])
        
        if misi_num in self.karakter.misi_dikunci:
            self.dialog("Narator", "Misi ini sudah pernah Anda selesaikan!")
            return
        
        if misi_id == "misi_1":
            self.misi_angkut_penumpang()
        elif misi_id == "misi_2":
            self.misi_perjalanan_malam()
        elif misi_id == "misi_3":
            self.misi_kedatangan_penumpang()
        elif misi_id == "misi_4":
            self.misi_rute_pasar()
        elif misi_id == "misi_5":
            self.pertarungan_pengganggu()
        elif misi_id == "misi_6":
            self.pertarungan_pedagang()
        elif misi_id == "misi_7":
            self.misi_rute_wisata()
        elif misi_id == "misi_8":
            self.misi_pengiriman_cadang()
        elif misi_id == "misi_9":
            self.misi_perbaikan_mesin()
        elif misi_id == "misi_10":
            self.misi_laporan_harian()
        elif misi_id == "misi_11":
            self.pertarungan_mekanik_bengis()
        elif misi_id == "misi_15":
            self.minigame_parkir()
        elif misi_id == "misi_16":
            self.minigame_keseimbangan()
        elif misi_id == "misi_17":
            self.minigame_teka_teki()
        elif misi_id == "misi_19":
            self.misi_spesial_teman()
        elif misi_id == "misi_20":
            self.misi_spesial_legendaris()
        elif misi_id == "misi_21":
            self.misi_final_spesial()
        elif misi_id == "misi_22":
            self.misi_cari_sidekick()

    # ==================== MISI PEKERJAAN ====================
    
    def misi_angkut_penumpang(self):
        """Misi 1: Angkut Penumpang"""
        self.dialog("Inspektur Stasiun", "Halo! Kami butuh bus untuk mengangkut penumpang rush hour!")
        self.dialog(self.karakter.nama, "Baik! Saya siap melayani!")
        
        opsi = {
            "1": "Angkut dengan kecepatan tinggi",
            "2": "Angkut dengan hati-hati",
            "3": "Tolak misi"
        }
        
        pilihan = self.pilihan(opsi)
        
        if pilihan == "1":
            if random.random() < 0.7:
                self.dialog("Penumpang", "Wah, cepat sekali! Terima kasih!")
                self.berhasil_misi("misi_1", 100, 500)
            else:
                self.dialog("Penumpang", "Terlalu cepat! Aku jatuh!")
                self.gagal_misi()
        elif pilihan == "2":
            self.dialog("Penumpang", "Nyaman sekali perjalanannya!")
            self.berhasil_misi("misi_1", 150, 750)
        else:
            self.dialog("Inspektur Stasiun", "Sayang sekali...")

    def misi_perjalanan_malam(self):
        """Misi 2: Perjalanan Malam"""
        self.dialog("Sopir Malam", "Cuaca gelap sekali malam ini... Bantu navigasi?")
        self.dialog(self.karakter.nama, "Tentu! Lampu saya akan menerangi!")
        
        opsi = {
            "1": "Gunakan lampu standar",
            "2": "Gunakan lampu super terang",
            "3": "Jalan tanpa lampu"
        }
        
        pilihan = self.pilihan(opsi)
        
        if pilihan == "1":
            self.dialog("Sopir Malam", "Cukup terang...")
            self.berhasil_misi("misi_2", 100, 400)
        elif pilihan == "2":
            self.dialog("Sopir Malam", "Sangat terang! Sempurna!")
            self.berhasil_misi("misi_2", 150, 600)
        else:
            self.dialog("Kapolda", "Anda melanggar keselamatan!")
            self.gagal_misi()

    def misi_kedatangan_penumpang(self):
        """Misi 3: Kedatangan Penumpang"""
        self.dialog("Manajer Terminal", "Penumpang dari bandara tiba 30 menit! Siap?")
        
        opsi = {
            "1": "Tunggu di depan gerbang",
            "2": "Parkir di area tunggu khusus",
            "3": "Pergi makan dulu"
        }
        
        pilihan = self.pilihan(opsi)
        
        if pilihan == "3":
            self.dialog("Manajer Terminal", "Penumpang sudah datang! Di mana Anda?!")
            self.gagal_misi()
        else:
            self.dialog("Penumpang", "Terima kasih menunggu!")
            bonus = 200 if pilihan == "2" else 100
            self.berhasil_misi("misi_3", 150, bonus + 400)

    def misi_rute_pasar(self):
        """Misi 4: Rute Pasar Ramai"""
        self.dialog("Pedagang", "Tolong angkut dagangan ke berbagai lokasi!")
        
        opsi = {
            "1": "Buka pintu dengan kasar",
            "2": "Buka pintu dengan lembut",
            "3": "Gunakan tempat khusus kargo"
        }
        
        pilihan = self.pilihan(opsi)
        
        if pilihan == "1":
            self.dialog("Pedagang", "Barang saya rusak!")
            self.karakter.uang -= min(1000, self.karakter.uang)
            self.gagal_misi()
        elif pilihan == "3":
            self.dialog("Pedagang", "Sempurna! Barangku aman!")
            self.berhasil_misi("misi_4", 200, 800)
        else:
            self.dialog("Pedagang", "Barangku masih aman. Terima kasih!")
            self.berhasil_misi("misi_4", 150, 600)

    def misi_rute_wisata(self):
        """Misi 7: Rute Wisata"""
        self.dialog("Pemandu Wisata", "Kami perlu mengangkut turis ke taman!")
        
        opsi = {
            "1": "Berkomentar tentang atraksi",
            "2": "Diam fokus mengemudi",
            "3": "Nyanyikan lagu lawas"
        }
        
        pilihan = self.pilihan(opsi)
        
        if pilihan == "1":
            self.dialog("Turis", "Informatif sekali!")
            self.berhasil_misi("misi_7", 150, 700)
        elif pilihan == "3":
            self.dialog("Turis", "Hahahaha! Bersenang-senanglah!")
            self.berhasil_misi("misi_7", 200, 800)
        else:
            self.dialog("Turis", "Perjalanannya tenang dan nyaman.")
            self.berhasil_misi("misi_7", 100, 500)

    def misi_pengiriman_cadang(self):
        """Misi 8: Pengiriman Suku Cadang"""
        self.dialog("Teknisi Pabrik", "Suku cadang harus tiba tepat waktu! 15 menit!")
        
        opsi = {
            "1": "Berkendara normal",
            "2": "Berkendara cepat",
            "3": "Berkendara super cepat (berisiko)"
        }
        
        pilihan = self.pilihan(opsi)
        
        if pilihan == "1":
            self.dialog("Teknisi Pabrik", "Terlambat! Produksi tertunda!")
            self.gagal_misi()
        elif pilihan == "2":
            self.dialog("Teknisi Pabrik", "Tepat waktu! Terima kasih!")
            self.berhasil_misi("misi_8", 150, 700)
        else:
            if random.random() < 0.5:
                self.dialog("Polisi", "Denda speeding Rp500!")
                self.karakter.uang -= min(500, self.karakter.uang)
                self.gagal_misi()
            else:
                self.dialog("Teknisi Pabrik", "Sangat cepat dan tepat waktu!")
                self.berhasil_misi("misi_8", 200, 900)

    def misi_perbaikan_mesin(self):
        """Misi 9: Perbaikan Mesin"""
        self.dialog("Mekanik", "Mesin Anda bergetar! Ada masalah!")
        
        opsi = {
            "1": "Periksa oli mesin",
            "2": "Periksa ban",
            "3": "Minta overhaul (Rp2000)"
        }
        
        pilihan = self.pilihan(opsi)
        
        if pilihan == "1":
            self.dialog("Mekanik", "Oli habis! Saya isi ulang.")
            self.berhasil_misi("misi_9", 100, 500)
        elif pilihan == "2":
            self.dialog("Mekanik", "Ban aus! Saya ganti.")
            self.berhasil_misi("misi_9", 100, 500)
        else:
            if self.karakter.uang >= 2000:
                self.karakter.uang -= 2000
                self.dialog("Mekanik", "Selesai! Like new!")
                self.berhasil_misi("misi_9", 150, 2000)
            else:
                self.dialog("Mekanik", "Uang Anda tidak cukup...")
                self.gagal_misi()

    def misi_laporan_harian(self):
        """Misi 10: Laporan Harian"""
        self.dialog("Direktur", "Laporan harian: berapa penumpang hari ini?")
        
        opsi = {
            "1": "100 penumpang",
            "2": "500 penumpang",
            "3": "1000 penumpang"
        }
        
        pilihan = self.pilihan(opsi)
        
        penumpang = 100 if pilihan == "1" else (500 if pilihan == "2" else 1000)
        self.dialog("Direktur", f"Bagus! {penumpang} penumpang!")
        self.berhasil_misi("misi_10", 150, penumpang // 2)

    # ==================== MISI PERTARUNGAN ====================
    
    def pertarungan_pengganggu(self):
        """Misi 5: Pertarungan Pengganggu"""
        self.dialog("Pengganggu", "Hei! Masuk sini atau kena imbas!")
        self.dialog(self.karakter.nama, "Tidak! Saya tidak ditakut-takuti!")
        
        self.pertarungan(musuh_nama="Pengganggu Jalanan", musuh_hp=50, misi_id="misi_5", 
                        reward_exp=150, reward_uang=500)

    def pertarungan_pedagang(self):
        """Misi 6: Pertarungan Pedagang Nakal"""
        self.dialog("Pedagang Nakal", "Harga tol saya lebih mahal!")
        self.dialog(self.karakter.nama, "Tidak ada tol ilegal di rute saya!")
        
        self.pertarungan(musuh_nama="Pedagang Nakal", musuh_hp=60, misi_id="misi_6",
                        reward_exp=150, reward_uang=600)

    def pertarungan_mekanik_bengis(self):
        """Misi 11: Pertarungan Mekanik Bengis"""
        self.dialog("Mekanik Bengis", "Kau merampas pelanggan saya!")
        self.dialog(self.karakter.nama, "Saya hanya melayani dengan baik!")
        
        self.pertarungan(musuh_nama="Mekanik Bengis", musuh_hp=70, misi_id="misi_11",
                        reward_exp=200, reward_uang=700)

    def pertarungan(self, musuh_nama, musuh_hp, misi_id, reward_exp, reward_uang):
        """Sistem pertarungan umum"""
        musuh_hp_asli = musuh_hp
        self.dialog("Narator", "⚔️ PERTARUNGAN DIMULAI! ⚔️")
        time.sleep(1)
        
        while self.karakter.hp > 0 and musuh_hp > 0:
            print("\n" + "="*50)
            print(f"HP Anda: {self.karakter.hp}/{self.karakter.max_hp}")
            print(f"HP {musuh_nama}: {musuh_hp}/{musuh_hp_asli}")
            print("="*50)
            
            opsi = {
                "1": "Serang biasa (70% akurat)",
                "2": "Serang kuat (50% akurat, damage besar)",
                "3": "Pertahanan (kurangi damage)",
                "4": "Gunakan potion (Rp500)"
            }
            
            pilihan = self.pilihan(opsi)
            
            jika_pertahanan = False
            
            if pilihan == "1":
                if random.random() < 0.7:
                    damage = random.randint(10, 25)
                    musuh_hp -= damage
                    self.dialog(self.karakter.nama, f"Mengenai! {damage} damage!")
                else:
                    self.dialog(self.karakter.nama, "Meleset...")
            elif pilihan == "2":
                if random.random() < 0.5:
                    damage = random.randint(30, 45)
                    musuh_hp -= damage
                    self.dialog(self.karakter.nama, f"Pukulan super! {damage} damage!")
                else:
                    self.dialog(self.karakter.nama, "Serangan kuat meleset!")
            elif pilihan == "3":
                jika_pertahanan = True
                self.dialog(self.karakter.nama, "Bersiap pertahanan!")
            elif pilihan == "4":
                if self.karakter.uang >= 500:
                    self.karakter.uang -= 500
                    self.karakter.hp = self.karakter.max_hp
                    self.dialog(self.karakter.nama, "Gunakan potion! HP penuh!")
                else:
                    self.dialog(self.karakter.nama, "Uang tidak cukup!")
            
            # Serangan musuh
            if musuh_hp > 0:
                musuh_damage = random.randint(5, 20)
                if jika_pertahanan:
                    musuh_damage = musuh_damage // 2
                    self.dialog(musuh_nama, f"Serangan dikurangi! {musuh_damage} damage!")
                else:
                    self.dialog(musuh_nama, f"Serang Anda! {musuh_damage} damage!")
                
                self.karakter.hp -= musuh_damage
        
        time.sleep(1)
        
        if self.karakter.hp > 0:
            self.dialog("Narator", "🎉 ANDA MENANG! 🎉")
            self.berhasil_misi(misi_id, reward_exp, reward_uang)
        else:
            self.dialog("Narator", "😢 ANDA KALAH! 😢")
            self.karakter.hp = self.karakter.max_hp // 2
            self.dialog("Dokter", "Anda masuk ICU! Perlu istirahat.")
            self.gagal_misi()

    # ==================== MINIGAME ====================
    
    def minigame_parkir(self):
        """Misi 15: Minigame Parkir"""
        self.dialog("Petugas Parkir", "Bisa parkir di tempat sempit?")
        
        print("\n" + "="*50)
        print("MINIGAME: PARKIR DI TEMPAT SEMPIT")
        print("="*50)
        
        posisi = 2
        target = 2
        
        for i in range(3):
            arah = input(f"Gerakan {i+1} - Maju (A) atau Mundur (U)? ").strip().upper()
            if arah == "A":
                posisi += 1
            elif arah == "U":
                posisi -= 1
            else:
                print("Invalid!")
                i -= 1
                continue
            
            if posisi < 0 or posisi > 4:
                self.dialog("Petugas Parkir", "Keluar area parkir! Gagal!")
                self.gagal_misi()
                return
        
        if posisi == target:
            self.dialog("Petugas Parkir", "Sempurna! Parkir rapi!")
            self.berhasil_misi("misi_15", 100, 400)
        else:
            self.dialog("Petugas Parkir", "Tidak di posisi benar...")
            self.gagal_misi()

    def minigame_keseimbangan(self):
        """Misi 16: Minigame Keseimbangan"""
        self.dialog("Penari Jambul", "Maintain keseimbangan sambil berdansa?")
        
        print("\n" + "="*50)
        print("MINIGAME: KESEIMBANGAN TARI")
        print("="*50)
        print("Urutan: KIRI KANAN TENGAH KANAN KIRI\n")
        
        urutan_benar = ["K", "N", "T", "N", "K"]
        skor = 0
        
        for i, tombol in enumerate(urutan_benar):
            input_pemain = input(f"Gerakan {i+1}/5 - Tekan {tombol} (K/N/T): ").strip().upper()
            
            if input_pemain == tombol:
                print("✅ Benar!")
                skor += 1
            else:
                print(f"❌ Salah!")
        
        if skor >= 4:
            self.dialog("Penari Jambul", "Luar biasa!")
            self.berhasil_misi("misi_16", 100 + skor * 20, 400 + skor * 50)
        elif skor >= 2:
            self.dialog("Penari Jambul", "Lumayan...")
            self.berhasil_misi("misi_16", 50 + skor * 10, 200 + skor * 30)
        else:
            self.dialog("Penari Jambul", "Coba lagi!")
            self.gagal_misi()

    def minigame_teka_teki(self):
        """Misi 17: Minigame Teka-teki"""
        self.dialog("Direktur", "Uji kecerdasan dengan teka-teki!")
        
        print("\n" + "="*50)
        print("MINIGAME: TEKA-TEKI DIREKTUR")
        print("="*50)
        
        teka_teki = [
            {"pertanyaan": "Berapa roda di 3 bus?", "jawaban": "12"},
            {"pertanyaan": "Rute transjakarta pertama adalah?", "jawaban": "1"},
            {"pertanyaan": "Berapa halte di koridor 1?", "jawaban": "13"},
        ]
        
        benar = 0
        for i, q in enumerate(teka_teki):
            print(f"\nTeka-teki {i+1}/3: {q['pertanyaan']}")
            jawab = input("Jawaban: ").strip()
            
            if jawab.lower() == q['jawaban'].lower():
                print("✅ Benar!")
                benar += 1
            else:
                print(f"❌ Salah! Jawaban benar: {q['jawaban']}")
        
        if benar == 3:
            self.dialog("Direktur", "Sempurna! Anda cerdas!")
            self.berhasil_misi("misi_17", 150, 600)
        elif benar == 2:
            self.dialog("Direktur", "Cukup bagus!")
            self.berhasil_misi("misi_17", 100, 400)
        else:
            self.dialog("Direktur", "Belajar lebih banyak...")
            self.gagal_misi()

    # ==================== MISI SPESIAL ====================
    
    def misi_spesial_teman(self):
        """Misi 19: Bertemu Bus Teman"""
        self.dialog("Sopir 1", "Bus apa yang baru kutemui?")
        
        self.dialog("Bus Baru", f"Halo! {self.karakter.nama}, senang bertemu!")
        self.dialog(self.karakter.nama, "Aku juga senang!")
        self.dialog("Bus Baru", "Mari kita bekerja sama melayani penumpang!")
        
        self.berhasil_misi("misi_19", 120, 500)

    def misi_spesial_legendaris(self):
        """Misi 20: Bertemu Bus Legendaris"""
        self.dialog("Senioritas", "Ada Bus Legendaris dari jaman dulu!")
        
        self.dialog("Bus Legendaris", "Sudah lama aku tidak bertemu bus muda...")
        self.dialog(self.karakter.nama, "Saya mendengar banyak tentang Anda!")
        
        self.dialog("Bus Legendaris", "Ada bus jahat yang ingin menguasai semua rute!")
        self.dialog("Bus Legendaris", "Hanya Anda yang dapat menghentikannya. Siap?")
        
        opsi = {
            "1": "Saya siap menghadapi apapun!",
            "2": "Saya takut...",
            "3": "Saya perlu waktu"
        }
        
        pilihan = self.pilihan(opsi)
        
        if pilihan == "1":
            self.dialog("Bus Legendaris", "Semangat yang kita butuhkan!")
            self.berhasil_misi("misi_20", 180, 800)
        elif pilihan == "2":
            self.dialog("Bus Legendaris", "Ketakutan normal... Tapi ingat, warga butuh Anda!")
            self.berhasil_misi("misi_20", 120, 600)
        else:
            self.dialog("Bus Legendaris", "Baik... Saat siap, datanglah.")
            self.berhasil_misi("misi_20", 100, 500)

    def misi_cari_sidekick(self):
        """Misi 22: Cari Sidekick - Teman Perjalanan Spesial dari Koridor Lain"""
        if self.karakter.sidekick:
            self.dialog("Direktur", "Anda sudah punya sidekick!")
            return
        
        self.dialog("Direktur", "Ada sidekick dari berbagai koridor yang siap menemani perjalananmu!")
        
        # Tentukan sidekick yang tersedia berdasarkan koridor pemain
        # Semua koridor memiliki 2-3 pilihan sidekick dari koridor lain
        koridor_pemain = self.karakter.koridor
        sidekick_tersedia = self.get_sidekick_untuk_koridor(koridor_pemain)
        
        print("\n" + "="*60)
        print(f"👥 PILIH SIDEKICK ANDA (dari koridor lain):")
        print("="*60)
        
        for idx, (key, sidekick) in enumerate(sidekick_tersedia.items(), 1):
            print(f"\n{key}. {sidekick.value[0]}")
            print(f"   📍 {sidekick.value[1]}")
            print(f"   Koridor: {sidekick.value[3]} {sidekick.value[2]}")
        
        pilihan = self.pilihan(sidekick_tersedia)
        sidekick_terpilih = sidekick_tersedia[pilihan]
        
        self.karakter.sidekick = sidekick_terpilih
        
        self.dialog("Narator", f"✨ Anda mendapatkan sidekick! {sidekick_terpilih.value[0]}")
        self.dialog(sidekick_terpilih.value[0], f"Halo {self.karakter.nama}! Aku dari {sidekick_terpilih.value[2]}, senang bisa menemanimu!")
        self.dialog(self.karakter.nama, f"Terima kasih! Dengan bantuanmu, kami pasti bisa menyelamatkan kota ini!")
        
        self.berhasil_misi("misi_22", 200, 1000)
    
    def get_sidekick_untuk_koridor(self, koridor):
        """Dapatkan pilihan sidekick yang tersedia untuk koridor tertentu"""
        # Mapping: setiap koridor memiliki 2-3 sidekick dari koridor lain
        sidekick_mapping = {
            BusKoridor.K1: {"1": Sidekick.SOPIR_K4, "2": Sidekick.GADIS_K5, "3": Sidekick.MEKANIK_K9},
            BusKoridor.K2: {"1": Sidekick.SOPIR_K7, "2": Sidekick.GADIS_K2, "3": Sidekick.MUSISI_K3},
            BusKoridor.K3: {"1": Sidekick.SOPIR_K4, "2": Sidekick.MEKANIK_K12, "3": Sidekick.MUSISI_K13},
            BusKoridor.K4: {"1": Sidekick.GADIS_K5, "2": Sidekick.MEKANIK_K9, "3": Sidekick.MUSISI_K3},
            BusKoridor.K5: {"1": Sidekick.SOPIR_K4, "2": Sidekick.GADIS_K2, "3": Sidekick.MEKANIK_K12},
            BusKoridor.K6: {"1": Sidekick.SOPIR_K7, "2": Sidekick.GADIS_K5, "3": Sidekick.MUSISI_K13},
            BusKoridor.K7: {"1": Sidekick.SOPIR_K4, "2": Sidekick.GADIS_K2, "3": Sidekick.MEKANIK_K9},
            BusKoridor.K8: {"1": Sidekick.GADIS_K5, "2": Sidekick.MEKANIK_K12, "3": Sidekick.MUSISI_K3},
            BusKoridor.K9: {"1": Sidekick.SOPIR_K7, "2": Sidekick.GADIS_K2, "3": Sidekick.MUSISI_K13},
            BusKoridor.K10: {"1": Sidekick.SOPIR_K4, "2": Sidekick.MEKANIK_K9, "3": Sidekick.GADIS_K5},
            BusKoridor.K11: {"1": Sidekick.GADIS_K2, "2": Sidekick.MEKANIK_K12, "3": Sidekick.MUSISI_K3},
            BusKoridor.K12: {"1": Sidekick.SOPIR_K7, "2": Sidekick.GADIS_K5, "3": Sidekick.MUSISI_K13},
            BusKoridor.K13: {"1": Sidekick.SOPIR_K4, "2": Sidekick.GADIS_K2, "3": Sidekick.MEKANIK_K9},
            BusKoridor.K14: {"1": Sidekick.SOPIR_K7, "2": Sidekick.MEKANIK_K12, "3": Sidekick.MUSISI_K13},
        }
        
        return sidekick_mapping.get(koridor, {})

    def misi_final_spesial(self):
        """Misi 21: Misi Final Spesial"""
        if self.karakter.misi_selesai >= 20:
            self.dialog("Narator", "Saatnya misi final!")
            self.misi_pertarungan_akhir()

    # ==================== PERTARUNGAN FINAL DAN ENDING ====================
    
    def misi_pertarungan_akhir(self):
        """Misi 21: Pertarungan Akhir Melawan Raja Jahat Bus"""
        self.lokasi_sekarang = Lokasi.ISTANA_JAHAT
        
        self.dialog("Narator", "Anda memasuki Istana Raja Jahat Bus...")
        time.sleep(1)
        
        self.dialog("Raja Jahat Bus", "Akhirnya Anda datang! Bersiaplah untuk kekalahan!")
        self.dialog(self.karakter.nama, "Saya di sini untuk menyelamatkan kota!")
        
        print("\n" + "="*60)
        print("⚔️ PERTARUNGAN FINAL - RAJA JAHAT BUS ⚔️".center(60))
        print("="*60)
        
        opsi_strategi = {
            "1": "Serangan Langsung (Agresif) → Bad Ending",
            "2": "Pertahanan Bertahap (Seimbang) → Good Ending",
            "3": "Taktik Cerdas (Penuh Trik) → Secret Ending"
        }
        
        pilihan_strategi = self.pilihan(opsi_strategi)
        
        if pilihan_strategi == "1":
            self.ending_buruk()
        elif pilihan_strategi == "2":
            self.ending_baik()
        else:
            self.ending_rahasia()

    def ending_buruk(self):
        """Bad Ending: Kekalahan Tragis"""
        print("\n" + "="*60)
        print("BAD ENDING: KEKALAHAN TRAGIS".center(60))
        print("="*60 + "\n")
        
        self.dialog(self.karakter.nama, "Saya akan mengalahkanmu dengan kekuatan murni!")
        
        musuh_hp = 150
        
        for i in range(4):
            print(f"\nRonde {i+1}:")
            damage = random.randint(30, 50)
            musuh_hp -= damage
            
            if musuh_hp > 0:
                self.dialog("Raja Jahat Bus", "Kuat... tapi tidak cukup!")
                damage_balik = random.randint(40, 60)
                self.karakter.hp -= damage_balik
                
                if self.karakter.hp <= 0:
                    print("\n💔 Pertarungan berakhir tragis...")
                    self.dialog(self.karakter.nama, "Aku kalah... kota ini...")
                    self.dialog("Raja Jahat Bus", "KOTA ADALAH MILIKKU!")
                    
                    time.sleep(2)
                    print("""
╔════════════════════════════════════════════════════════════╗
║                   🌙 BAD ENDING 🌙                         ║
║                                                            ║
║  Kota terserah pada kegelapan. Raja Jahat Bus menguasai   ║
║  semua rute. Penumpang menderita di bawah tirani busnya.  ║
║                                                            ║
║  Kekuatan saja tidak cukup. Kerendahan hati dan           ║
║  bijaksana itu penting.                                   ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
                    """)
                    self.game_aktif = False
                    return

    def ending_baik(self):
        """Good Ending: Kemenangan Heroik"""
        print("\n" + "="*60)
        print("GOOD ENDING: KEMENANGAN HEROIK".center(60))
        print("="*60 + "\n")
        
        self.dialog(self.karakter.nama, "Saya tidak untuk menghancurkan... tapi untuk melindungi!")
        
        musuh_hp = 120
        ronde = 0
        
        while self.karakter.hp > 0 and musuh_hp > 0:
            ronde += 1
            damage = random.randint(20, 40)
            musuh_hp -= damage
            
            if musuh_hp > 0:
                damage_musuh = random.randint(15, 30)
                self.karakter.hp -= damage_musuh
        
        if self.karakter.hp > 0:
            print("\n" + "="*60)
            print("🎉 KEMENANGAN! 🎉".center(60))
            
            time.sleep(2)
            print("""
╔════════════════════════════════════════════════════════════╗
║                 ☀️ GOOD ENDING ☀️                         ║
║                                                            ║
║  Dengan keberanian dan keseimbangan, Anda mengalahkan     ║
║  Raja Jahat Bus!                                           ║
║                                                            ║
║  Kota kembali damai. Transportasi umum berjalan normal.   ║
║  Anda menjadi PAHLAWAN TRANSJAKARTA yang terkenal!        ║
║  Cerita Anda dikenang sepanjang masa.                     ║
║                                                            ║
║  Pesan: Keseimbangan dan ketekunan membawa kemenangan.    ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
            """)
            self.karakter.misi_selesai = 21
            self.game_aktif = False

    def ending_rahasia(self):
        """Secret Ending: Kemenangan Luar Biasa"""
        print("\n" + "="*60)
        print("SECRET ENDING: KEMENANGAN LUAR BIASA".center(60))
        print("="*60 + "\n")
        
        self.dialog(self.karakter.nama, "Saya tahu kelemahan Anda... dengan data dan strategi!")
        
        musuh_hp = 100
        
        while musuh_hp > 0:
            angka1 = random.randint(1, 10)
            angka2 = random.randint(1, 10)
            jawaban_benar = angka1 + angka2
            
            print(f"Puzzle: {angka1} + {angka2} = ?")
            try:
                jawaban = int(input("Jawaban: "))
                
                if jawaban == jawaban_benar:
                    damage = 35 + random.randint(10, 20)
                    musuh_hp -= damage
                    self.dialog(self.karakter.nama, f"Benar! Kombinasi! {damage} damage!")
                else:
                    damage = 15
                    musuh_hp -= damage
            except:
                damage = 10
                musuh_hp -= damage
        
        print("""
╔════════════════════════════════════════════════════════════╗
║          🌟 SECRET ENDING: TRANSCENDENTAL 🌟              ║
║                                                            ║
║  Dengan kecerdasan dan taktik brilian, Anda lebih dari    ║
║  memenangkan pertarungan... Anda MENGUBAH hati Raja!      ║
║                                                            ║
║  Raja Jahat Bus: "Aku salah selama ini. Terima kasih!"    ║
║                                                            ║
║  Dia berubah menjadi bus baik dan membantu Anda!          ║
║  Kota mengalami RENAISSANCE TRANSPORTASI!                ║
║                                                            ║
║  Anda bukan hanya PAHLAWAN, tapi PENDAMAI DUNIA!         ║
║  Kisah Anda adalah LEGENDA ABADI!                         ║
║                                                            ║
║  Pesan: Kecerdasan & empati adalah kekuatan terbesar.    ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
        """)
        self.karakter.misi_selesai = 21
        self.game_aktif = False

    def berhasil_misi(self, misi_id, exp_reward, uang_reward):
        """Misi berhasil"""
        misi_num = int(misi_id.split("_")[1])
        self.karakter.misi_dikunci.add(misi_num)
        self.karakter.misi_selesai += 1
        self.karakter.exp += exp_reward
        self.karakter.uang += uang_reward
        
        if self.karakter.exp >= self.karakter.exp_untuk_level_up:
            self.karakter.level += 1
            self.karakter.exp = 0
            self.karakter.exp_untuk_level_up = int(self.karakter.exp_untuk_level_up * 1.2)
            self.dialog("Narator", f"🎉 LEVEL UP! Level {self.karakter.level}!")
        
        print("\n" + "="*50)
        print("✅ MISI BERHASIL!")
        print("="*50)
        print(f"EXP: +{exp_reward}")
        print(f"Uang: +Rp{uang_reward}")
        print(f"Misi Selesai: {self.karakter.misi_selesai}/22")
        print("="*50 + "\n")

    def gagal_misi(self):
        """Misi gagal"""
        print("\n" + "="*50)
        print("❌ MISI GAGAL!")
        print("="*50)
        print("Coba lagi dengan strategi berbeda...")
        print("="*50 + "\n")

    def lihat_inventori(self):
        """Lihat inventori"""
        print("\n" + "="*60)
        print("📦 INVENTORI")
        print("="*60)
        if self.karakter.inventory:
            for item in self.karakter.inventory:
                print(f"  - {item}")
        else:
            print("  Inventori kosong")
        print("="*60 + "\n")

    def istirahat(self):
        """Istirahat"""
        print("\n" + "="*60)
        print("😴 ISTIRAHAT")
        print("="*60)
        self.dialog("Narator", "Anda beristirahat...")
        time.sleep(2)
        
        self.karakter.energi = self.karakter.max_energi
        self.karakter.hp = self.karakter.max_hp
        
        self.dialog("Narator", "Anda merasa segar kembali!")
        print("="*60 + "\n")

    def main_game_loop(self):
        """Loop utama game dengan opsi untuk bermain ulang"""
        while True:
            self.game_aktif = True
            self.karakter = None
            self.lokasi_sekarang = Lokasi.STASIUN
            self.dialog_index = 0
            
            self.intro_game()
            self.pilih_karakter()
            self.tampilkan_map()
            self.main_menu()
            
            # Selesai atau game over
            print("\n" + "="*70)
            print("TERIMA KASIH TELAH BERMAIN!".center(70))
            print("="*70)
            
            if self.karakter and self.karakter.misi_selesai >= 21:
                print(f"\n🎉 Anda menyelesaikan game dengan misi selesai: {self.karakter.misi_selesai}/22")
                print(f"Level akhir: {self.karakter.level}")
                print(f"Total uang: Rp{self.karakter.uang:,}")
            
            # Opsi bermain ulang
            opsi = input("\nMain ulang? (Y/N): ").strip().upper()
            if opsi.upper() != "Y":
                self.dialog("Narator", "Sampai jumpa lagi, pahlawan! Terima kasih telah bermain!")
                break

# ==================== MAIN ====================

def main():
    """Fungsi main untuk memulai game"""
    game = Game()
    game.main_game_loop()

if __name__ == "__main__":
    main()
