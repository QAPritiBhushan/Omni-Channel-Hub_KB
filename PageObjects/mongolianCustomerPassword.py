import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class MongolianCustomerPassword:
    link_foreignCustomer_xpath = "/html[1]/body[1]/div[1]/div[1]/section[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]"
    link_corporateCustomer_xpath = "/html[1]/body[1]/div[1]/div[1]/section[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/a[1]"
    link_mongolianCustomer_xpath = "//div[@class='ant-form-item-control-input-content']//div[1]//div[2]//a[1]"
    title_forgotPassword_xpath = "//span[@title='Forgot Password']"
    text_username_id = "customerAuthForm_loginUserId"
    dropdown_reg1_xpath = "//input[@type='search'])[1]"
    dropdown_reg2_xpath = "//input[@type='search'])[2]"
    text_regNumber_xpath = "//input[@class='ant-input'][2]"
    button_continue_xpath = "//button[@type='submit']"
    option_reg1_xpath = "//div[@class='ant-select-item-option-content'][text()='A']"

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element_by_id(self.text_username_id).send_keys(username)

    def clickOnRegDrpDwn1(self):
        self.driver.find_element_by_xpath(self.dropdown_reg1_xpath).click()

    def setRegDrpDwn1(self):
        self.driver.find_element_by_xpath(self.option_reg1_xpath).click()

    def clearAndSetUsername(self,username):
        self.driver.find_element_by_xpath(self.text_username_id).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.text_username_id).send_keys(Keys.DELETE)
        self.driver.find_element_by_id(self.text_regNumber_xpath).send_keys(username)

    def clearAndSetRegNum(self,reg_num):
        self.driver.find_element_by_xpath(self.text_regNumber_xpath).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.text_regNumber_xpath).send_keys(Keys.DELETE)
        self.driver.find_element_by_id(self.text_regNumber_xpath).send_keys(reg_num)





    def selectRegValues(self, DropD1, DropD2):
        action2 = ActionChains(self.driver)
        element2 = self.driver.find_element_by_xpath("(//div[@class='ant-select-selector'])[1]")
        action2.move_to_element(element2).click().perform()
        D_1 = str(DropD1)
        D_2 = str(DropD2)
        action2.send_keys(Keys.DOWN + Keys.ENTER).perform()
        i = 1
        while i <= 36:
            action2.send_keys(Keys.DOWN + Keys.ENTER).perform()
            # easygui.msgbox("down?")
            data = self.driver.find_element_by_xpath("//span[@class='ant-select-selection-item']")
            if data.text == D_1:
                break
            i += 1
            # *********************************Second dropdown
        action3 = ActionChains(self.driver)
        element3 = self.driver.find_element_by_xpath("(//div[@class='ant-select-selector'])[2]")
        action3.move_to_element(element3).click().perform()
        action3.send_keys(Keys.DOWN + Keys.ENTER).perform()
        # action2.send_keys(Keys.TAB + Keys.DOWN).perform()

        i = 1
        while i <= 36:
            action3.send_keys(Keys.DOWN + Keys.ENTER).perform()
            data3 = self.driver.find_element_by_xpath(
                "//input[@aria-owns='rc_select_1_list']//parent::span//following::span[@class='ant-select-selection-item']")
            if data3.text == D_2:
                break
            i += 1




    def clickOnRegDrpDwn2(self):
        self.driver.find_element_by_xpath(self.dropdown_reg2_xpath).click()

    def setRegDrpDwn2(self):
        self.driver.find_element_by_xpath(self.dropdown_reg2_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.dropdown_reg2_xpath).send_keys(Keys.DOWN + Keys.DOWN + Keys.ENTER)

    def setRegNum(self,regNum):
        self.driver.find_element_by_xpath(self.text_regNumber_xpath).send_keys(regNum)

    def clickOnContinue(self):
        self.driver.find_element_by_xpath(self.button_continue_xpath).click()

    def clickOnForeignCustomer(self):
        self.driver.find_element_by_xpath(self.link_foreignCustomer_xpath).click()

    def clickOnCorporateCustomer(self):
        self.driver.find_element_by_xpath(self.link_corporateCustomer_xpath).click()


    def clickOnMongolianCustomer(self):
        self.driver.find_element_by_xpath(self.link_mongolianCustomer_xpath).click()

    def clearUsername(self):
        self.driver.find_element_by_id(self.text_username_id).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_id(self.text_username_id).send_keys(Keys.DELETE)
        self.driver.find_element_by_id(self.text_username_id).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_id(self.text_username_id).send_keys(Keys.DELETE)

    def clearRegistrationNumber(self):
        self.driver.find_element_by_xpath(self.text_regNumber_xpath).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.text_regNumber_xpath).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(self.text_regNumber_xpath).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.text_regNumber_xpath).send_keys(Keys.DELETE)