import os
from Developer import view_personal_information as developerInformation
from Company import view_personal_information as companyInformation

def execute(recruiter_email):
    while True:
        print("\n### Recruiter Panel ###")
        print("1. View Personal Information")
        print("2. View Messages")
        print("3. See Interviews")
        print("4. Set Interview")
        print("5. Approve/Reject Developer")
        print("6. Back to Login Menu")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_personal_information(recruiter_email)
        elif choice == "2":
            view_messages(recruiter_email)
        elif choice == "3":
            see_interviews(recruiter_email)
        elif choice == "4":
            set_interview(recruiter_email)
        elif choice == "5":
            approve_reject_developer(recruiter_email)
        elif choice == "6":
            break
        elif choice == "7":
            exit()
        else:
            print("Invalid choice. Please try again.")

def view_personal_information(recruiter_email):
    # Read recruiter information from RegisteredRecruiters.txt
    with open("DB\\RegisteredRecruiters.txt", "r") as file:
        for line in file:
            email, password, name, age, expertise_skills, project_links, linkedin_link = line.strip().split("#")
            if email == recruiter_email:
                print("\n### Personal Information ###")
                print(f"Email: {email}")
                print(f"Password: {password}")  
                print(f"Name: {name}")
                print(f"Age: {age}")
                print(f"Expertise Skills: {expertise_skills}")
                print(f"Project Links: {project_links}")
                print(f"LinkedIn Link: {linkedin_link}")
                break

def view_messages(recruiter_email):
    # Read messages from MessagesForRecruiters.txt
    with open("DB\\MessagesForRecruiters.txt", "r") as file:
        messages = [line.strip() for line in file]

    if not messages:
        print("No messages available.")
    else:
        count = 0
        print("\n### Messages ###")
        for message in messages:
            elements = message.split("#")
            if recruiter_email in elements[7]:
                
                print(f"-------------------Message No: {count+1}----------------------")
                developerInformation(elements[1])
                print("Applied in Company:")
                companyInformation(elements[2])
                print("--------------------------------------\n")
                count += 1


def see_interviews(recruiter_email):
    # Read interviews from Interviews.txt
    with open("DB\\Interviews.txt", "r") as file:
        interviews = [line.strip() for line in file if recruiter_email in line]

    if not interviews:
        print("No interviews scheduled.")
    else:
        print("\n### Interviews ###")
        for interview in interviews:
            print(interview)

def set_interview(recruiter_email):
    # Read applied jobs from MessagesForRecruiters.txt
    with open("DB\\MessagesForRecruiters.txt", "r") as file:
        applied_jobs = [line.strip() for line in file if line.startswith(recruiter_email)]

    if not applied_jobs:
        print("No developers assigned to you.")
        return

    print("\n### Assigned Developers ###")
    for i, applied_job in enumerate(applied_jobs, start=1):
        print(f"{i}. {applied_job}")

    applied_job_choice = int(input("Enter the number of the assigned developer: "))
    selected_applied_job = applied_jobs[applied_job_choice - 1]

    # Extract developer email from the selected applied job
    developer_email = selected_applied_job.split("#")[1]

    date_and_time = input("Enter date and time for the interview: ")
    assignment_link = input("Enter assignment link: ")
    google_meet_link = input("Enter Google Meet link: ")
    participators = input("Enter a comma-separated list of participators' emails: ")

    # Save interview information to file (Interviews.txt)
    with open("DB\\Interviews.txt", "a") as file:
        file.write(f"{developer_email}#{date_and_time}#{assignment_link}#{google_meet_link}#{participators}\n")

    print("Interview scheduled successfully!")

def approve_reject_developer(recruiter_email):
    # Read applied jobs from MessagesForRecruiters.txt
    with open("DB\\MessagesForRecruiters.txt", "r") as file:
        applied_jobs = [line.strip() for line in file if line.startswith(recruiter_email)]

    if not applied_jobs:
        print("No developers assigned to you.")
        return

    print("\n### Assigned Developers ###")
    for i, applied_job in enumerate(applied_jobs, start=1):
        print(f"{i}. {applied_job}")

    applied_job_choice = int(input("Enter the number of the assigned developer: "))
    selected_applied_job = applied_jobs[applied_job_choice - 1]

    # Extract developer email from the selected applied job
    developer_email = selected_applied_job.split("#")[1]

    decision = input("Enter 'approve' or 'reject' for the developer: ")

    # Save decision to MessagesForDevelopers.txt
    with open("DB\\MessagesForDevelopers.txt", "a") as file:
        file.write(f"{developer_email}#{decision}\n")

    print("Decision communicated successfully!")

if __name__ == "__main__":
    execute("recruiter@example.com")  #
