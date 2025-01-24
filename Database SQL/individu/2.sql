SELECT universitas AS univ_daftar_finance
FROM mahasiswa m 
JOIN pendaftaran_magang pm ON m.nrp = pm.nrp
JOIN peserta_magang psm ON pm.id_pendaftar = psm.id_pendaftar
JOIN divisi d ON d.id_divisi = psm.id_divisi
WHERE d.nama_divisi = "Finance"