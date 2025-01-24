#memperkirakan berapa banyak bagian utuh dari suatu kelompok
# masukkan data
jumlah_siswa_terdafatar = int(input("siswa terdaftar: "))

# siswa setiap bagian
siswa_setiap_bagian = 30 

# bagian yang diperlukan
total_bagian_dibutuhkan = jumlah_siswa_terdafatar // siswa_setiap_bagian

# sisanya
sisa = jumlah_siswa_terdafatar % siswa_setiap_bagian

print(f"siswa terdaftar: {jumlah_siswa_terdafatar}\njumlah bagian dibutuhkan: {total_bagian_dibutuhkan}\nsiswa tersosa: {sisa}")


