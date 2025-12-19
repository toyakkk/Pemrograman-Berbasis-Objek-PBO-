import unittest
from diskon_service import DiskonCalculator

class TestDiskonCalculator(unittest.TestCase):

    def setUp(self):
        """Arrange: Siapkan instance Calculator."""
        self.calc = DiskonCalculator()

    def test_diskon_standar_10_persen(self):
        """Tes 1: Memastikan diskon 10% pada 1000 menghasilkan 900."""
        # act
        hasil = self.calc.hitung_diskon(1000, 10)
        # assert
        self.assertEqual(hasil, 900.0)

    def test_diskon_nol(self):
        """Tes 2 (Boundary): Memastikan diskon 0% tidak mengubah harga."""
        hasil = self.calc.hitung_diskon(500, 0)
        self.assertEqual(hasil, 500.0)

    def test_diskon_batas_atas(self):
        """Tes 3 (Boundary): Memastikan diskon 100% menghasilkan 0."""
        hasil = self.calc.hitung_diskon(750, 100)
        self.assertEqual(hasil, 0.0)


class TestDiskonLanjut(unittest.TestCase):
    
    def setUp(self):
        """Arrange: Siapkan instance DiskonCalculator."""
        self.calc = DiskonCalculator()

    def test_diskon_float(self):
        """Tes 5: Uji nilai float Diskon 33% dari 999"""
        hasil = self.calc.hitung_diskon(999, 33)
        # ASSERT
        self.assertAlmostEqual(hasil, 669.33, places=2)

    def test_harga_awal_nol(self):
        """Tes 6: Edge Case Harga awal 0 harus menghasilkan 0"""
        hasil = self.calc.hitung_diskon(0, 50)
        self.assertEqual(hasil, 0.0)


if __name__ == '__main__':
    unittest.main() # jalankan semua tes