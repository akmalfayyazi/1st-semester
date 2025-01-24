# masukan data tanah
panjang_tanah = int(input('panjang tanah: '))
lebar_tanah = int(input('lebar tanah: '))

# masukkan data rumah
panjang_rumah = int(input('panjang rumah: '))
lebar_rumah = int(input('lebar rumah: '))

# luas tanah kosong
luas_tanah_kosong = (int(panjang_tanah * lebar_tanah) - (panjang_rumah * lebar_rumah))

# waltu motong rumput
print(f"waktu motong rumput {int(luas_tanah_kosong / 2)} detik" )
