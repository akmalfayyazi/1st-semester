# Input format
data = list(map(int, input().split()))

# n adalah jarak maksimum yang bisa dilompat oleh B
n = data[0]

# Jarak antar pilar (A->Bee, Bee->C, C->D, D->E)
distances = data[1:]

# Cek apakah ada jarak yang lebih besar dari n
# all() untuk memeriksa apakah semua true
if all(distance <= n for distance in distances):
    print("YES HE CAN")
else:
    print("NO HE CAN'T")
