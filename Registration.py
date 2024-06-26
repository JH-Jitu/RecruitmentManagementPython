import os
import random
import string

def execute():
    while True:
        print("\n### Registration ###")
        print("1. Register as Developer")
        print("2. Register as Company")
        print("3. Back to Main Menu")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_developer()
        elif choice == "2":
            register_company()
        elif choice == "3":
            break
        elif choice == "4":
            exit()
        else:
            print("Invalid choice. Please try again.")

def generate_random_password():
    
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return password

def register_developer():
    print("\n### Register as Developer ###")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    expertise_skills = input("Enter your expertise skills (comma-separated): ")
    project_links = input("Enter your project links (comma-separated): ")
    linkedin_link = input("Enter your LinkedIn link: ")

    
    with open("DB\\RegisteredDevelopers.txt", "a") as file:
        file.write(f"{email}#{password}#{name}#{age}#{expertise_skills}#{project_links}#{linkedin_link}\n")

    print("Registration successful!")
    print(f"Your password is: {password}")

def register_company():
    print("\n### Register as Company ###")
    name = input("Enter company name: ")
    email = input("Enter company email: ")
    password = input("Enter your password: ")
    license_no = input("Enter company license number: ")
    employee_number = input("Enter company employee number: ")

    
    with open("DB\\RegisteredCompanies.txt", "a") as file:
        file.write(f"{email}#{password}#{name}#{license_no}#{employee_number}\n")

    print("Registration successful!")
    print(f"Your password is: {password}")

