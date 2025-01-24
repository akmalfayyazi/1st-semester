t = int(input())
harga = list(map(int, input().split()))

counter = [0] * t

for i in harga:
    counter[i] += 1
print(counter)

modus = 0

for i in counter:
    if i > modus:
        modus = i
print(modus)

angka_modus = []

for i in range(len(counter)):
    if counter[i] == modus:
        angka_modus.append(i)
print(angka_modus)

modus_tergede = 0

for i in range(len(angka_modus)):
    if angka_modus[i] > modus_tergede:
        modus_tergede = angka_modus[i]
print(modus_tergede)