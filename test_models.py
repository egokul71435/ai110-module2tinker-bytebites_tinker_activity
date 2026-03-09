from models import FoodItem, Menu, Order, Customer

# Sample FoodItems
burger = FoodItem("Spicy Burger", 8.99, "Burgers", 4.5)
soda = FoodItem("Large Soda", 2.49, "Drinks", 3.8)
brownie = FoodItem("Chocolate Brownie", 3.99, "Desserts", 4.2)

print("--- FoodItems ---")
print(f"  {burger.name} | ${burger.price} | {burger.category} | rating: {burger.popularity_rating}")
print(f"  {soda.name} | ${soda.price} | {soda.category} | rating: {soda.popularity_rating}")
print(f"  {brownie.name} | ${brownie.price} | {brownie.category} | rating: {brownie.popularity_rating}")

# Menu
menu = Menu()
menu.add_item(burger)
menu.add_item(soda)
menu.add_item(brownie)

print("\n--- Menu ---")
print(f"  Total items: {len(menu.items)}")
drinks = menu.filter_by_category("Drinks")
print(f"  filter_by_category('Drinks'): {[item.name for item in drinks]}")

# Order
order = Order()
order.add_item(burger)
order.add_item(soda)

print("\n--- Order ---")
print(f"  Items: {[item.name for item in order.items]}")
print(f"  calculate_total(): ${order.calculate_total():.2f}")

# Customer
customer = Customer("Alice")
customer.purchase_history.append(order)

print("\n--- Customer ---")
print(f"  name: {customer.name}")
print(f"  purchase_history count: {len(customer.purchase_history)}")
print(f"  last order total: ${customer.purchase_history[-1].calculate_total():.2f}")
