Feature: KhanBank application Login
  Scenario: Verify Login page functionalities
    Given  I launch the Khan Bank application
    When I enter the valid credentials
    And I click on login button
    Then I should be displayed with the Homepage
    And I click on Logout