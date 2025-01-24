# masukkan berapa jam (2)
jam = int(input('masukkan berapa jam: '))

# masukkan menit (30)
menit = int(input('masukkan berapa menit: '))

# waktu total
total = jam + (menit / 60)

# suhu
suhu = (4 * (total ** 2) / (total + 2)) - 20

# hasil perkiraan suhu
print(f'perkiraan suhu dalam lemari: {suhu:.2f} c')