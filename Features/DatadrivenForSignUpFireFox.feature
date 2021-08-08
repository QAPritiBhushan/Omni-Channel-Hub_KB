Feature:Datadriven SignUp_Page_Firefox

  Scenario:To CheckMultiple Data For Signup Page Khan Bank Retail Environment In Mongolian Language in firefox
    Given I initiate the Mozilla Firefox Browser
      And I launch the Khan Bank Retail application in Firefox
     When I Click on SignUp link in Firefox
      And I Enter all Values in signup page Using DD
     Then I close the browser
