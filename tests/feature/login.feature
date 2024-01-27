Feature: Access management
  As a user of the website
  I want to have an access control
  so that I can be indentify in purchase process

  Scenario: Successful Login
    Given I am on the home page
    And I click on the login button in the top bar
    And I enter valid credentials
    When I click on the login button in the login form
    Then I am signed in
    And my name appears in the top bar

