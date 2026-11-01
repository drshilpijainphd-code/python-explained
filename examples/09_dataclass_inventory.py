"""Represent inventory with a dataclass."""

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class InventoryItem:
    name: str
    quantity: int
    unit_price: Decimal

    def __post_init__(self) -> None:
        if self.quantity < 0 or self.unit_price < 0:
            raise ValueError("Quantity and price must be non-negative.")

    @property
    def total_value(self) -> Decimal:
        return self.quantity * self.unit_price


def main() -> None:
    item = InventoryItem("Keyboard", 3, Decimal("49.99"))
    print(f"{item.name} inventory value: {item.total_value:.2f}")


if __name__ == "__main__":
    main()
