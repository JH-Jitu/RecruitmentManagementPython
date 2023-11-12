import os
from Registration import register_developer, register_company
from Developer import execute as execute_developer
from Company import execute as execute_company
from Recruiter import execute as execute_recruiter
from Admin import execute as execute_admin
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

    
    if validate_credentials("DB\\RegisteredDevelopers.txt", email, password):
        
        execute_developer(email)
    else:
        print("Invalid credentials. Please try again.")

def login_as_recruiter():
    email = input("Enter recruiter email: ")
    password = input("Enter recruiter password: ")

    
    if validate_credentials("DB\\RegisteredRecruiters.txt", email, password):
        
        execute_recruiter(email)
    else:
        print("Invalid credentials. Please try again.")

def login_as_company():
    email = input("Enter company email: ")
    password = input("Enter company password: ")

    
    if validate_credentials("DB\\RegisteredCompanies.txt", email, password):
        
        execute_company(email)
    else:
        print("Invalid credentials. Please try again.")

def login_as_admin():
    email = input("Enter admin email: ")
    password = input("Enter admin password: ")

    
    if validate_credentials("DB\\Admins.txt", email, password):
        
        execute_admin(email)
    else:
        print("Invalid credentials. Please try again.")





def validate_credentials(file_path, email, password):
    
    with open(file_path, "r") as file:
        for line in file:
            
            parts = line.strip().split("#")
            
            if email == parts[0] and password == parts[1]:
                return True
    return False




if __name__ == "__main__":
    execute()
