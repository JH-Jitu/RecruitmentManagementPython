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

    
    recruiters = get_recruiters()
    print("\n### Available Recruiters ###")
    for i, recruiter in enumerate(recruiters, start=1):
        print(f"{i}. {recruiter}")

    recruiter_choice = int(input("Enter the recruiter number: "))
    selected_recruiter = recruiters[recruiter_choice - 1]

    
    with open("DB\\AvailableJobs.txt", "a") as file:
        file.write(f"{company_email}#{role_name}#{required_skills}#{job_description}#{joining_date}#{selected_recruiter}\n")

    print("Job created successfully!")

def delete_job(company_email):
    
    filteredJobs = []
    with open("DB\\AvailableJobs.txt", "r") as file:
        available_jobs = [line.strip() for line in file]

    if not available_jobs:
        print("No jobs available for deletion.")
        return
    else:
        count = 0
        print("\n### Available Jobs for Deletion ###")
        for i, job in enumerate(available_jobs, start=1):
            elements = job.split("#")
            if company_email in elements[0]:
                print(f"###Count {count+1}\n")
                print(f"Role:  {elements[1]}")
                print(f"Skill Required:  {elements[2]}")
                print(f"Job Description:  {elements[3]}")
                print(f"Joining Date:  {elements[4]}")
                print("--------------------------------------\n")
                count += 1
                filteredJobs.append(job)

    job_choice = int(input("Enter the job number to delete: "))
    selected_job = filteredJobs[job_choice - 1]

    
    available_jobs.remove(selected_job)
    with open("DB\\AvailableJobs.txt", "w") as file:
        file.write("\n".join(available_jobs))

    print("Job deleted successfully!")

def view_available_jobs(company_email):
    from Recruiter import view_personal_information as recruiterInformation
    
    with open("DB\\AvailableJobs.txt", "r") as file:
        available_jobs = [line.strip() for line in file if line.startswith(company_email)]

    if not available_jobs:
        print("No available jobs.")
    else:
        print("\n### Available Jobs ###")
        for i, job in enumerate(available_jobs, start=1):
            elements = job.split("#")
            print(f"###Count {i}\n")
            print(f"Role:  {elements[1]}")
            print(f"Skill Required:  {elements[2]}")
            print(f"Job Description:  {elements[3]}")
            print(f"Joining Date:  {elements[4]}")
            print("\nRecruiter....")
            recruiterInformation(elements[5])
            print("--------------------------------------\n")

def view_personal_information(company_email):
    
    with open("DB\\RegisteredCompanies.txt", "r") as file:
        for line in file:
            email, password, name, license_no, employee_number = line.strip().split("#")
            if email == company_email:
                print("\n### Personal Information ###")
                print(f"Email: {email}")
                print(f"Name: {name}")
                print(f"License No: {license_no}")
                print(f"Employee Number: {employee_number}")
                break

def get_recruiters():
    
    with open("DB\\RegisteredRecruiters.txt", "r") as file:
        recruiters = [line.split("#")[0] for line in file]

    return recruiters

if __name__ == "__main__":
    execute("company@example.com")  
