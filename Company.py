import os

def execute(company_email):
    while True:
        print("\n### Company Panel ###")
        print("1. Create Job")
        print("2. Delete Job")
        print("3. View Available Jobs")
        print("4. View Personal Information")
        print("5. Back to Login Menu")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_job(company_email)
        elif choice == "2":
            delete_job(company_email)
        elif choice == "3":
            view_available_jobs(company_email)
        elif choice == "4":
            view_personal_information(company_email)
        elif choice == "5":
            break
        elif choice == "6":
            exit()
        else:
            print("Invalid choice. Please try again.")

def create_job(company_email):
    print("\n### Create Job ###")
    role_name = input("Enter role name: ")
    required_skills = input("Enter required skills: ")
    job_description = input("Enter job description: ")
    joining_date = input("Enter joining date: ")

    # Assign a recruiter from the list
    recruiters = get_recruiters()
    print("\n### Available Recruiters ###")
    for i, recruiter in enumerate(recruiters, start=1):
        print(f"{i}. {recruiter}")

    recruiter_choice = int(input("Enter the recruiter number: "))
    selected_recruiter = recruiters[recruiter_choice - 1]

    # Save job information to file (AvailableJobs.txt)
    with open("DB\\AvailableJobs.txt", "a") as file:
        file.write(f"{company_email}#{role_name}#{required_skills}#{job_description}#{joining_date}#{selected_recruiter}\n")

    print("Job created successfully!")

def delete_job(company_email):
    # Read available jobs from AvailableJobs.txt
    with open("DB\\AvailableJobs.txt", "r") as file:
        available_jobs = [line.strip() for line in file if line.startswith(company_email)]

    if not available_jobs:
        print("No jobs available for deletion.")
        return

    print("\n### Available Jobs for Deletion ###")
    for i, job in enumerate(available_jobs, start=1):
        print(f"{i}. {job}")

    job_choice = int(input("Enter the job number to delete: "))
    selected_job = available_jobs[job_choice - 1]

    # Remove the job from AvailableJobs.txt
    with open("DB\\AvailableJobs.txt", "w") as file:
        for line in available_jobs:
            if line != selected_job:
                file.write(line + "\n")

    print("Job deleted successfully!")

def view_available_jobs(company_email):
    # Read available jobs from AvailableJobs.txt
    with open("DB\\AvailableJobs.txt", "r") as file:
        available_jobs = [line.strip() for line in file if line.startswith(company_email)]

    if not available_jobs:
        print("No available jobs.")
    else:
        print("\n### Available Jobs ###")
        for job in available_jobs:
            print(job)

def view_personal_information(company_email):
    # Read company information from RegisteredCompanies.txt
    with open("DB\\RegisteredCompanies.txt", "r") as file:
        for line in file:
            email, password, name, license_no, employee_number = line.strip().split("#")
            if email == company_email:
                print("\n### Personal Information ###")
                print(f"Email: {email}")
                print(f"Password: {password}")  
                print(f"Name: {name}")
                print(f"License No: {license_no}")
                print(f"Employee Number: {employee_number}")
                break

def get_recruiters():
    # Read registered recruiters from RegisteredRecruiters.txt
    with open("DB\\RegisteredRecruiters.txt", "r") as file:
        recruiters = [line.split("#")[0] for line in file]

    return recruiters

if __name__ == "__main__":
    execute("company@example.com")  
