matkul = int(input())
m=[]
for i in range(matkul):
    nm= input()
    m.append(nm)

nama_matkul= int(input())
pipel_matkul=[]
for i in range(nama_matkul):
    x= input().split()
    pipel_matkul.append(x)

dosen_matkul= int(input())
d_s=[]
for i in range(dosen_matkul):
    dosmat= input().split()
    if len(dosmat)==1:
        dosmat.append("")
    d_s.append(dosmat)

#----------------------------------------------------------------
dosen_jumlah_matkul={}
for x,y in d_s:
    if x not in dosen_jumlah_matkul:
        dosen_jumlah_matkul[x]=[]
    if y not in dosen_jumlah_matkul[x] and y!="":
        dosen_jumlah_matkul[x].append(y)

for a,b in dosen_jumlah_matkul.items():
    if len(b)==0:
        print("ada dosen yang ga ngajar matkul")
        break
else: 
    print("semua dosen ngajar matkul")

#-----------------------------------------------------------------
bnyk_student={}
for a,b in pipel_matkul:
    if a not in bnyk_student:
        bnyk_student[a]=[]
    if b not in bnyk_student[a]:
        bnyk_student[a].append(b)
      
dosen_siswa={}
for a,b in d_s:
    if a not in dosen_siswa:
        dosen_siswa[a]={}
    if b not in dosen_siswa[a]:
        dosen_siswa[a][b] = []

for a,b in pipel_matkul:
    for i,j in dosen_siswa.items():
        if b in j:
           dosen_siswa[i][b].append(a)

for i, j in dosen_siswa.items():
    nama_siswa=[]
    for sisw in j.items():
        for i in sisw:
            nama_siswa.append(i)
    semw_kena=True
    for i in bnyk_student:
        if i not in nama_siswa:
          semw_kena=False
          break

    if semw_kena:
        print("Ya, terdapat dosen yang mengjar semua mahasiswa")
        break
else:
    print("Tidak, tidak ada dosen yang mengajar semua mahasiswa")
