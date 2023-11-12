# \***\*Recruiting Management Console Project in Python\*\***

## **Introduction**

This Python console project aims to create a robust Recruiting Management system with dedicated functionalities for Developers, Recruiters, Companies, and Admins. The project architecture is designed for modularity and ease of maintenance through the division of functionality across multiple files.

## **Files and Functions**

### **Panel Files**

1. **Developers (Developer.py):**
   - Properties: Email, Password, Name, Age, Expertise skills, Project links, LinkedIn link.
   - Functionality: Developers can apply to jobs, view messages, and interviews.
2. **Recruiters (Recruiter.py):**
   - Properties: Same as Developers.
   - Functionality: Recruiters can view messages, interviews, set interviews, and approve/reject developers.
3. **Companies (Company.py):**
   - Properties: Company Name, Email, Password, License No, Employee Number.
   - Functionality: Companies can create and delete jobs, view available jobs.
4. **Admin (Admin.py):**
   - Properties: Name, Email, Password, Created Date.
   - Functionality: Admins can create recruiters, delete companies, recruiters, and developers, and create new admins.

### **Process Execution Files and Functions**

1. **Login (Login.py):**
   - Functionality: Authenticate users (Developers, Recruiters, Companies, Admins) based on their credentials.
2. **Registration (Registration.py):**
   - Functionality: Allows users to register as Developers or Companies, collecting necessary information.
3. **ApplyToJob (ApplyToJob.py):**
   - Functionality: Developers can apply to jobs based on their expertise, saving the data in AppliedJobsOfDevelopers.txt.
4. **AssignRecruiterFromCompany (AssignRecruiterFromCompany.py):**
   - Functionality: Companies can assign recruiters to jobs, updating the database.
5. **SetInterviewByRecruiter (SetInterviewByRecruiter.py):**
   - Functionality: Recruiters can set interviews for developers, storing relevant details in Interviews.txt.
6. **Utility (Utility.py):**
   - Functionality: Handles database management, ensuring the existence of required text files.
7. **Execute (Execute.py):**
   - Functionality: Orchestrates the execution of various functions based on user inputs.

## **Database Folder (DB)**

1. **AvailableJobs.txt:**
   - Contains information about jobs from companies.
2. **AppliedJobsOfDevelopers.txt:**
   - Records developers' applications to jobs.
3. **RegisteredDevelopers.txt:**
   - Stores personal information of registered developers.
4. **RegisteredRecruiters.txt:**
   - Stores personal information of registered recruiters.
5. **RegisteredCompanies.txt:**
   - Holds personal information of registered companies.
6. **Admins.txt:**
   - Keeps records of admin personal information.
7. **Interviews.txt:**
   - Stores scheduled interviews.
8. **MessagesForDevelopers.txt:**
   - Captures messages for developers from recruiters.
9. **MessagesForRecruiters.txt:**
   - Documents messages for recruiters from developers.
10. **MessagesForCompanies.txt:**
    - Logs messages for companies from recruiters.

## **Execution Flow**

1. Display: Login or Registration.
2. If Registration is chosen:
   - Register as Developer or Company.
   - Input personal information.
   - Return to the main display.
3. If Login is chosen:
   - Authenticate based on user type.
4. Display After Logged In: Panels for Developer, Recruiter, Company, Admin.
5. Based on user selection, execute the corresponding functionality.
6. Repeat the process until the user chooses to exit.

## Conclusion

This design ensures a structured and modular approach to the Recruiting Management system, making it easy to expand and maintain. The separation of concerns into different files allows for better organization and scalability of the project, facilitating future enhancements and modifications.
