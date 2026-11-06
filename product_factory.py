from digital_product import DigitalProduct
from physical_product import PhysicalProduct
from product import Product
from subscription_product import SubscriptionProduct

# The only place a new product type needs to be registered.
PRODUCT_TYPES = {cls.TYPE: cls
                 for cls in (PhysicalProduct, DigitalProduct, SubscriptionProduct)}


def product_class_for(type_name: str) -> type[Product] | None:
    """Return the Product subclass for a type identifier, or None if unknown."""
    return PRODUCT_TYPES.get(type_name)
