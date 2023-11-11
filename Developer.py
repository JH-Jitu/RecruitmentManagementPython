import os

def execute(developer_email):
    while True:
        print("\n### Developer Panel ###")
        print("1. View Personal Information")
        print("2. Apply to Job")
        print("3. View Applied Jobs")
        print("4. View Messages")
        print("5. View Interviews")
        print("6. Back to Main Menu")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_personal_information(developer_email)
        elif choice == "2":
            apply_to_job(developer_email)
        elif choice == "3":
            view_applied_jobs(developer_email)
        elif choice == "4":
            view_messages(developer_email)
        elif choice == "5":
            view_interviews(developer_email)
        elif choice == "6":
            break
        elif choice == "7":
            exit()
        else:
            print("Invalid choice. Please try again.")

def view_personal_information(developer_email):
    # Read developer information from RegisteredDevelopers.txt
    with open("DB\\RegisteredDevelopers.txt", "r") as file:
        for line in file:
            email, password, name, age, expertise_skills, project_links, linkedin_link = line.split("#")
            if email == developer_email:
                print("\n### Personal Information ###")
                print(f"Email: {email}")
                print(f"Name: {name}")
                print(f"Age: {age}")
                print(f"Expertise Skills: {expertise_skills}")
                print(f"Project Links: {project_links}")
                print(f"LinkedIn Link: {linkedin_link}")
                break

def apply_to_job(developer_email):
    # Read available jobs from AvailableJobs.txt
    with open("DB\\AvailableJobs.txt", "r") as file:
        available_jobs = [line.strip() for line in file]

    if not available_jobs:
        print("No available jobs to apply.")
        return

    print("\n### Available Jobs for Application ###")
    for i, job in enumerate(available_jobs, start=1):
        print(f"{i}. {job}")

    job_choice = int(input("Enter the job number to apply: "))
    selected_job = available_jobs[job_choice - 1]

    # Extract company email from the selected job
    company_email = selected_job.split("#")[0]

    # Save application to file (AppliedJobsOfDevelopers.txt)
    with open("DB\\AppliedJobsOfDevelopers.txt", "a") as file:
        file.write(f"{developer_email}#{selected_job}\n")

    # Notify the company about the application
    with open("DB\\MessagesForCompanies.txt", "a") as file:
        file.write(f"{company_email}#Developer {developer_email} applied to job: {selected_job}\n")

    print("Application submitted successfully!")

def view_applied_jobs(developer_email):
    # Read applied jobs from AppliedJobsOfDevelopers.txt
    with open("DB\\AppliedJobsOfDevelopers.txt", "r") as file:
        applied_jobs = [line.strip() for line in file if line.startswith(developer_email)]

    if not applied_jobs:
        print("No applied jobs.")
    else:
        print("\n### Applied Jobs ###")
        for applied_job in applied_jobs:
            print(applied_job)

def view_messages(developer_email):
    # Read messages from MessagesForDevelopers.txt
    with open("DB\\MessagesForDevelopers.txt", "r") as file:
        messages = [line.strip() for line in file if line.startswith(developer_email)]

    if not messages:
        print("No messages available.")
    else:
        print("\n### Messages ###")
        for message in messages:
            print(message)

def view_interviews(developer_email):
    # Read interviews from Interviews.txt
    with open("DB\\Interviews.txt", "r") as file:
        interviews = [line.strip() for line in file if developer_email in line]

    if not interviews:
        print("No interviews scheduled.")
    else:
        print("\n### Scheduled Interviews ###")
        for interview in interviews:
            print(interview)

if __name__ == "__main__":
    execute("developer@example.com")  
