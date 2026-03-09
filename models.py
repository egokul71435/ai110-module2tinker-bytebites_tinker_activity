# FoodItem
# Represents a single product available for sale (e.g. "Spicy Burger").
# Stores name, price, category, and popularity_rating.

class FoodItem:
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


# Menu
# Acts as the catalog of all FoodItems. Supports add_item to add a FoodItem
# and filter_by_category to return only items matching a given category.

class Menu:
    def __init__(self):
        self.items: list[FoodItem] = []

    def add_item(self, food_item: FoodItem) -> None:
        self.items.append(food_item)

    def filter_by_category(self, category: str) -> list[FoodItem]:
        return [item for item in self.items if item.category == category]


# Order
# Represents a single purchase transaction. Holds a list of selected FoodItems
# and provides calculate_total to sum their prices.

class Order:
    def __init__(self):
        self.items: list[FoodItem] = []

    def add_item(self, food_item: FoodItem) -> None:
        self.items.append(food_item)

    def calculate_total(self) -> float:
        return sum(item.price for item in self.items)


# Customer
# Represents an app user. Stores the customer's name and a purchase_history
# list of past Orders, used to verify they are a real user.

class Customer:
    def __init__(self, name: str):
        self.name = name
        self.purchase_history: list[Order] = []
