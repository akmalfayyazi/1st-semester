def fibonacci(n):
    fibonacci = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci.append(a)
        a, b = b, a + b
    return fibonacci

n = int(input())
print(fibonacci(n))