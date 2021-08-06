import time
import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObjects.login import Login
from PageObjects.selectPassword import SelectPwd
from PageObjects.mongolianCustomerPassword import MongolianCustomerPassword
from Utilities.constants import Constants
from Utilities.customLogger import LogGen

myLogger = LogGen.logGen()

@when(u'I click on Forgot Password link')
def click_forgot_pwd_link(context):
    global login_page
    login_page = Login(context.driver)
    global select_password_page
    select_password_page = SelectPwd(context.driver)

    try:
        login_page.clickOnForgotPassword()
        login_password_element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"//input[@value='SPWD']")))
        if login_password_element:
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "SelectPasswordPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Select Password Page",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Expected Element Login Password Radio Button Found*****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "SelectPasswordPageNotDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Select Password Page Not Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Expected Element Login Password Radio Button Not Found*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to verify the presence of Login Password Radio Button******")


@when(u'I select the login password to be reset')
def select_login_pwd(context):
    global select_password_page
    select_password_page = SelectPwd(context.driver)
    try:
        select_password_page.selectLoginPassword()
        select_password_page.clickOnContinue()
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to select login password and click on Continue")


@then(u'I select the transaction password to be reset')
def select_transaction_pwd(context):
    global select_password_page
    select_password_page = SelectPwd(context.driver)
    try:
        select_password_page.selectTransactionPassword()
        select_password_page.clickOnContinue()
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to select transaction password and click on Continue")


@when(u'I select the transaction password to be reset')
def select_transaction_pwd(context):
    global select_password_page
    select_password_page = SelectPwd(context.driver)
    try:
        select_password_page.selectTransactionPassword()
        select_password_page.clickOnContinue()
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to select transaction password and click on Continue")



@then(u'I should be displayed with the Forgot password page for Mongolian Customer')
def display_forgotPWD_mongolian_customer(context):
    global mongolian_customer_password_page
    mongolian_customer_password_page = MongolianCustomerPassword(context.driver)
    try:
        username_element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID,"customerAuthForm_loginUserId")))
        if username_element:
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "ForgotPWDPageMongolian.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Khan Bank Forgot Password Page for Mongolian Customers Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Expected Element Username Text field Found*****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "ForgotPWDPageMongolianNotDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Khan Bank Forgot Password Page for Mongolian Customers Not Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Expected Element Username Text field Not Found*****")


    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to verify the presence of Username Element******")


@then(u'I click on Continue button without selecting a password')
def continue_without_pwd_selection(context):
    global select_password_page
    select_password_page = SelectPwd(context.driver)
    try:
        select_password_page.clickOnContinue()
        time.sleep(3)
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to Click on Continue******")



@then(u'Warning message should be displayed to select password')
def display_warning_pwd_selection(context):
    global select_password_page
    select_password_page = SelectPwd(context.driver)

    try:
        warning_select_password_msg = context.driver.find_element_by_xpath("//div[@role='alert']").text
        if warning_select_password_msg == "Нууц үгийн төрөл сонгоно уу":
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "SelectPWDTypeWarning.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Select Password Type Warning Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("Warning message - Select Password Type is displayed")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "NoSelectPWDTypeWarning.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Select Password Type Warning Not Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("Warning message - Select Password Type is not displayed")
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("Unable to test the negative test - Without selecting a password type ")
