import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.recoverPassword import RecoverPassword
from PageObjects.foreignCustomerPassword import ForeignCustomerPassword
from PageObjects.setPassword import SetPassword
from Utilities.customLogger import LogGen
import Utilities.excelUtils

myLogger = LogGen.logGen()


@when(u'I enter username and passport number for Foreign Customer')
def enter_username_passportnum_foreign(context):
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    username = Utilities.excelUtils.readData(data_sheet_path, "Foreign_Valid", 2, 1)
    passport = Utilities.excelUtils.readData(data_sheet_path, "Foreign_Valid", 2, 2)
    global foreign_customer_page
    foreign_customer_page = ForeignCustomerPassword(context.driver)
    try:
        foreign_customer_page.setUsername(username)
        foreign_customer_page.setPassportNumber(passport)
        context.driver.save_screenshot(".\\Screenshots\\" + "ForeignCustomerDataEntered.png")
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="Data for Foreign Customer entered",
                      attachment_type=AttachmentType.PNG)
        myLogger.info("*****Foreign Customer Data Entered*****")
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Foreign Customer Data Not entered*****")


@when(u'I set the new login password for a Foreign customer and proceed')
def set_login_pwd_foreign(context):
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    enter_pwd = Utilities.excelUtils.readData(data_sheet_path, "Foreign_NewPWD", 2, 1)
    reenter_pwd = Utilities.excelUtils.readData(data_sheet_path, "Foreign_NewPWD", 2, 2)
    global set_password_page
    set_password_page = SetPassword(context.driver)
    try:
        set_password_page.setNewPassword(enter_pwd)
        set_password_page.reenterPassword(reenter_pwd)
        set_password_page.clickOnProceed()
        context.driver.save_screenshot(".\\Screenshots\\" + "NewSPWDForForeignCustomerEntered.png")
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="New SPWD for Foreign Customer entered",
                      attachment_type=AttachmentType.PNG)
        myLogger.info("*****New SPWD for Foreign Customer Entered*****")
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****New SPWD for Foreign Customer Not entered*****")



@when(u'I set the new transaction password for a Foreign customer and proceed')
def set_transaction_pwd_foreign(context):
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    enter_pwd = Utilities.excelUtils.readData(data_sheet_path, "Foreign_NewPWD", 2, 1)
    reenter_pwd = Utilities.excelUtils.readData(data_sheet_path, "Foreign_NewPWD", 2, 2)
    global set_password_page
    set_password_page = SetPassword(context.driver)
    try:
        set_password_page.setNewPassword(enter_pwd)
        set_password_page.reenterPassword(reenter_pwd)
        set_password_page.clickOnProceed()
        context.driver.save_screenshot(".\\Screenshots\\" + "NewTPWDForForeignCustomerEntered.png")
        allure.attach(context.driver.get_screenshot_as_png(),
                  name="New TPWD for Foreign Customer entered",
                  attachment_type=AttachmentType.PNG)
        myLogger.info("*****New TPWD for Foreign Customer Entered*****")
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****New TPWD for Foreign Customer Not entered*****")





@then(u'I click on Continue button without entering username and passport number')
def continue_without_username_passportnum(context):
    global foreign_customer_page
    foreign_customer_page = ForeignCustomerPassword(context.driver)
    try:
        foreign_customer_page.clickOnContinue()
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to Click on Continue*****")



@then(u'User should be displayed with a warning message for the username field for Foreign Customer')
def username_warning_foreign(context):
    try:
        username_warning_message = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Enter username')]")))
        if context.driver.find_element(By.XPATH,"//div[contains(text(),'Enter username')]").text == "Enter username":
            myLogger.info("*****Warning Message to Enter username is displayed")
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "ForeignUsernameWarningDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Enter Username Warning Message for Foreign Customer displayed",
                          attachment_type=AttachmentType.PNG)
        else:
            assert False
            myLogger.info("*****Warning Message to Enter username is not displayed")
            context.driver.save_screenshot(".\\Screenshots\\" + "NoForeignUsernameWarningDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Enter Username Warning Message for Foreign Customer Not Displayed",
                          attachment_type=AttachmentType.PNG)
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to validate the warning message to Enter Username*****")



@then(u'User should be displayed with a warning message for the passport number field for Foreign Customer')
def passportnum_warning_foreign(context):
    try:
        passportNum_warning_message = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Enter Passport Number')]")))
        if context.driver.find_element(By.XPATH,"//div[contains(text(),'Enter Passport Number')]").text == "Enter Passport Number":
            myLogger.info("*****Warning Message to Enter Passport Number is displayed")
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "ForeignPassportNumWarningDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Enter Passport Number Warning Message for Foreign Customer displayed",
                          attachment_type=AttachmentType.PNG)
        else:
            assert False
            myLogger.info("*****Warning Message to Enter Passport Number is not displayed")
            context.driver.save_screenshot(".\\Screenshots\\" + "NoForeignPassportNumWarningNotDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Enter Passport Number Warning Message for Foreign Customer Not Displayed",
                          attachment_type=AttachmentType.PNG)
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to validate the warning message to Enter Passport Number*****")


