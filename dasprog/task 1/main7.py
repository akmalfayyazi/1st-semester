# program untuk menghitung btu panas yang disalurkan ke sebuah rumah
energi_barel = 5800000
galon_perbarel = 42
efisiensi = 0.65

# jumlah galon 100
galon = int(input('masukkan total galon: '))

# jumlah barel
jumlah_barel = galon / galon_perbarel

# total energi
energi = jumlah_barel * energi_barel

# akhir
energi_akhir = energi * efisiensi

print(f'jumlah btu panas yang dihasilkan: {energi_akhir:.2f} btu')