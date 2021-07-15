Feature: Forgot Password - Login Password for Mongolian Customer

  Background: Common Steps
    Given I launch the Khan Bank application
    When I click on Forgot Password link
    And I select the login password to be reset
    And I click on the Click here link for Foreign Customer
    Then I should be displayed with the Forgot password page for Foreign Customer
    When I enter username and passport number
    And I click on Continue button


  Scenario: Verifying if user is displayed with OTP channel selection Page after entering the required data for recovering login password
    Then I should be displayed with the OTP channel selection page
    And I close the browser


 Scenario: Verifying if user is displayed with the OTP Page with a timer of 15 minutes when OTP channel is selected as email for recovering login password
    Then I should be displayed with the OTP channel selection page
    When I select email as OTP channel
    And I click on Continue button
    Then I should be displayed with the OTP Page with a timer of 15 minutes
    And I close the browser




