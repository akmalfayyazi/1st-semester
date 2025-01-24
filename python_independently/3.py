def palindrome():
    n = input()
    if n == n[::-1]:
        print(True)
    else:
        print(False)

def factorial_finderr(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_finderr(n - 1)

add = lambda a, b: a + b
    
def count_vowel():
    n = input()
    count = 0
    for i in n.lower():
        if i in "aiueo":
            count += 1
    return count

def prime_number():
    n = int(input())
    if n < 2:
        return "it's not prime"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "it's not a prime"
        else:
            return "it's prime"
        
def multiplication_table():
    n = int(input())
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

