#odometer awal 78602.5
odometer_awal = float(input("masukan odometer awal "))

#odometer akhir 78622.7
odometer_akhir = float(input("masukan odometer akhir "))

#jarak yang ditempuh
jarak_tempuh = odometer_akhir - odometer_awal

#tarif
tarif = jarak_tempuh * 1.50

#hasil
print(f"Anda menempuh jarak {jarak_tempuh:.1f} mil. Dengan tarif $1.50 per mil, tarif Anda adalah ${tarif:.2f}.")
