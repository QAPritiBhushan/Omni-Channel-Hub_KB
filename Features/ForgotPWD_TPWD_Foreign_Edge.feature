Feature: Forgot Password - Transaction Password for Foreign Customer

  Background: Common Steps
    Given I initiate the Microsoft Edge Browser
      And I launch the Khan Bank application in Retail Domain
    When I click on Forgot Password link
      And I select the transaction password to be reset
      And I click on the Click here link for Foreign Customer
    Then I should be displayed with the Forgot password page for Foreign Customer

  Scenario: Verifying if user is displayed with warning messages upon clicking on Continue button without providing username and passport number
      And I click on Continue button without entering username and passport number
    Then User should be displayed with a warning message for the username field for Foreign Customer
      And User should be displayed with a warning message for the passport number field for Foreign Customer
      And I close the browser


  Scenario: Verifying if user is displayed with OTP channel selection Page after entering the required data for recovering transaction password
    When I enter username and passport number for Foreign Customer
      And I click on Continue button
    Then I should be displayed with the OTP channel selection page
      And I close the browser


 Scenario: Verifying if user is displayed with the OTP Page with a timer of 15 minutes when OTP channel is selected as email for recovering transaction password
    When I enter username and passport number for Foreign Customer
      And I click on Continue button
    Then I should be displayed with the OTP channel selection page
    When I select email as OTP channel
      And I click on Continue button
    Then I should be displayed with the OTP Page with a timer of 15 minutes
      And I close the browser

 Scenario: Verifying if user is able to successfully reset the login password for a Foreign Customer
    When I enter username and passport number for Foreign Customer
      And I click on Continue button
    Then I should be displayed with the OTP channel selection page
    When I select email as OTP channel
      And I click on Continue button and enter OTP and continue
    Then I should be displayed with the Set Password Page
    When I set the new transaction password for a Foreign customer and proceed
    Then I should be displayed with a password reset success pop-up message
      And I close the browser


