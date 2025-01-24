def last_man_standing(n, c):
    # Buat array untuk menentukan pemenang pada setiap jumlah bola
    winning_position = [False] * (n + 1)

    # Iterasi untuk menentukan apakah pada jumlah bola tertentu, pemain yang memulai bisa menang
    for i in range(1, n + 1):
        if i >= 1 and not winning_position[i - 1]:
            winning_position[i] = True
        elif i >= 2 and not winning_position[i - 2]:
            winning_position[i] = True
        elif i >= 5 and not winning_position[i - 5]:
            winning_position[i] = True

    # Jika c = 1, berarti Lala yang mulai
    if c == 1:
        return "Lala" if winning_position[n] else "Lili"
    else:
        return "Lili" if winning_position[n] else "Lala"

# Input
n, c = map(int, input("Masukkan jumlah bola dan pemain pertama (1 untuk Lala, 2 untuk Lili): ").split())

# Output
print(last_man_standing(n, c))
