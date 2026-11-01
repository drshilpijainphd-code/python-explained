"""Summarize sample sales with decimal arithmetic."""

import csv
from decimal import Decimal
from io import StringIO

SAMPLE_CSV = "product,quantity,unit_price\nNotebook,2,12.50\nPen,5,3.00\n"


def sales_totals(csv_text: str) -> dict[str, Decimal]:
    totals: dict[str, Decimal] = {}
    for row in csv.DictReader(StringIO(csv_text)):
        product = row["product"]
        amount = int(row["quantity"]) * Decimal(row["unit_price"])
        totals[product] = totals.get(product, Decimal("0")) + amount
    return totals


def main() -> None:
    totals = sales_totals(SAMPLE_CSV)
    for product, amount in totals.items():
        print(f"{product}: {amount:.2f}")
    print(f"Total sales: {sum(totals.values(), Decimal('0')):.2f}")


if __name__ == "__main__":
    main()
