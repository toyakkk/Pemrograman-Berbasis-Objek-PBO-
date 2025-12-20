from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class IValidationRule(ABC):
    """
    Interface untuk aturan validasi registrasi mahasiswa.
    Setiap rule harus mengimplementasikan method validate().
    """

    @abstractmethod
    def validate(self, student):
        """
        Melakukan validasi terhadap data mahasiswa.

        Args:
            student (dict): Data mahasiswa yang akan divalidasi.

        Returns:
            bool: True jika valid, False jika tidak valid.
        """
        pass


class SKSLimitRule(IValidationRule):
    """
    Rule untuk memvalidasi batas maksimal SKS mahasiswa.
    """

    def __init__(self, max_sks=24):
        """
        Inisialisasi rule batas SKS.

        Args:
            max_sks (int): Batas maksimal SKS.
        """
        self.max_sks = max_sks

    def validate(self, student):
        """
        Mengecek apakah jumlah SKS mahasiswa melebihi batas.

        Args:
            student (dict): Data mahasiswa.

        Returns:
            bool: True jika valid, False jika melebihi batas.
        """
        if student["sks"] > self.max_sks:
            logging.warning(
                f"SKS mahasiswa {student['nama']} melebihi batas ({student['sks']} SKS)"
            )
            return False

        logging.INFO(
            f"Validasi SKS mahasiswa {student['nama']} berhasil"
        )
        return True


class RegistrationService:
    """
    Service untuk memproses registrasi mahasiswa
    berdasarkan aturan validasi.
    """

    def __init__(self, rules):
        """
        Inisialisasi service registrasi.

        Args:
            rules (list): Daftar rule validasi.
        """
        self.rules = rules

    def register(self, student):
        """
        Menjalankan proses registrasi mahasiswa.

        Args:
            student (dict): Data mahasiswa.

        Returns:
            bool: True jika registrasi berhasil, False jika gagal.
        """
        logging.info(
            f"memulai proses registrasi mahasiswa {student['nama']}"
        )

        for rule in self.rules:
            if not rule.validate(student):
                logging.warning(
                    f"Registrasi mahasiswa {student['nama']} gagal"
                )
                return False
            
        logging.info(
            f"Registrasi mahasiswa {student['nama']} berhasil"
        )
        return True


# ====== TEST PROGRAM (UNTUK SCREENSHOT) ======

rules = [SKSLimitRule()]
service = RegistrationService(rules)

student = {
    "nama": "Nela",
    "sks": 26
}

service.register(student)
