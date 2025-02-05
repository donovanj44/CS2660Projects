# Running the application

With the `database.json` file in the same directory as `authentication.py` and `test_authentication.py`, run `test_authentication.py` from your IDE, or from the command line (whichever of the following runs the script in Python 3.8+ in your operating system):

    python test_authentication.py

or
    
    python3 test_authentication.py
    
Read through the code and experiment with the various options presented in the menu, such as creating a new user and logging in as an existing user. Once you are comfortable with how the program works, begin writing your test cases as described in the lab instructions.


# Explanation of Test Cases
## Database Function Tests

test_database_valid_user: Checks if the function correctly authenticates a registered user with valid credentials.

test_database_invalid_user: Verifies that an unregistered user is not authenticated.

test_database_wrong_password: Ensures that a registered user with an incorrect password is not authenticated.

## Password Strength Function Tests

test_password_strength_min_length: Ensures that passwords shorter than the minimum required length fail the strength test.

test_password_strength_max_length: Ensures that passwords exceeding the maximum allowed length fail the strength test.

test_password_strength_no_special_char: Verifies that a password without a special character fails the strength test.

test_password_strength_no_digit: Ensures that a password lacking a numeric digit fails the strength test.

test_password_strength_no_uppercase: Ensures that a password without an uppercase letter fails the strength test.

test_password_strength_no_lowercase: Ensures that a password without a lowercase letter fails the strength test.

test_password_strength_valid: Confirms that a password meeting all the necessary complexity requirements passes the strength test.

