N, M = map(int,input().split())
P = list(map(int,input().split())) #harga
C = list(map(int,input().split())) #uang
harga = 0 #jika jumlah harga == len(P) maka semua positif
uang = 0 #jika jumlah uang == len(C) maka semua negatif
utang = 0
temp1 = 0
temp2 = 0

for i in P:
    if i > 0:
        harga += 1 #maka ada positif
        temp1 += i

for j in C:
    if j < 0:
        uang += 1 #maka ada negatif
        temp2 += j

if harga == len(P) and uang == 0: #ini kalau barang dan uang positif semua
    utang = min(C) - sum(P)
elif harga == 0 and uang == len(C):#ini kalau barang dan uang negatif semua
    utang = sum(C) - max(P)
elif harga > 0 and uang > 0:#ini kalau ada yang positif dan negatif
    utang = temp2 - temp1

print(utang)