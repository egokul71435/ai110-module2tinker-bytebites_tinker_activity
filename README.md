# ByteBites — Core Architecture

A Python backend for a campus food ordering app. This project implements the core data model — customers, menu items, menus, and orders — using clean class design and a test suite.

---

## Project Structure

```
bytebites_spec.md          # Original feature request and class definitions
bytebites_design.md        # UML class diagram and agent design instructions
models.py                  # The four core classes
test_models.py             # Exploratory script with sample objects
test_bytebites.py          # Full unit test suite (19 tests)
```

---

## Classes

| Class | Responsibility |
|---|---|
| `FoodItem` | Represents a single product: name, price, category, popularity_rating |
| `Menu` | Catalog of all FoodItems; supports `add_item` and `filter_by_category` |
| `Order` | A purchase transaction; holds selected items and computes `calculate_total` |
| `Customer` | An app user; stores name and a `purchase_history` list of past Orders |

---

## Running the Tests

```bash
python -m pytest
```

pytest auto-discovers `test_bytebites.py` and runs all 19 tests. No configuration required.

---

## How AI Was Used

AI (Claude) was used throughout as a design and implementation partner:

- **Spec interpretation** — Claude parsed the feature request and identified the four candidate classes, their attributes, methods, and relationships before any code was written.

- **UML diagram generation** — Claude produced the Mermaid `classDiagram` in `bytebites_design.md`, including correct relationship types (association, composition, aggregation) and typed attributes. The diagram was reviewed and confirmed against the spec before implementation began.

- **Agent definition** — Claude drafted the `bytebites_design.md` agent instructions, which constrain future AI interactions to stay within the four defined classes and avoid over-engineering.

- **Code scaffolding** — Claude generated the initial class stubs in `models.py` following the UML design, with type hints and no unnecessary extras.

- **Test suite** — Claude wrote `test_bytebites.py` using `unittest.TestCase`, covering happy paths and edge cases. Each test has a single-sentence description of the behavior being verified, not the implementation.

In all cases, AI output was reviewed against the spec and design files before being accepted. The spec and UML diagram served as ground truth — AI suggestions that introduced extra classes, methods, or complexity were rejected.
