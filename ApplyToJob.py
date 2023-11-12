import os

def execute(developer_email):
    while True:
        print("\n### Apply to Job ###")
        print("1. View Available Jobs")
        print("2. Apply to Job")
        print("3. View Applied Jobs")
        print("4. View Messages")
        print("5. Back to Developer Panel")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_available_jobs(developer_email)
        elif choice == "2":
            apply_to_job(developer_email)
        elif choice == "3":
            view_applied_jobs(developer_email)
        elif choice == "4":
            view_messages(developer_email)
        elif choice == "5":
            break
        elif choice == "6":
            exit()
        else:
            print("Invalid choice. Please try again.")

def view_available_jobs(developer_email):
    
    with open("DB\\AvailableJobs.txt", "r") as file:
        available_jobs = [line.strip() for line in file]

    if not available_jobs:
        print("No available jobs.")
    else:
        print("\n### Available Jobs ###")
        for i, job in enumerate(available_jobs, start=1):
            print(f"{i}. {job}")

def apply_to_job(developer_email):
    from Company import view_personal_information as companyInformation
    from Recruiter import view_personal_information as recruiterInformation

    
    developer_skills = None
    with open("DB\\RegisteredDevelopers.txt", "r") as file:
        for line in file:
            if line.startswith(developer_email):
                developer_skills = line.split("#")[4].split(", ")

    if developer_skills is None:
        print("Developer skills not found.")
        return

    
    with open("DB\\AvailableJobs.txt", "r") as file:
        available_jobs = [line.strip() for line in file]

    if not available_jobs:
        print("No available jobs to apply.")
        return

    
    matching_jobs = []
    for job in available_jobs:
        
        company_email = job.split("#")[0]
        required_skills = job.split("#")[2]
        company_required_skills = set(required_skills.split(", "))
        developer_skills_set = set(developer_skills)
        
        
        if developer_skills_set.intersection(company_required_skills):
            matching_jobs.append(job)

    if not matching_jobs:
        print("No available jobs matching your skills.")
        return
    

    print("\n### Available Jobs for Application ###")
    for i, job in enumerate(matching_jobs, start=1):
        elements = job.split("#")
        print(f"###Count {i}\n")
        companyInformation(elements[0])
        print(f"Role:  {elements[1]}")
        print(f"Skill Required:  {elements[2]}")
        print(f"Job Description:  {elements[3]}")
        print(f"Joining Date:  {elements[4]}")
        print("\nRecruiter....")
        recruiterInformation(elements[5])
        print("--------------------------------------\n")

    job_choice = int(input("Enter the job number to apply: "))
    selected_job = matching_jobs[job_choice - 1]

    
    company_email = selected_job.split("#")[0]

    
    if not is_duplicate_application(developer_email, selected_job):
        
        with open("DB\\AppliedJobsOfDevelopers.txt", "a") as file:
            file.write(f"{developer_email}#{selected_job}\n")

        
        company_email = selected_job.split("#")[0]
        with open("DB\\MessagesForRecruiters.txt", "a") as file:
            file.write(f"{company_email}#Developer {developer_email} applied to job: {selected_job}\n")

        print("Application submitted successfully!")
    else:
        print("Application already exists. Cannot submit duplicate application.")

def is_duplicate_application(developer_email, selected_job):
    
    with open("DB\\AppliedJobsOfDevelopers.txt", "r") as file:
        for line in file:
            if line.strip() == f"{developer_email}#{selected_job}":
                return True
    return False
    


def view_applied_jobs(developer_email):
    
    with open("DB\\AppliedJobsOfDevelopers.txt", "r") as file:
        applied_jobs = [line.strip() for line in file if line.startswith(developer_email)]

    if not applied_jobs:
        print("No applied jobs.")
    else:
        print("\n### Applied Jobs ###")
        for applied_job in applied_jobs:
            print(applied_job)

def view_messages(developer_email):
    
    with open("DB\\MessagesForDevelopers.txt", "r") as file:
        messages = [line.strip() for line in file if line.startswith(developer_email)]

    if not messages:
        print("No messages available.")
    else:
        print("\n### Messages ###")
        for message in messages:
            print(message)

if __name__ == "__main__":
    execute("developer@example.com")  