Feature: Forgot Password - Transaction Password for Mongolian Customer

  Background: Common Steps
    Given I launch the Khan Bank application
    When I click on Forgot Password link
    And I select the transaction password to be reset
    Then I should be displayed with the Forgot password page for Mongolian Customer
    When I enter username and registration number
    And I click on Continue button

  Scenario: Verifying if user is displayed with OTP channel selection Page after entering the required data for recovering transaction password
    Then I should be displayed with the OTP channel selection page

 Scenario: Verifying if user is displayed with the OTP Page with a timer of 15 minutes when OTP channel is selected as email for recovering transaction password
    Then I should be displayed with the OTP channel selection page
    When I select email as OTP channel
    And I click on Continue button
    Then I should be displayed with the OTP Page with a timer of 15 minutes