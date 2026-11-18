class Kendaraan:
    
    bahan_bakar = "Bensin"

    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"Kendaraan {self.merk} warna {self.warna} tahun {self.tahun}"

kendaraan1 = Kendaraan("Toyota Avanza", "Hitam", 2022)
kendaraan2 = Kendaraan("Honda Beat", "Merah", 2023)

print("=== Akses Instance Attribute (berbeda tiap object) ===")
print(kendaraan1.info_kendaraan())
print(kendaraan2.info_kendaraan())
print(f"Merk kendaraan1: {kendaraan1.merk}")
print(f"Merk kendaraan2: {kendaraan2.merk}")

print("\n=== Akses Class Attribute (sama untuk semua object) ===")
print(f"Bahan bakar lewat class      : {Kendaraan.bahan_bakar}")
print(f"Bahan bakar lewat kendaraan1 : {kendaraan1.bahan_bakar}")
print(f"Bahan bakar lewat kendaraan2 : {kendaraan2.bahan_bakar}")

print("\n=== Mengubah Class Attribute (berlaku untuk semua object) ===")
Kendaraan.bahan_bakar = "Pertalite"
print(f"kendaraan1: {kendaraan1.bahan_bakar}")
print(f"kendaraan2: {kendaraan2.bahan_bakar}")

print("\n=== Mengubah Instance Attribute (hanya object itu saja) ===")
kendaraan1.warna = "Putih"
print(kendaraan1.info_kendaraan())
print(kendaraan2.info_kendaraan())