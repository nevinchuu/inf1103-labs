from src.discounts.discount_strategy import DiscountStrategy


class StudentDiscount(DiscountStrategy):
    """Added without changing Order (Section 2.4)."""

    def apply(self, total: float) -> float:
        return total * 0.95
