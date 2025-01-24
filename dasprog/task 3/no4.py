def is_prime(limit):
    urutan = [True] * (limit + 1)  
    urutan[0] = urutan[1] = False   
    prime = []
    for angka in range(2, limit + 1):
        if urutan[angka]:
            prime.append(angka)
            for pangkat in range(angka * angka, limit + 1, angka):
                urutan[pangkat] = False
    return prime

# MAX 78498
limit = 1000000  

prime = is_prime(limit)

T = int(input())

for t in range(1, T + 1):
    Ai, Bi = map(int, input().split())
    
    print(f"Test Case #{t} :")
    for i in range(Ai, Bi + 1):
        print(prime[i - 1])  