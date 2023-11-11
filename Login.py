import os
from Registration import register_developer, register_company, register_recruiter
from Developers import execute_developer
from Company import execute_company
from Recruiters import execute_recruiter
from Admins import execute_admin
from ApplyToJob import execute as execute_apply_to_job
from AssignRecruiterFromCompany import execute as execute_assign_recruiter
from SetInterviewByRecruiter import execute as execute_set_interview

def execute():
    while True:
        print("\n### Login ###")
        print("1. Developer")
        print("2. Recruiter")
        print("3. Company")
        print("4. Admin")
        print("5. Back to Main Menu")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            login_as_developer()
        elif choice == "2":
            login_as_recruiter()
        elif choice == "3":
            login_as_company()
        elif choice == "4":
            login_as_admin()
        elif choice == "5":
            break
        elif choice == "6":
            exit()
        else:
            print("Invalid choice. Please try again.")

def login_as_developer():
    email = input("Enter developer email: ")
    password = input("Enter developer password: ")

    # Validate developer credentials
    if validate_credentials("DB\\RegisteredDevelopers.txt", email, password):
        # Call developer panel
        execute_developer(email)
    else:
        print("Invalid credentials. Please try again.")

def login_as_recruiter():
    email = input("Enter recruiter email: ")
    password = input("Enter recruiter password: ")

    # Validate recruiter credentials
    if validate_credentials("DB\\RegisteredRecruiters.txt", email, password):
        # Call recruiter panel
        execute_recruiter(email)
    else:
        print("Invalid credentials. Please try again.")

def login_as_company():
    email = input("Enter company email: ")
    password = input("Enter company password: ")

    # Validate company credentials
    if validate_credentials("DB\\RegisteredCompanies.txt", email, password):
        # Call company panel
        execute_company(email)
    else:
        print("Invalid credentials. Please try again.")

def login_as_admin():
    email = input("Enter admin email: ")
    password = input("Enter admin password: ")

    # Validate admin credentials
    if validate_credentials("DB\\Admins.txt", email, password):
        # Call admin panel
        execute_admin(email)
    else:
        print("Invalid credentials. Please try again.")

def validate_credentials(file_path, email, password):
    # Validate credentials from the specified file
    with open(file_path, "r") as file:
        for line in file:
            stored_email, stored_password, _ = line.strip().split("#")
            if email == stored_email and password == stored_password:
                return True
    return False

if __name__ == "__main__":
    execute()
