Feature: Forgot Password Page Validation for Mongolian Customer

  Background: Common Steps
    Given I initiate the Mozilla Firefox Browser
      And I launch the Khan Bank application in Retail Domain
    When I click on Forgot Password link

  Scenario: Verifying if Forgot Password Page for Mongolian Customer is displayed when user selects login password
      And I select the login password to be reset
    Then I should be displayed with the Forgot password page for Mongolian Customer
      And I close the browser

  Scenario: Verifying if Forgot Password Page for Mongolian Customer is displayed when user selects transaction password
      And I select the transaction password to be reset
    Then I should be displayed with the Forgot password page for Mongolian Customer
      And I close the browser

  Scenario: Validation of warning message when no password type is selected
      And I click on Continue button without selecting a password
    Then Warning message should be displayed
      And I close the browser






