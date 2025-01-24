n = int(input())
m = int(input())

operation = input("add or subtract or multiply or define : ")

if operation == "multiply":
    hasil = n * m
    print(hasil)

elif operation == "add":
    hasil = n + m
    print(hasil)

elif operation == "subtract":
    hasil = n - m
    print(hasil)

if operation == "define":
    hasil = n / m
    print(hasil)
