from character import Character


def create_character():
    name = input("Enter name: ")
    race = input("Enter race (Human, Elf, Dwarf): ")
    character_class = input("Enter class (Fighter, Wizard, Rogue): ")
    character = Character(name=name, race=race, character_class=character_class)
    character.roll_stats()
    return character


def run():
    current_character = None
    while True:
        print("1. Create character")
        print("2. Show character sheet")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            current_character = create_character()
            print("Character created!")
        elif choice == "2":
            if current_character is None:
                print("No character created yet.")
            else:
                print(current_character.display_sheet())
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    run()