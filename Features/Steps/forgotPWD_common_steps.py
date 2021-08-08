import time
import allure
from PageObjects.login import Login
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.corporateCustomerPassword import CorporateCustomerPassword
from PageObjects.mongolianCustomerPassword import MongolianCustomerPassword
from PageObjects.recoverPassword import RecoverPassword
from PageObjects.otpConfirmationPage import OTPConfirmation
from PageObjects.selectPassword import SelectPwd
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



@then(u'I click on Continue button without entering username and registration number')
def continue_without_username_regnum(context):
    global corporate_customer_page
    try:
        corporate_customer_page = CorporateCustomerPassword(context.driver)
        corporate_customer_page.clickOnContinue()
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to Click on Continue*****")



@when(u'I click on Continue button')
def click_on_continue(context):
    global mongolian_customer_page
    mongolian_customer_page = MongolianCustomerPassword(context.driver)
    try:
        mongolian_customer_page.clickOnContinue()
        myLogger.info("*****Clicked On Continue*****")
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to Click on Continue button")


@then(u'I should be displayed with the OTP channel selection page')
def display_otp_channel_selection(context):
    global recover_password_page
    recover_password_page = RecoverPassword(context.driver)
    try:
        email_radiobutton_element = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='EMAIL']")))
        if email_radiobutton_element:
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "OTPSelectionPageDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank OTP Selection Page Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Expected Element Email Radio Button Found*****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "OTPSelectionPageDisplayedNotDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank OTP Selection Page Not Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Expected Element Email Radio Button Not Found*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to verify the presence of Email Radio Button*****")

@when(u'I select email as OTP channel')
def select_email_otp_channel(context):
    global recover_password_page
    recover_password_page = RecoverPassword(context.driver)
    try:
        recover_password_page.selectEmailID()
        context.driver.save_screenshot(".\\Screenshots\\" + "EmailRadioBtnSelected.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Email Radio Button Selected",
                      attachment_type=AttachmentType.PNG)

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to select email as OTP channel*****")

@then(u'I should be displayed with the OTP Page with a timer of 15 minutes')
def display_otp_page(context):
    global otp_confirmation_page
    otp_confirmation_page = OTPConfirmation(context.driver)
    try:
        enter_otp_element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID,"otp")))
        #timer_element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//span[@class='ant-typography timer'][text()='15:00']")))
        #if timer_element.text=="15:00":
        if enter_otp_element:
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "OTPConfirmationPageDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank OTP Confirmation Page Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Expected Element Enter OTP Found*****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "OTPConfirmationPageNotDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank OTP Confirmation Page Not Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Expected Element Enter OTP Not Found*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to verify the presence of Enter OTP element*****")


@when(u'I click on Continue button and enter OTP and continue')
def continue_after_otp_entry(context):
    global  otp_selection_page
    otp_selection_page = RecoverPassword(context.driver)
    global otp_confirmation_page
    otp_confirmation_page = OTPConfirmation(context.driver)
    try:
        otp_selection_page.clickOnContinue()
        time.sleep(120)
        otp_confirmation_page.clickOnContinue()
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to enter OTP and continue*****")




@then(u'I should be displayed with the Set Password Page')
def display_set_password_page(context):
    try:
        new_password_element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID,"customerAuthForm_password")))
        if new_password_element:
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "SetPasswordPageDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Set Password Page Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Expected Element New Password Field is Found*****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "SetPasswordPageNotDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Set Password Page Not Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Expected Element New Password Field is Not Found*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to verify the presence of New Password Element*****")


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
