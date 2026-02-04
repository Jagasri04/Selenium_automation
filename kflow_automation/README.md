Selenium Automation – KFlow Authentication Tests

This repository contains Selenium UI automation tests written in Python for the KFlow authentication module. The goal of this project is to automatically verify that critical user authentication flows work correctly after frontend or backend changes.


## What This Project Tests

 1. Forgot Password UI Test
File: `test_forgot_password.py`

This test:
- Opens the Login page
- Clicks the "Forgot Password" link
- Enters the user email address
- Submits the forgot password form
- Verifies that a success message is shown
Purpose:
To ensure the forgot password screen works and users can request a reset email without UI issues.

2. Reset Password UI Test
File: `test_reset_password.py`

This test:
- Opens the reset password page using a token
- Enters a new password and confirmation password
- Clicks the Reset button
- Verifies redirection to the Login page

Purpose:
To ensure the reset password screen accepts valid input and completes the flow correctly.

## Setup Instructions

### Step 1: Clone the Repository

git clone https://github.com/Jagasri04/selenium_automation.git  
cd selenium_automation

---

### Step 2: Create Virtual Environment

python -m venv venv

Activate it:

Windows:  
venv\Scripts\activate

Mac / Linux:  
source venv/bin/activate


### Step 3: Install Required Packages

pip install selenium pytest webdriver-manager


## How to Run the Tests

Run all tests:
pytest kflow_automation -v

Run individual tests:

pytest kflow_automation/test_forgot_password.py  
pytest kflow_automation/test_reset_password.py

