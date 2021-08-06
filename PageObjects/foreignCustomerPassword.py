import time

from selenium.webdriver.common.keys import Keys


class ForeignCustomerPassword:
    text_username_xpath = "//div[@class='ant-form-item-control-input-content']/input[@id='customerAuthForm_loginUserId']"
    text_passportNumber_xpath = "//div[@class='ant-col ant-col-22']/input[@class='ant-input']"
    button_continue_xpath = "//button[@type='submit']"

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element_by_xpath(self.text_username_xpath).send_keys(username)

    def setPassportNumber(self,passport):
        self.driver.find_element_by_xpath(self.text_passportNumber_xpath).send_keys(passport)

    def clickOnContinue(self):
        self.driver.find_element_by_xpath(self.button_continue_xpath).click()

    def clearUsername(self):
        self.driver.find_element_by_xpath(self.text_username_xpath).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.text_username_xpath).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(self.text_username_xpath).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.text_username_xpath).send_keys(Keys.DELETE)

    def clearPassportNumber(self):
        self.driver.find_element_by_xpath(self.text_passportNumber_xpath).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.text_passportNumber_xpath).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(self.text_passportNumber_xpath).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.text_passportNumber_xpath).send_keys(Keys.DELETE)



