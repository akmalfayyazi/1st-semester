-- 1. Insert Mahasiswa
INSERT INTO mahasiswa (nrp, nama, umur, jenis_kelamin, departemen, universitas) VALUES 
(1019084562, 'Nini Meliani', 19, 'P', 'Teknik Informatika', 'Universitas Indonesia'),
(1123468192, 'Vania Angela', 19, 'P', 'Sistem Informasi', 'Universitas Lampung'),
(1390472236, 'Patricia Nabila', 18, 'P', 'Teknik Komputer', 'Universitas Airlangga'),
(1281938469, 'Keneth Adijaya', 19, 'L', 'Teknik Informatika', 'Universitas Gajah Mada'),
(1032864281, 'Aini Nurul', 20, 'P', 'Sistem Informasi', 'Universitas Indonesia'),
(1489173219, 'Juna Prasetya', 19, 'L', 'Teknik Informatika', 'Universitas Brawijaya'),
(1581344242, 'Nilam Ayu', 18, 'P', 'Sistem Informasi', 'Universitas Jember'),
(1678881467, 'Felicia Maharani', 20, 'P', 'Teknik Komputer', 'Universitas Diponegoro'),
(1738476421, 'Arka Pratama', 18, 'L', 'Teknik Informatika', 'Universitas Padjajaran'),
(1831568955, 'Bayu Rahaja', 19, 'L', 'Sistem Informasi', 'Universitas Udayana'),
(1988664182, 'Keisha Cantika', 18, 'P', 'Teknik Komputer', 'Universitas Sriwijaya'),
(1385757483, 'Aura Wulandari', 18, 'P', 'Teknologi Informasi', 'Institut Teknologi Sepuluh Nopember');

-- 2. Insert Pendaftaran Magang
INSERT INTO pendaftaran_magang (id_pendaftar, nrp, status, Tanggal_daftar, dokumen) VALUES 
('PD0001', 1019084562, True, '2024-11-20', 'CV'),
('PD0002', 1123468192, True, '2024-11-24', 'CV'),
('PD0003', 1390472236, False, '2024-11-22', 'Portofolio'),
('PD0004', 1281938469, True, '2024-11-22', 'Sertifikat Keahlian'),
('PD0005', 1032864281, True, '2024-11-26', 'CV'),
('PD0006', 1489173219, True, '2024-11-23', 'Surat Rekomendasi'),
('PD0007', 1581344242, False, '2024-11-21', 'Surat Rekomendasi'),
('PD0008', 1678881467, True, '2024-11-24', 'CV'),
('PD0009', 1738476421, True, '2024-11-28', 'Sertifikat Keahlian'),
('PD0010', 1831568955, True, '2024-11-25', 'CV'),
('PD0011', 1385757483, True, '2024-11-23', 'Sertifikat Keahlian'),
('PD0012', 1988664182, True, '2024-11-21', 'Surat Rekomendasi');

-- 3. Insert Divisi
INSERT INTO divisi (id_divisi, nama_divisi) VALUES
('DV0001', 'Research and Development'),
('DV0002', 'Human Resource'),
('DV0003', 'Finance'),
('DV0004', 'Marketing');

-- 4. Insert Staf
INSERT INTO staf (nik, id_divisi, nama, jabatan) VALUES
(1012345678, 'DV0001', 'Ahmad Syahrir', 'Peneliti Utama'),
(1023456789, 'DV0001', 'Nur Aisyah', 'Asisten Peneliti'),
(1034567891, 'DV0001', 'Fahmi Hakim', 'Ilmuwan Data'),
(1045678912, 'DV0002', 'Indah Permatasari', 'Manajer HR'),
(1056789123, 'DV0002', 'Rizki Ananda', 'Spesialis Rekrutmen'),
(1067891234, 'DV0002', 'Sarah Dwi', 'Generalist HR'),
(1078912345, 'DV0003', 'Budi Santoso', 'Analis Keuangan'),
(1089123456, 'DV0003', 'Fitriani Zain', 'Akuntan'),
(1091234567, 'DV0003', 'Hendra Wijaya', 'Spesialis Pajak'),
(1102345678, 'DV0004', 'Siti Rahmawati', 'Spesialis Pemasaran'),
(1113456789, 'DV0004', 'Andi Pratama', 'Pemasar Digital'),
(1124567891, 'DV0004', 'Putri Melati', 'Pembuat Konten');

