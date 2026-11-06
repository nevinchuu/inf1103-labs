from product import Product
from supplier import Supplier


class DigitalProduct(Product):
    """A product delivered by download."""

    TYPE = "digital"
    EXTRA_FIELDS = [("download_size", "Download size (MB)", float)]

    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier, download_size: float) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size

    def get_download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"    Download size: {self.__download_size} MB")

    def get_fulfilment_info(self) -> str:
        return "Digital product: delivered digitally via download link."

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["download_size"] = self.__download_size
        return data
