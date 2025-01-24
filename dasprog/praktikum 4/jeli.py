def digit_root_sum(angka):
    while angka >= 10:
        angka = sum(int(i) for i in str(angka))
    return angka

def sort_by_digit_root(lst):
    a = sorted(lst)
    return sorted(a, key=digit_root_sum)

a = list(map(int, input().split()))
print(*sort_by_digit_root(a))    