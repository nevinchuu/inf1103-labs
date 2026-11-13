FROM python:3.11-slim

WORKDIR /app

COPY inventory_manager.py inventory.py product.py can_be_shipped.py \
     physical_product.py digital_product.py subscription_product.py \
     product_factory.py supplier.py order_line.py order.py test.py \
     discount_strategy.py products.csv ./

CMD ["python", "inventory_manager.py"]
