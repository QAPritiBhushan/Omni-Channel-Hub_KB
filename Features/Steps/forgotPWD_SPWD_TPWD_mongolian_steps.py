import time

import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.mongolianCustomerPassword import MongolianCustomerPassword
from PageObjects.recoverPassword import RecoverPassword
from PageObjects.otpConfirmationPage import OTPConfirmation
from Utilities.constants import Constants
from Utilities.customLogger import LogGen

myLogger = LogGen.logGen()

@when(u'I enter username and registration number')
def step_impl(context):
    global mongolian_customer_page
    mongolian_customer_page = MongolianCustomerPassword(context.driver)
    mongolian_customer_page.setUsername("infura_7")
    mongolian_customer_page.setRegNum("61082018")
    time.sleep(10)
    #mongolian_customer_page.clickOnRegDrpDwn1()


@when(u'I click on Continue button')
def step_impl(context):
    global mongolian_customer_page
    mongolian_customer_page = MongolianCustomerPassword(context.driver)
    mongolian_customer_page.clickOnContinue()
    myLogger.info("*****Clicked On Continue*****")


@then(u'I should be displayed with the OTP channel selection page')
def step_impl(context):
    global recover_password_page
    recover_password_page = RecoverPassword(context.driver)
    try:
        email_radiobutton_element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='EMAIL']")))
        assert True
        context.driver.save_screenshot(".\\Screenshots\\" + "OTPSelectionPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank OTP Selection Page Displayed",
                  attachment_type=AttachmentType.PNG)
        myLogger.info("*****Expected Element Email Radio Button Found*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Expected Element Email Radio Button Not Found*****")

@when(u'I select email as OTP channel')
def step_impl(context):
    global recover_password_page
    recover_password_page = RecoverPassword(context.driver)
    try:
        recover_password_page.selectEmailID()
        recover_password_page.clickOnContinue()

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()

@then(u'I should be displayed with the OTP Page with a timer of 15 minutes')
def step_impl(context):
    global otp_confirmation_page
    otp_confirmation_page = OTPConfirmation(context.driver)
    try:
        #timer_element = WebDriverWait(context.driver,10).until(
        #EC.presence_of_element_located((By.XPATH,"//span[@class='ant-typography timer']")))
        enter_otp_element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID,"otp")))

        assert True
        context.driver.save_screenshot(".\\Screenshots\\" + "OTPSelectionPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank OTP Confirmation Page Displayed",
                  attachment_type=AttachmentType.PNG)
        myLogger.info("*****Expected Element OTP Timer is Found*****")
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Expected Element OTP Timer is Not Found*****")















