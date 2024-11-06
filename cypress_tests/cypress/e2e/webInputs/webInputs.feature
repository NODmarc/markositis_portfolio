Feature: Submit form

    User open the form, input own data.
    User see own data and clear this.

    Scenario: User can fill in and clear Submit form
        Given user open Submit form page
        And user fill in Number, Text, Password, Date fields
        When user press button Display Inputs
        Then user sees own data
        When user press button Clear Inputs
        Then user sees blank fields