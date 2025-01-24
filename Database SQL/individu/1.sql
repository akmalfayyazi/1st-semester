-- mencari cumlah mahasiswa laki laki
SELECT COUNT(jenis_kelamin) AS jumlah_laki_laki
FROM mahasiswa
WHERE jenis_kelamin = "L"
GROUP BY jenis_kelamin; 