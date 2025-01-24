N = int(input())

for i in range(1, N+1):
    for r in range(1, N -i + 1):
        print(" ", end="")

    value = 1

    for r in range(1, i+1):
        print(value, "", end="")
        value = value * (i-r)//r

    print()