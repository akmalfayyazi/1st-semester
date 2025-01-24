import sys
sys.setrecursionlimit(10**9)

mod = 10**9 + 7
x = {}

def variasi(n):
    if n in x:
        return x[n]
    if n == 0 or n ==1:
        return 0
    elif n == 2 or n == 3:
        return 1 
    elif n == 4 or n == 5:
        return 2
    else:
        x[n] = (variasi(n-2) + variasi(n-3)+ variasi(n-4)) % mod
        return x[n]
    
ukuran_pancong = int(input().strip())
print(variasi(ukuran_pancong))
