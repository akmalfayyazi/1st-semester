beratnya = float(input("masukkan berat anda : "))
tingginya = float(input("masukkan tinggi anda : "))

# menghitung bmi
bmi = (703 * beratnya) / (tingginya ** 2) 

# data bmi
if bmi < 18.5:
    print(f"{bmi:.1f}")
    print("underweight")
elif bmi < 24.9:
    print(f"{bmi:.1f}") 
    print("normal")
elif bmi < 29.9:
    print(f"{bmi:.1f}")
    print("overweight")
else:
    print(f"{bmi:.1f}")
    print("obese")