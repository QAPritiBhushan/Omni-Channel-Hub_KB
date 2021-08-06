Feature: Forgot Password - Transaction Password for Mongolian Customer

  Background: Common Steps
    Given I initiate the Google Chrome Browser
      And I launch the Khan Bank application in Retail Domain
    When I click on Forgot Password link
      And I select the transaction password to be reset
    Then I should be displayed with the Forgot password page for Mongolian Customer


 Scenario: Verifying if user is displayed with warning messages upon clicking on Continue button without providing username and registration number
     And I click on Continue button without entering username and registration number
   Then User should be displayed with a warning message for the username field for Mongolian Customer
     And User should be displayed with a warning message for the registration number field for Mongolian Customer
     And I close the browser



  Scenario: Verifying if user is displayed with OTP channel selection Page after entering the required data for recovering transaction password
    When I enter username and registration number for Mongolian Customer
      And I click on Continue button
    Then I should be displayed with the OTP channel selection page
      And I close the browser

 Scenario: Verifying if user is displayed with the OTP Page with a timer of 15 minutes when OTP channel is selected as email for recovering transaction password
    When I enter username and registration number for Mongolian Customer
      And I click on Continue button
    Then I should be displayed with the OTP channel selection page
    When I select email as OTP channel
      And I click on Continue button
    Then I should be displayed with the OTP Page with a timer of 15 minutes
      And I close the browser


