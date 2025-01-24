#cairan dalam kantong 100
volume_cairan = int(input("volume cairan: "))

#menit yang dibutuhkan untuk menginfus cairan 20
jumlah_menit = int(input("jumlah menit: "))

#kecepatan infus dalam
kecepatan_infus = int(volume_cairan / jumlah_menit) * 60

#volume cairan dan kecepatan infus
print(f"volume cairan: {volume_cairan} ml\nKecepatan infus: {kecepatan_infus} ml/jam")

