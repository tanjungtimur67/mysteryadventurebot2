import time
import random
from enum import Enum

class BusType(Enum):
    """Enum untuk tipe bus Transjakarta"""
    BLUEBIRD = "🔵 Bluebird Express"
    KOPAJA = "🚌 Kopaja Standard"
    MRTJ = "🟦 MRTJ Rapid"
    MAYASARI = "🟩 Mayasari Bakti"
    APM = "🟨 APM Transjakarta"

class Lokasi(Enum):
    """Enum untuk lokasi dalam game"""
    STASIUN = "Stasiun Sentral"
    JALAN_UTAMA = "Jalan Utama"
    TERMINAL = "Terminal Pusat"
    PASAR = "Pasar Tradisional"
    TAMAN = "Taman Hiburan"
    PABRIK = "Pabrik Suku Cadang"
    BENGKEL = "Bengkel Hitam"
    KANTOR_PUSAT = "Kantor Pusat Transjakarta"
    ISTANA_JAHAT = "Istana Raja Jahat Bus"

class Karakter:
    """Kelas untuk menyimpan data karakter pemain"""
    def __init__(self, nama, bus_type):
        self.nama = nama
        self.bus_type = bus_type
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
        self.stats = {
            "kecepatan": 50,
            "ketahanan": 50,
            "kerajinan": 50,
            "kecerdasan": 50
        }

    def tampilkan_status(self):
        """Menampilkan status karakter"""
        print("\n" + "="*50)
        print(f"🚌 STATUS {self.nama.upper()}")
        print("="*50)
        print(f"Tipe Bus: {self.bus_type.value}")
        print(f"Level: {self.level}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Energi: {self.energi}/{self.max_energi}")
        print(f"Uang: Rp{self.uang:,}")
        print(f"Misi Selesai: {self.misi_selesai}/21")
        print(f"EXP: {self.exp}/{self.exp_untuk_level_up}")
        print("\nStats:")
        for stat, nilai in self.stats.items():
            print(f"  {stat.capitalize()}: {nilai}")
        if self.inventory:
            print(f"\nInventory: {', '.join(self.inventory)}")
        print("="*50 + "\n")

