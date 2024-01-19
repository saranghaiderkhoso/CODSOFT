# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:29:18 2024

@author: PMLS
"""

class contact_book:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact {name} added successfully.")

    def view_contact_list(self):
        print("Contact List:")
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

    def search_contact(self, search_term):
        search_results = []
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details['phone']:
                search_results.append((name, details))
        if search_results:
            print("Search Results:")
            for name, details in search_results:
                print(f"Name: {name}, Phone: {details['phone']}")
        else:
            print("No matching contacts found.")

    def update_contact(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")

# Sample usage
contact_manager = contact_book()

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        contact_manager.add_contact(name, phone, email, address)

    elif choice == '2':
        contact_manager.view_contact_list()

    elif choice == '3':
        search_term = input("Enter Name or Phone Number to search: ")
        contact_manager.search_contact(search_term)

    elif choice == '4':
        name = input("Enter Name of the contact to update: ")
        phone = input("Enter new Phone Number: ")
        email = input("Enter new Email: ")
        address = input("Enter new Address: ")
        contact_manager.update_contact(name, phone, email, address)

    elif choice == '5':
        name = input("Enter Name of the contact to delete: ")
        contact_manager.delete_contact(name)

    elif choice == '6':
        print("Exiting Contact Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