-- 5. Insert Pembimbing
INSERT INTO pembimbing (id_pembimbing, nik, jumlah_bimbing) VALUES
('PB0001', 1023456789, 2),
('PB0002', 1056789123, 3),
('PB0003', 1089123456, 1),
('PB0004', 1113456789, 1),
('PB0005', 1091234567, 2),	
('PB0006', 1124567891, 1);

-- 6. Insert Project
INSERT INTO project (id_project, nama_project, tanggal_mulai, Tanggal_Tengat, Progress, ID_Pembimbing) VALUES 
('PR0001', 'Proyek Penelitian AI', '2024-12-01', '2025-02-28', 'Perencanaan', 'PB0001'),
('PR0002', 'Transformasi Digital Pemasaran', '2024-12-05', '2025-03-05', 'Inisiasi', 'PB0004'),
('PR0003', 'Platform Analisis Keuangan', '2024-12-10', '2025-03-10', 'Perencanaan', 'PB0003'),
('PR0004', 'Optimalisasi Proses HR', '2024-12-15', '2025-03-15', 'Inisiasi', 'PB0002');

-- 7. Insert Peserta Magang
INSERT INTO peserta_magang (id_magang, id_pendaftar, id_Project, id_pembimbing, id_divisi, nama_Peserta, Tanggal_Mulai, Tanggal_Selesai) VALUES 
('PM0001', 'PD0001', 'PR0001', 'PB0001', 'DV0001', 'Nini Meliani', '2024-12-01', '2025-05-31'),
('PM0002', 'PD0002', 'PR0002', 'PB0004', 'DV0004', 'Vania Angela', '2024-12-05', '2025-06-04'),
('PM0003', 'PD0004', 'PR0003', 'PB0003', 'DV0003', 'Keneth Adijaya', '2024-12-10', '2025-06-09'),
('PM0004', 'PD0005', 'PR0004', 'PB0002', 'DV0002', 'Aini Nurul', '2024-12-15', '2025-06-14'),
('PM0005', 'PD0006', 'PR0002', 'PB0005', 'DV0003', 'Juna Prasetya', '2024-12-20', '2025-06-19'),
('PM0006', 'PD0008', 'PR0002', 'PB0005', 'DV0003', 'Felicia Maharani', '2024-12-25', '2025-06-24'),
('PM0007', 'PD0009', 'PR0001', 'PB0005', 'DV0003', 'Arka Pratama', '2024-12-30', '2025-06-29'),
('PM0008', 'PD0010', 'PR0003', 'PB0006', 'DV0004', 'Bayu Rahaja', '2025-01-05', '2025-07-04'),
('PM0009', 'PD0011', 'PR0004', 'PB0003', 'DV0003', 'Aura Wulandari', '2025-01-10', '2025-07-09'),
('PM0010', 'PD0012', 'PR0001', 'PB0006', 'DV0004', 'Keisha Cantika', '2025-01-15', '2025-07-14');

-- 8. Insert Transkrip Penilaian
INSERT INTO transkrip_penilaian (id_penilaian, ID_Pembimbing, id_magang, nilai_kedisiplinan, nilai_komunikasi, nilai_skill, nilai_laporan, nilai_total) VALUES 
('TP0001', 'PB0001', 'PM0001', 0.85, 0.90, 0.88, 0.92, 0.89),
('TP0002', 'PB0004', 'PM0002', 0.80, 0.85, 0.82, 0.88, 0.84),
('TP0003', 'PB0003', 'PM0003', 0.75, 0.80, 0.78, 0.85, 0.79),
('TP0004', 'PB0002', 'PM0004', 0.88, 0.92, 0.90, 0.95, 0.91),
('TP0005', 'PB0005', 'PM0005', 0.82, 0.86, 0.84, 0.90, 0.85),
('TP0006', 'PB0005', 'PM0006', 0.80, 0.85, 0.82, 0.88, 0.84),
('TP0007', 'PB0005', 'PM0007', 0.78, 0.82, 0.80, 0.86, 0.81),
('TP0008', 'PB0006', 'PM0008', 0.82, 0.86, 0.84, 0.90, 0.85),
('TP0009', 'PB0003', 'PM0009', 0.75, 0.80, 0.78, 0.85, 0.79),
('TP0010', 'PB0006', 'PM0010', 0.60, 0.50, 0.81, 0.87, 0.82);