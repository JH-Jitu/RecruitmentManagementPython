import os

def execute(company_email):
    while True:
        print("\n### Assign Recruiter to Job ###")
        print("1. View Available Jobs")
        print("2. Assign Recruiter")
        print("3. View Assigned Recruiters")
        print("4. Back to Company Panel")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_available_jobs(company_email)
        elif choice == "2":
            assign_recruiter(company_email)
        elif choice == "3":
            view_assigned_recruiters(company_email)
        elif choice == "4":
            break
        elif choice == "5":
            exit()
        else:
            print("Invalid choice. Please try again.")

def view_available_jobs(company_email):
    
    with open("DB\\AvailableJobs.txt", "r") as file:
        available_jobs = [line.strip() for line in file if line.startswith(company_email)]

    if not available_jobs:
        print("No available jobs.")
    else:
        print("\n### Available Jobs ###")
        for job in available_jobs:
            print(job)

def assign_recruiter(company_email):
    
    with open("DB\\AvailableJobs.txt", "r") as file:
        available_jobs = [line.strip() for line in file if line.startswith(company_email)]

    if not available_jobs:
        print("No available jobs to assign recruiters.")
        return

    print("\n### Available Jobs for Assigning Recruiters ###")
    for i, job in enumerate(available_jobs, start=1):
        print(f"{i}. {job}")

    job_choice = int(input("Enter the job number to assign a recruiter: "))
    selected_job = available_jobs[job_choice - 1]

    
    recruiter_email = selected_job.split("#")[-1]

    
    with open("DB\\AssignedRecruiters.txt", "a") as file:
        file.write(f"{company_email}#{selected_job}\n")

    
    with open("DB\\MessagesForRecruiters.txt", "a") as file:
        file.write(f"{recruiter_email}#You have been assigned to job: {selected_job} by {company_email}\n")

    print("Recruiter assigned successfully!")

def view_assigned_recruiters(company_email):
    
    with open("DB\\AssignedRecruiters.txt", "r") as file:
        assigned_recruiters = [line.strip() for line in file if line.startswith(company_email)]

    if not assigned_recruiters:
        print("No assigned recruiters.")
    else:
        print("\n### Assigned Recruiters ###")
        for assigned_recruiter in assigned_recruiters:
            print(assigned_recruiter)

if __name__ == "__main__":
    execute("company@example.com")  
