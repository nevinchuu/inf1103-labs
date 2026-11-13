from src.discounts.discount_strategy import DiscountStrategy


class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount: float) -> None:
        self.__threshold = threshold
        self.__amount = amount

    def apply(self, total: float) -> float:
        return total - self.__amount if total >= self.__threshold else total
