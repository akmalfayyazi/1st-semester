t = int(input())
arr = []

for i in range(t):
   
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    
    q = int(input())
    
    jumlah_sekarang = sum(A[:k])

    max = jumlah_sekarang
    min = jumlah_sekarang
    # Sliding window 

    for i in range(1, k+1):
        jumlah_sekarang = sum(A[:i])
        max = max(max, jumlah_sekarang)
        min = min(min, jumlah_sekarang)
        for j in range (1, n - i + 1):
            jumlah_sekarang = jumlah_sekarang - A[j - 1] + A[j + i - 1]
            max = max(max, jumlah_sekarang)
            min = min (min, jumlah_sekarang)
    
    if (q == 1):
        arr.append(max)
    elif ( q == 2):
        arr.append(min)

for a in arr:
    print(a)