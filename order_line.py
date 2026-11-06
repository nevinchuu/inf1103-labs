from product import Product


class OrderLine:
    """One product and quantity within an Order. Created and owned by that Order."""

    def __init__(self, product: Product, quantity: int) -> None:
        # Association: the Product exists independently and is only referenced.
        self.__product: Product = product
        self.__quantity: int = quantity

    def get_product(self) -> Product:
        return self.__product

    def get_quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity

    def display_information(self) -> None:
        print(f"{self.__product.get_name()} x {self.__quantity} | "
              f"Subtotal: ${self.calculate_subtotal():.2f}")
