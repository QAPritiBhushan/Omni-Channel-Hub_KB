Feature: Reset Transaction Password for Mongolian Customer

  Scenario: Verifying if user is able to successfully reset the login password for a Mongolian Customer
    Given I initiate the Google Chrome Browser
      And I launch the Khan Bank application in Retail Domain
    When I click on Forgot Password link
      And I select the transaction password to be reset
    Then I should be displayed with the Forgot password page for Mongolian Customer
    When I enter username and registration number for Mongolian Customer
      And I click on Continue button
    Then I should be displayed with the OTP channel selection page
    When I select email as OTP channel
      And I click on Continue button and enter OTP and continue
    Then I should be displayed with the Set Password Page
    When I set the new transaction password for a Mongolian customer and proceed
    Then I should be displayed with a password reset success pop-up message
      And I close the browser