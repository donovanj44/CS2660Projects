# Testing
1. Extract the zip file containing `main.py` and the sample `access.csv` file to a folder named `Lab01`
2. In your `Lab01` folder, open a command prompt
3. Run the command ```python main.py```
4. Enter the name of your credentials file
    * `access.csv` is a usable file, however the program accepts all files in the same format
5. The program sample comes with 3 users, all of different access levels

| Username | Password | Access Level |
|----------|----------|--------------|
| jdonova9 | password | 3 (Highest)  |
| user1    | password | 2 (Medium)   |
| user2    | password | 1 (Lowest)   |
   
6. Each menu option has an access level, and a user must either have that access level or higher in order to use.

| Option                | Access Level |
|-----------------------|--------------|
| Time Reporting        | 2            |
| Accounting            | 3            |
| IT Helpdesk           | 2            |
| Engineering Documents | 3            |
| Other                 | 1            |

7. If a user tries to access an option they are not authorized to, they are prompted to return to the main menu