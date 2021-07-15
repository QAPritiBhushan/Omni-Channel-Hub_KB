Feature: Forgot Password Page Validation for Mongolian Customer

  Background: Common Steps
    Given I launch the Khan Bank application in Corporate domain
    When I click on Forgot Password link

  Scenario: Verifying if Forgot Password Page for Mongolian Customer is displayed when user selects login password
    And I select the login password to be reset
    And I click on the Click here link for Foreign Customer
    Then I should be displayed with the Forgot password page for Foreign Customer
    And I close the browser

  Scenario: Verifying if Forgot Password Page for Mongolian Customer is displayed when user selects login password
    And I select the transaction password to be reset
    And I click on the Click here link for Foreign Customer
    Then I should be displayed with the Forgot password page for Foreign Customer
    And I close the browser
