class FoodItem:
    """A single product available for sale (e.g. "Spicy Burger")."""

    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

    def __repr__(self) -> str:
        return f"FoodItem({self.name!r}, ${self.price}, {self.category}, rating={self.popularity_rating})"


class Menu:
    """Catalog of all FoodItems; supports filtering by category."""

    def __init__(self):
        self.items: list[FoodItem] = []

    def add_item(self, food_item: FoodItem) -> None:
        self.items.append(food_item)

    def filter_by_category(self, category: str) -> list[FoodItem]:
        return [item for item in self.items if item.category == category]


class Order:
    """A single purchase transaction; holds selected FoodItems and computes the total."""

    def __init__(self):
        self.items: list[FoodItem] = []

    def add_item(self, food_item: FoodItem) -> None:
        self.items.append(food_item)

    def calculate_total(self) -> float:
        return sum(item.price for item in self.items)


class Customer:
    """An app user with a name and a history of past Orders."""

    def __init__(self, name: str):
        self.name = name
        self.purchase_history: list[Order] = []
