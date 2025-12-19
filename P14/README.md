# Praktikum 14 – Debugging dan Unit Testing Sederhana

## Deskripsi Praktikum
Proyek ini merupakan bagian dari Praktikum Pemrograman Berorientasi Objek (INF2143) 
Pertemuan 14. Fokus praktikum ini adalah melakukan debugging dan unit testing 
sederhana menggunakan bahasa pemrograman Python.

Studi kasus yang digunakan adalah perhitungan harga akhir setelah diskon dengan 
tujuan untuk menemukan bug logika, melakukan perbaikan, serta memverifikasi 
perilaku kode menggunakan unit testing.

## Tujuan Pembelajaran
Setelah menyelesaikan proyek ini, mahasiswa diharapkan mampu:
- Menjelaskan perbedaan antara debugging dan testing
- Menggunakan pdb untuk menelusuri alur program
- Menemukan akar masalah dari bug logika
- Menulis unit test menggunakan modul unittest
- Menguji boundary condition dan nilai float

## Struktur Proyek
├── diskon_service.py
├── test_diskon.py
├── test_diskon_advanced.py
├── DEBUG_REPORT.md
└── README.md


## Teknologi yang Digunakan
- Python 3
- pdb (Python Debugger)
- unittest

## Unit Testing
### Test Dasar (test_diskon.py)
Pengujian yang dilakukan:
- Diskon 10% pada harga 1000
- Diskon 0% (boundary condition)
- Diskon 100% (boundary condition)

### Test Lanjutan (test_diskon_advanced.py)
Pengujian lanjutan meliputi:
- Pengujian nilai float (diskon 33% dari 999) menggunakan assertAlmostEqual
- Pengujian edge case dengan harga awal bernilai 0

## Debugging
Debugging dilakukan menggunakan modul pdb untuk menemukan kesalahan logika 
dalam perhitungan diskon dan bug lanjutan berupa perhitungan PPN 10% yang 
dilakukan dua kali.

Seluruh proses debugging didokumentasikan pada file DEBUG_REPORT.md.

## Cara Menjalankan Program
Menjalankan program utama:
python diskon_service.py

Menjalankan unit test:
python -m unittest test_diskon.py
python -m unittest test_diskon_advanced.py

Jika semua pengujian berhasil, maka hasil yang ditampilkan adalah OK.

## Catatan
Unit test digunakan untuk memverifikasi perilaku fungsi, sedangkan analisis bug PPN dilakukan melalui proses debugging dan tidak diuji secara langsung melalui unit test.

## Identitas
Nama : Athaya Hassya Fausta
Nim : 2411102441221
Program Studi :  Teknik Informatika
Mata Kuliah : Pemrograman Berorientasi Objek (OOP)

## Referensi
- Lutz, M. (2013). Learning Python
- Guttag, J. V. (2016). Introduction to Computation and Programming Using Python