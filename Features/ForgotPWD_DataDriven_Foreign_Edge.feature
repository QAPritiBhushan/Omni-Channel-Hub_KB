Feature: Forgot Password - Valid and Invalid data for Foreign Customer
  Background: Common Steps
    Given I initiate the Microsoft Edge Browser
      And I launch the Khan Bank application in Retail Domain
    When I click on Forgot Password link


  Scenario: Verifying if user is able to proceed to the OTP Channel Selection page using valid set of login password data
      And I select the login password to be reset
      And I click on the Click here link for Foreign Customer
    Then I should be displayed with the Forgot password page for Foreign Customer
    Then I enter valid username and passport - SPWD for Foreign Customer
      And I close the browser



  Scenario: Verifying if user is able to proceed to the OTP Channel Selection page using valid set of transaction password data
      And I select the transaction password to be reset
      And I click on the Click here link for Foreign Customer
    Then I should be displayed with the Forgot password page for Foreign Customer
    Then I enter valid username and passport - TPWD for Foreign Customer
      And I close the browser



  Scenario: Verifying if user is displayed with error pop-up using invalid set of login password data
      And I select the login password to be reset
      And I click on the Click here link for Foreign Customer
    Then I should be displayed with the Forgot password page for Foreign Customer
    Then I enter invalid username and passport - SPWD for Foreign Customer
      And I close the browser

  Scenario: Verifying if user is displayed with error pop-up using invalid set of transaction password data
      And I select the transaction password to be reset
      And I click on the Click here link for Foreign Customer
    Then I should be displayed with the Forgot password page for Foreign Customer
    Then I enter invalid username and passport - TPWD for Foreign Customer
      And I close the browser














