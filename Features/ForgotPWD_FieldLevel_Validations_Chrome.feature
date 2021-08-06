Feature: Field Level Validations for all customer types


  Scenario: Verifying warning message for disallowed characters in username field for SPWD for Mongolian Customer
    Given I initiate the Google Chrome Browser
      And I launch the Khan Bank application in Retail Domain
    When I click on Forgot Password link
      And I select the login password to be reset
    Then I should be displayed with the Forgot password page for Mongolian Customer
    When I enter disallowed characters in the username field for Mongolian Customer
    Then I should be displayed with a warning message for username for SPWD for the Mongolian Customer
      And I close the browser


  Scenario: Verifying warning message for disallowed characters in username field for TPWD for Mongolian Customer
    Given I initiate the Google Chrome Browser
      And I launch the Khan Bank application in Retail Domain
    When I click on Forgot Password link
      And I select the transaction password to be reset
    Then I should be displayed with the Forgot password page for Mongolian Customer
    When I enter disallowed characters in the username field for Mongolian Customer
    Then I should be displayed with a warning message for username for TPWD the Mongolian Customer
      And I close the browser


  Scenario: Verifying warning message for disallowed characters in username field for SPWD for Foreign Customer
    Given I initiate the Google Chrome Browser
      And I launch the Khan Bank application in Retail Domain
    When I click on Forgot Password link
      And I select the login password to be reset
      And I click on the Click here link for Foreign Customer
    Then I should be displayed with the Forgot password page for Foreign Customer
    When I enter disallowed characters in the username field for Foreign Customer
    Then I should be displayed with a warning message for username for SPWD for the Foreign Customer
      And I close the browser


  Scenario: Verifying warning message for disallowed characters in username field for TPWD for Foreign Customer
    Given I initiate the Google Chrome Browser
      And I launch the Khan Bank application in Retail Domain
    When I click on Forgot Password link
      And I select the transaction password to be reset
      And I click on the Click here link for Foreign Customer
    Then I should be displayed with the Forgot password page for Foreign Customer
    When I enter disallowed characters in the username field for Foreign Customer
    Then I should be displayed with a warning message for username for TPWD the Foreign Customer
      And I close the browser


  Scenario: Verifying warning message for disallowed characters in username field for SPWD for Corporate Customer
    Given I initiate the Google Chrome Browser
      And I launch the Khan Bank application in Corporate domain
    When I click on Forgot Password link
      And I select the login password to be reset
      And I click on the Click here link for Corporate Customer
    Then I should be displayed with the Forgot password page for Corporate Customer
    When I enter disallowed characters in the username field for Corporate Customer
    Then I should be displayed with a warning message for username for SPWD for the Corporate Customer
      And I close the browser


  Scenario: Verifying warning message for disallowed characters in username field for TPWD for Corporate Customer
    Given I initiate the Google Chrome Browser
      And I launch the Khan Bank application in Corporate domain
    When I click on Forgot Password link
      And I select the transaction password to be reset
      And I click on the Click here link for Corporate Customer
    Then I should be displayed with the Forgot password page for Corporate Customer
    When I enter disallowed characters in the username field for Corporate Customer
    Then I should be displayed with a warning message for username for TPWD the Corporate Customer
      And I close the browser





