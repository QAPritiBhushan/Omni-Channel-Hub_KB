import time
import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.mongolianCustomerPassword import MongolianCustomerPassword
from PageObjects.foreignCustomerPassword import ForeignCustomerPassword
from PageObjects.corporateCustomerPassword import CorporateCustomerPassword
from Utilities.customLogger import LogGen
import Utilities.excelUtils

myLogger = LogGen.logGen()

@when(u'I enter disallowed characters in the username field for Mongolian Customer')
def enter_incorrect_username_mongolian(context):
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    username = Utilities.excelUtils.readData(data_sheet_path, "MN_Username_Error", 2, 1)
    global mongolian_customer_page
    mongolian_customer_page = MongolianCustomerPassword(context.driver)
    try:
        mongolian_customer_page.setUsername(username)
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to enter characters in the username field for Mongolian Customer*****")



@when(u'I enter disallowed characters in the username field for Foreign Customer')
def enter_incorrect_username_foreign(context):
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    username = Utilities.excelUtils.readData(data_sheet_path, "Foreign_Username_Error", 2, 1)
    global foreign_customer_page
    foreign_customer_page = ForeignCustomerPassword(context.driver)
    try:
        foreign_customer_page.setUsername(username)
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to enter characters in the username field for Foreign Customer*****")




@when(u'I enter disallowed characters in the username field for Corporate Customer')
def enter_incorrect_username_corporate(context):
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    username = Utilities.excelUtils.readData(data_sheet_path, "Corporate_Username_Error", 2, 1)
    global corporate_customer_page
    corporate_customer_page = CorporateCustomerPassword(context.driver)
    try:
        corporate_customer_page.setUsername(username)
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to enter characters in the username field for Corporate Customer*****")


@then(u'I should be displayed with a warning message for username for SPWD for the Mongolian Customer')
def username_warning_spwd_mongolian(context):
    try:

        warning_message_username = WebDriverWait(context.driver,20).until(EC.presence_of_element_located((By.XPATH,"//div[@role='alert'][text()='Нэвтрэх нэр 0-9, A-Z, a-z . - _ тэмдэгтүүдээс бүрдэнэ']")))
        myLogger.info("The warning is"+warning_message_username.text)
        if warning_message_username.text == "Нэвтрэх нэр 0-9, A-Z, a-z . - _ тэмдэгтүүдээс бүрдэнэ":
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "MN_SPWD_UsernameWarningDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Warning message for disallowed characters for username field is displayed for MN_SPWD",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Warning Message for Disallowed Characters for Username field Displayed*****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "MN_SPWD_UsernameWarningNotDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Warning message for disallowed characters for username field is not displayed for MN_SPWD",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Warning Message for Disallowed Characters for Username field Not Displayed*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to verify the error message for disallowed characters for the username field for Mongolian Customer*****")

@then(u'I should be displayed with a warning message for username for TPWD the Mongolian Customer')
def username_warning_tpwd_mongolian(context):
    try:

        warning_message_username = WebDriverWait(context.driver,20).until(EC.presence_of_element_located((By.XPATH,"//div[@role='alert'][text()='Нэвтрэх нэр 0-9, A-Z, a-z . - _ тэмдэгтүүдээс бүрдэнэ']")))
        myLogger.info("The warning is"+warning_message_username.text)
        if warning_message_username.text == "Нэвтрэх нэр 0-9, A-Z, a-z . - _ тэмдэгтүүдээс бүрдэнэ":
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "MN_TPWD_UsernameWarningDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Warning message for disallowed characters for username field is displayed for MN_TPWD",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Warning Message for Disallowed Characters for Username field Displayed*****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "MN_TPWD_UsernameWarningNotDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Warning message for disallowed characters for username field is not displayed for MN_TPWD",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Warning Message for Disallowed Characters for Username field Not Displayed*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to verify the error message for disallowed characters for the username field for Mongolian Customer*****")

