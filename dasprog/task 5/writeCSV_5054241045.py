import csv

file = open("chocolate.csv", "w")
writer = csv.writer(file)
writer.writerow(["jenis", "Harga"])
writer.writerow(["Cokelat dubai", "123000"])
writer.writerow(["Cokelat Hitam", "321000"])
writer.writerow(["Cokelat putih", "120000"])
writer.writerow(["Cokelat susu", "100000"])
writer.writerow(["Cokelat kuning", "100000"])
