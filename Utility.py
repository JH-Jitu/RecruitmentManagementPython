import os

def create_db_folder():
    
    if not os.path.exists("DB"):
        os.makedirs("DB")

def create_db_files():
    
    files = [
        "DB\\RegisteredDevelopers.txt",
        "DB\\RegisteredCompanies.txt",
        "DB\\RegisteredRecruiters.txt",
        "DB\\Admins.txt",
        "DB\\AvailableJobs.txt",
        "DB\\AppliedJobsOfDevelopers.txt",
        "DB\\MessagesForDevelopers.txt",
        "DB\\MessagesForRecruiters.txt",
        "DB\\MessagesForCompanies.txt",
        "DB\\AssignedRecruiters.txt",
        "DB\\Interviews.txt"
    ]

    for file in files:
        if not os.path.exists(file):
            with open(file, "w"):
                pass

def execute():
    create_db_folder()
    create_db_files()

if __name__ == "__main__":
    execute()
