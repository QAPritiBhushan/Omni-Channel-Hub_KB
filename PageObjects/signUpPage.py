import easygui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class Signup:

    text_username_id = "customerAuthForm_loginUserId"
    language_button_xpath = "//button[@class='ant-btn ant-btn-link button-language']"
    Firstdropdown_xpath = "//*[@class='ant-select-selection-search-input'][1]"
    dropdown_reg1_value_xpath = "//*[@title='Б'][1]"
    dropdown_xpath2 = "(//input[@type='search'])[2]"
    dropdown_reg2_value_xpath_of_Д = "//*[@title='Д']"
    dropdown_reg2_value_xpath_Д = "Keys.DOWN + Keys.DOWN +Keys.DOWN +Keys.DOWN +Keys.DOWN +Keys.DOWN + Keys.ENTER"
    reg_number_xpath = "//input[@class='ant-input'][2]"
    reg_number_value = "91101304"
    emailid_xpath = "//input[@id='email']"
    emailid_value = "infura7@gmail.com"
    phone_number_xpath = "//input[@id='phoneNumber']"
    phone_number_value = "88131370"
    continue_button_xpath="//button[@class='ant-btn ant-btn-primary ant-btn-lg ant-btn-block']"

    def __init__(self, driver):
        self.driver = driver

    def selectDropdown1(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath("(//div[@class='ant-select-selector'])[1]")
        action.move_to_element(element).click().perform()

        Char1 = "Ё"
        for i in range(35):
            action.send_keys(Keys.DOWN + Keys.ENTER).perform()

            data = self.driver.find_element_by_xpath("//span[@class='ant-select-selection-item']//ancestor::div[@class='ant-select-selector'][1]")
            #easygui.msgbox(data.text)
            if data.text == Char1:
                break
            #action.send_keys(Keys.DOWN).perform()

    def MyDropwon(self, goto=None):
        action2 = ActionChains(self.driver)
        element2 = self.driver.find_element_by_xpath("(//div[@class='ant-select-selector'])[1]")
        action2.move_to_element(element2).click().perform()

        #self.driver.find_element_by_xpath("//*[text()='A']").click()
        i=1
        while i <=36 :
            action2.send_keys(Keys.DOWN+Keys.ENTER).perform()
            #easygui.msgbox("down?")
            data = self.driver.find_element_by_xpath("//span[@class='ant-select-selection-item']")
            if data.text == "У":
                break
            i+=1
        #*********************************Second dropdown
        action3 = ActionChains(self.driver)
        element3 = self.driver.find_element_by_xpath("(//div[@class='ant-select-selector'])[2]")
        action3.move_to_element(element3).click().perform()
        action3.send_keys(Keys.DOWN + Keys.ENTER).perform()
        i=1
        while i <=36 :
            action3.send_keys(Keys.DOWN+Keys.ENTER).perform()
            data3 = self.driver.find_element_by_xpath("//input[@aria-owns='rc_select_1_list']//parent::span//following::span[@class='ant-select-selection-item']")

            if data3.text == "З":
                break
            i+=1

    def enterReg_number(self,Reg_number):
        self.driver.find_element_by_xpath(self.reg_number_xpath).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.reg_number_xpath).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(self.reg_number_xpath).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.reg_number_xpath).send_keys(Keys.DELETE)

        self.driver.find_element_by_xpath(self.reg_number_xpath).send_keys(Reg_number)

    def enterValidSignUpdata(self,Reg_number,Emailid,Phone_number):


        self.driver.find_element_by_xpath(self.reg_number_xpath).send_keys(Reg_number)
        self.driver.find_element_by_xpath(self.emailid_xpath).send_keys(Emailid)
        self.driver.find_element_by_xpath(self.phone_number_xpath).send_keys(Phone_number)

    def enterEmailid(self,Emailid):

        self.driver.find_element_by_xpath(self.emailid_xpath).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.emailid_xpath).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(self.emailid_xpath).send_keys(Emailid)

    def enterPhone_number(self,Phone_number):
        self.driver.find_element_by_xpath(self.phone_number_xpath).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.phone_number_xpath).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(self.phone_number_xpath).send_keys(Phone_number)

    def clickOn_ContinueButton(self):
        self.driver.find_element_by_xpath(self.continue_button_xpath).click()

    def ClickonLanguageLink(self):
        self.driver.find_element_by_xpath(self.language_button_xpath).click()

    def CheckAllCharatorsfromDropdown(self):
        action2 = ActionChains(self.driver)
        element2 = self.driver.find_element_by_xpath("(//div[@class='ant-select-selector'])[1]")
        action2.move_to_element(element2).click().perform()
        # self.driver.find_element_by_xpath("//*[text()='A']").click()
        i = 1
        while i <= 36:
            action2.send_keys(Keys.DOWN + Keys.ENTER).perform()
            # easygui.msgbox("down?")
            data = self.driver.find_element_by_xpath("//span[@class='ant-select-selection-item']")
            self.driver.find_element_by_xpath(self.reg_number_xpath).click()
            if data.text == "Я":
                break
            i += 1
        action3 = ActionChains(self.driver)
        element3 = self.driver.find_element_by_xpath("(//div[@class='ant-select-selector'])[2]")
        action3.move_to_element(element3).click().perform()
        i = 1
        while i <= 36:
            action3.send_keys(Keys.DOWN + Keys.ENTER).perform()
            data3 = self.driver.find_element_by_xpath(
                "//input[@aria-owns='rc_select_1_list']//parent::span//following::span[@class='ant-select-selection-item']")
            self.driver.find_element_by_xpath(self.reg_number_xpath).click()
            if data3.text == "Я":
                break
            i += 1

    def MyDropwonForIE(self, goto=None):
        action2 = ActionChains(self.driver)
        element2 = self.driver.find_element_by_xpath("(//div[@class='ant-select-selector'])[1]")
        action2.move_to_element(element2).click().perform()

        self.driver.find_element_by_xpath("//*[text()='A']").click()
        i=1
        while i <=36 :
            action2.send_keys(Keys.DOWN+Keys.ENTER).perform()
            #easygui.msgbox("down?")
            data = self.driver.find_element_by_xpath("//span[@class='ant-select-selection-item']")
            if data.text == "Т":
                break
            i+=1
        #*********************************Second dropdown
        action3 = ActionChains(self.driver)
        element3 = self.driver.find_element_by_xpath("(//div[@class='ant-select-selector'])[2]")
        action3.move_to_element(element3).click().perform()
        action2.send_keys(Keys.TAB+ Keys.DOWN).perform()
        i=1
        while i <=36 :
            action3.send_keys(Keys.DOWN+Keys.ENTER).perform()
            data3 = self.driver.find_element_by_xpath("//input[@aria-owns='rc_select_1_list']//parent::span//following::span[@class='ant-select-selection-item']")
            if data3.text == "З":
                break
            i+=1

    def MyDropwonDD(self,DropD1,Dropd2):
        action2 = ActionChains(self.driver)
        element2 = self.driver.find_element_by_xpath("(//div[@class='ant-select-selector'])[1]")
        action2.move_to_element(element2).click().perform()
        D_1=str(DropD1)
        D_2 = str(Dropd2)
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
        action3.send_keys(Keys.DOWN+Keys.ENTER).perform()
        #action2.send_keys(Keys.TAB + Keys.DOWN).perform()

        i = 1
        while i <= 36:
            action3.send_keys(Keys.DOWN + Keys.ENTER).perform()
            data3 = self.driver.find_element_by_xpath(
              "//input[@aria-owns='rc_select_1_list']//parent::span//following::span[@class='ant-select-selection-item']")
            if data3.text == D_2:
                break
            i += 1

    def OTP_Page(self):
        easygui.msgbox("otppage")

