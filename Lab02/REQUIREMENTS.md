# Lab Assignment 2.0
Lab Assignment 2.0 requires you to download the source code to an authentication system your company is working on. Setup and run the program and experiment with the functionality, and read through to ensure you understand the code. Your position at the company is a "test engineer", and your assignment for this lab is to write a test script to automate the testing of several key features that are relevant to the overall system security.

# Process
1. Download the files found on GitLab: https://gitlab.uvm.edu/James.Eddy/cs-2660-software-testing requires your UVM NetID to login).

2. Clone or click the download button to download the project source code.download location gitlab

3. Follow the steps in the README.md file to set up and run the project (execute the authentication.py script with the database.json file in the same directory).

4. Create a new file called test_authentication.py that contains ten (10) test cases using the unittest library for the following functions in the authentication.py script:

   * Write a test case for the "database" function that accepts the credentials of a registered user (see .json file) and verifies that the "database" function returns True for that user
   * Write a test case for the "database" function that accepts the credentials of a user NOT registered (see .json file) and verifies that the "database" function returns False for that user
   * Write a test case for the "database" function that accepts the credentials of a registered user with an incorrect password (see .json file) and verifies that the "database" function returns False for that case
   * Write a test case for the "password_strength" function that tests the minimum password length requirement
   * Write a test case for the "password_strength" function that tests the maximum password length requirement
   * Write a test case for the "password_strength" function that tests that the supplied password does NOT contain only letters
   * Write a test case for the "password_strength" function that tests that the supplied password does NOT contain only digits
   * Write a test case for the "password_strength" function that tests that the supplied password contains at least one uppercase letter
   * Write a test case for the "password_strength" function that tests that the supplied password contains at least one lowercase letter
   * Write a test case for the "password_strength" function that verifies that the function returns True if a password that satisfies all the basic criteria in the password strength policy (and implemented in the password_strength function) is supplied (i.e. a "good" password). This should confirm the "special character" requirement as well.
# Submit
Please submit all the following to Brightspace:

1. Your test script (test_authentication.py) that contains all ten (10) of your test cases
2. A detailed README.txt file that outlines the steps required to run your test script, as well as an explanation for each of the test cases
3. A screenshot of the results of running your test script