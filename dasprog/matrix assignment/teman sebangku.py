N, r, c = map(int,input().split())
matrix = [[0 for _ in range(r)] for _ in range(c)]

for i in range(N):
    X, Y, Z = map(int,input().split())
    X = matrix[Y-1][Z-1]    

sebelah = [0] * N

for i in range(0, r):
    for j in range(0, c):
        if matrix[i][j] != 0:
            if matrix[i][(j - 1)] > 0:
                sebelah[(matrix[i][j] - 1)] = matrix[i][(j - 1)]
            elif matrix[i][(j + 1)] > 0:
                sebelah[(matrix[i][j] - 1)] = matrix[i][(j + 1)]
            else:
                sebelah[(matrix[i][j] - 1)] = 0
for i in sebelah:
    print(i)