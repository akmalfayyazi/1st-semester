import math

# Membaca input dari pengguna
n = int(input())

# Fungsi untuk memeriksa apakah n adalah bilangan prima
def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True  # 2 adalah bilangan prima
    if number % 2 == 0:
        return False  # Semua bilangan genap lebih besar dari 2 bukan bilangan prima
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

# Mengecek apakah n adalah bilangan prima
if is_prime(n):
    print("IT IS A PRIME")
else:
    print("IT IS NOT A PRIME")
