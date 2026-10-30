from product import Product


class SubscriptionProduct(Product):
    """A product billed on a recurring basis (Lab 7, Section 8)."""

    TYPE = "subscription"
    EXTRA_FIELDS = [("billing_period", "Billing period (e.g. monthly)", str)]

    def __init__(self, product_id, name, price, stock, billing_period):
        super().__init__(product_id, name, price, stock)
        self.__billing_period = billing_period

    def get_billing_period(self):
        return self.__billing_period

    def display_information(self):
        super().display_information()
        print(f"    Billed: {self.__billing_period}")

    def get_fulfilment_info(self):
        return "Subscription product: activated online and billed periodically."

    def to_dict(self):
        data = super().to_dict()
        data["billing_period"] = self.__billing_period
        return data
