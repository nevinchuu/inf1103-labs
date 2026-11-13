FROM python:3.11-slim

WORKDIR /app

COPY src/ src/
COPY data/products.csv data/
COPY tests/ tests/

CMD ["python", "-m", "src.main.inventory_manager"]
