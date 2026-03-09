# Client Feature Request
We need to build the backend logic for the ByteBites app. The system needs to manage our customers, tracking their names and their past purchase history so the system can verify they are real users.

These customers need to browse specific food items (like a "Spicy Burger" or "Large Soda"), so we must track the name, price, category, and popularity rating for every item we sell.

We also need a way to manage the full collection of items — a digital list that holds all items and lets us filter by category such as "Drinks" or "Desserts".

Finally, when a user picks items, we need to group them into a single transaction. This transaction object should store the selected items and compute the total cost.

# Candidate Classes
The system must model:

- Customer: Represents the user of the app. It will store personal identification (name) and a record of their Purchase History for verification purposes.

- FoodItem: Represents the individual products available for sale. This class will encapsulate specific attributes like name, price, category, and its popularity rating.

- Menu: Acts as the "digital list" or collection manager. This class will be responsible for storing the aggregate of all FoodItem objects and providing the logic for filtering by category.

- Order (or Transaction): Represents a specific purchase event. It serves as the container for the items selected by a Customer and contains the logic to calculate the final total cost.