Feature: Login functionality


  Scenario: Verifying if user is displayed with warning messages in Mongolian when disallowed characters in username are provided
    Given I initiate the Mozilla Firefox Browser
      And  I launch the Khan Bank application in Retail Domain
      And I enter invalid set of username data to validate the warning message in Mongolian
      And I close the browser



  Scenario: Verifying if user is displayed with warning messages in English when disallowed characters in username are provided
    Given I initiate the Mozilla Firefox Browser
      And  I launch the Khan Bank application in Retail Domain
      And I change to English Language
      And I enter invalid set of username data to validate the warning message in English
      And I close the browser


  Scenario: Verifying if user is able to login to the application with a valid set of credentials
    Given I initiate the Mozilla Firefox Browser
      And  I launch the Khan Bank application in Retail Domain
      And I enter valid set of credentials to validate login functionality
      And I close the browser


  Scenario: Verifying the warning messages in Mongolian when username and password fields are left blank
    Given I initiate the Mozilla Firefox Browser
      And  I launch the Khan Bank application in Retail Domain
    When  I enter valid credentials
      And I clear the username
    Then I should be displayed with a warning message to enter username in Mongolian
    When I clear the password
    Then I should be displayed with a warning message to enter password in Mongolian
      And I close the browser

  Scenario: Verifying the warning messages in English when username and password fields are left blank
    Given I initiate the Mozilla Firefox Browser
      And  I launch the Khan Bank application in Retail Domain
      And I change to English Language
    When  I enter valid credentials
      And I clear the username
    Then I should be displayed with a warning message to enter username in English
    When I clear the password
    Then I should be displayed with a warning message to enter password in English
      And I close the browser


  Scenario: Verify is the loginID is not retained in the username field when user doesn't check the 'Remember Me' checkbox in Mongolian
    Given I initiate the Mozilla Firefox Browser
      And  I launch the Khan Bank application in Retail Domain
    When I enter valid credentials
      And I click on login button
    Then I should be displayed with the home page
    When I log out
    Then username field should not display the loginID entered for Mongolian Language
      And I close the browser


  Scenario: Verify is the loginID is retained in the username field when user checks the 'Remember Me' checkbox in Mongolian
    Given I initiate the Mozilla Firefox Browser
      And  I launch the Khan Bank application in Retail Domain
    When I enter valid credentials
      And I check the Remember Me checkbox and login
    Then I should be displayed with the home page
    When I log out
    Then username field should display the loginID entered for Mongolian Language
      And I close the browser



  Scenario: Verify is the loginID is not retained in the username field when user doesn't check the 'Remember Me' checkbox in English
    Given I initiate the Mozilla Firefox Browser
      And  I launch the Khan Bank application in Retail Domain
      And I change to English Language
    When I enter valid credentials
      And I click on login button
    Then I should be displayed with the home page
    When I log out
    Then username field should not display the loginID entered for English Language
      And I close the browser

  Scenario: Verify is the loginID is retained in the username field when user checks the 'Remember Me' checkbox in English
    Given I initiate the Mozilla Firefox Browser
      And  I launch the Khan Bank application in Retail Domain
      And I change to English Language
    When I enter valid credentials
      And I check the Remember Me checkbox and login
    Then I should be displayed with the home page
    When I log out
    Then username field should display the loginID entered for English Language
      And I close the browser





