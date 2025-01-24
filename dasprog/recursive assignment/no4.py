def odd_number(n):
    a = 0
    for i in n:
        if i % 2 != 0:
            a += 1
    return a

n = list(map(int, input().split()))
print(odd_number(n))