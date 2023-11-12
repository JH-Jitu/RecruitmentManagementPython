import os
from Login import execute as execute_login
from Registration import execute as execute_registration
from Utility import execute as execute_utility

print("Hello")

def execute():
    while True:
        print("\n### Press any option and hit enter ###")
        print("1. Login")
        print("2. Registration")
        print("3. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            execute_login()
        elif option == "2":
            execute_registration()
        elif option == "3":
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    execute_utility()
    execute()
