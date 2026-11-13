from src.discounts.discount_strategy import DiscountStrategy


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float) -> None:
        self.__percent = percent

    def apply(self, total: float) -> float:
        return total * (1 - self.__percent / 100)
