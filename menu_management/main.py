from menu.meal_with_cache import MealWithCache
from interface.user_interface import add_menu_item_interface, display_menu

def main():
    # Initialize meals with caching
    breakfast = MealWithCache("Breakfast", cache_size=4)
    lunch = MealWithCache("Lunch", cache_size=4)
    dinner = MealWithCache("Dinner", cache_size=4)
    snacks = MealWithCache("Snacks", cache_size=4)

    # User interaction loop
    while True:
        print("\nChoose an option:")
        print("1. Add Menu Item")
        print("2. Display Menu")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nSelect meal to add an item:")
            print("1. Breakfast")
            print("2. Lunch")
            print("3. Dinner")
            print("4. Snacks")
            meal_choice = input("Enter your choice: ")

            if meal_choice == "1":
                add_menu_item_interface(breakfast)
            elif meal_choice == "2":
                add_menu_item_interface(lunch)
            elif meal_choice == "3":
                add_menu_item_interface(dinner)
            elif meal_choice == "4":
                add_menu_item_interface(snacks)
            else:
                print("Invalid meal choice.")

        elif choice == "2":
            print("\nSelect meal to display:")
            print("1. Breakfast")
            print("2. Lunch")
            print("3. Dinner")
            print("4. Snacks")
            meal_choice = input("Enter your choice: ")

            if meal_choice == "1":
                display_menu(breakfast)
            elif meal_choice == "2":
                display_menu(lunch)
            elif meal_choice == "3":
                display_menu(dinner)
            elif meal_choice == "4":
                display_menu(snacks)
            else:
                print("Invalid meal choice.")

        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
