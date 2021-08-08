import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Utilities.excelUtils
from PageObjects.corporateCustomerPassword import CorporateCustomerPassword
from PageObjects.setPassword import SetPassword
from Utilities.customLogger import LogGen

myLogger = LogGen.logGen()

@when(u'I enter username and registration number for the Corporate Customer')
def enter_username_regnum_corporate(context):
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    username = Utilities.excelUtils.readData(data_sheet_path, "Corporate_Valid", 2, 1)
    regNum = Utilities.excelUtils.readData(data_sheet_path, "Corporate_Valid", 2, 2)
    global corporate_customer_page
    corporate_customer_page = CorporateCustomerPassword(context.driver)
    try:
        corporate_customer_page.setUsername(username)
        corporate_customer_page.setRegistrationNumber(regNum)
        context.driver.save_screenshot(".\\Screenshots\\" + "CorporateCustomerDataEntered.png")
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="Data for Corporate Customer entered",
                      attachment_type=AttachmentType.PNG)
        myLogger.info("*****Corporate Customer Data Entered*****")
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Corporate Customer Data Not entered*****")


@when(u'I set the new login password for a Corporate customer and proceed')
def set_login_pwd_corporate(context):
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    enter_pwd = Utilities.excelUtils.readData(data_sheet_path, "Corporate_NewPWD", 2, 1)
    reenter_pwd = Utilities.excelUtils.readData(data_sheet_path, "Corporate_NewPWD", 2, 2)
    global set_password_page
    set_password_page = SetPassword(context.driver)
    try:
        set_password_page.setNewPassword(enter_pwd)
        set_password_page.reenterPassword(reenter_pwd)
        set_password_page.clickOnProceed()
        context.driver.save_screenshot(".\\Screenshots\\" + "NewSPWDForCorporateCustomerEntered.png")
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="New SPWD for Corporate Customer entered",
                      attachment_type=AttachmentType.PNG)
        myLogger.info("*****New SPWD for Corporate Customer Entered*****")
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****New SPWD for Corporate Customer Not entered*****")


@when(u'I set the new transaction password for a Corporate customer and proceed')
def set_transaction_pwd_corporate(context):
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    enter_pwd = Utilities.excelUtils.readData(data_sheet_path, "Corporate_NewPWD", 2, 1)
    reenter_pwd = Utilities.excelUtils.readData(data_sheet_path, "Corporate_NewPWD", 2, 2)
    global set_password_page
    set_password_page = SetPassword(context.driver)
    try:
        set_password_page.setNewPassword(enter_pwd)
        set_password_page.reenterPassword(reenter_pwd)
        set_password_page.clickOnProceed()
        context.driver.save_screenshot(".\\Screenshots\\" + "NewTPWDForCorporateCustomerEntered.png")
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="New TPWD for Corporate Customer entered",
                      attachment_type=AttachmentType.PNG)
        myLogger.info("*****New TPWD for Corporate Customer Entered*****")
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****New TPWD for Corporate Customer Not entered*****")



@then(u'User should be displayed with a warning message for the username field for Corporate Customer')
def username_warning_corporate(context):
    try:
        username_warning_message = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Нэвтрэх нэрээ оруулна уу')]")))
        if context.driver.find_element(By.XPATH,"//div[contains(text(),'Нэвтрэх нэрээ оруулна уу')]").text == "Нэвтрэх нэрээ оруулна уу":
            myLogger.info("*****Warning Message to Enter username is displayed")
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "CorporateUsernameWarningDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Enter Username Warning Message for Corporate Customer displayed",
                          attachment_type=AttachmentType.PNG)
        else:
            myLogger.info("*****Warning Message to Enter username is not displayed")
            context.driver.save_screenshot(".\\Screenshots\\" + "NoCorporateUsernameWarningDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Enter Username Warning Message for Corporate Customer Not Displayed",
                          attachment_type=AttachmentType.PNG)
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to validate the warning message to Enter Username*****")

@then(u'User should be displayed with a warning message for the registration number field for Corporate Customer')
def regnum_warning_corporate(context):
    try:
        regNum_warning_message = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Байгууллагын регистрийн дугаар оруулна уу')]")))
        if context.driver.find_element(By.XPATH,"//div[contains(text(),'Байгууллагын регистрийн дугаар оруулна уу')]").text == "Байгууллагын регистрийн дугаар оруулна уу":
            myLogger.info("*****Warning Message to Enter Company Registration Number is displayed")
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "CorporateRegNumWarningDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Khan Bank Enter Registration Number Warning Message for Corporate Customer displayed",
                          attachment_type=AttachmentType.PNG)
        else:
            myLogger.info("*****Warning Message to Enter Company Registration Number is not displayed")
            context.driver.save_screenshot(".\\Screenshots\\" + "NoCorporateRegNumWarningDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Khan Bank Enter Registration Number Warning Message for Corporate Customer Not displayed",
                          attachment_type=AttachmentType.PNG)
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to validate the warning message to Enter Company Registration Number*****")




