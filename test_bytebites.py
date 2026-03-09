import unittest
from models import FoodItem, Menu, Order, Customer


class TestFoodItem(unittest.TestCase):

    def test_fooditem_stores_all_attributes(self):
        """A FoodItem created with all four fields stores them correctly."""
        item = FoodItem("Spicy Burger", 8.99, "Burgers", 4.5)
        self.assertEqual(item.name, "Spicy Burger")
        self.assertEqual(item.price, 8.99)
        self.assertEqual(item.category, "Burgers")
        self.assertEqual(item.popularity_rating, 4.5)


class TestMenu(unittest.TestCase):

    def setUp(self):
        self.menu = Menu()
        self.burger = FoodItem("Spicy Burger", 8.99, "Burgers", 4.5)
        self.soda = FoodItem("Large Soda", 2.49, "Drinks", 3.8)
        self.milkshake = FoodItem("Vanilla Milkshake", 4.99, "Drinks", 4.7)
        self.brownie = FoodItem("Chocolate Brownie", 3.99, "Desserts", 4.2)

    def test_menu_is_empty_on_creation(self):
        """A new Menu starts with no items."""
        self.assertEqual(len(self.menu.items), 0)

    def test_add_item_increases_menu_size(self):
        """Adding an item to the menu increases its count by one."""
        self.menu.add_item(self.burger)
        self.assertEqual(len(self.menu.items), 1)

    def test_add_multiple_items(self):
        """Adding three items results in a menu of three items."""
        self.menu.add_item(self.burger)
        self.menu.add_item(self.soda)
        self.menu.add_item(self.brownie)
        self.assertEqual(len(self.menu.items), 3)

    def test_filter_by_category_returns_only_matching_items(self):
        """Filtering by 'Drinks' returns only the drink items."""
        self.menu.add_item(self.burger)
        self.menu.add_item(self.soda)
        self.menu.add_item(self.milkshake)
        results = self.menu.filter_by_category("Drinks")
        self.assertEqual(len(results), 2)
        self.assertIn(self.soda, results)
        self.assertIn(self.milkshake, results)

    def test_filter_by_category_excludes_other_categories(self):
        """Filtering by 'Drinks' does not return items from other categories."""
        self.menu.add_item(self.burger)
        self.menu.add_item(self.soda)
        results = self.menu.filter_by_category("Drinks")
        self.assertNotIn(self.burger, results)

    def test_filter_by_category_returns_empty_for_unknown_category(self):
        """Filtering by a category that doesn't exist returns an empty list."""
        self.menu.add_item(self.burger)
        results = self.menu.filter_by_category("Pizza")
        self.assertEqual(results, [])

    def test_filter_by_category_on_empty_menu_returns_empty(self):
        """Filtering an empty menu returns an empty list without error."""
        results = self.menu.filter_by_category("Drinks")
        self.assertEqual(results, [])


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.burger = FoodItem("Spicy Burger", 8.99, "Burgers", 4.5)
        self.soda = FoodItem("Large Soda", 2.49, "Drinks", 3.8)
        self.fries = FoodItem("Crispy Fries", 3.49, "Sides", 4.1)

    def test_order_total_is_zero_when_empty(self):
        """An order with no items has a total of zero."""
        order = Order()
        self.assertEqual(order.calculate_total(), 0.0)

    def test_calculate_total_with_single_item(self):
        """An order with one item totals to that item's price."""
        order = Order()
        order.add_item(self.burger)
        self.assertAlmostEqual(order.calculate_total(), 8.99)

    def test_calculate_total_with_multiple_items(self):
        """An order with a burger ($8.99) and soda ($2.49) totals $11.48."""
        order = Order()
        order.add_item(self.burger)
        order.add_item(self.soda)
        self.assertAlmostEqual(order.calculate_total(), 11.48)

    def test_calculate_total_with_three_items(self):
        """An order with three items sums all their prices correctly."""
        order = Order()
        order.add_item(self.burger)
        order.add_item(self.soda)
        order.add_item(self.fries)
        self.assertAlmostEqual(order.calculate_total(), 14.97)

    def test_add_item_appears_in_order(self):
        """An item added to an order is present in the order's item list."""
        order = Order()
        order.add_item(self.burger)
        self.assertIn(self.burger, order.items)

    def test_order_starts_with_no_items(self):
        """A new Order starts with an empty item list."""
        order = Order()
        self.assertEqual(order.items, [])


class TestCustomer(unittest.TestCase):

    def test_customer_stores_name(self):
        """A Customer created with a name stores it correctly."""
        customer = Customer("Alice")
        self.assertEqual(customer.name, "Alice")

    def test_customer_starts_with_empty_purchase_history(self):
        """A new Customer has no orders in their purchase history."""
        customer = Customer("Alice")
        self.assertEqual(customer.purchase_history, [])

    def test_customer_purchase_history_records_orders(self):
        """Adding an order to purchase_history makes it retrievable."""
        customer = Customer("Alice")
        order = Order()
        order.add_item(FoodItem("Spicy Burger", 8.99, "Burgers", 4.5))
        customer.purchase_history.append(order)
        self.assertEqual(len(customer.purchase_history), 1)
        self.assertIn(order, customer.purchase_history)

    def test_customer_purchase_history_tracks_multiple_orders(self):
        """A customer with two past orders has a history count of two."""
        customer = Customer("Alice")
        customer.purchase_history.append(Order())
        customer.purchase_history.append(Order())
        self.assertEqual(len(customer.purchase_history), 2)

    def test_customer_can_access_order_total_from_history(self):
        """A customer can retrieve and compute the total of a past order."""
        customer = Customer("Alice")
        order = Order()
        order.add_item(FoodItem("Large Soda", 2.49, "Drinks", 3.8))
        customer.purchase_history.append(order)
        self.assertAlmostEqual(customer.purchase_history[0].calculate_total(), 2.49)


if __name__ == "__main__":
    unittest.main(verbosity=2)
