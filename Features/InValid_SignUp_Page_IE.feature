Feature:Invalid_SignUp_Page_IE


  Scenario:To Check Invalifield validation Signup Khan Bank Retail Envirnoment In Mongolian Language in IE
    Given I initiate the IE Browser
      And I launch the Khan Bank Retail application in IE
     When I Click on Language Link in IE
      And I Click on SignUp link in IE
      And I Select dropdown Values for IE
      And I Enter Input fields For signUp In IE
     Then I close the browser


  Scenario: To Check Invalifield validation Signup Khan Bank Retail Envirnoment In English Language in IE
    Given I initiate the IE Browser
      And I launch the Khan Bank Retail application in IE
     When I Click on SignUp link in IE
      And I Select dropdown Values for IE
      And I Enter Input fields For signUp In IE
     Then I close the browser



