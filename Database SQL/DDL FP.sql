CREATE DATABASE FP;

USE FP;
-- Tabel mahasiswa table
CREATE TABLE mahasiswa (
    nrp INTEGER PRIMARY KEY,
    nama VARCHAR(50) NOT NULL,
    umur INTEGER NOT NULL,
    jenis_kelamin CHAR(1) NOT NULL,
    departemen VARCHAR(50) NOT NULL,
    Universitas VARCHAR(50) NOT NULL
);

-- Tabel divisi table
CREATE TABLE divisi (
    id_divisi VARCHAR(6) PRIMARY KEY,
    nama_divisi VARCHAR(50) NOT NULL
);
 
-- Tabel staf table
CREATE TABLE staf (
    nik INTEGER PRIMARY KEY NOT NULL,
    id_divisi VARCHAR(6) NOT NULL,
    nama VARCHAR(50) NOT NULL,
    jabatan VARCHAR(30) NOT NULL,
    FOREIGN KEY (id_divisi) REFERENCES divisi(id_divisi)
);

-- Tabel pembimbing table
CREATE TABLE pembimbing (
    id_pembimbing VARCHAR(6) PRIMARY KEY,
    nik INTEGER NOT NULL,
    jumlah_bimbing INTEGER NOT NULL,
    FOREIGN KEY (nik) REFERENCES staf(nik)
);

-- Tabel project table
CREATE TABLE project (
    id_project VARCHAR(6) PRIMARY KEY,
    nama_project VARCHAR(50) NOT NULL,
    tanggal_mulai DATE NOT NULL,
    Tanggal_Tengat DATE NOT NULL,
    Progress VARCHAR(50) NOT NULL,
    ID_Pembimbing VARCHAR(6) NOT NULL,
    FOREIGN KEY (ID_Pembimbing) REFERENCES pembimbing(id_pembimbing)
);

-- Tabel pendaftaran_magang table
CREATE TABLE pendaftaran_magang (
    id_pendaftar VARCHAR(6) PRIMARY KEY,
    nrp INTEGER NOT NULL,
    Status BOOLEAN NOT NULL,
    Tanggal_Daftar DATE NOT NULL,
    dokumen VARCHAR(100) NOT NULL,
    FOREIGN KEY (nrp) REFERENCES mahasiswa(nrp)
);

-- Tabel peserta_magang table
CREATE TABLE peserta_magang (
    id_magang VARCHAR(6) PRIMARY KEY,
    id_pendaftar VARCHAR(6) NOT NULL,
    id_Project VARCHAR(6) NOT NULL,
    id_pembimbing VARCHAR(6) NOT NULL,
    id_divisi VARCHAR(6) NOT NULL,
    nama_Peserta VARCHAR(50) NOT NULL,
    Tanggal_Mulai DATE NOT NULL,
    Tanggal_Selesai DATE NOT NULL,
    FOREIGN KEY (id_pendaftar) REFERENCES pendaftaran_magang(id_pendaftar),
    FOREIGN KEY (id_Project) REFERENCES project(id_project),
    FOREIGN KEY (id_pembimbing) REFERENCES pembimbing(id_pembimbing),
    FOREIGN KEY (id_divisi) REFERENCES divisi(id_divisi)
);

-- Tabel transkrip_penilaian table
CREATE TABLE transkrip_penilaian (
    id_penilaian VARCHAR(6) PRIMARY KEY,
    ID_Pembimbing VARCHAR(6) NOT NULL,
    id_magang VARCHAR(6) NOT NULL,
    nilai_kedisiplinan FLOAT(2,2) NOT NULL,
    nilai_komunikasi FLOAT(2,2) NOT NULL,
    nilai_skill FLOAT(2,2) NOT NULL,
    nilai_laporan FLOAT(2,2) NOT NULL,
    nilai_total FLOAT(2,2) NOT NULL,
    FOREIGN KEY (ID_Pembimbing) REFERENCES pembimbing(id_pembimbing),
    FOREIGN KEY (id_magang) REFERENCES peserta_magang(id_magang)
);