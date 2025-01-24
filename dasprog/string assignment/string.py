#create string
string1 = "mohammad akmal fayyazi"
string2 = "5054241045"
string3 = "bekasi"

#print string
print("nama saya adalah " + string1)
print("nrp " + string2)
print("asal daerah " + string3)

#access character in string
print("inisial saya " + string1[0]+string1[9]+string1[15])

#string slicing
print("nama belakang saya " + string1[15:])
print("nama banggilan saya " + string1[15:])

#reverse string
print("reverse dari nrp saya adalah " + string2[::-1])

#update string
string3 = "saya mahasiswa rka"
print(string3)

#ubah menjadi "saya bukan mahasiswa rpl" menggunakan convert list lalu join
list3 = list(string3)
list3[4] = " bukan "
string4 = "".join(list3)
string5 = string4[:21] + "rpl"
print(string5)

#menggunakana method
string6 = string3.replace("mahasiswa rka", "bukan mahasiswa rpl")
print(string6)