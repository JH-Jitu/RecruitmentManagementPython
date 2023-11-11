import os



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
                # print(f"Password: {password}")  
                print(f"Name: {name}")
                print(f"Age: {age}")
                print(f"Expertise Skills: {expertise_skills}")
                print(f"Project Links: {project_links}")
                print(f"LinkedIn Link: {linkedin_link}")
                break


def openMessages(recruiter_email): 
    # Read messages from MessagesForRecruiters.txt
    with open("DB\\MessagesForRecruiters.txt", "r") as file:
        messages = [line.strip() for line in file]
        return messages


def detailedInformation(developerEmail, companyEmail):
    from Company import view_personal_information as companyInformation
    from Developer import view_personal_information as developerInformation
    developerInformation(developerEmail)
    print("Applied in Company:...")
    companyInformation(companyEmail)
    print("--------------------------------------\n")
    
    

def view_messages(recruiter_email):
    messages = openMessages(recruiter_email)

    if not messages:
        print("No messages available.")
    else:
        count = 0
        print("\n### Messages ###")
        for message in messages:
            elements = message.split("#")
            if recruiter_email in elements[7]:
                print(f"\n###Count No: {count+1}###")               
                detailedInformation(elements[1], elements[2])
                count += 1


def see_interviews(recruiter_email):
    # Read interviews from Interviews.txt
    with open("DB\\Interviews.txt", "r") as file:
        interviews = [line.strip() for line in file]

    if not interviews:
        print("No interviews available.")
    else:
        count = 0
        print("\n### Interviews ###")
        for interview in interviews:
            elements = interview.split("#")
            if recruiter_email in elements[7]:
                print(f"\n###Count No: {count+1}###")               
                detailedInformation(elements[1], elements[0])
                count += 1

        print(f"Total interviews for {recruiter_email}: {count}")

def set_interview(recruiter_email):
    # Read applied jobs from MessagesForRecruiters.txt
    filteredJobs = []
    applied_jobs = openMessages(recruiter_email)

    if not applied_jobs:
        print("No developers/jobs assigned to you.")
        return

    count = 0
    print("\n### Assigned Developers ###")
    for i, applied_job in enumerate(applied_jobs, start=1):
        elements = applied_job.split("#")
        if recruiter_email in elements[7]:
            print(f"\n###Count No: {count+1}###")               
            detailedInformation(elements[1], elements[2])
            count += 1
            filteredJobs.append(applied_job)

    applied_job_choice = int(input("Enter the number of the assigned developer to set Interview: "))
    selected_applied_job = filteredJobs[applied_job_choice - 1]

    # Extract developer  from the selected applied job
    developer = selected_applied_job


    date_and_time = input("Enter date and time for the interview: ")
    assignment_link = input("Enter assignment link: ")
    google_meet_link = input("Enter Google Meet link: ")
    participators = input("Enter a comma-separated list of participators' emails: ")

    # Save interview information to file (Interviews.txt)
    with open("DB\\Interviews.txt", "a") as file:
        file.write(f"{developer}#{date_and_time}#{assignment_link}#{google_meet_link}#{participators}\n")

    print("Interview scheduled successfully!")

def approve_reject_developer(recruiter_email):
    # Read interviews from Interviews.txt

    filteredInterviews = []
    with open("DB\\Interviews.txt", "r") as file:
        interviews = [line.strip() for line in file]

    if not interviews:
        print("No interviews assigned to you.")
        return
    
    else:
        count = 0
        print("\n### Interviews ###")
        for i, interview in enumerate(interviews, start=1):
            elements = interview.split("#")
            if recruiter_email in elements[7]:
                print(f"\n###Count No: {count+1}###")               
                detailedInformation(elements[1], elements[0])
                count += 1
                filteredInterviews.append(interview)

        print(f"Total interviews for {recruiter_email}: {count}")

    applied_job_choice = int(input("Enter the number of the assigned developer: "))
    selected_interview = filteredInterviews[applied_job_choice - 1]

    # Extract developer email from the selected interview
    developer_email = selected_interview.split("#")[0]

    decision = input("Enter 'approve' or 'reject' for the developer: ")

    # Save decision to MessagesForDevelopers.txt
    with open("DB\\MessagesForDevelopers.txt", "a") as file:
        file.write(f"{decision}#{selected_interview}\n")
    with open("DB\\MessagesForCompanies.txt", "a") as file:
        file.write(f"{decision}#{selected_interview}\n")

    # Remove the selected interview from Interviews.txt
    interviews.remove(selected_interview)
    with open("DB\\Interviews.txt", "w") as file:
        file.write("\n".join(interviews))

    print("Decision communicated successfully!")

if __name__ == "__main__":
    execute("recruiter@example.com")  #
