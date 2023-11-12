import os

def execute(recruiter_email):
    while True:
        print("\n### Set Interview by Recruiter ###")
        print("1. View Applied Jobs")
        print("2. Set Interview")
        print("3. View Scheduled Interviews")
        print("4. Back to Recruiter Panel")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_applied_jobs(recruiter_email)
        elif choice == "2":
            set_interview(recruiter_email)
        elif choice == "3":
            view_scheduled_interviews(recruiter_email)
        elif choice == "4":
            break
        elif choice == "5":
            exit()
        else:
            print("Invalid choice. Please try again.")

def view_applied_jobs(recruiter_email):
    
    with open("DB\\MessagesForRecruiters.txt", "r") as file:
        applied_jobs = [line.strip() for line in file if line.startswith(recruiter_email)]

    if not applied_jobs:
        print("No developers applied to your jobs.")
    else:
        print("\n### Applied Jobs ###")
        for applied_job in applied_jobs:
            print(applied_job)

def set_interview(recruiter_email):
    
    with open("DB\\MessagesForRecruiters.txt", "r") as file:
        applied_jobs = [line.strip() for line in file if line.startswith(recruiter_email)]

    if not applied_jobs:
        print("No developers applied to your jobs.")
        return

    print("\n### Applied Jobs for Setting Interviews ###")
    for i, applied_job in enumerate(applied_jobs, start=1):
        print(f"{i}. {applied_job}")

    applied_job_choice = int(input("Enter the number of the applied job to set an interview: "))
    selected_applied_job = applied_jobs[applied_job_choice - 1]

    
    developer_email = selected_applied_job.split("#")[1]

    date_and_time = input("Enter date and time for the interview: ")
    assignment_link = input("Enter assignment link: ")
    google_meet_link = input("Enter Google Meet link: ")
    participators = input("Enter a comma-separated list of participators' emails: ")

    
    with open("DB\\Interviews.txt", "a") as file:
        file.write(f"{developer_email}#{date_and_time}#{assignment_link}#{google_meet_link}#{participators}\n")

    
    with open("DB\\MessagesForDevelopers.txt", "a") as file:
        file.write(f"{developer_email}#You have been scheduled for an interview by {recruiter_email}\n")

    print("Interview scheduled successfully!")

def view_scheduled_interviews(recruiter_email):
    
    with open("DB\\Interviews.txt", "r") as file:
        interviews = [line.strip() for line in file if recruiter_email in line]

    if not interviews:
        print("No interviews scheduled.")
    else:
        print("\n### Scheduled Interviews ###")
        for interview in interviews:
            print(interview)

if __name__ == "__main__":
    execute("recruiter@example.com") 
