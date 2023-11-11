import os

def register_user():
    while True:
        print("\n### Registration ###")
        print("1. Developer")
        print("2. Company")
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

def register_developer():
    print("\n### Developer Registration ###")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    expertise_skills = input("Enter your expertise skills: ")
    project_links = input("Enter your project links: ")
    linkedin_link = input("Enter your LinkedIn link: ")

    # Save developer information to file (RegisteredDevelopers.txt)
    with open("DB\\RegisteredDevelopers.txt", "a") as file:
        file.write(f"{email}#{password}#{name}#{age}#{expertise_skills}#{project_links}#{linkedin_link}\n")

    print("Developer registered successfully!")

def register_company():
    print("\n### Company Registration ###")
    name = input("Enter company name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    license_no = input("Enter company license number: ")
    employee_number = input("Enter company employee number: ")

    # Save company information to file (RegisteredCompanies.txt)
    with open("DB\\RegisteredCompanies.txt", "a") as file:
        file.write(f"{name}#{email}#{password}#{license_no}#{employee_number}\n")

    print("Company registered successfully!")

# You can add more functions for additional registration logic as needed

if __name__ == "__main__":
    register_user()