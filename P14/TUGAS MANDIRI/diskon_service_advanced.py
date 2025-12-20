import pdb

class DiskonCalculator:
    """Menghitung harga akhir setelah diskon."""

    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:
        pdb.set_trace()
        
        jumlah_diskon = harga_awal * persentase_diskon / 100
        harga_setelah_diskon = harga_awal - jumlah_diskon

        # BUG: PPN 10% dihitung dua kali
        harga_setelah_ppn = harga_setelah_diskon * 1.1
        harga_akhir = harga_setelah_ppn * 1.1 # PPN KEDUA

        return harga_akhir
    

if __name__ == '__main__':
    calc = DiskonCalculator()
    print(calc.hitung_diskon(1000, 10))