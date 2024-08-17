class Category:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __repr__(self):
        return f"Category(name='{self.name}', items={self.items})"
