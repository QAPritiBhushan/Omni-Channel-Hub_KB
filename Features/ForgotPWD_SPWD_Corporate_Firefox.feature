Feature: Forgot Password - Login Password for Corporate Customer

  Background: Common Steps
    Given I initiate the Mozilla Firefox Browser
      And I launch the Khan Bank application in Corporate domain
    When I click on Forgot Password link
      And I select the login password to be reset
      And I click on the Click here link for Corporate Customer
    Then I should be displayed with the Forgot password page for Corporate Customer



  Scenario: Verifying if user is displayed with warning messages upon clicking on Continue button without providing username and registration number
      And I click on Continue button without entering username and registration number
    Then User should be displayed with a warning message for the username field for Corporate Customer
      And User should be displayed with a warning message for the registration number field for Corporate Customer
      And I close the browser


  Scenario: Verifying if user is displayed with OTP channel selection Page after entering the required data for recovering login password
    When I enter username and registration number for the Corporate Customer
      And I click on Continue button
    Then I should be displayed with the OTP channel selection page
      And I close the browser


  Scenario: Verifying if user is displayed with the OTP Page with a timer of 15 minutes when OTP channel is selected as email for recovering login password
    When I enter username and registration number for the Corporate Customer
      And I click on Continue button
    Then I should be displayed with the OTP channel selection page
    When I select email as OTP channel
      And I click on Continue button
    Then I should be displayed with the OTP Page with a timer of 15 minutes
      And I close the browser

  Scenario: Verifying if user is able to successfully reset the login password for a Corporate Customer
    When I enter username and registration number for the Corporate Customer
      And I click on Continue button
    Then I should be displayed with the OTP channel selection page
    When I select email as OTP channel
      And I click on Continue button and enter OTP and continue
    Then I should be displayed with the Set Password page
    When I set the new login password for a Corporate customer and proceed
    Then I should be displayed with a password reset success pop-up message
      And I close the browser
