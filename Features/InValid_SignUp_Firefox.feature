Feature:InValid SignUp_Page_Firefox

Scenario: To Check FieldLevelValidation InValid Data For Signup Khan Bank Retail Envirnoment In Mongolian Language in Firefox
    Given I initiate the Mozilla Firefox Browser
      And I launch the Khan Bank Retail application in Firefox
     When I Click on SignUp link in Firefox
      And I select dropdown Values for Firefox
      And I Enter Input fields For signup PageDD
     Then I close the browser

 Scenario: To Check FieldLevelValidation InValid Data For Signup Khan Bank Retail Envirnoment In English Language in Firefox
    Given I initiate the Mozilla Firefox Browser
      And I launch the Khan Bank Retail application in Firefox
     When I Click on Language Link
      And I Click on SignUp link in Firefox
      And I select dropdown Values for Firefox
      And I Enter Input fields For signup PageDD In English Language
     Then I close the browser

 Scenario: To Check FieldLevelValidation InValid Data For Signup Khan Bank Corporate Envirnoment In Mongolian Language in Firefox
    Given I initiate the Mozilla Firefox Browser
      And I launch the Khan Bank Corporate application in Firefox
     When I Click on SignUp link in Firefox
      And I select dropdown Values for Firefox
      And I Enter Input fields For signup PageDD For corporate
     Then I close the browser

Scenario: To Check FieldLevelValidation InValid Data For Signup Khan Bank Retail Envirnoment In Mongolian Language in Firefox
    Given I initiate the Mozilla Firefox Browser
      And I launch the Khan Bank Retail application in Firefox
     When I Click on Language Link
      And I Click on SignUp link in Firefox
      And I select dropdown Values for Firefox
      And I Enter Input Fields For Signup PageDD For Blank EmailID
     Then I close the browser


