Feature: Forgot Password Page Validation for Corporate Customer

  Background: Common Steps
    Given I initiate the Google Chrome Browser
      And I launch the Khan Bank application in Corporate domain
    When I click on Forgot Password link



  Scenario: Verifying if Forgot Password Page for Corporate Customer is displayed when user selects login password
      And I select the login password to be reset
      And I click on the Click here link for Corporate Customer
    Then I should be displayed with the Forgot password page for Corporate Customer
      And I close the browser


  Scenario: Verifying if Forgot Password Page for Corporate Customer is displayed when user selects transaction password
      And I select the transaction password to be reset
      And I click on the Click here link for Corporate Customer
    Then I should be displayed with the Forgot password page for Corporate Customer
      And I close the browser
