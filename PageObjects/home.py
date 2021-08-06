from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Homepage:
    link_logOut_xpath = "//li[@class='lo']"
    #popup_yes_xpath="//button[normalize-space()='Yes']"
    popup_yes_xpath = "//button[@class='kb-button']"


    def __init__(self, driver):
        self.driver = driver

    def clickOnLogOut(self):
        self.driver.find_element_by_xpath(self.link_logOut_xpath).click()
        self.driver.find_element_by_xpath(self.popup_yes_xpath).click()

