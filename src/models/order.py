from src.discounts.discount_strategy import DiscountStrategy
from src.discounts.no_discount import NoDiscount
from src.models.order_line import OrderLine
from src.models.product import Product


class Order:
    """A customer order. It creates and manages its own OrderLine objects."""

    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []
        # Association: the strategy is given to the Order and can be shared.
        self.__discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.__discount = discount

    def get_order_id(self) -> str:
        return self.__order_id

    def get_order_lines(self) -> list[OrderLine]:
        """Return a copy of the order lines (for inspection)."""
        return list(self.__order_lines)

    def add_order_line(self, product: Product, quantity: int) -> None:
        """Composition: the Order creates the OrderLine itself."""
        self.__order_lines.append(OrderLine(product, quantity))

    def remove_order_line(self, product_id: str) -> bool:
        """Remove the line for a product. Returns False if there is none."""
        for order_line in self.__order_lines:
            if order_line.get_product().get_product_id().lower() == product_id.lower():
                self.__order_lines.remove(order_line)
                return True
        return False

    def calculate_total(self) -> float:
        total = sum(order_line.calculate_subtotal() for order_line in self.__order_lines)
        return self.__discount.apply(total)

    def display_information(self) -> None:
        print(f"Order {self.__order_id}")
        for order_line in self.__order_lines:
            order_line.display_information()
        print(f"Total: ${self.calculate_total():.2f}")
