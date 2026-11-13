from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float) -> None:
        self.__percent = percent

    def apply(self, total: float) -> float:
        return total * (1 - self.__percent / 100)


class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount: float) -> None:
        self.__threshold = threshold
        self.__amount = amount

    def apply(self, total: float) -> float:
        return total - self.__amount if total >= self.__threshold else total


class StudentDiscount(DiscountStrategy):
    """Added without changing Order (Section 2.4)."""

    def apply(self, total: float) -> float:
        return total * 0.95
