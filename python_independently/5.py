import random

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)

def aritmatik():
    n = int(input())
    m = int(input())
    print(f"sum: {n+m}")
    print(f"diference: {n-m}")
    print(f"product: {n*m}")
    print(f"division: {int(n/m)}")
    
def odd_even(n):
    if n % 2 == 0:
        return f"{n} is an even"
    return f"{n} is an odd"

def fibonaccii(n):
    if n <= 1:
        return n
    return fibonaccii(n-1) + fibonaccii(n-2)

def reverse_string(n):
    return n[::-1]

def factoriall(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def guess_number():
    number = random.randint(1, 100)
    tries = 0
    while True:
        guess = int(input("input the number: "))
        tries += 1
        if guess > number:
            print("too high")
        elif guess < number:
            print("too low")
        elif guess == number:
            print(f"correct! you guessed {tries} times")

def prime_check():
    n = int(input("enter the number: "))
    if n < 2:
        return f"{n} not a prime"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return f"{n} not a prime"
    return f"{n} is a prime"

def palindrome():
    n = input("enter a string: ")
    if n == n[::-1]:
        return f"{n} is a palindrome"
    return f"{n} isn't a palindrome"

def multiple():
    n = int(input("enter a number: "))
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

def anagrams():
    n = input()
    m = input()
    for i in n:
        if i in m:
            return "yes"
        else:
            return "no"

print(anagrams())