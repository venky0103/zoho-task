from menu.category import Category

class Meal:
    def __init__(self, name):
        self.name = name
        self.categories = {}

    def add_category(self, category_name):
        if category_name not in self.categories:
            self.categories[category_name] = Category(category_name)

    def add_menu_item(self, category_name, item):
        if category_name not in self.categories:
            self.add_category(category_name)
        self.categories[category_name].add_item(item)

    def __repr__(self):
        return f"Meal(name='{self.name}', categories={self.categories})"
