import pandas as pd
import os

# membaca data dari file Excel (2 sheet)
file_path = "/Users/fayyazi/Documents/programing/python/kuliah/matdis/no2/tabel_penjualan12.xlsx"

sheet1 = pd.read_excel(file_path, sheet_name=2, engine="openpyxl")  
sheet2 = pd.read_excel(file_path, sheet_name=1, engine="openpyxl")  

#ada 1 kolom di indeks 0 yang tidak diinginkan. jadi dihapus
#sheet2 = sheet2.drop(columns=["Unnamed: 0"])

#di sheet 2 namanya tidak berdasarkan baris pertama jadi di rename
sheet2.columns = ["KATEGORI", "NAMA PRODUK"]

#saat di excel bagian kategori di merge centre. jadi perlu mengisi kategori pada produk
sheet2["KATEGORI"] = sheet2["KATEGORI"].ffill()

#menghilangkan strip jika ada
sheet1["NAMA PRODUK"] = sheet1["NAMA PRODUK"].str.strip()
sheet2["NAMA PRODUK"] = sheet2["NAMA PRODUK"].str.strip()

#menggabungkan sheet1 dan 2
merged_df = pd.merge(sheet1, sheet2, on="NAMA PRODUK", how="left")

# fungsi untuk menghitung total pembelian per produk (dengan kategori)
def total_pembelian_dengan_kategori(df):
    # simpan di dict
    penjualan_per_kategori = {}

    # Loop untuk menghitung total pembelian per kategori dan produk
    for i, row in df.iterrows():
        kategori = row["KATEGORI"]  
        produk = row["NAMA PRODUK"]  
        pembelian = row["JUMLAH PRODUK"]  
        
        # struktur dict: {Kategori: {Produk: Total Pembelian}}
        if kategori not in penjualan_per_kategori:
            penjualan_per_kategori[kategori] = {}
        if produk not in penjualan_per_kategori[kategori]:
            penjualan_per_kategori[kategori][produk] = 0
        penjualan_per_kategori[kategori][produk] += pembelian

    return penjualan_per_kategori

# Fungsi yang mengururtkan berdasarkan jumlah pembelian
def merge_sort_dict(penjualan_per_kategori):
    sorted_result = {}

    
    for kategori, produk_dict in penjualan_per_kategori.items():
        items = list(produk_dict.items())  # Konversi ke list of tuples
        sorted_items = merge_sort(items)  # Urutkan
        sorted_result[kategori] = sorted_items

    return sorted_result

# Fungsi merge sort untuk list of tuples
def merge_sort(items):
    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    
    return merge(left, right)

# Fungsi merge untuk menggabungkan dua bagian yang sudah terurut
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i][1] > right[j][1]:  # Membandingkan berdasarkan jumlah pembelian
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# hitung total pembelian per kategori dan produk
penjualan = total_pembelian_dengan_kategori(merged_df)

# urutkan produk dalam setiap kategori berdasarkan jumlah pembelian
sorted_penjualan = merge_sort_dict(penjualan)

# Menampilkan hasil sebagai DataFrame
result_data = []
for kategori, produk_list in sorted_penjualan.items():
    for produk, jumlah in produk_list:
        result_data.append({"Kategori": kategori, "Nama Produk": produk, "Jumlah Pembelian": jumlah})

# konversi ke DataFrame
tabel_hasil = pd.DataFrame(result_data)

# Pastikan DataFrame diurutkan kembali berdasarkan kategori dan jumlah pembelian
tabel_hasil = tabel_hasil.sort_values(by=["Kategori", "Jumlah Pembelian"], ascending=[True, False])
tabel_hasil.reset_index(drop=True, inplace=True)
tabel_hasil.index += 1 
# Menampilkan tabel hasil
print(tabel_hasil)
