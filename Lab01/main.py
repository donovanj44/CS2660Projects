# Imports
import csv
import sys

# Variables
username = ""
password = ""
accessLevel = 0

# Example generated usernameDict
# {
#     'jdonova9': ['password', '3'],
#     'user1': ['password', '2'],
#     'user2': ['password', '1']
# }
usernameDict = {}

# Dictionary structure: Option 1, Time Reporting, requires at least permission level 2, etc.
permissionsDict = {
    "1": ["Time Reporting", 2],
    "2": ["Accounting", 3],
    "3": ["IT Helpdesk", 2],
    "4": ["Engineering Documents", 3],
    "5": ["Other", 1],
}

# Main Function
if __name__ == "__main__":
    print("Welcome to Company X!")
    while True:
        fileName = input("Enter the relative path of your credentials file with extension: ")
        try:
            with open(fileName, mode='r') as file:
                csvFile = csv.reader(file)
                for lines in csvFile:
                    usernameDict[lines[0]] = [lines[1], lines[2]]
            break
        except FileNotFoundError:
            print("Could not find credentials file with specified name, try again.")

    # Sign in process, sets access level when given a valid username/password combo
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in usernameDict and password == usernameDict.get(username)[0]:
            print(f"Welcome {username}!")
            accessLevel = int(usernameDict.get(username)[1])
            break
        else:
            print("Username or password incorrect, try again")

    # Main menu dialogue loop, loops until user wishes to exit
    while True:
        print("1. Time Reporting\n"
              "2. Accounting\n"
              "3. IT Helpdesk\n"
              "4. Engineering Documents\n"
              "5. Other")
        choice = input("Choose your option: ")
        sectionName = permissionsDict.get(choice)[0]
        if permissionsDict.get(choice)[1] <= accessLevel:
            print(f"You have accessed the {sectionName} menu.")
        else:
            print(f"You do not have access to the {sectionName} menu.")
        while True:
            again = input("Return to main menu? (y/n): ")
            if again == "y":
                break
            elif again == "n":
                sys.exit(1)
