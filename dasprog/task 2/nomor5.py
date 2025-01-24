total_data = float(input("masukkan penggunaan data : "))

if 0.0 < total_data <= 1.0:
    print("charges = 250")
elif 1.0 < total_data <= 2.0:
    print("charges = 500")
elif 2.0 < total_data <= 5.0:
    print("charges = 1000")
elif total_data > 10.0:
    print("charges = 2000")
else:
    print("bad data")
