from product import Product


class Inventory:
    """Manages a collection of Product objects."""

    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> bool:
        """Add a product. Returns False if the ID already exists."""
        if self.find_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True

    def find_product(self, product_id: str) -> Product | None:
        """Return the Product with the given ID (case-insensitive), or None."""
        for product in self.__products:
            if product.get_product_id().lower() == product_id.lower():
                return product
        return None

    def remove_product(self, product_id: str) -> Product | None:
        """Remove the reference to a product and return it, or None if not found.

        The Product itself is not destroyed; it can be added to another Inventory."""
        product = self.find_product(product_id)
        if product is not None:
            self.__products.remove(product)
        return product

    def get_products(self) -> list[Product]:
        """Return a copy of the product list (for saving)."""
        return list(self.__products)

    def display_all(self) -> None:
        print("Current Inventory")
        print("-" * 48)
        if not self.__products:
            print("No products in inventory.")
        for product in self.__products:
            product.display_information()
        print("-" * 48)
