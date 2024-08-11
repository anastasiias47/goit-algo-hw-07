from classes import AddressBook
from functionality import parse_input, add_contact, change_contact, show_contact, all_contacts, add_birthday, show_birthday


def main():
    address_book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, address_book))

        elif command == "change":
            print(change_contact(args, address_book))

        elif command == "phone":
            print(show_contact(args, address_book))

        elif command == "all":
            print(all_contacts(address_book))

        elif command == "add-birthday":
            print(add_birthday(args, address_book))

        elif command == "show-birthday":
            print(show_birthday(args, address_book))

        elif command == "birthdays":
            print(address_book.get_upcoming_birthdays())

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

