layanan = int(input("enter the free services number : "))
miles = int(input("enter number of miles : "))

if layanan == 1 and 1500 < miles <= 3000 or layanan == 2 and 3000 < miles <= 4500:
    print("vehicle must be serviced")
else:
    print("vehicle mustn't be serviced")