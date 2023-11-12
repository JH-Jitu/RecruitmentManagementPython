import os
from ApplyToJob import apply_to_job


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


def view_applied_jobs(developer_email):
    from Company import view_personal_information as companyInformation
    from Recruiter import view_personal_information as recruiterInformation
    
    with open("DB\\AppliedJobsOfDevelopers.txt", "r") as file:
        applied_jobs = [line.strip() for line in file if line.startswith(developer_email)]

    if not applied_jobs:
        print("No applied jobs.")
    else:
        print("\n### Applied Jobs ###")
        for i, applied_job in enumerate(applied_jobs):
            elements = applied_job.split("#")

            

            print(f"###{i}. Company....###")
            companyInformation(elements[1])
            print(f"Role:  {elements[2]}")
            print(f"Skill Required:  {elements[3]}")
            print(f"Job Description:  {elements[4]}")
            print(f"Joining Date:  {elements[5]}")
            print("\nRecruiter....")
            
            recruiterInformation(elements[6])
            
            print("--------------------------------------\n")


def detailedInformation(developerEmail, companyEmail):
    from Company import view_personal_information as companyInformation
    view_personal_information(developerEmail)
    print("Applied in Company:...")
    companyInformation(companyEmail)
    print("--------------------------------------\n")
    
    

def view_messages(developer_email):
    
    with open("DB\\MessagesForDevelopers.txt", "r") as file:
        messages = [line.strip() for line in file if line.startswith(developer_email)]

    if not messages:
        print("No messages available.")
    else:
        print("\n### Messages ###")
        for message in messages:
            print(message)

    with open("DB\\MessagesForDevelopers.txt", "r") as file:
        messages = [line.strip() for line in file]

    if not messages:
        print("No messages available.")
    else:
        count = 0
        print("\n### Messages ###")
        for message in messages:
            elements = message.split("#")
            if developer_email in elements[2]:
                messageOfApprovement = "***🎉🎉🎉 Successfully Passed Interview! You are joining 🎉🎉🎉***" if elements[0] == "approve" else "***😔 You Failed the Interview! You are joining 😔***"
                print(f"\n###Count No: {count+1}###")               
                print(messageOfApprovement)               
                detailedInformation(elements[2], elements[1])
                count += 1

def view_interviews(developer_email):
    
    with open("DB\\Interviews.txt", "r") as file:
        interviews = [line.strip() for line in file if developer_email in line]

    if not interviews:
        print("No interviews scheduled.")
    else:
        count = 0
        print("\n### Scheduled Interviews ###")
        for interview in interviews:
            elements = interview.split("#")
            if developer_email in elements[1]:
                print(f"\n###Count No: {count+1}")       
                print(f"Job Role: {elements[3]}")       
                print(f"Job Description: {elements[4]}")       
                print(f"Join time for Interview: {elements[7]}")     
                print(f"Interview Meet Link: {elements[9]}")
                print("................................")
                
                count += 1

if __name__ == "__main__":
    execute("developer@example.com")  
