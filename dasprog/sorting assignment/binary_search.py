def binary_search(item, target):
    left = 0
    right = len(item) - 1

    while left <= right:
        mid = right // 2  # Perbaiki cara hitung mid
        mid_val = item[mid]
        if mid_val == target:
            return mid  # Mengembalikan indeks
        elif target < mid_val:
            right = mid - 1  # Menggunakan assignment (=)
        else:
            left = mid + 1  # Menggunakan assignment (=)

    return None  # Jika tidak ditemukan

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = 2

print(binary_search(a, b))  # Output: 2
