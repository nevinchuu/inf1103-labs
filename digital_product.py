from product import Product


class DigitalProduct(Product):
    """A product delivered by download."""

    TYPE = "digital"
    EXTRA_FIELDS = [("download_size", "Download size (MB)", float)]

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_download_size(self):
        return self.__download_size

    def display_information(self):
        super().display_information()
        print(f"    Download size: {self.__download_size} MB")

    def get_fulfilment_info(self):
        return "Digital product: delivered digitally via download link."

    def to_dict(self):
        data = super().to_dict()
        data["download_size"] = self.__download_size
        return data
