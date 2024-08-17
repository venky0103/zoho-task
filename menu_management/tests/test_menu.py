import unittest
from menu.meal_with_cache import MealWithCache
from menu.menu_item import MenuItem

class TestMenu(unittest.TestCase):
    def test_add_menu_item(self):
        meal = MealWithCache("Breakfast")
        item = MenuItem("Pancakes", "Delicious pancakes with syrup")
        meal.add_menu_item("Main Course", item)
        self.assertIn("Main Course", meal.categories)
        self.assertIn(item, meal.categories["Main Course"].items)

if __name__ == '__main__':
    unittest.main()
