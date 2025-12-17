# Refactoring Struktur Kode Menggunakan Prinsip SOLID

## Informasi Umum

* **Mata Kuliah**: Pemrograman Berorientasi Objek – Praktikum (INF2143)
* **Topik**: Refactoring Struktur Kode dengan Prinsip SOLID
* **Studi Kasus**: Sistem Checkout Order

---

## Deskripsi Singkat

Repository ini berisi contoh refactoring kode Python dari struktur yang bersifat *God Class* menjadi struktur yang modular, fleksibel, dan mudah dikembangkan dengan menerapkan prinsip desain **SOLID**, khususnya:

* Single Responsibility Principle (SRP)
* Open/Closed Principle (OCP)
* Dependency Inversion Principle (DIP)

---

## Kode Sebelum Refactoring (Kode Bermasalah)

### Gambaran Umum

Pada tahap awal, sistem menggunakan satu class utama yaitu `OrderManager` yang menangani:

* Proses checkout
* Pemilihan metode pembayaran menggunakan `if/else`
* Pengiriman notifikasi

### Permasalahan (Code Smell)

1. **Pelanggaran SRP**
   `OrderManager` memiliki lebih dari satu tanggung jawab (pembayaran dan notifikasi).

2. **Pelanggaran OCP**
   Penambahan metode pembayaran baru mengharuskan perubahan kode di dalam `OrderManager`.

3. **Pelanggaran DIP**
   Class bergantung langsung pada implementasi konkret, bukan pada abstraksi.

---

## Kode Setelah Refactoring (SOLID)

Refactoring dilakukan dengan memisahkan tanggung jawab dan memperkenalkan abstraksi.

### Struktur Class Setelah Refactoring

* `Order` → Model data
* `IPaymentProcessor` → Abstraksi pembayaran
* `CreditCardProcessor`, `QrisProcessor` → Implementasi pembayaran
* `INotificationService` → Abstraksi notifikasi
* `EmailNotifier` → Implementasi notifikasi
* `CheckoutService` → Kelas koordinator checkout

---

## Penerapan Prinsip SOLID

### 1. Single Responsibility Principle (SRP)

Setiap class hanya memiliki satu tanggung jawab. Contohnya:

* `CheckoutService` hanya mengatur alur checkout
* `PaymentProcessor` hanya menangani pembayaran
* `EmailNotifier` hanya menangani notifikasi

### 2. Open/Closed Principle (OCP)

Sistem terbuka untuk ekstensi namun tertutup untuk modifikasi. Hal ini dibuktikan dengan penambahan metode pembayaran baru (`QrisProcessor`) tanpa mengubah kode `CheckoutService`.

### 3. Dependency Inversion Principle (DIP)

Class `CheckoutService` bergantung pada abstraksi (`IPaymentProcessor` dan `INotificationService`), bukan pada implementasi konkret. Dependency disuntikkan melalui constructor (*Dependency Injection*).

---

## Pembuktian OCP

Pembuktian OCP ditunjukkan dengan penambahan class baru berikut:

```python
class QrisProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        print("Payment: Memproses QRIS.")
        return True
```

Tanpa melakukan perubahan pada class `CheckoutService`, sistem dapat mendukung metode pembayaran baru.

---

## Kesimpulan

Refactoring yang dilakukan berhasil meningkatkan kualitas kode dengan menerapkan prinsip SOLID. Kode menjadi lebih modular, mudah dirawat, serta fleksibel untuk pengembangan fitur di masa depan.

---

## Refleksi

Pendekatan Dependency Injection lebih efektif dibandingkan penggunaan `if/else` karena memungkinkan penambahan fitur tanpa memodifikasi kode inti. Hal ini mengurangi risiko bug dan meningkatkan maintainability sistem.
