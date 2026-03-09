from models import FoodItem, Menu, Order, Customer

# --- Sample FoodItems ---
burger = FoodItem("Spicy Burger", 8.99, "Burgers", 4.5)
soda = FoodItem("Large Soda", 2.49, "Drinks", 3.8)
brownie = FoodItem("Chocolate Brownie", 3.99, "Desserts", 4.2)
milkshake = FoodItem("Vanilla Milkshake", 4.99, "Drinks", 4.7)
fries = FoodItem("Crispy Fries", 3.49, "Sides", 4.1)
cheesecake = FoodItem("Cheesecake Slice", 5.49, "Desserts", 4.8)
veggie = FoodItem("Veggie Wrap", 7.49, "Burgers", 3.9)

print("=" * 40)
print("1. FOOD ITEM ATTRIBUTES")
print("=" * 40)
for item in [burger, soda, brownie, milkshake, fries, cheesecake, veggie]:
    print(f"  {item.name:<25} ${item.price:<6} {item.category:<10} rating: {item.popularity_rating}")

# --- Menu: adding items ---
print("\n" + "=" * 40)
print("2. MENU — ADDING ITEMS")
print("=" * 40)
menu = Menu()
for item in [burger, soda, brownie, milkshake, fries, cheesecake, veggie]:
    menu.add_item(item)
print(f"  Items added: {len(menu.items)}")
print(f"  Names: {[i.name for i in menu.items]}")

# --- Menu: filtering by category ---
print("\n" + "=" * 40)
print("3. MENU — FILTER BY CATEGORY")
print("=" * 40)
for category in ["Burgers", "Drinks", "Desserts", "Sides", "Pizza"]:
    results = menu.filter_by_category(category)
    names = [i.name for i in results]
    print(f"  {category:<10} → {names}")

# --- Menu: sorting by popularity ---
print("\n" + "=" * 40)
print("4. MENU — SORTED BY POPULARITY (desc)")
print("=" * 40)
sorted_by_rating = sorted(menu.items, key=lambda i: i.popularity_rating, reverse=True)
for item in sorted_by_rating:
    print(f"  {item.popularity_rating}  {item.name}")

# --- Menu: sorting by price ---
print("\n" + "=" * 40)
print("5. MENU — SORTED BY PRICE (asc)")
print("=" * 40)
sorted_by_price = sorted(menu.items, key=lambda i: i.price)
for item in sorted_by_price:
    print(f"  ${item.price:<6} {item.name}")

# --- Order: computing total ---
print("\n" + "=" * 40)
print("6. ORDER — COMPUTE TOTAL")
print("=" * 40)
order1 = Order()
order1.add_item(burger)
order1.add_item(soda)
order1.add_item(fries)
print(f"  Items: {[i.name for i in order1.items]}")
expected1 = round(burger.price + soda.price + fries.price, 2)
actual1 = round(order1.calculate_total(), 2)
print(f"  Expected total: ${expected1}")
print(f"  calculate_total(): ${actual1:.2f}")
print(f"  Match: {expected1 == actual1}")

# --- Order: empty order ---
print("\n" + "=" * 40)
print("7. ORDER — EMPTY ORDER TOTAL")
print("=" * 40)
empty_order = Order()
print(f"  Items: {empty_order.items}")
print(f"  calculate_total(): ${empty_order.calculate_total():.2f}")

# --- Customer: multiple orders in history ---
print("\n" + "=" * 40)
print("8. CUSTOMER — PURCHASE HISTORY")
print("=" * 40)
order2 = Order()
order2.add_item(milkshake)
order2.add_item(cheesecake)

customer = Customer("Alice")
customer.purchase_history.append(order1)
customer.purchase_history.append(order2)

print(f"  Customer: {customer.name}")
print(f"  Orders in history: {len(customer.purchase_history)}")
for idx, order in enumerate(customer.purchase_history, 1):
    items = [i.name for i in order.items]
    print(f"  Order {idx}: {items} — total: ${order.calculate_total():.2f}")

lifetime = sum(o.calculate_total() for o in customer.purchase_history)
print(f"  Lifetime spend: ${lifetime:.2f}")
