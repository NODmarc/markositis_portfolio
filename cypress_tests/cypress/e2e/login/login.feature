Feature: Login Page Test

    User can input username and password in form and pass access.

    Background: Login to Page
        Given user open Login Portal

    Scenario: Successful / Unsuccessful User Login with valid credentials
        When user input <username> and <password> in login form and submit form
        Then user sees success "<expectedAlertText>"

        Examples:
            | username  | password     | expectedAlertText    |
            | webdriver | webdriver123 | validation succeeded |
            | webdriver | password123  | validation failed    |