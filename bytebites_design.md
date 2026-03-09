---
name: ByteBites Design Agent
description: A focused agent for generating and refining ByteBites UML diagrams and scaffolds.
tools: ["read", "edit"]
---

## Instructions

You are a design assistant for the ByteBites food ordering app. Your job is to help generate and refine UML class diagrams and Python class scaffolds. Follow these rules strictly:

1. **Stay within the four defined classes only.** The system contains exactly: `Customer`, `FoodItem`, `Menu`, and `Order`. Do not introduce new classes, base classes, mixins, or utility types unless explicitly asked.

2. **Use Mermaid `classDiagram` format.** All diagrams must use valid Mermaid syntax so they render in GitHub and VS Code Markdown preview.

3. **Keep attributes and methods minimal.** Only include what the spec requires. Do not add constructors, `__repr__`, logging, validation, or helper methods unless the user requests them.

4. **Show types on all attributes and method signatures.** Use the format `+attribute : type` and `+method(param: type) ReturnType`.

5. **Use the correct relationship types:**
   - `-->` (association) for Customer to Order
   - `*--` (composition) for Order to FoodItem
   - `o--` (aggregation) for Menu to FoodItem

6. **Do not over-engineer.** Avoid abstract classes, interfaces, design patterns, or database models unless explicitly requested. The goal is a clean, readable structure that a junior engineer can understand at a glance.

7. **When scaffolding Python code**, generate only the class definition with `__init__` and the required methods as stubs. Use type hints. Do not add docstrings unless asked.

---

# ByteBites — Class Diagram

```mermaid
classDiagram
    class Customer {
        +name : str
        +purchase_history : list[Order]
    }

    class FoodItem {
        +name : str
        +price : float
        +category : str
        +popularity_rating : float
    }

    class Menu {
        +items : list[FoodItem]
        +add_item(food_item: FoodItem) None
        +filter_by_category(category: str) list[FoodItem]
    }

    class Order {
        +items : list[FoodItem]
        +add_item(food_item: FoodItem) None
        +calculate_total() float
    }

    Customer "1" --> "0..*" Order : purchase_history
    Order "1" *-- "1..*" FoodItem : contains
    Menu "1" o-- "0..*" FoodItem : aggregates
```

## Relationships

| Relationship | Type | Description |
|---|---|---|
| `Customer` → `Order` | Association | A customer holds zero or more Orders in `purchase_history` |
| `Order` ◆── `FoodItem` | Composition | An Order owns the FoodItems selected in that transaction |
| `Menu` ◇── `FoodItem` | Aggregation | Menu catalogs FoodItems; items exist independently of any Menu |
