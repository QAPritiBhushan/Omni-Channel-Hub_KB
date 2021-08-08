Feature:Valid SignUp_Page_IE

  Scenario: To Check Valid Data For Signup Khan Bank Retail Envirnoment In Mongolian Language in IE
    Given I initiate the IE Browser
      And I Launch the Khan Bank Retail application in IE
     When I Click on Language Link in IE
      And I Click on SignUp link in IE
      And I Select dropdown Values for IE
      And I Enter all Valid Values in signup page for Corporate
     Then I close the browser


  Scenario: To Check Valid Data For Signup Khan Bank Retail Envirnoment In English Language in IE
    Given I initiate the IE Browser
      And I Launch the Khan Bank Retail application in IE
     When I Click on SignUp link in IE
      And I Select dropdown Values for IE
      And I Enter all Valid Values in signup page for Corporate
     Then I close the browser
