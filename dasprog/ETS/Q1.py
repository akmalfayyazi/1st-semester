# tentang modus juga
n = int(input()) #input 3
results = []

for _ in range(n):
    m = int(input())
    angka = list(map(int, input().split()))
    if m == 1:
        print('-1')
        continue
    wadah = [0]*10 #menginisiasi wadah yang mau diakses
    for i in angka:
        wadah[i] += 1
    print(wadah)
    jumlah_angka_terbesar_yang_muncul = max(wadah)
    simpan_modus = []
    for i in range(len(wadah)):
        if wadah[i] == max(wadah):
            simpan_modus.append(i)
    if len(simpan_modus) == 1:
        print(str(jumlah_angka_terbesar_yang_muncul)+' * '+str(simpan_modus[0])+ ' = ', end='')
        print(simpan_modus[0]*jumlah_angka_terbesar_yang_muncul)
    else:
        p = 1
        s = ''
        for i in range(len(simpan_modus)):
            s += str(simpan_modus[i])
            if i != len(simpan_modus)-1:
                s += '*'
        s += ' = '
        print(s, end='')
        for i in simpan_modus:
            p *= i
        print(p)