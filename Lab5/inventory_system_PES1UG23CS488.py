"""
Inventory Management System
---------------------------
A simple inventory management module with safe file handling,
input validation, and clean coding practices.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional

# Global variable holding current stock
stock_data: Dict[str, int] = {}


def add_item(item: str = "default", qty: int = 0,
             logs: Optional[List[str]] = None) -> None:
    """Add an item to the inventory."""
    if not isinstance(item, str) or not isinstance(qty, int):
        print(f"Invalid types for item='{item}', qty='{qty}' — skipping.")
        return

    if qty <= 0:
        print(f"Cannot add non-positive quantity for '{item}'.")
        return

    if logs is None:
        logs = []

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item: str, qty: int) -> None:
    """Remove a specified quantity of an item."""
    if not isinstance(item, str) or not isinstance(qty, int) or qty <= 0:
        print(f"Invalid input for remove_item: item={item}, qty={qty}")
        return

    if item not in stock_data:
        print(f"Item '{item}' not found in inventory.")
        return

    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except (KeyError, TypeError, ValueError) as error:
        print(f"Error removing item '{item}': {error}")


def get_qty(item: str) -> Optional[int]:
    """Get quantity of a given item."""
    return stock_data.get(item)


def load_data(file: str = "inventory.json") -> None:
    """Load inventory data from a JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                stock_data.clear()
                stock_data.update(
                    {str(k): int(v) for k, v in data.items()}
                )
    except FileNotFoundError:
        print(f"File '{file}' not found — starting with empty inventory.")
    except (json.JSONDecodeError, ValueError) as error:
        print(f"Error loading data from '{file}': {error}")


def save_data(file: str = "inventory.json") -> None:
    """Save current inventory data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
    except OSError as error:
        print(f"Error saving data: {error}")


def print_data() -> None:
    """Display all inventory items and their quantities."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold: int = 5) -> List[str]:
    """Return list of items with quantity below the threshold."""
    return [
        item for item, qty in stock_data.items()
        if qty < threshold
    ]


def main() -> None:
    """Demonstration function for the inventory system."""
    logs: List[str] = []

    add_item("apple", 10, logs)
    add_item("banana", 2, logs)
    add_item("123", "ten")  # Invalid types handled safely

    remove_item("apple", 3)
    remove_item("orange", 1)

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    save_data()
    load_data()
    print_data()

    print("System check complete.")


if __name__ == "__main__":
    main()