class Game:
    """Kelas utama untuk menjalankan game"""
    def __init__(self):
        self.karakter = None
        self.lokasi_sekarang = Lokasi.STASIUN
        self.misi_aktif = None
        self.dialog_index = 0

    def dialog(self, pembicara, teks, delay=0.03):
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
        """Pemilihan karakter bus"""
        print("\n📋 PILIH KARAKTER BUS ANDA:")
        print("="*50)
        
        bus_options = {
            "1": BusType.BLUEBIRD,
            "2": BusType.KOPAJA,
            "3": BusType.MRTJ,
            "4": BusType.MAYASARI,
            "5": BusType.APM
        }
        
        deskripsi_bus = {
            BusType.BLUEBIRD: "Cepat dan andal, master dalam kecepatan (Rute: 1, 2, 5, 8)",
            BusType.KOPAJA: "Tangguh dan berkekuatan, master dalam ketahanan (Rute: 4, 6, 7, 12)",
            BusType.MRTJ: "Cerdas dan efisien, master dalam kecerdasan (Rute: 3, 9, 10, 11)",
            BusType.MAYASARI: "Ahli dalam kerajinan, dapat memperbaiki dengan cepat (Rute: 13, 14, 15)",
            BusType.APM: "Seimbang dalam semua skill (Rute: 16, 17, 18, 19, 20)"
        }
        
        for key, bus in bus_options.items():
            print(f"{key}. {bus.value}")
            print(f"   ℹ️  {deskripsi_bus[bus]}\n")
        
        pilihan_bus = self.pilihan(bus_options)
        bus_terpilih = bus_options[pilihan_bus]
        
        print(f"\n✅ Anda memilih: {bus_terpilih.value}")
        
        nama = input("\nSiapa nama bus Anda? ").strip()
        if not nama:
            nama = "Bus Pemberani"
        
        self.karakter = Karakter(nama, bus_terpilih)
        self.sesuaikan_stats_karakter(bus_terpilih)
        
        self.dialog(nama, f"Aku adalah {bus_terpilih.value}! Siap untuk menyelamatkan kota ini!")
        time.sleep(1)

    def sesuaikan_stats_karakter(self, bus_type):
        """Sesuaikan stats karakter berdasarkan tipe bus yang dipilih"""
        if bus_type == BusType.BLUEBIRD:
            self.karakter.stats["kecepatan"] = 80
            self.karakter.stats["ketahanan"] = 40
        elif bus_type == BusType.KOPAJA:
            self.karakter.stats["ketahanan"] = 80
            self.karakter.stats["kecepatan"] = 40
        elif bus_type == BusType.MRTJ:
            self.karakter.stats["kecerdasan"] = 80
            self.karakter.stats["kerajinan"] = 50
        elif bus_type == BusType.MAYASARI:
            self.karakter.stats["kerajinan"] = 80
            self.karakter.stats["kecerdasan"] = 50
        else:  # APM
            for stat in self.karakter.stats:
                self.karakter.stats[stat] = 60

    def tampilkan_map(self):
        """Menampilkan peta game dengan lokasi dan aktivitas"""
        print("\n" + "🗺️ "*30)
        print("\n🚌 PETA PETUALANGAN TRANSJAKARTA 🚌")
        print("="*60)
        
        peta = """
        ┌─────────────────────────────────────────────────┐
        │  DUNIA TRANSJAKARTA - PETA PETUALANGAN          │
        ├─────────────────────────────────────────────────┤
        │                                                  │
        │  🏛️ KANTOR PUSAT ────────── 🏭 PABRIK          │
        │      │                         │                │
        │      │                         │                │
        │  🛠️ BENGKEL HITAM ──────── 🎪 TAMAN HIBURAN   │
        │      │                         │                │
        │      │      🌆 JALAN UTAMA    │                │
        │      │            │            │                │
        │  🚉 STASIUN SENTRAL ──── 🏪 PASAR TRADISIONAL  │
        │      │                         │                │
        │      └─────── 🚐 TERMINAL PUSAT                │
        │                    │                            │
        │                    │                            │
        │             👑 ISTANA RAJA JAHAT BUS             │
        │                                                  │
        └─────────────────────────────────────────────────┘
        
        Lokasi Saat Ini: {lokasi}
        """
        
        print(peta.format(lokasi=self.lokasi_sekarang.value))
        print("="*60)
        print("Ketik 'peta' untuk melihat peta, 'status' untuk lihat status,")
        print("'jelajahi' untuk melihat lokasi yang tersedia, 'inventori' untuk lihat item.")
        print("="*60 + "\n")

    def main_menu(self):
        """Menu utama game"""
        while True:
            print("\n" + "="*50)
            print(f"📍 Lokasi: {self.lokasi_sekarang.value}")
            print(f"🚌 Bus: {self.karakter.bus_type.value}")
            print(f"Misi Selesai: {self.karakter.misi_selesai}/21")
            print("="*50)
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
                exit()
            else:
                print("❌ Pilihan tidak valid!")

    def jelajahi_lokasi(self):
        """Menu jelajahi lokasi"""
        print("\n" + "="*50)
        print("🚌 LOKASI YANG DAPAT DIJELAJAHI:")
        print("="*50)
        
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
        
        print("\n" + "="*50)
        print(f"📍 {self.lokasi_sekarang.value}")
        print("="*50)
        print("\nAktivitas yang tersedia:")
        
        for key, aktiv in aktivitas.items():
            print(f"{key}. {aktiv['nama']}")
        
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
                "2": {"nama": "Pertarungan Mekanik Bengis (Pertarungan)", "id": "misi_7", "tipe": "pertarungan"},
            }
        elif self.lokasi_sekarang == Lokasi.KANTOR_PUSAT:
            aktivitas = {
                "1": {"nama": "Misi Laporan Harian (Pekerjaan)", "id": "misi_10", "tipe": "pekerjaan"},
                "2": {"nama": "Minigame Teka-teki Direktur (Minigame)", "id": "misi_17", "tipe": "minigame"},
                "3": {"nama": "Temui Bus Paling Kuat (Spesial)", "id": "misi_21", "tipe": "spesial"},
            }
        
        return aktivitas

    def mulai_misi(self, misi):
        """Mulai misi yang dipilih"""
        misi_id = misi["id"]
        
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

    # ==================== MISI PEKERJAAN ====================
    
    def misi_angkut_penumpang(self):
        """Misi 1: Angkut Penumpang di Stasiun"""
        if self.karakter.misi_selesai >= 1 and 1 in self.karakter.misi_dikunci:
            self.dialog("Pengemudi", "Misi ini sudah selesai!")
            return
        
        self.dialog("Inspektur Stasiun", "Halo! Kami butuh bus untuk mengangkut penumpang rush hour pagi ini!")
        self.dialog(self.karakter.nama, "Baik! Saya siap melayani!")
        
        opsi = {
            "1": "Angkut dengan kecepatan tinggi",
            "2": "Angkut dengan hati-hati",
            "3": "Tolak misi"
        }
        
        pilihan = self.pilihan(opsi)
        
        if pilihan == "1":
            self.dialog(self.karakter.nama, "Saya akan angkut dengan cepat!")
            if random.random() < 0.7:
                self.dialog("Penumpang", "Wah, cepat sekali! Terima kasih!")
                self.dialog("Inspektur Stasiun", "Bagus! Penumpang puas dengan layanan Anda!")
                self.berhasil_misi("misi_1", 100, 500)
            else:
                self.dialog("Penumpang", "Terlalu cepat! Aku jatuh!")
                self.dialog("Inspektur Stasiun", "Misi gagal, coba lagi lebih hati-hati!")
                self.gagal_misi()
        elif pilihan == "2":
            self.dialog(self.karakat.nama, "Saya akan angkut dengan aman dan nyaman.")
            self.dialog("Penumpang", "Nyaman sekali perjalanannya! Terima kasih!")
            self.dialog("Inspektur Stasiun", "Sempurna! Semua penumpang puas!")
            self.berhasil_misi("misi_1", 150, 750)
        else:
            self.dialog("Inspektur Stasiun", "Sayang sekali... Kami tunggu lain kali!")

    def misi_perjalanan_malam(self):
        """Misi 2: Perjalanan Malam"""
        if self.karakter.misi_selesai >= 2 and 2 in self.karakter.misi_dikunci:
            self.dialog("Sopir Malam", "Misi ini sudah selesai!")
            return
        
        self.dialog("Sopir Malam", "Cuaca gelap sekali malam ini... Bisa bantu saya navigasi?")
        self.dialog(self.karakter.nama, "Tentu! Lampu saya akan menerangi jalan!")
        
        opsi = {
            "1": "Gunakan lampu standar",
            "2": "Gunakan lampu super terang",
            "3": "Jalan tanpa lampu"
        }
        
        pilihan = self.pilihan(opsi)
        
        if pilihan == "1":
            self.dialog("Sopir Malam", "Cukup terang, tapi sedikit gelap...")
            self.berhasil_misi("misi_2", 100, 400)
        elif pilihan == "2":
            self.dialog("Sopir Malam", "Wow! Sangat terang! Kami bisa melihat jarak jauh!")
            self.dialog("Penumpang", "Selamat malam yang aman!")
            self.berhasil_misi("misi_2", 150, 600)
        else:
            self.dialog("Sopir Malam", "Ini berbahaya sekali!")
            self.dialog("Kapolda", "Anda melanggar peraturan keselamatan!")
            self.gagal_misi()

    def misi_kedatangan_penumpang(self):
        """Misi 3: Kedatangan Penumpang"""
        if self.karakter.misi_selesai >= 3 and 3 in self.karakter.misi_dikunci:
            self.dialog("Manajer Terminal", "Misi ini sudah selesai!")
            return
        
        self.dialog("Manajer Terminal", "Penumpang dari bandara tiba 30 menit lagi! Siap?")
        self.dialog(self.karakter.nama, "Saya siap mengangkut mereka!")
        
        opsi = {
            "1": "Tunggu di depan gerbang",
            "2": "Parkir di area tunggu khusus",
            "3": "Pergi makan dulu"
        }
        
        pilihan = self.pilihan(opsi)
        
        if pilihan == "3":
            self.dialog("Manajer Terminal", "Penumpang sudah datang! Di mana Anda?!")
            self.dialog("Penumpang", "Kami menunggu! Ini menyusahkan!")
            self.gagal_misi()
        else:
            self.dialog("Penumpang", "Terima kasih menunggu kami!")
            self.dialog("Manajer Terminal", "Bagus! Penumpang puas dengan respons Anda!")
            bonus = 200 if pilihan == "2" else 100
            self.berhasil_misi("misi_3", 150, bonus + 400)

    def misi_rute_pasar(self):
        """Misi 4: Rute Pasar Ramai"""
        if self.karakter.misi_selesai >= 4 and 4 in self.karakter.misi_dikunci:
            self.dialog("Pedagang", "Misi ini sudah selesai!")
            return
        
        self.dialog("Pedagang", "Tolong angkut barang dagangan saya ke berbagai lokasi pasar!")
        self.dialog(self.karakter.nama, "Baik! Saya akan hati-hati dengan barang Anda!")
        
        opsi = {
            "1": "Buka pintu dengan kasar",
            "2": "Buka pintu dengan lembut",
            "3": "Gunakan tempat khusus kargo"
        }
        
        pilihan = self.pilihan(opsi)
        
        if pilihan == "1":
            self.dialog("Pedagang", "Barang saya rusak! Ganti rugi!")
            self.dialog(self.karakter.nama, "Maaf... aku bayar Rp1000!")
            self.karakter.uang -= 1000
            self.gagal_misi()
        elif pilihan == "3":
            self.dialog("Pedagang", "Sempurna! Barangku aman!")
            self.berhasil_misi("misi_4", 200, 800)
        else:
            self.dialog("Pedagang", "Barangku masih aman. Terima kasih!")
            self.berhasil_misi("misi_4", 150, 600)

    def misi_rute_wisata(self):
        """Misi 7: Rute Wisata ke Taman"""
        if self.karakter.misi_selesai >= 7 and 7 in self.karakter.misi_dikunci:
            self.dialog("Pemandu Wisata", "Misi ini sudah selesai!")
            return
        
        self.dialog("Pemandu Wisata", "Kami perlu mengangkut turis ke taman hiburan!")
        self.dialog(self.karakter.nama, "Saya akan memberikan pengalaman terbaik!")
        
        opsi = {
            "1": "Berkomentar tentang atraksi di jalan",
            "2": "Diam fokus mengemudi",
            "3": "Nyanyikan lagu lawas"
        }
        
        pilihan = self.pilihan(opsi)
        
        if pilihan == "1":
            self.dialog("Turis", "Wow! Informatif sekali! Kami menikmati perjalanan ini!")
            self.berhasil_misi("misi_7", 150, 700)
        elif pilihan == "3":
            self.dialog("Turis", "Hahahaha! Lawak sekali! Bersenang-senanglah bersama kami!")
            self.berhasil_misi("misi_7", 200, 800)
        else:
            self.dialog("Turis", "Perjalanannya tenang dan nyaman.")
            self.berhasil_misi("misi_7", 100, 500)

    def misi_pengiriman_cadang(self):
        """Misi 8: Pengiriman Suku Cadang"""
        if self.karakter.misi_selesai >= 8 and 8 in self.karakter.misi_dikunci:
            self.dialog("Teknisi Pabrik", "Misi ini sudah selesai!")
            return
        
        self.dialog("Teknisi Pabrik", "Suku cadang penting harus tiba tepat waktu!")
        self.dialog(self.karakter.nama, "Berapa lama waktu yang saya punya?")
        self.dialog("Teknisi Pabrik", "Hanya 15 menit!")
        
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
                self.dialog("Polisi", "Anda melanggar batas kecepatan! Denda Rp500!")
                self.karakter.uang -= 500 if self.karakter.uang >= 500 else self.karakter.uang
                self.gagal_misi()
            else:
                self.dialog("Teknisi Pabrik", "Cepat sekali! Sangat tepat waktu!")
                self.berhasil_misi("misi_8", 200, 900)

    def misi_perbaikan_mesin(self):
        """Misi 9: Perbaikan Mesin"""
        if self.karakter.misi_selesai >= 9 and 9 in self.karakter.misi_dikunci:
            self.dialog("Mekanik", "Misi ini sudah selesai!")
            return
        
        self.dialog("Mekanik", "Mesin Anda bergetar! Ada masalah!")
        self.dialog(self.karakter.nama, "Apa yang harus dilakukan?")
        
        opsi = {
            "1": "Periksa oli mesin",
            "2": "Periksa ban",
            "3": "Minta overhaul (biaya Rp2000)"
        }
        
        pilihan = self.pilihan(opsi)
        
        self.dialog("Mekanik", "Bagus! Masalah terletak pada...")
        
        if pilihan == "1":
            self.dialog("Mekanik", "Oli habis! Saya isi ulang.")
            self.berhasil_misi("misi_9", 100, 500)
        elif pilihan == "2":
            self.dialog("Mekanik", "Bannya aus! Saya ganti.")
            self.berhasil_misi("misi_9", 100, 500)
        else:
            if self.karakter.uang >= 2000:
                self.karakter.uang -= 2000
                self.dialog("Mekanik", "Selesai! Mesin Anda like new!")
                self.berhasil_misi("misi_9", 150, 2000)
            else:
                self.dialog("Mekanik", "Uang Anda tidak cukup...")
                self.gagal_misi()

    def misi_laporan_harian(self):
        """Misi 10: Laporan Harian"""
        if self.karakter.misi_selesai >= 10 and 10 in self.karakter.misi_dikunci:
            self.dialog("Direktur", "Misi ini sudah selesai!")
            return
        
        self.dialog("Direktur", "Laporan harian Anda: berapa banyak penumpang hari ini?")
        self.dialog(self.karakter.nama, "Saya melayani dengan sebaik-baiknya!")
        
        opsi = {
            "1": "Lapor 100 penumpang",
            "2": "Lapor 500 penumpang",
            "3": "Lapor 1000 penumpang"
        }
        
        pilihan = self.pilihan(opsi)
        
        penumpang = int(pilihan[0]) * 100 if pilihan == "1" else (500 if pilihan == "2" else 1000)
        
        self.dialog("Direktur", f"Bagus! {penumpang} penumpang adalah pencapaian yang solid!")
        self.berhasil_misi("misi_10", 150, penumpang // 2)

    # ==================== MISI PERTARUNGAN ====================
    
    def pertarungan_pengganggu(self):
        """Misi 5: Pertarungan dengan Pengganggu Jalan"""
        if self.karakter.misi_selesai >= 5 and 5 in self.karakter.misi_dikunci:
            self.dialog("Polisi", "Misi ini sudah selesai!")
            return
        
        self.dialog("Pengganggu", "Hei! Masuk sini atau kena imbas!")
        self.dialog(self.karakter.nama, "Tidak! Saya tidak akan ditakut-takuti!")
        
        self.pertarungan(musuh_nama="Pengganggu Jalanan", musuh_hp=50, misi_id="misi_5", 
                        reward_exp=150, reward_uang=500)

    def pertarungan_pedagang(self):
        """Misi 6: Pertarungan dengan Pedagang Nakal"""
        if self.karakter.misi_selesai >= 6 and 6 in self.karakter.misi_dikunci:
            self.dialog("Aparat", "Misi ini sudah selesai!")
            return
        
        self.dialog("Pedagang Nakal", "Harga tol saya lebih mahal! Bayar atau hadapi konsekuensi!")
        self.dialog(self.karakter.nama, "Tidak ada tol ilegal di rute saya!")
        
        self.pertarungan(musuh_nama="Pedagang Nakal", musuh_hp=60, misi_id="misi_6",
                        reward_exp=150, reward_uang=600)

    def pertarungan_mekanik_bengis(self):
        """Misi 7: Pertarungan dengan Mekanik Bengis (duplicate function)"""
        if self.karakter.misi_selesai >= 11 and 11 in self.karakter.misi_dikunci:
            self.dialog("Polisi", "Misi ini sudah selesai!")
            return
        
        self.dialog("Mekanik Bengis", "Kau merampas pelanggan saya! Balas dendam!")
        self.dialog(self.karakter.nama, "Saya hanya melayani dengan baik!")
        
        self.pertarungan(musuh_nama="Mekanik Bengis", musuh_hp=70, misi_id="misi_11",
                        reward_exp=200, reward_uang=700)

    def pertarungan_komplotan(self):
        """Misi 12: Pertarungan dengan Komplotan Bus Jahat"""
        if self.karakter.misi_selesai >= 12 and 12 in self.karakter.misi_dikunci:
            self.dialog("Komandan Komplotan", "Kami sudah bertemu sebelumnya...")
            return
        
        self.dialog("Komplotan Bus Jahat", "Bergabunglah dengan kami atau hadapi kekalahan!")
        self.dialog(self.karakter.nama, "Saya tidak akan menjadi jahat!")
        
        self.pertarungan(musuh_nama="Komplotan Bus Jahat", musuh_hp=80, misi_id="misi_12",
                        reward_exp=250, reward_uang=800)

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
                "3": "Pertahanan (kurangi damage masuk)",
                "4": "Gunakan potion (Rp500)"
            }
            
            pilihan = self.pilihan(opsi)
            
            jika_pertahanan = False
            
            if pilihan == "1":
                if random.random() < 0.7:
                    damage = random.randint(10, 25)
                    musuh_hp -= damage
                    self.dialog(self.karakter.nama, f"Seranganku mengenai! {damage} damage!")
                else:
                    self.dialog(self.karakter.nama, "Seranganku meleset...")
            elif pilihan == "2":
                if random.random() < 0.5:
                    damage = random.randint(30, 45)
                    musuh_hp -= damage
                    self.dialog(self.karakter.nama, f"Pukulan super! {damage} damage besar!")
                else:
                    self.dialog(self.karakter.nama, "Serangan kuat ku meleset... Sayang sekali!")
            elif pilihan == "3":
                jika_pertahanan = True
                self.dialog(self.karakter.nama, "Aku bersiap untuk pertahanan!")
            elif pilihan == "4":
                if self.karakter.uang >= 500:
                    self.karakter.uang -= 500
                    self.karakter.hp = self.karakter.max_hp
                    self.dialog(self.karakter.nama, "Saya gunakan potion! HP penuh kembali!")
                else:
                    self.dialog(self.karakter.nama, "Uang saya tidak cukup untuk potion...")
            
            # Serangan musuh
            if musuh_hp > 0:
                musuh_damage = random.randint(5, 20)
                if jika_pertahanan:
                    musuh_damage = musuh_damage // 2
                    self.dialog(musuh_nama, f"Seranganku dikurangi karena pertahananmu! {musuh_damage} damage!")
                else:
                    self.dialog(musuh_nama, f"Aku serang Anda! {musuh_damage} damage!")
                
                self.karakter.hp -= musuh_damage
        
        time.sleep(1)
        
        if self.karakter.hp > 0:
            self.dialog("Narator", "🎉 ANDA MENANG! 🎉")
            self.berhasil_misi(misi_id, reward_exp, reward_uang)
        else:
            self.dialog("Narator", "😢 ANDA KALAH! 😢")
            self.karakter.hp = self.karakter.max_hp // 2
            self.dialog("Dokter", "Anda masuk ICU! Anda selamat, tapi perlu istirahat.")
            self.gagal_misi()

    # ==================== MINIGAME ====================
    
    def minigame_parkir(self):
        """Misi 15: Minigame Parkir"""
        if self.karakter.misi_selesai >= 15 and 15 in self.karakter.misi_dikunci:
            self.dialog("Petugas Parkir", "Misi ini sudah selesai!")
            return
        
        self.dialog("Petugas Parkir", "Bisa parkir di tempat yang sempit?")
        self.dialog(self.karakter.nama, "Tentu saja!")
        
        print("\n" + "="*50)
        print("MINIGAME: PARKIR DI TEMPAT SEMPIT")
        print("="*50)
        print("""
        Gunakan koordinat untuk parkir:
        [  ][ ][X][ ][ ]  <- Posisi awal Anda (X)
        
        Target parkir: Posisi [2] (tengah)
        """)
        
        posisi = 2  # Tengah (0-indexed)
        target = 2
        gerakan = 0
        
        for i in range(3):
            arah = input(f"Gerakan {i+1} - Maju (A) atau Mundur (U)? ").strip().upper()
            if arah == "A":
                posisi += 1
                gerakan += 1
            elif arah == "U":
                posisi -= 1
                gerakan += 1
            else:
                print("Input tidak valid!")
                i -= 1
                continue
            
            if posisi < 0 or posisi > 4:
                self.dialog("Petugas Parkir", "Anda keluar dari area parkir! Gagal!")
                self.gagal_misi()
                return
            
            tampil_posisi = ""
            for j in range(5):
                if j == posisi:
                    tampil_posisi += "[X]"
                else:
                    tampil_posisi += "[ ]"
            print(f"Posisi sekarang: {tampil_posisi}")
        
        if posisi == target:
            self.dialog("Petugas Parkir", "Sempurna! Parkir dengan rapi!")
            self.berhasil_misi("misi_15", 100 + (50 - gerakan * 10), 400)
        else:
            self.dialog("Petugas Parkir", "Tidak di posisi yang benar...")
            self.gagal_misi()

    def minigame_keseimbangan(self):
        """Misi 16: Minigame Keseimbangan"""
        if self.karakter.misi_selesai >= 16 and 16 in self.karakter.misi_dikunci:
            self.dialog("Penari Jambul", "Misi ini sudah selesai!")
            return
        
        self.dialog("Penari Jambul", "Bisa maintain keseimbangan sambil berdansa?")
        self.dialog(self.karakter.nama, "Mari kita mainkan!")
        
        print("\n" + "="*50)
        print("MINIGAME: KESEIMBANGAN TARI")
        print("="*50)
        print("Tekan tombol sesuai urutan yang muncul!")
        print("Urutan: KIRI KANAN TENGAH KANAN KIRI\n")
        
        urutan_benar = ["K", "N", "T", "N", "K"]
        skor = 0
        
        for i, tombol in enumerate(urutan_benar):
            print(f"Gerakan {i+1}/5: Tekan {tombol} (KIRI=K, KANAN=N, TENGAH=T)")
            input_pemain = input("Input: ").strip().upper()
            
            if input_pemain == tombol:
                print("✅ Benar!")
                skor += 1
            else:
                print(f"❌ Salah! Yang benar adalah {tombol}")
        
        print(f"\nSkor akhir: {skor}/5")
        
        if skor >= 4:
            self.dialog("Penari Jambul", "Luar biasa! Tamu kami sangat terhibur!")
            self.berhasil_misi("misi_16", 100 + skor * 20, 400 + skor * 50)
        elif skor >= 2:
            self.dialog("Penari Jambul", "Lumayan... tapi bisa lebih baik.")
            self.berhasil_misi("misi_16", 50 + skor * 10, 200 + skor * 30)
        else:
            self.dialog("Penari Jambul", "Sayang sekali... coba lagi!")
            self.gagal_misi()

    def minigame_teka_teki(self):
        """Misi 17: Minigame Teka-teki Direktur"""
        if self.karakter.misi_selesai >= 17 and 17 in self.karakter.misi_dikunci:
            self.dialog("Direktur", "Misi ini sudah selesai!")
            return
        
        self.dialog("Direktur", "Ijin saya uji kecerdasan Anda dengan teka-teki!")
        
        print("\n" + "="*50)
        print("MINIGAME: TEKA-TEKI DIREKTUR")
        print("="*50)
        
        teka_teki = [
            {
                "pertanyaan": "Berapa banyak roda yang dimiliki 3 bus?",
                "jawaban": "12",
                "petunjuk": "(setiap bus memiliki 4 roda)"
            },
            {
                "pertanyaan": "Rute transjakarta tertua adalah rute berapa?",
                "jawaban": "1",
                "petunjuk": "(coridor pertama)"
            },
            {
                "pertanyaan": "Berapa banyak halte di rute 1 dari Blok M ke Kota?",
                "jawaban": "13",
                "petunjuk": "(lebih dari 10 tapi kurang dari 15)"
            }
        ]
        
        benar = 0
        for i, q in enumerate(teka_teki):
            print(f"\nTeka-teki {i+1}/3: {q['pertanyaan']}")
            print(f"Petunjuk: {q['petunjuk']}")
            jawab = input("Jawaban Anda: ").strip()
            
            if jawab.lower() == q['jawaban'].lower():
                print("✅ Benar!")
                benar += 1
            else:
                print(f"❌ Salah! Jawaban yang benar adalah {q['jawaban']}")
        
        print(f"\nJawaban benar: {benar}/3")
        
        if benar == 3:
            self.dialog("Direktur", "Sempurna! Anda adalah bus yang cerdas!")
            self.berhasil_misi("misi_17", 150, 600)
        elif benar == 2:
            self.dialog("Direktur", "Cukup bagus! Tapi masih bisa lebih pintar.")
            self.berhasil_misi("misi_17", 100, 400)
        else:
            self.dialog("Direktur", "Anda harus belajar lebih banyak...")
            self.gagal_misi()

    # ==================== MISI SPESIAL ====================
    
    def misi_spesial_teman(self):
        """Misi 19: Bertemu Bus Teman"""
        if self.karakter.misi_selesai >= 19 and 19 in self.karakter.misi_dikunci:
            self.dialog("Bus Teman", "Kita sudah bertemu sebelumnya!")
            return
        
        self.dialog("Sopir 1", "Bus apa yang baru kutemui?")
        
        opsi = {
            "1": self.karakter.bus_type.value,
            "2": "Bus Lamborghini Mewah",
            "3": "Bus Bermerek Baru"
        }
        
        print("\n📋 Siapa bus teman Anda?")
        for k, v in opsi.items():
            print(f"{k}. {v}")
        
        pilihan = input("\nPilihan Anda: ").strip()
        
        self.dialog("Bus Baru", f"Halo! Senang bertemu denganmu, {self.karakter.nama}!")
        self.dialog(self.karakter.nama, "Aku juga senang bertemu denganmu!")
        
        self.dialog("Bus Baru", "Mari kita bekerja sama melayani penumpang!")
        self.dialog(self.karakter.nama, "Ide bagus! Kita bersama lebih kuat!")
        
        self.berhasil_misi("misi_19", 120, 500)

    def misi_spesial_legendaris(self):
        """Misi 20: Bertemu Bus Legendaris"""
        if self.karakter.misi_selesai >= 20 and 20 in self.karakter.misi_dikunci:
            self.dialog("Bus Legendaris", "Kami sudah pernah bertemu...")
            return
        
        self.dialog("Senioritas", "Ada kehadiran yang istimewa... Bus Legendaris dari jaman dulu!")
        
        self.dialog("Bus Legendaris", "Sudah lama aku tidak bertemu bus muda sepertimu...")
        self.dialog(self.karakter.nama, "Anda adalah! Saya mendengar banyak tentang Anda!")
        
        self.dialog("Bus Legendaris", "Dengarkan, ada sesuatu yang gelap mendekat ke kota kita.")
        self.dialog("Bus Legendaris", "Ada satu bus jahat bernama 'Raja Jahat Bus' yang ingin menguasai semua rute!")
        self.dialog("Bus Legendaris", "Hanya Anda yang dapat menghentikannya. Apakah Anda siap?")
        
        opsi = {
            "1": "Saya siap menghadapi apapun!",
            "2": "Saya takut...",
            "3": "Saya perlu waktu untuk berpikir"
        }
        
        pilihan = self.pilihan(opsi)
        
        if pilihan == "1":
            self.dialog("Bus Legendaris", "Semangat itu yang kita butuhkan! Pergi dan selamatkan kota!")
            self.berhasil_misi("misi_20", 180, 800)
        elif pilihan == "2":
            self.dialog("Bus Legendaris", "Ketakutan itu normal... Tapi ingat, warga kota membutuhkanmu!")
            self.berhasil_misi("misi_20", 120, 600)
        else:
            self.dialog("Bus Legendaris", "Baik... Saat Anda siap, datanglah ke Istana Jahat.")
            self.berhasil_misi("misi_20", 100, 500)

    def misi_final_spesial(self):
        """Misi 21: Misi Final Spesial - hanya placeholder untuk menunjukkan pola"""
        if self.karakter.misi_selesai >= 20:
            self.dialog("Narator", "Anda telah menyelesaikan 20 misi! Saatnya misi final!")
            self.misi_pertarungan_akhir()

    # ==================== PERTARUNGAN FINAL DAN ENDING ====================
    
    def misi_pertarungan_akhir(self):
        """Misi 21: Pertarungan Akhir Melawan Raja Jahat Bus"""
        self.lokasi_sekarang = Lokasi.ISTANA_JAHAT
        
        self.dialog("Narator", "Anda memasuki Istana Raja Jahat Bus...")
        time.sleep(1)
        
        self.dialog("Raja Jahat Bus", "Akhirnya Anda datang juga! Bersiaplah untuk kekalahan!")
        self.dialog(self.karakter.nama, "Saya di sini untuk menyelamatkan kota ini!")
        
        print("\n" + "="*60)
        print("⚔️ PERTARUNGAN FINAL MELAWAN RAJA JAHAT BUS ⚔️".center(60))
        print("="*60)
        print("\nMemilih strategi sangat penting untuk ending yang berbeda!\n")
        
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
        """Bad Ending: Serangan Langsung"""
        print("\n" + "="*60)
        print("BAD ENDING: KEKALAHAN TRAGIS".center(60))
        print("="*60 + "\n")
        
        self.dialog(self.karakter.nama, "Saya akan mengalahkanmu dengan kekuatan murni!")
        
        # Pertarungan agresif tapi berisiko
        musuh_hp = 150
        
        for i in range(4):
            print(f"\nRonde {i+1}:")
            self.dialog(self.karakter.nama, "Serangu dengan semua kekuatanku!")
            damage = random.randint(30, 50)
            musuh_hp -= damage
            
            if musuh_hp > 0:
                self.dialog("Raja Jahat Bus", "Serangan yang kuat... tapi tidak cukup!")
                damage_balik = random.randint(40, 60)
                self.karakter.hp -= damage_balik
                
                if self.karakter.hp <= 0:
                    print("\n💔 Pertarungan yang melelahkan...")
                    self.dialog(self.karakter.nama, "Aku... kalah... kota ini...")
                    self.dialog("Raja Jahat Bus", "HAH! Ini petunjaran sia-sia mu!")
                    
                    time.sleep(2)
                    print("\n" + "="*60)
                    print("LAYAR HITAM...")
                    time.sleep(2)
                    print("""
╔════════════════════════════════════════════════════════════╗
║                     🌙 BAD ENDING 🌙                       ║
║                                                            ║
║  Kota terserah pada kegelapan. Raja Jahat Bus menguasai   ║
║  semua rute transportasi. Penumpang menderita di bawah    ║
║  tirani busnya yang kejam.                                ║
║                                                            ║
║  Meskipun Anda berjuang dengan sepenuh hati, Anda tidak   ║
║  memiliki pengetahuan dan kecerdasan untuk mengalahkan    ║
║  musuh yang sangat kuat ini.                              ║
║                                                            ║
║  Pesan: Kekuatan saja tidak cukup.                        ║
║          Kerendahan hati dan bijak itu penting.           ║
║                                                            ║
║  Credits: Terima kasih telah bermain sampai akhir.        ║
╚════════════════════════════════════════════════════════════╝
                    """)
                    self.game_over()
                    return

    def ending_baik(self):
        """Good Ending: Pertahanan Bertahap dan Seimbang"""
        print("\n" + "="*60)
        print("GOOD ENDING: KEMENANGAN HEROIK".center(60))
        print("="*60 + "\n")
        
        self.dialog(self.karakter.nama, "Saya tidak untuk menghancurkan... tapi untuk melindungi!")
        self.dialog(self.karakter.nama, "Mari kita berakhir ini!")
        
        # Pertarungan seimbang
        musuh_hp = 120
        ronde = 0
        
        while self.karakter.hp > 0 and musuh_hp > 0:
            ronde += 1
            print(f"\nRonde {ronde}:")
            print(f"HP Anda: {self.karakter.hp}, HP Raja Jahat Bus: {musuh_hp}")
            
            opsi = {
                "1": "Serang",
                "2": "Bertahan",
                "3": "Berdoa untuk kemenangan"
            }
            
            pilihan = self.pilihan(opsi)
            
            if pilihan == "1":
                damage = random.randint(20, 40)
                musuh_hp -= damage
                self.dialog(self.karakter.nama, f"Seranganku! {damage} damage!")
            elif pilihan == "2":
                damage_incoming = random.randint(10, 25)
                damage_kecil = damage_incoming // 2
                self.karakter.hp -= damage_kecil
                self.dialog(self.karakter.nama, "Aku bertahan! Serangan dilesatkan!")
            else:
                self.dialog(self.karakter.nama, "Walau muncul lagi, semangat warga kota...")
                damage = random.randint(25, 35)
                musuh_hp -= damage
            
            if musuh_hp > 0:
                damage_musuh = random.randint(15, 30)
                self.karakter.hp -= damage_musuh
                self.dialog("Raja Jahat Bus", f"Daganknya! {damage_musuh} damage ke busmu!")
        
        print("\n" + "="*60)
        print("KEMENANGAN!!!".center(60))
        print("="*60)
        
        self.dialog("Narator", "Cahaya matahari menyingsing... kegelapan surut...")
        
        time.sleep(2)
        print("""
╔════════════════════════════════════════════════════════════╗
║                   ☀️ GOOD ENDING ☀️                        ║
║                                                            ║
║  Dengan keberanian dan keseimbangan, Anda berhasil        ║
║  mengalahkan Raja Jahat Bus!                              ║
║                                                            ║
║  Kota kembali damai. Transportasi umum berjalan normal.   ║
║  Penumpang bersukacita dan menghargai jasa-jasa Anda.     ║
║                                                            ║
║  Anda menjadi PAHLAWAN TRANSJAKARTA yang terkenal.        ║
║  Cerita Anda dikenang sepanjang masa.                     ║
║                                                            ║
║  Pesan: Keseimbangan dan ketekunan membawa kemenangan.    ║
║                                                            ║
║  Credits: Terima kasih telah bermain sampai akhir!        ║
╚════════════════════════════════════════════════════════════╝
        """)
        self.game_over()

    def ending_rahasia(self):
        """Secret Ending: Strategi Cerdas dan Taktik"""
        print("\n" + "="*60)
        print("SECRET ENDING: KEMENANGAN LUAR BIASA".center(60))
        print("="*60 + "\n")
        
        self.dialog(self.karakter.nama, "Saya tahu kelemahan Anda...")
        self.dialog(self.karakter.nama, "Dengan data dan strategi, saya akan mengalahkanmu!")
        
        # Pertarungan dengan puzzle
        musuh_hp = 100
        ronde = 0
        
        while musuh_hp > 0:
            ronde += 1
            print(f"\nRonde {ronde}: Setiap ronde, selesaikan puzzle untuk damage besar!")
            
            # Puzzle sederhana
            angka1 = random.randint(1, 10)
            angka2 = random.randint(1, 10)
            jawaban_benar = angka1 + angka2
            
            print(f"Puzzle: {angka1} + {angka2} = ?")
            try:
                jawaban = int(input("Jawaban Anda: "))
                
                if jawaban == jawaban_benar:
                    damage = 35 + random.randint(10, 20)
                    musuh_hp -= damage
                    self.dialog(self.karakter.nama, f"Ansalah! Serangan kombinasi! {damage} damage besar!")
                else:
                    damage = 15
                    musuh_hp -= damage
                    self.dialog(self.karakter.nama, f"Serangan biasa! {damage} damage!")
            except:
                self.dialog(self.karakter.nama, "Input tidak valid!")
                damage = 10
                musuh_hp -= damage
            
            if musuh_hp > 0:
                print(f"HP Raja Jahat Bus: {musuh_hp}")
                self.dialog("Raja Jahat Bus", "Strategi yang cerdas... tapi tidak akan cukup!")
        
        self.dialog("Raja Jahat Bus", "Tidak mungkin! Aku kalah pada bus yang lebih cerdas!")
        
        time.sleep(2)
        print("""
╔════════════════════════════════════════════════════════════╗
║              🌟 SECRET ENDING: TRANSCENDENTA 🌟            ║
║                                                            ║
║  Dengan kecerdasan dan taktik yang brilian, Anda lebih    ║
║  dari sekadar memenangkan pertarungan...                  ║
║                                                            ║
║  Anda MENGUBAH hati Raja Jahat Bus!                       ║
║                                                            ║
║  Dialog tersembunyi terbuka:                              ║
║  Raja Jahat Bus: "Aku jadi mengerti... aku salah selama   ║
║                  ini. Terima kasih telah mengajarkanku    ║
║                  arti berbagi dan melayani."              ║
║                                                            ║
║  Dia berubah menjadi bus baik dan membantu Anda          ║
║  melayani penumpang!                                      ║
║                                                            ║
║  Kota mengalami RENAISSANCE TRANSPORTASI!                ║
║  Semua bus bekerja sama dalam harmoni sempurna.          ║
║                                                            ║
║  Anda tidak hanya PAHLAWAN, tapi PENDAMAI DUNIA!         ║
║  Kisah Anda menjadi LEGENDA ABADI di Transjakarta!       ║
║                                                            ║
║  Pesan: Kecerdasan dan empati adalah kekuatan terbesar.  ║
║                                                            ║
║  Credits: Terima kasih telah menemukan ending rahasia!    ║
║           Ending ini adalah puncak cerita kami.           ║
╚════════════════════════════════════════════════════════════╝
        """)
        self.game_over()

    def game_over(self):
        """Layar game over"""
        time.sleep(3)
        print("""
        
╔═══════════════════════════════════════════════════════════╗
║                  🎮 GAME OVER 🎮                          ║
║                                                           ║
║           Terima kasih telah bermain!                    ║
║                                                           ║
║    Statistik Akhir:                                       ║
║    - Misi Selesai: {}/21                                 ║
║    - Uang: Rp{}                                          ║
║    - Level: {}                                            ║
║    - Total EXP: {}                                        ║
║                                                           ║
║    Mainkan lagi untuk menemukan ending berbeda!          ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
        """.format(self.karakter.misi_selesai, self.karakter.uang, 
                   self.karakter.level, self.karakter.exp))
        
        exit()

    def berhasil_misi(self, misi_id, exp_reward, uang_reward):
        """Misi berhasil"""
        self.karakter.misi_dikunci.add(int(misi_id.split("_")[1]))
        self.karakter.misi_selesai += 1
        self.karakter.exp += exp_reward
        self.karakter.uang += uang_reward
        
        # Check level up
        if self.karakter.exp >= self.karakter.exp_untuk_level_up:
            self.karakter.level += 1
            self.karakter.exp = 0
            self.karakter.exp_untuk_level_up = int(self.karakter.exp_untuk_level_up * 1.2)
            self.dialog("Narator", f"🎉 LEVEL UP! Anda sekarang level {self.karakter.level}!")
        
        print("\n" + "="*50)
        print("✅ MISI BERHASIL!")
        print("="*50)
        print(f"EXP Diperoleh: +{exp_reward}")
        print(f"Uang Diperoleh: +Rp{uang_reward}")
        print(f"Total Misi Selesai: {self.karakter.misi_selesai}/21")
        
        if self.karakter.misi_selesai == 20:
            self.dialog("Narator", "Anda telah menyelesaikan 20 misi! Satu misi terakhir menunggu Anda!")
        
        print("="*50 + "\n")

    def gagal_misi(self):
        """Misi gagal"""
        print("\n" + "="*50)
        print("❌ MISI GAGAL!")
        print("="*50)
        print("Coba lagi dengan strategi berbeda...")
        print("="*50 + "\n")

    def lihat_inventori(self):
        """Lihat inventori pemain"""
        print("\n" + "="*50)
        print("📦 INVENTORI")
        print("="*50)
        if self.karakter.inventory:
            for item in self.karakter.inventory:
                print(f"  - {item}")
        else:
            print("  Inventori kosong")
        print("="*50 + "\n")

    def istirahat(self):
        """Istirahat untuk isi energi"""
        print("\n" + "="*50)
        print("😴 ISTIRAHAT")
        print("="*50)
        self.dialog("Narator", "Anda beristirahat di hotel nyaman...")
        time.sleep(2)
        
        self.karakter.energi = self.karakter.max_energi
        self.karakter.hp = self.karakter.max_hp
        
        self.dialog("Narator", "Anda merasa segar kembali setelah istirahat!")
        print("="*50 + "\n")

    def run(self):
        """Menjalankan game"""
        self.intro_game()
        self.pilih_karakter()
        self.tampilkan_map()
        self.main_menu()

# ==================== MAIN ====================

def main():
    """Fungsi main untuk memulai game"""
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
