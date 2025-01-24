import random

def odd_even():
    n = int(input())
    if n % 2 == 0:
        print ("genap")
    else:
        print ("ganjil")

def sum_of_numbers():
    m = list(map(int, input().split()))
    print (sum(m))

def fizz_buzz():
    a = []
    for i in range(1,51):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} fizzbuzz")
        elif i % 3 == 0:
            print(f"{i} fizz")
        elif i % 5 == 0:
            print(f"{i} buzz")
        else:
            a.append(i)
    print(a)

def reverse_string():
    a = input()
    print(a[::-1])

def guess_number():
    number = random.randint(1,100)

    while True:
        guess = int(input())
        if guess > number:
            print("it's too high")
        elif guess < number:
            print("it's too low")
        else:
            print("correct")
            break

odd_even()
sum_of_numbers()
fizz_buzz()
reverse_string()
guess_number()