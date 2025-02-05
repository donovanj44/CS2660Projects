# Introduction
Write a Python program: Create a login and menu to a company intranet system that requires users (employees) to enter a username and password in order to view a menu of options (such as Time Reporting, Accounting, IT Helpdesk, Engineering Documents, etc.). 

# Technical requirements
1. Plaintext usernames/passwords/access level stored in a csv (or text) file
2. Create three different access levels (roles for different users). For example, User A should have access to all menu items ('admin' access), while User B has limited access (no Accounting or Engineering Documents), etc. 
3. Once logged in the user should be able to select different menu options with a number input (for example, "press 1 for the Time Reporting area", "press 2 for the Accounting area", etc.).
4. When a user enters a menu area they have access to, a simple message similar to 'You have now accessed the accounting application' is sufficient to indicate a successful demonstration of the access control (no need to build out any actual accounting functionality). Likewise, if a user does not have the appropriate access level to view a menu area, the program should display a 'You are not authorized to access this area.' message and provide an option to return them to the main menu.
5. Good programming practices: Must adhere to Python PEP8 style guide (refer to the attached style guide reference PDF). Reasonable amount of error/exception handling. Modular design - must organize code into functions (no duplicate code!). Well-documented. Written in Python 3.9+ (standard library). No GUI, this should be a command menu-driven program.

# Submission
Please submit a compressed folder containing all files associated with your assignment, as well as instructions for testing your program. Note: you will be adding functionality to this system in a subsequent assignment, so take your time and plan out your design.

1. All project files (.py, .csv or .txt, etc.)
2. Detailed README.md (or .txt) file including a description of your program and testing instructions