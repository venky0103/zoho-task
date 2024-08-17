from menu.meal import Meal
from menu.menu_cache import MenuCache

class MealWithCache(Meal):
    def __init__(self, name, cache_size=4):
        super().__init__(name)
        self.cache = MenuCache(max_size=cache_size)

    def add_menu_item(self, category_name, item):
        super().add_menu_item(category_name, item)
        self.cache.add(category_name, self.categories[category_name])

    def get_category(self, category_name):
        category = self.cache.get(category_name)
        if category is None:
            if category_name in self.categories:
                category = self.categories[category_name]
                self.cache.add(category_name, category)
        return category

    def __repr__(self):
        return f"MealWithCache(name='{self.name}', categories={self.categories}, cache={self.cache})"
