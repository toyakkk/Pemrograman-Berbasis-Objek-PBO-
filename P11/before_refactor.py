from abc import ABC, abstractmethod
from dataclasses import dataclass

#model sederhana
@dataclass
class Order:
    customer_name: str
    total_price: float
    status: str = "open"


# === KODE BURUK (sebelum refactor) ===
class OrderManager:
    def process_checkout(self, order: Order, payment_method: str):
        print(f"Memulai checkout untuk {order.customer_name}...")

        #logika pembayaran (pelanggaran OCP/DIP)
        if payment_method == "credit card":
            #logika detail implementasi hardcoded di sini
            print("Processing Credit Card...")
        elif payment_method == "bank_transfer":
            #logika detail implementasi hardcoded di sini
            print("Processing Bank Transfer...")
        else:
            print("Metode tidak valid.")
            return False
        
        #logika notifikasi (pelanggaran SRP)
        print(f"Mengirim notifikasi ke {order.customer_name}...")
        order.status = "paid"
        return True

# --- ABTRAKSI (kontrak untuk OCP/DIP) ---
class IPaymentProcessor(ABC):
    """Kontrak: Semua prosesor pembayaran harus punya method 'process'."""
    @abstractmethod
    def process(self, order: Order) -> bool:
        pass


class INotificationService(ABC):
    """Kontrak: Semua layanan notifikasi harus punya method 'send'."""
    @abstractmethod
    def send(self, order: Order):
        pass


# --- impelementasi konkrit (Plug-in) ---
class CreditCardProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        print("Payment: Memproses Kartu Kredit.")
        return True


class QrisProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        print("Payment: Memproses QRIS.")
        return True


class EmailNotifier(INotificationService):
    def send(self, order: Order):
        print(f"Notif: Mengirim email konfirmasi ke {order.customer_name}.")


# --- kelas koordinator (SRP & DIP) ---
class CheckoutService: # tanggung jawab tunggal: mengkoordinasi Checkout
    def __init__(self, payment_processor: IPaymentProcessor, notifier: INotificationService):
        # dependency injection (DIP): bergantung pada Abstraksi, bukan konkrit
        self.payment_processor = payment_processor
        self.notifier = notifier

    def run_checkout(self, order: Order) -> bool:
        if self.payment_processor.process(order):
            order.status = "paid"
            self.notifier.send(order)
            print("Checkout Sukses.")
            return True
        return False
        

# --- PROGRAM UTAMA ---
# setup dependencies
andi_order = Order("Andi, 500000")
checkout_cc = CheckoutService(
    payment_processor=CreditCardProcessor(),
    notifier=EmailNotifier()
)
checkout_cc.run_checkout(andi_order)

print("----")

# skenario 2: QRIS tanpa ubah CheckoutService
budi_order = Order("Budi", 100000)
checkout_qris = CheckoutService(
    payment_processor=QrisProcessor(),
    notifier=EmailNotifier()
)
checkout_qris.run_checkout(budi_order)
