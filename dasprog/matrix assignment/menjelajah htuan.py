r, c, N = map(int,input().split())

matriks =[]
for _ in range(c):
    a = list(map(int,input().split()))
    matriks.append(a)
moves = input()

i ,j = 0 , 0
emas1 = 0 + matriks[0][0]
emas2 = matriks[i][j]

for move in moves:
    if move == 'R':
        j += 1
        if j > r:
            print(emas1)
            print("gerakanmu salah bung!")
            break
        else:
            emas1 += 3
            emas1 += matriks[i][j]
            matriks[i][j] = 0
    elif move == 'U':
        i -= 1
        if i < 0:
            print(emas1)
            print("gerakanmu salah bung!")
            break
        else:
            emas1 += 3
            emas1 += matriks[i][j]
            matriks[i][j] = 0
    elif move == 'L':
        j -= 1
        if j < 0:
            print(emas1)
            print("gerakanmu salah bung!")
            break
        else:
            emas1 -= 2
            emas1 += matriks[i][j]
            matriks[i][j] = 0
    elif move == 'D':
        i += 1
        if i > c:
            print(emas1)
            print("gerakanmu salah bung!")
            break
        else:
            emas1 -= 2
            emas1 += matriks[i][j]
            matriks[i][j] = 0
    else:
        print(emas1)