@then(u'I should be displayed with a warning message for username for SPWD for the Foreign Customer')
def username_warning_spwd_foreign(context):
    try:

        warning_message_username = WebDriverWait(context.driver,20).until(EC.presence_of_element_located((By.XPATH,"//div[@role='alert'][text()='Allowed characters 0-9, A-Z, a-z . - _']")))
        myLogger.info("The warning is"+warning_message_username.text)
        if warning_message_username.text == "Allowed characters 0-9, A-Z, a-z . - _":
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "Foreign_SPWD_UsernameWarningDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Warning message for disallowed characters for username field is displayed for Foreign_SPWD",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Warning Message for Disallowed Characters for Username field Displayed*****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "Foreign_SPWD_UsernameWarningNotDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Warning message for disallowed characters for username field is not displayed for Foreign_SPWD",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Warning Message for Disallowed Characters for Username field Not Displayed*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to verify the error message for disallowed characters for the username field for Foreign Customer*****")

@then(u'I should be displayed with a warning message for username for TPWD the Foreign Customer')
def username_warning_tpwd_foreign(context):
    try:

        warning_message_username = WebDriverWait(context.driver,20).until(EC.presence_of_element_located((By.XPATH,"//div[@role='alert'][text()='Allowed characters 0-9, A-Z, a-z . - _']")))
        myLogger.info("The warning is"+warning_message_username.text)
        if warning_message_username.text == "Allowed characters 0-9, A-Z, a-z . - _":
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "Foreign_TPWD_UsernameWarningDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Warning message for disallowed characters for username field is displayed for Foreign_TPWD",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Warning Message for Disallowed Characters for Username field Displayed*****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "Foreign_TPWD_UsernameWarningNotDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Warning message for disallowed characters for username field is not displayed for Foreign_TPWD",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Warning Message for Disallowed Characters for Username field Not Displayed*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to verify the error message for disallowed characters for the username field for Foreign Customer*****")


@then(u'I should be displayed with a warning message for username for SPWD for the Corporate Customer')
def username_warning_spwd_corporate(context):
    try:
        time.sleep(3)
        warning_message_username = WebDriverWait(context.driver,30).until(EC.presence_of_element_located((By.XPATH,"//div[@role='alert'][text()='Нэвтрэх нэр 0-9, A-Z, a-z . - _ тэмдэгтүүдээс бүрдэнэ']")))
        myLogger.info("The warning is"+warning_message_username.text)
        if warning_message_username.text == "Нэвтрэх нэр 0-9, A-Z, a-z . - _ тэмдэгтүүдээс бүрдэнэ":
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "Corporate_SPWD_UsernameWarningDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Warning message for disallowed characters for username field is displayed for Corporate_SPWD",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Warning Message for Disallowed Characters for Username field Displayed*****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "Corporate_SPWD_UsernameWarningNotDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Warning message for disallowed characters for username field is not displayed for Corporate_SPWD",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Warning Message for Disallowed Characters for Username field Not Displayed*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to verify the error message for disallowed characters for the username field for Corporate Customer*****")

@then(u'I should be displayed with a warning message for username for TPWD the Corporate Customer')
def username_warning_tpwd_corporate(context):
    try:

        warning_message_username = WebDriverWait(context.driver,20).until(EC.presence_of_element_located((By.XPATH,"//div[@role='alert'][text()='Нэвтрэх нэр 0-9, A-Z, a-z . - _ тэмдэгтүүдээс бүрдэнэ']")))
        myLogger.info("The warning is"+warning_message_username.text)
        if warning_message_username.text == "Нэвтрэх нэр 0-9, A-Z, a-z . - _ тэмдэгтүүдээс бүрдэнэ":
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "Corporate_TPWD_UsernameWarningDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Warning message for disallowed characters for username field is displayed for Corporate_TPWD",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Warning Message for Disallowed Characters for Username field Displayed*****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "Corporate_TPWD_UsernameWarningNotDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Warning message for disallowed characters for username field is not displayed for Corporate_TPWD",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Warning Message for Disallowed Characters for Username field Not Displayed*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to verify the error message for disallowed characters for the username field for corporate customer*****")



