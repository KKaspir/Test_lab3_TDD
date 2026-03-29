def run():
    current_character = None
    while True:
        print("1. Create character")
        print("2. Show character sheet")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "2":
            if current_character is None:
                print("No character created yet.")
            else:
                print(current_character.display_sheet())
        if choice == "3":
            print("Goodbye!")
            break


if __name__ == "__main__":
    run()