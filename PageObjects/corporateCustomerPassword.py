from selenium.webdriver.common.keys import Keys


class CorporateCustomerPassword:
    text_username_id = "customerAuthForm_loginUserId"
    text_registratioNumber_id = "customerAuthForm_registrationNumber"
    button_continue_xpath = "//button[@type='submit']"

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_id(self.text_username_id).send_keys(username)

    def setRegistrationNumber(self, regNum):
        self.driver.find_element_by_id(self.text_registratioNumber_id).send_keys(regNum)

    def clickOnContinue(self):
        self.driver.find_element_by_xpath(self.button_continue_xpath).click()

    def clearUsername(self):
        self.driver.find_element_by_xpath(self.text_username_id).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.text_username_id).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(self.text_username_id).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.text_username_id).send_keys(Keys.DELETE)

    def clearRegistrationNumber(self):
        self.driver.find_element_by_xpath(self.text_registratioNumber_id).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.text_registratioNumber_id).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(self.text_registratioNumber_id).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.text_registratioNumber_id).send_keys(Keys.DELETE)