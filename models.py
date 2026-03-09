# Customer
# Represents an app user. Stores the customer's name and a purchase_history
# list of past Orders, used to verify they are a real user.

# FoodItem
# Represents a single product available for sale (e.g. "Spicy Burger").
# Stores name, price, category, and popularity_rating.

# Menu
# Acts as the catalog of all FoodItems. Supports add_item to add a FoodItem
# and filter_by_category to return only items matching a given category.

# Order
# Represents a single purchase transaction. Holds a list of selected FoodItems
# and provides calculate_total to sum their prices.
