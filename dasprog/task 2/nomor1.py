diskon = 0.20
penambahanPajak = 0.05
totalPembelian = float(input("masukkan total pembelian : "))
statusPembeli = input("status pembeli mahasiswa? (ya / tidak) :")

if statusPembeli == "ya":
    total_pembelian_mahasiswa = totalPembelian - (totalPembelian * diskon)
    total_setelah_pajak = total_pembelian_mahasiswa + (total_pembelian_mahasiswa * 0.05)
    print(f"{total_setelah_pajak:.2f}")
else:
    total_pembelian_orang = totalPembelian + (totalPembelian * penambahanPajak)
    print(f"{total_pembelian_orang:.2f}")



