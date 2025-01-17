def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def handle_choice(choice, shopping_list):
    if choice == '1':
        item = "Sample Item to Add"
        shopping_list.append(item)
        print(f"'{item}' has been added to the shopping list.")
    elif choice == '2':
        item = "Sample Item to Remove"
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from the shopping list.")
        else:
            print(f"'{item}' is not in the shopping list.")
    elif choice == '3':
        if shopping_list:
            print("\nCurrent Shopping List:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        else:
            print("\nYour shopping list is empty.")
    elif choice == '4':
        print("Goodbye!")
        return False
    else:
        print("Invalid choice. Please try again.")
    return True

def main():
    shopping_list = []
    print("\nShopping List Manager") 
    choices = ['1', '2', '3', '4']  
    for choice in choices:
        display_menu()
        print(f"Simulated choice: {choice}")  
        if not handle_choice(choice, shopping_list):
            break

if __name__ == "__main__":
    main()
