Feature: Online shopping
  As a registered user
  I want to make a successful purchase
  So that I can receive the desired product


  Scenario: Navigate to shopping coffee page
    Given I am on the home page
    When I click the coffee icon in menu bar
    Then I can see the shopping Coffee page


  Scenario: User adds a product to the shopping cart
    Given I am logged in
    And I am on the shopping Coffee page
    When I add 10 Napoli capsules
    Then the product is in shopping cart
