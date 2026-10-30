"""Lab 7 checks (run: python test_lab7.py)."""
import os
import tempfile

from digital_product import DigitalProduct
from physical_product import PhysicalProduct
from product import Product
from product_factory import product_class_for
from subscription_product import SubscriptionProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory

os.environ["INVENTORY_FILE"] = os.path.join(tempfile.mkdtemp(), "test.json")
import inventory_manager as im  # noqa: E402  (after env var so FILENAME is the temp file)

laptop = PhysicalProduct("P1", "Laptop", 1200.0, 5, 2.0)
guitar = PhysicalProduct("P2", "Guitar", 500.0, 2, 4.5)
os_ = DigitalProduct("D1", "OS", 199.0, 10, 4096.0)

print("-- display (common + specific info)")
laptop.display_information()
os_.display_information()

print("-- fulfilment info")
print(laptop.get_fulfilment_info())
print(os_.get_fulfilment_info())

print("-- abstract Product cannot be instantiated")
try:
    Product("X", "X", 1.0, 1)
except TypeError as error:
    print("TypeError:", error)

print("-- shipping cost by weight")
print(f"2.0 kg -> {laptop.calculate_shipping_cost():.2f}")
print(f"4.5 kg -> {guitar.calculate_shipping_cost():.2f}")
assert laptop.calculate_shipping_cost() == 9.0 and guitar.calculate_shipping_cost() == 14.0

print("-- digital is not CanBeShipped")
assert isinstance(laptop, CanBeShipped) and not isinstance(os_, CanBeShipped)
assert not hasattr(os_, "calculate_shipping_cost")

print("-- JSON round trip")
inv = Inventory()
for product in (laptop, os_, SubscriptionProduct("S1", "Cloud", 9.99, 100, "monthly")):
    inv.add_product(product)
im.save_inventory(inv)
loaded, loaded_ok = im.load_inventory()
assert loaded_ok
for original, restored in zip(inv.get_products(), loaded.get_products()):
    assert type(original) is type(restored), (original, restored)
    assert original.to_dict() == restored.to_dict()
print([type(p).__name__ for p in loaded.get_products()])
assert product_class_for("nope") is None

print("-- unreadable file is not overwritten")
with open(im.FILENAME, "w") as file:
    file.write('[{"id": "OLD", "name": "No type", "price": 1.0, "stock": 1}]')
before = open(im.FILENAME).read()
empty, loaded_ok = im.load_inventory()
assert not loaded_ok
im.save_inventory(empty, loaded_ok)
assert open(im.FILENAME).read() == before
print("ALL CHECKS PASSED")
