N,M = map(int, input().split())
matrix = []

for i in range(N):
    masuk = list(map(str,input().split()))
    matrix.append(masuk)

duduk = set()
for i in range(N):
    for j in range(M):
        if(i - 1 < 0 or i + 1 >= N or j - 1 < 0 or j + 1 >= M):
            continue
        if (matrix[i][j - 1] != 0 and j - 1 >= 0  ):
            duduk.add(matrix[i][j - 1])
        if(matrix[i][j + 1] != 0  and j + 1 < M ):
            duduk.add(matrix[i][j + 1])
        if(matrix[i - 1][j] !=0 and i - 1 >= 0):
            duduk.add(matrix[i- 1][j])
        if(matrix[i + 1][j] != 0 and i + 1 < N):
            duduk.add(matrix[i + 1][j])
        if(matrix[ i - 1][j + 1] !=0 and i - 1 >= 0 and j + 1 < M):
            duduk.add(matrix[ i - 1][j + 1])
        if(matrix[i - 1][j - 1] !=0 and i - 1 >= 0 and j - 1 >= 0):
            duduk.add(matrix[i - 1][j - 1])
        if(matrix[i + 1][j - 1] != 0 and i + 1 < N and j - 1 >= 0):
            duduk.add(matrix[i + 1][j - 1])
        if(matrix[i + 1][j + 1] != 0 and i + 1 < N and j + 1 < M):
            duduk.add(matrix[i + 1][j + 1])

duduk.remove("0")
print(len(duduk))