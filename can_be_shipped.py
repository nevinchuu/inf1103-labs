from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    """Interface: anything that can be shipped must be able to price its shipping."""

    @abstractmethod
    def calculate_shipping_cost(self):
        """Return the cost of shipping this item."""
