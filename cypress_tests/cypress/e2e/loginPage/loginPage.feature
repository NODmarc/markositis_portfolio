Feature: Login Page Test 

    User can input username and password in form and pass access to Secure page.

    Background: Open Login Page
        Given user open Test Login Page
    
    Scenario: Successful User Login with valid credentials
        When user input username and password in login form and submit form  
        Then user sees success message and secure area page link

    Scenario: User Logout after successful login
        When user input username and password in login form and submit form
        And user press Logout
        Then sees Login page form

    Scenario: Unsuccessful User Login with invalid credentials
        When user input invalid "username" and "password" and submit form
            | username | password |
            |          |          |
            | qa_test  | 12345    |
            | practice |          |
        Then user error message



