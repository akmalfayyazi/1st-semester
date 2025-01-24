N = int(input())
B = list(map(int, input().split()))

result = 1
for i in range(N):
    for j in range(1+i, N):
        if(B[i] != B[j]):
            result *= B[i]^B[j]
        else:
            result = 0
            break
print(result)