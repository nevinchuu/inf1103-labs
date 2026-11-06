"""Lab 7 and Lab 8 checks (run: python test.py)."""
import os
import tempfile

from digital_product import DigitalProduct
from physical_product import PhysicalProduct
from product import Product
from product_factory import product_class_for
from subscription_product import SubscriptionProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory
from order import Order
from supplier import Supplier

os.environ["INVENTORY_FILE"] = os.path.join(tempfile.mkdtemp(), "test.json")
import inventory_manager as im  # noqa: E402  (after env var so FILENAME is the temp file)

acme = Supplier("S1", "Acme", "sales@acme.com")
laptop = PhysicalProduct("P1", "Laptop", 1200.0, 5, acme, 2.0)
guitar = PhysicalProduct("P2", "Guitar", 500.0, 2, acme, 4.5)
os_ = DigitalProduct("D1", "OS", 199.0, 10, acme, 4096.0)

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
for product in (laptop, os_, SubscriptionProduct("S1", "Cloud", 9.99, 100, acme, "monthly")):
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

# ------------------------------------------------------------------ Lab 8
print("-- association: Supplier and Product")
supplier = Supplier("S9", "Globex", "info@globex.com")
physical = PhysicalProduct("P9", "Monitor", 300.0, 3, supplier, 5.0)
digital = DigitalProduct("D9", "Editor", 49.0, 50, supplier, 120.0)
physical.get_supplier().display_information()
digital.get_supplier().display_information()
assert physical.get_supplier() is supplier and digital.get_supplier() is supplier
del supplier
physical.get_supplier().display_information()
assert digital.get_supplier().get_name() == "Globex"

print("-- aggregation: Inventory and Product")
inventory_a, inventory_b = Inventory(), Inventory()
inventory_a.add_product(physical)
assert inventory_a.remove_product("p9") is physical
assert inventory_a.find_product("P9") is None
assert inventory_a.remove_product("P9") is None
physical.display_information()
assert inventory_b.add_product(physical)
assert inventory_b.find_product("P9") is physical

print("-- composition: Order and OrderLine")
order_1, order_2 = Order("O1"), Order("O2")
order_1.add_order_line(physical, 2)
order_1.add_order_line(digital, 1)
order_2.add_order_line(physical, 1)
order_1.display_information()
assert order_1.calculate_total() == 300.0 * 2 + 49.0
lines_1, lines_2 = order_1.get_order_lines(), order_2.get_order_lines()
assert lines_1[0] is not lines_2[0]
assert lines_1[0].get_product() is lines_2[0].get_product() is physical
assert order_1.remove_order_line("D9") and not order_1.remove_order_line("D9")
assert order_1.calculate_total() == 600.0
physical.display_information()

print("-- polymorphism and LSP through Product")


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


cloud = SubscriptionProduct("S9", "Cloud", 9.99, 100, acme, "monthly")
mixed = Inventory()
for product in (physical, digital, cloud):
    mixed.add_product(product)
expected = {"P9": "Physical product: requires physical shipping.",
            "D9": "Digital product: delivered digitally via download link.",
            "S9": "Subscription product: activated online and billed periodically."}
for product in mixed.get_products():
    show_product_details(product)
    assert product.get_fulfilment_info() == expected[product.get_product_id()]

print("ALL CHECKS PASSED")
