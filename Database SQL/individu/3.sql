-- mencari nilai tertinggi

SELECT m.nama AS nama_tertinggi, MAX(tp.nilai_total) AS nilai_tertinggi
FROM mahasiswa m
JOIN pendaftaran_magang pm ON m.nrp = pm.nrp
JOIN peserta_magang psm ON pm.id_pendaftar = psm.id_pendaftar
JOIN transkrip_penilaian tp ON psm.id_magang = tp.id_magang
WHERE tp.nilai_total = (
    SELECT MAX(nilai_total)
    FROM transkrip_penilaian
    );
