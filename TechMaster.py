from abc import ABC, abstractmethod

class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar, stok_awal=0):
        self.nama = nama
        self.__harga_dasar = harga_dasar
        self.__stok = stok_awal

    @property
    def stok(self):
        return self.__stok
    
    @property
    def harga_dasar(self):
        return self.__harga_dasar

    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
            return False
        self.__stok += jumlah
        print(f"Berhasil menambahkan stok {self.nama}: {self.__stok} unit.")
        return True

    def kurangi_stok(self, jumlah):
        if jumlah > self.__stok:
            print(f"Stok {self.nama} tidak mencukupi!")
            return False
        self.__stok -= jumlah
        return True

    @abstractmethod
    def tampilkan_detail(self, jumlah_beli):
        pass
    
    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass

class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor, stok_awal=0):
        super().__init__(nama, harga_dasar, stok_awal)
        self.processor = processor
    
    def hitung_harga_total(self, jumlah):
        pajak = self.harga_dasar * 0.10
        harga_per_unit = self.harga_dasar + pajak
        return harga_per_unit * jumlah, pajak
    
    def tampilkan_detail(self, jumlah_beli):
        total, pajak = self.hitung_harga_total(jumlah_beli)
        # Format titik untuk ribuan (Indonesia)
        h_str = f"{self.harga_dasar:,.0f}".replace(',', '.')
        p_str = f"{pajak:,.0f}".replace(',', '.')
        t_str = f"{total:,.0f}".replace(',', '.')
        
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f"  Harga Dasar: Rp {h_str} | Pajak(10%): Rp {p_str}")
        print(f"  Beli: {jumlah_beli} unit | Subtotal: Rp {t_str}")
        return total

class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera, stok_awal=0):
        super().__init__(nama, harga_dasar, stok_awal)
        self.kamera = kamera
    
    def hitung_harga_total(self, jumlah):
        pajak = self.harga_dasar * 0.05
        harga_per_unit = self.harga_dasar + pajak
        return harga_per_unit * jumlah, pajak
    
    def tampilkan_detail(self, jumlah_beli):
        total, pajak = self.hitung_harga_total(jumlah_beli)
        h_str = f"{self.harga_dasar:,.0f}".replace(',', '.')
        p_str = f"{pajak:,.0f}".replace(',', '.')
        t_str = f"{total:,.0f}".replace(',', '.')
        
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f"  Harga Dasar: Rp {h_str} | Pajak(5%): Rp {p_str}")
        print(f"  Beli: {jumlah_beli} unit | Subtotal: Rp {t_str}")
        return total

def proses_transaksi(daftar_barang):
    print("\n--- \nSTRUK TRANSAKSI ---")
    total_tagihan = 0
    for index, (barang, jumlah) in enumerate(daftar_barang, 1):
        print(f"{index}. ")
        subtotal = barang.tampilkan_detail(jumlah)
        total_tagihan += subtotal
        barang.kurangi_stok(jumlah)
    
    total_tagihan_str = f"{total_tagihan:,.0f}".replace(',', '.')
    print("\n" + "-"*40)
    print(f"TOTAL TAGIHAN: Rp {total_tagihan_str}")
    print("-"*40)

def main():
    print("--- SETUP DATA ---")
    laptop1 = Laptop("ROG Zephyrus", 20000000, "Ryzen 9")
    smartphone1 = Smartphone("iPhone 13", 15000000, "12MP")
    
    laptop1.tambah_stok(10)
    smartphone1.tambah_stok(-5)
    smartphone1.tambah_stok(20)
    
    keranjang = [(laptop1, 2), (smartphone1, 1)]
    proses_transaksi(keranjang)
    
    print(f"\n--- SISA STOK ---")
    print(f"{laptop1.nama}: {laptop1.stok} unit")
    print(f"{smartphone1.nama}: {smartphone1.stok} unit")

if __name__ == "__main__":
    main()