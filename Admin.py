import os

def execute(admin_email):
    while True:
        print("\n### Admin Panel ###")
        print("1. Create Recruiter")
        print("2. Delete Company")
        print("3. Delete Recruiter")
        print("4. Delete Developer")
        print("5. Create Admin")
        print("6. Back to Login Menu")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_recruiter()
        elif choice == "2":
            delete_company()
        elif choice == "3":
            delete_recruiter()
        elif choice == "4":
            delete_developer()
        elif choice == "5":
            create_admin()
        elif choice == "6":
            break
        elif choice == "7":
            exit()
        else:
            print("Invalid choice. Please try again.")

def create_recruiter():
    print("\n### Create Recruiter ###")
    email = input("Enter recruiter email: ")
    password = input("Enter recruiter password: ")
    name = input("Enter recruiter name: ")
    age = input("Enter recruiter age: ")
    expertise_skills = input("Enter recruiter expertise skills: ")
    project_links = input("Enter recruiter project links: ")
    linkedin_link = input("Enter recruiter LinkedIn link: ")

    # Save recruiter information to file (RegisteredRecruiters.txt)
    with open("DB\\RegisteredRecruiters.txt", "a") as file:
        file.write(f"{email}#{password}#{name}#{age}#{expertise_skills}#{project_links}#{linkedin_link}\n")

    print("Recruiter created successfully!")

def delete_company():
    # Read companies from RegisteredCompanies.txt
    with open("DB\\RegisteredCompanies.txt", "r") as file:
        companies = [line.strip() for line in file]

    if not companies:
        print("No companies available for deletion.")
        return

    print("\n### Available Companies for Deletion ###")
    for i, company in enumerate(companies, start=1):
        print(f"{i}. {company}")

    company_choice = int(input("Enter the company number to delete: "))
    selected_company = companies[company_choice - 1]

    # Remove the company from RegisteredCompanies.txt
    with open("DB\\RegisteredCompanies.txt", "w") as file:
        for line in companies:
            if line != selected_company:
                file.write(line + "\n")

    # Extract company email from the selected company
    selectedCompanyElements = selected_company.split("#")
    company_email = selectedCompanyElements[0]

    # Remove jobs associated with the company from AvailableJobs.txt
    with open("DB\\AvailableJobs.txt", "r") as file:
        available_jobs = [line.strip() for line in file if not line.startswith(company_email)]

    # Write the updated list back to AvailableJobs.txt
    with open("DB\\AvailableJobs.txt", "w") as file:
        file.write("\n".join(available_jobs))

    print("Company deleted successfully!")

def delete_recruiter():
    # Read recruiters from RegisteredRecruiters.txt
    with open("DB\\RegisteredRecruiters.txt", "r") as file:
        recruiters = [line.strip() for line in file]

    if not recruiters:
        print("No recruiters available for deletion.")
        return

    print("\n### Available Recruiters for Deletion ###")
    for i, recruiter in enumerate(recruiters, start=1):
        print(f"{i}. {recruiter}")

    recruiter_choice = int(input("Enter the recruiter number to delete: "))
    selected_recruiter = recruiters[recruiter_choice - 1]

    # Remove the recruiter from RegisteredRecruiters.txt
    with open("DB\\RegisteredRecruiters.txt", "w") as file:
        for line in recruiters:
            if line != selected_recruiter:
                file.write(line + "\n")

    # Extract recruiter email from the selected recruiter
    recruiter_email = selected_recruiter.split("#")[0]

    # Remove jobs associated with the recruiter from AvailableJobs.txt
    with open("DB\\AvailableJobs.txt", "r") as file:
        available_jobs = [line.strip() for line in file if recruiter_email not in line]

    # Write the updated list back to AvailableJobs.txt
    with open("DB\\AvailableJobs.txt", "w") as file:
        file.write("\n".join(available_jobs))

    print("Recruiter deleted successfully!")


def delete_developer():
    # Read developers from RegisteredDevelopers.txt
    with open("DB\\RegisteredDevelopers.txt", "r") as file:
        developers = [line.strip() for line in file]

    if not developers:
        print("No developers available for deletion.")
        return

    print("\n### Available Developers for Deletion ###")
    for i, developer in enumerate(developers, start=1):
        print(f"{i}. {developer}")

    developer_choice = int(input("Enter the developer number to delete: "))
    selected_developer = developers[developer_choice - 1]

    # Remove the developer from RegisteredDevelopers.txt
    with open("DB\\RegisteredDevelopers.txt", "w") as file:
        for line in developers:
            if line != selected_developer:
                file.write(line + "\n")

    # Remove applications and messages associated with the developer
    with open("DB\\AppliedJobsOfDevelopers.txt", "r") as file:
        applied_jobs = [line.strip() for line in file if selected_developer.split("#")[0] in line]

    with open("DB\\AppliedJobsOfDevelopers.txt", "w") as file:
        for line in applied_jobs:
            if selected_developer.split("#")[0] not in line:
                file.write(line + "\n")

    with open("DB\\MessagesForDevelopers.txt", "r") as file:
        messages = [line.strip() for line in file if selected_developer.split("#")[0] in line]

    with open("DB\\MessagesForDevelopers.txt", "w") as file:
        for line in messages:
            if selected_developer.split("#")[0] not in line:
                file.write(line + "\n")

    print("Developer deleted successfully!")

def create_admin():
    print("\n### Create Admin ###")
    email = input("Enter admin email: ")
    password = input("Enter admin password: ")
    name = input("Enter admin name: ")

    # Save admin information to file (Admins.txt)
    with open("DB\\Admins.txt", "a") as file:
        file.write(f"{email}#{password}#{name}\n")

    print("Admin created successfully!")

if __name__ == "__main__":
    execute("admin@example.com")  
