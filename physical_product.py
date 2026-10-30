from can_be_shipped import CanBeShipped
from product import Product

BASE_SHIPPING = 5.00
SHIPPING_PER_KG = 2.00


class PhysicalProduct(Product, CanBeShipped):
    """A product that is stored and shipped."""

    TYPE = "physical"
    EXTRA_FIELDS = [("weight", "Weight (kg)", float)]

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"    Weight: {self.__weight} kg | "
              f"Shipping: ${self.calculate_shipping_cost():.2f}")

    def get_fulfilment_info(self):
        return "Physical product: requires physical shipping."

    def calculate_shipping_cost(self):
        return BASE_SHIPPING + SHIPPING_PER_KG * self.__weight

    def to_dict(self):
        data = super().to_dict()
        data["weight"] = self.__weight
        return data
