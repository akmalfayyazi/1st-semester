x1, y1 = map(int, input().split()) # Titik tengah lingkaran
x2, y2 = map(int, input().split()) # Titik awal melangkah
x3, y3 = map(int, input().split()) # Titik akhir melangkah
jarak_raja_lingkaran = ((x1-x2)*2+(y1-y2)*2)
jarak_tujuan_lingkaran = ((x1-x3)*2+(y1-y3)*2)
jarak_perjalanan = ((x2-x3)*2+(y2-y3)*2)
if jarak_tujuan_lingkaran>jarak_perjalanan :
    print("Yes")
else:
    print("No")
