from product import Product
from supplier import Supplier


class SubscriptionProduct(Product):
    """A product billed on a recurring basis (Lab 7, Section 8)."""

    TYPE = "subscription"
    EXTRA_FIELDS = [("billing_period", "Billing period (e.g. monthly)", str)]

    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier, billing_period: str) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__billing_period = billing_period

    def get_billing_period(self) -> str:
        return self.__billing_period

    def display_information(self) -> None:
        super().display_information()
        print(f"    Billed: {self.__billing_period}")

    def get_fulfilment_info(self) -> str:
        return "Subscription product: activated online and billed periodically."

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["billing_period"] = self.__billing_period
        return data
