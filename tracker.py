import json
import os

def load_applications():
    filename = "applications.json"
    if not os.path.exists(filename):
        return []
    with open("applications.json", "r") as file:
        try: 
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            print("Invalid JSON file: Starting fresh\n")
            return []
valid_statuses = {"rejected", "interview", "applied", "offer"}

def get_valid_status():
    while True:
        validated_status = input("Enter the status:")
        if validated_status not in valid_statuses:
            print("Invalid Status.")
            continue
        return validated_status

def get_interviews(applications):
    interview_list = []

    for application in applications:
        if (application["status"] == "interview"):
            interview_list.append(application["company"])
    return interview_list

def print_applications(applications):
    for application in applications:
        print(application)
    
def add_application(applications):
    company = input("Enter the company name:")
    role = input("Enter the role:")
    status = get_valid_status()
    new_company = {'company': company, 'role': role, 'status': status}
    applications.append(new_company)
    save_applications(applications)

def save_applications(applications):
    with open("applications.json", "w") as file:
        json.dump(applications, file, indent = 4)

def find_applications(applications,company):
    company_list = []
    for application in applications:
        if application["company"] == company:
            company_list.append(application)
    return company_list



def main():
    applications = load_applications()
    while True:
        print("Job Application Tracker\n")
        print("1. Add application")
        print("2. View applications")
        print("3. View interviews")
        print("4. Filter applications by company")
        print("5. Quit\n")
        choice = input("Choose an option:\n")

        if(choice == "1"):
            add_application(applications)
        elif(choice == "2"):
            print_applications(applications)
        elif(choice == "3"):
            print(get_interviews(applications))
        elif(choice == "4"):
            company = input("Please input a company name:")
            results = find_applications(applications, company)
            if not results:
                print("Company not found in tracker\n")
            else:
                print(results\n)
        elif(choice == "5"):
            print("Goodbye")
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()