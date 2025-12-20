# Sistem Validasi Registrasi Mahasiswa
Latihan Mandiri – Praktikum 11  
Pemrograman Berorientasi Objek

## Deskripsi
Folder ini merupakan hasil **Latihan Mandiri** pada mata kuliah Pemrograman Berorientasi Objek (PBO). Latihan ini bertujuan untuk menerapkan proses **refactoring kode** dengan menggunakan prinsip **SOLID**, khususnya *Single Responsibility Principle (SRP)*, *Open–Closed Principle (OCP)*, dan *Dependency Inversion Principle (DIP)*.

Studi kasus yang digunakan adalah **Sistem Validasi Registrasi Mahasiswa**, yang mencakup validasi jumlah SKS, validasi prasyarat mata kuliah, serta validasi IPK yang bersifat opsional.

---

## Analisis Kode Sebelum Refactoring
Pada versi awal, seluruh logika validasi berada dalam satu class `ValidatorManager` dan menggunakan struktur `if/else`. Kondisi ini menimbulkan beberapa pelanggaran prinsip SOLID, yaitu:

- Melanggar Single Responsibility Principle (SRP) karena satu class menangani lebih dari satu tanggung jawab.
- Melanggar Open–Closed Principle (OCP) karena penambahan aturan validasi baru mengharuskan perubahan kode yang sudah ada.
- Melanggar Dependency Inversion Principle (DIP) karena class utama bergantung langsung pada implementasi konkret, bukan abstraksi.

---

## Implementasi Setelah Refactoring

### Single Responsibility Principle (SRP)
Setiap aturan validasi dipisahkan ke dalam class tersendiri:
- `SKSValidator` bertanggung jawab untuk validasi jumlah SKS.
- `PraSyaratValidator` bertanggung jawab untuk validasi prasyarat.
- `OptionalIPKValidator` bertanggung jawab untuk validasi IPK opsional.
- `ValidatorManager` hanya bertugas mengoordinasikan proses validasi.

### Dependency Inversion Principle (DIP)
Sistem menggunakan abstraksi `ValidationRule` sebagai kontrak validasi. Class `ValidatorManager` tidak bergantung pada class konkret, melainkan pada abstraksi.

### Open–Closed Principle (OCP)
Penambahan aturan validasi baru dilakukan dengan menambahkan class validator baru tanpa mengubah kode `ValidatorManager`. Hal ini menunjukkan bahwa sistem bersifat terbuka untuk pengembangan dan tertutup untuk perubahan.

---

## Challenge – Pembuktian OCP
Pembuktian prinsip OCP dilakukan dengan menambahkan validasi IPK opsional melalui class `OptionalIPKValidator`. Validator ini dapat digunakan atau tidak digunakan sesuai kebutuhan tanpa mengubah kode utama.

Sistem mendukung dua skenario:
1. Registrasi mahasiswa tanpa validasi IPK.
2. Registrasi mahasiswa dengan validasi IPK.

---

## Kesimpulan
Melalui latihan mandiri ini, refactoring sistem validasi registrasi mahasiswa berhasil dilakukan dengan menerapkan prinsip SRP, OCP, dan DIP. Hasil refactoring membuat sistem lebih modular, fleksibel, dan mudah dikembangkan tanpa mengubah kode utama. Seluruh tujuan latihan mandiri telah tercapai sesuai dengan ketentuan yang diberikan.


## Identitas
- Nama: Athaya Hasssya Fausta
- Nim: 2411102441221
- Program Studi: Teknik Informatika
- Mata Kuliah: Pemrograman Berbasis Objek (PBO)