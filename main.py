from schema.schema import prompt_contact_input, PersonSchema
from services.system import BookSystem
from services.search import BookSearcher

class AddressBookApp:
    system = BookSystem()

    @staticmethod
    def start():
        print("\nWelcome to the Smart Address Book App!")

    @staticmethod
    def menu():
        print("\nOptions:")
        print("1. Create Address Book")
        print("2. Add Contact")
        print("3. Display Contacts")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Search by City")
        print("7. Search by State")
        print("8. Export Contacts")
        print("9. Exit")

        try:
            option = int(input("Select option: "))
            if option == 1:
                name = input("Enter book name: ")
                AddressBookApp.system.create_book(name)

            elif option == 2:
                name = input("Book to add contact to: ")
                book = AddressBookApp.system.get_book(name)
                person_data = prompt_contact_input(PersonSchema)
                book.add_person(**person_data.__dict__)

            elif option == 3:
                name = input("Book name to view: ")
                book = AddressBookApp.system.get_book(name)
                for p in sorted(book.contacts, key=lambda x: x.first_name.lower()): #UC10
                    print(p)

            elif option == 4:
                # Implement contact edit logic here
                pass

            elif option == 5:
                # Implement contact delete logic here
                pass

            elif option == 6:
                searcher = BookSearcher(AddressBookApp.system.list_books())
                city = input("City to search: ")
                for person in searcher.search_by_city(city):
                    print(person)

            elif option == 7:
                searcher = BookSearcher(AddressBookApp.system.list_books())
                state = input("State to search: ")
                for person in searcher.search_by_state(state):
                    print(person)

            elif option == 8:
                name = input("Export contacts from book: ")
                book = AddressBookApp.system.get_book(name)
                fmt = input("Format (txt/csv/json): ").strip().lower()
                filename = f"{name}.{fmt}"
                if fmt == 'txt':
                    book.export_txt(filename)
                elif fmt == 'csv':
                    book.export_csv(filename)
                elif fmt == 'json':
                    book.export_json(filename)

            elif option == 9:
                print("Goodbye!")
                exit()
            else:
                print("Invalid option.")
        except ValueError as ve:
            print(f"Input error: {ve}")
#UC11: Sort Location is here 
           
if __name__ == "__main__":
    AddressBookApp.start()
    while True:
        AddressBookApp.menu()
