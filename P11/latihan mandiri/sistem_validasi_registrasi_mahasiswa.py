from abc import ABC, abstractmethod

class ValidationRule(ABC):
    @abstractmethod
    def validate(self, mahasiswa) -> bool:
        pass


class SKSValidator(ValidationRule):
    def validate(self, mahasiswa) -> bool:
        sks = mahasiswa["sks"]
        if sks > 24:
            print(f"Total SKS yang diambil: {sks} MELEBIHI BATAS (MAKS: 24)")
            return False

        print(f"Total SKS yang diambil: {sks} SKS AMAN")
        return True
    

class PraSyaratValidator(ValidationRule):
    def validate(self, mahasiswa) -> bool:
        if not mahasiswa["lulus_prasyarat"]:
            print("Validasi Prasyarat: TIDAK TERPENUHI")
            return False
        
        print("Validasi Prasyarat: TERPENUHI")
        return True
    
class OptionalIPKValidator(ValidationRule):
    def validate(self, mahasiswa) -> bool:
        if "ipk" not in mahasiswa:
            print("Validasi IPK: DILEWATI (TIDAK DI ISI)")
            return True
        

        ipk = mahasiswa["ipk"]
        if ipk < 2.75:
            print(f"VALIDASI IPK: {ipk} TIDAK MEMENUHI (MINIMAL 2.75)")
            return False
        
        print(f"Validasi IPK: {ipk} MEMENUHI")
        return True
    

class ValidatorManager:
    def __init__(self, validators: list):
        self.validators = validators

    def validate(self, mahasiswa) -> bool:
        is_valid = True

        for validator in self.validators:
            if not validator.validate(mahasiswa):
                is_valid = False

        if is_valid:
            print("REGISTRASI MAHASISWA BERHASIL")
        else:
            print("REGISTRASI MAHASISWA TIDAK BERHASIL")


# --- MAIN PROGRAM ---

print("=== VALIDASI REGISTRASI MAHASISWA ===")

validators = [
    SKSValidator(),
    PraSyaratValidator(),
    OptionalIPKValidator()
]

validator_manager = ValidatorManager(validators)

print("\n --- Memulai Validasi Mahasiswa: Nela --- ")
nela = {
    "nama": "Nela",
    "sks": 22,
    "lulus_prasyarat": True,
    "ipk": 3.47
}
validator_manager.validate(nela)


print("\n --- Memulai Validasi Mahasiswa: Toya --- ")
toya = {
    "nama": "toya",
    "sks": 26,
    "lulus_prasyarat": False
}
validator_manager.validate(toya)

print("\n Memulai Validasi Mahasiswa: Devino")
devino = {
    "nama": "devino",
    "sks": 18,
    "lulus_prasyarat": True,
    "ipk": 3.0
}
validator_manager.validate(devino)