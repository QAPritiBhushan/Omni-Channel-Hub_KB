class OTPConfirmation:
    text_enterOTP_id = "otp"
    button_continue_xpath = "//button[@type='submit']"
    button_sendAgain_xpath = "//span[text()='SEND AGAIN']"



    def __init__(self,driver):
        self.driver = driver

    def setOTP(self,OTP):
        self.driver.find_element_by_id(self.text_enterOTP_id).send_keys(OTP)

    def clickOnContinue(self):
        self.driver.find_element_by_xpath(self.button_continue_xpath).click()

    def clickOnSendAgain(self):
        self.driver.find_element_by_xpath(self.button_sendAgain_xpath).click()

