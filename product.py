from abc import ABC, abstractmethod

from supplier import Supplier


class Product(ABC):
    """Abstract base for every product. Use PhysicalProduct or DigitalProduct."""

    # Overridden by subclasses: the JSON type identifier and the extra
    # (attribute, prompt, converter) fields that type needs.
    TYPE = None
    EXTRA_FIELDS = []

    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, supplier: Supplier) -> None:
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        # Association: the Supplier is created independently and only referenced here.
        self.__supplier: Supplier = supplier

    # Read-only access to the private attributes
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def get_supplier(self) -> Supplier:
        return self.__supplier

    def update_stock(self, quantity):
        """Set the stock level. Returns True if accepted, False if invalid."""
        if not isinstance(quantity, int) or quantity < 0:
            return False
        self.__stock = quantity
        return True

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")
    @abstractmethod
    def get_fulfilment_info(self):
        """Return a message describing how this product is fulfilled."""

    def to_dict(self):
        """Common fields for saving; subclasses add their own."""
        return {"type": self.TYPE, "id": self.__product_id, "name": self.__name,
                "price": self.__price, "stock": self.__stock,
                "supplier": self.__supplier.to_dict()}

    @classmethod
    def from_dict(cls, data):
        """Build a product from saved data, reading this type's extra fields."""
        extras = [data[key] for key, _, _ in cls.EXTRA_FIELDS]
        supplier = Supplier.from_dict(data["supplier"])
        return cls(data["id"], data["name"], data["price"], data["stock"],
                   supplier, *extras)
