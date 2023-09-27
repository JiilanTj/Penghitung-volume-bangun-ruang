# Fungsi untuk menghitung volume bola
def hitung_volume_bola(radius):
    return (4/3) * 3.14159265359 * radius**3

# Fungsi untuk menghitung volume tabung
def hitung_volume_tabung(radius, tinggi):
    return 3.14159265359 * radius**2 * tinggi

# Fungsi untuk menghitung volume limas segitiga
def hitung_volume_limas_segitiga(alas, tinggi):
    return (1/3) * (alas**2) * tinggi

# Fungsi untuk login
def login():
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")

    if nama == "Your Name" and nim == "999":
        print("Login berhasil!\n")
        return True
    else:
        print("Login gagal. Coba lagi.\n")
        return False

# Fungsi utama
def main():
    while True:
        if login():
            print("Pilih bangun ruang:")
            print("1. Bola")
            print("2. Tabung")
            print("3. Limas Segitiga")
            pilihan = input("Masukkan pilihan (1/2/3): ")

            if pilihan == "1":
                radius = float(input("Masukkan jari-jari bola: "))
                volume = hitung_volume_bola(radius)
                print(f"Volume bola dengan jari-jari {radius} adalah {volume}\n")
            elif pilihan == "2":
                radius = float(input("Masukkan jari-jari tabung: "))
                tinggi = float(input("Masukkan tinggi tabung: "))
                volume = hitung_volume_tabung(radius, tinggi)
                print(f"Volume tabung dengan jari-jari {radius} dan tinggi {tinggi} adalah {volume}\n")
            elif pilihan == "3":
                alas = float(input("Masukkan panjang sisi alas limas segitiga: "))
                tinggi = float(input("Masukkan tinggi limas segitiga: "))
                volume = hitung_volume_limas_segitiga(alas, tinggi)
                print(f"Volume limas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {volume}\n")
            else:
                print("Pilihan tidak valid.\n")

            ulang = input("Apakah ingin menghitung volume bangun ruang lainnya? (ya/tidak): ")
            if ulang.lower() != "ya":
                break

if __name__ == "__main__":
    main()
