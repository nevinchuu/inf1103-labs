from src.models.digital_product import DigitalProduct
from src.models.physical_product import PhysicalProduct
from src.models.product import Product
from src.models.subscription_product import SubscriptionProduct
from src.models.supplier import Supplier

# The only place a new product type needs to be registered.
PRODUCT_TYPES = {cls.TYPE: cls
                 for cls in (PhysicalProduct, DigitalProduct, SubscriptionProduct)}


def product_class_for(type_name: str) -> type[Product] | None:
    """Return the Product subclass for a type identifier, or None if unknown."""
    return PRODUCT_TYPES.get(type_name)


class ProductFactory:
    """Centralises product creation so callers only need to know about Product."""

    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
               stock: int, supplier: Supplier, *extras) -> Product:
        product_class = product_class_for(product_type)
        if product_class is None:
            raise ValueError(f"Unknown product type: {product_type}")
        return product_class(product_id, name, price, stock, supplier, *extras)
