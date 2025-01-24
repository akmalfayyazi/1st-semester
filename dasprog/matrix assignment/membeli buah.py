N, K = map(int,input().split())
A = list(map(int,input().split()))
beli = 0

for j in range(N):
    if A[j] <= K:
        beli += 1

print(beli)