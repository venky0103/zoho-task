from menu.menu_item import MenuItem

def add_menu_item_interface(meal):
    try:
        category_name = input("Enter the category (Starters, Main Course, etc.): ")
        if not category_name:
            raise ValueError("Category name cannot be empty.")
        item_name = input("Enter the item name: ")
        item_description = input("Enter the item description: ")
        item = MenuItem(item_name, item_description)
        meal.add_menu_item(category_name, item)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def display_menu(meal):
    for category_name, category in meal.categories.items():
        print(f"\n{category_name}:")
        for item in category.items:
            print(f"  - {item.name}: {item.description}")
