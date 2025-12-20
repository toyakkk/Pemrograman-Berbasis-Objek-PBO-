# DEBUG REPORT - Bug PPN 10%

## Informasi Umum
Studi kasus pada praktikum ini adalah perhitungnan harga akhir setelah diskon menggunakan class DiskonCalculator. Pada tahap latihan mandiri, dilakukan simulasi bug baru berupa kesalahan perhitungan PPN 10%.

## Tujuan Debugging
Menemukan dan membuktikan bug logika yang menyebabkan PPN 10% dihitung dua kali
pada perhitungan harga akhir.

## Kode yang Dianalisis
Method hitung_diskon pada file diskon_service.py dengan simulasi bug PPN.

## Langkah Debugging
1. Menambahkan breakpoint menggunakan `pdb.set_trace()` di awal method
   hitung_diskon.
2. Menjalankan program menggunakan perintah:
python diskon_service.py
3. Program Berhenti pada mode debugger `(Pdb)`.
4. Melakukan penelusuran nilai variabel menggunakan perintah `p`.

## Hasil Penelusuran Variabel
Perintah dan hasil yang diperoleh selama debugging:

(Pdb) p harga_awal
1000

(Pdb) p persentase_diskon
10

(Pdb) p jumlah_diskon
100.0

(Pdb) p harga_setelah_diskon
900.0

(Pdb) p harga_setelah_ppn
990.0000000000001

(Pdb) p harga_akhir
1089.0000000000002

---


## Analisis Bug
Berdasarkan hasil penelusuran:
- Harga setelah diskon adalah 900
- PPN 10% pertama menghasilkan nilai 990
- Harga akhir menjadi 1089, yang menunjukkan PPN kembali ditambahkan

Hal ini membuktikan bahwa PPN 10% diterapkan dua kali secara tidak sengaja,
sehingga harga akhir menjadi lebih besar dari yang seharusnya.

## Akar Masalah
Bug disebabkan oleh kesalahan logika pada kode berikut:

harga_setelah_ppn = harga_setelah_diskon * 1.1
harga_akhir = harga_setelah_ppn * 1.1


PPN 10% dihitung dua kali karena harga akhir kembali dikalikan dengan 1.1.

## Kesimpulan
Bug PPN 10% berhasil ditemukan menggunakan debugger pdb.
Kesalahan terjadi karena perhitungan PPN dilakukan dua kali,
yang menyebabkan harga akhir meningkat sebesar 20%.
Debugging dengan pdb membantu mengidentifikasi nilai variabel
secara bertahap sehingga akar masalah dapat ditemukan dengan jelas.
