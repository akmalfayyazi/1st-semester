def move_number_to_front(daftar, jumlah_angka_pindah, berapa_kali_pindah):
    # Ulangi langkah pemindahan sebanyak berapa_kali_pindah kali
    for _ in range(berapa_kali_pindah):
        # Pindahkan jumlah_angka_pindah angka dari belakang ke depan
        daftar = daftar[-jumlah_angka_pindah:] + daftar[:-jumlah_angka_pindah]
    return daftar

def main():
    # Membaca input
    daftar = list(map(int, input("Masukkan 7 angka: ").split()))
    jumlah_angka_pindah = int(input("Masukkan jumlah angka yang dipindahkan: ").strip())
    berapa_kali_pindah = int(input("Masukkan jumlah pemindahan: ").strip())
    d, e, f = map(int, input("Masukkan tiga indeks: ")
    .split())
    
    # Mengubah daftar sesuai dengan aturan
    modified_list = move_number_to_front(daftar, jumlah_angka_pindah, berapa_kali_pindah)
    
    # Mengambil angka dari indeks yang diinginkan
    result = [modified_list[d], modified_list[e], modified_list[f]]
    
    # Menampilkan hasil
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
