from abc import ABC, abstractmethod
from dataclasses import dataclass
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

LOGGER = logging.getLogger('Checkout')

#model sederhana
@dataclass
class Order:
    customer_name: str
    total_price: float
    status: str = "open"

# konfigurasi logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# --- model ---
@dataclass
class OrderManager:
    """
    Merepresentasikan data pesanan pelanggan.
    
    Attributes:
        customer_name (str): Nama pelanggan.
        total_price (float): Total harga pesanan.
        status (str): status pesanan
    """
    customer_name: str
    total_price: float
    status: str = "open"

    def process_checkout(self, order: Order, payment_method: str):
        print(f"Memulai checkout untuk {order.customer_name}...")

        if payment_method == "credit card":
            print("Processing Credit Card...")
        elif payment_method == "bank_transfer":
            print("Processing Bank Transfer...")
        else:
            print("Metode tidak valid.")
            return False
        
        print(f"Mengirim notifikasi ke {order.customer_name}...")
        order.status = "paid"
        return True
    


# --- Abstraksi pembayaran
class IPaymentProcessor(ABC):
    """
    Interface untuk semua metode pembayaran.
    
    """
    
    @abstractmethod
    def process(self, order: Order) -> bool:
        """
        Memproses pembayran pesanan.
        
        Args:
            order (Order): Objek Pesanan
            
        Returns:
            bool: True jika berhasil
        """
        pass

    
class INotificationService(ABC):
    """
    Interface untuk layanan notifikasi.
    """

    @abstractmethod
    def send(self, order: Order):
        """
        Mengirim notifikasi pesanan.

        Args:
            order (Order): Objek Pesanan
        """
        pass

    
# --- impelementasi konkrit ---
class CreditCardProcessor(IPaymentProcessor):
    """Proses pembayaran menggunakan Kartu Kredit."""
    def process(self, order: Order) -> bool:
        logging.info("Memproses pembayaran Kartu Kredit.")
        return True
    
class QrisProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        logging.info("Memproses pembayaran menggunakan QRIS.")
        return True
    
class EmailNotifier(INotificationService):
    """Mengirim Notifikasi melalui Email."""

    def send(self, order: Order):
        logging.info(
            f"email konfirmasi dikirim ke {order.customer_name}"
        )

    
# --- kelas koordinator ---
class CheckoutService:
    """
    Mengkoordinasikan proses checkout pesanan.
    """

    def __init__(
            self,
            payment_processor: IPaymentProcessor,
            notifier: INotificationService
        ):
            """
            Args:
                payment_processor (IPaymentProcessor): metode pembayaran
                notifier (INotificationService): layanan notifikasi
            """
            self.payment_processor = payment_processor
            self.notifier = notifier

    def run_checkout(self, order: Order) -> bool:
        """
        Menjalankan proses checkout.

        Args:
            order (Order): Objek Pesanan

        Returns:
            bool: True jika checkout berhasil
        """
        logging.info(
            f"Checkout dimulai untuk {order.customer_name}"
        )


        if self.payment_processor.process(order):
            order.status = "paid"
            self.notifier.send(order)
            print("Checkout Sukses.")
            return True

        logging.warning("Checkout gagal.")
        return False
        


# --- PROGRAM UTAMA ---
# skenario 1
andi_order = Order("Andi", 500000)
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