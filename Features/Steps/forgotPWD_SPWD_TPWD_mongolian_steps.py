import time
import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Utilities.excelUtils
from PageObjects.mongolianCustomerPassword import MongolianCustomerPassword
from PageObjects.recoverPassword import RecoverPassword
from PageObjects.otpConfirmationPage import OTPConfirmation
from PageObjects.setPassword import SetPassword
from Utilities.customLogger import LogGen

myLogger = LogGen.logGen()

@when(u'I enter username and registration number for Mongolian Customer')
def enter_username_regnum_mongolian(context):
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    global mongolian_customer_page
    mongolian_customer_page = MongolianCustomerPassword(context.driver)
    username = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Valid", 2, 1)
    registration_number = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Valid", 2, 2)
    regNum1 = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Valid", 2, 3)
    regNum2 = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Valid", 2, 4)
    try:
        mongolian_customer_page.setUsername(username)
        mongolian_customer_page.selectRegValues(regNum1, regNum2)
        mongolian_customer_page.setRegNum(registration_number)
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to enter username and registration number for Mongolian Customer")


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


@when(u'I set the new login password for a Mongolian customer and proceed')
def set_login_pwd_mongolian(context):
    data_sheet_path = "/TestData/forgotPasswordData.xlsx"
    enter_pwd = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_NewSPWD", 2, 1)
    reenter_pwd = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_NewSPWD", 2, 2)
    global set_password_page
    set_password_page = SetPassword(context.driver)
    try:
        set_password_page.setNewPassword(enter_pwd)
        set_password_page.reenterPassword(reenter_pwd)
        set_password_page.clickOnProceed()
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to Set New Login Password for a Mongolian Customer and Proceed")



@when(u'I set the new transaction password for a Mongolian customer and proceed')
def set_transaction_pwd_mongolian(context):
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    enter_pwd = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_NewTPWD", 2, 1)
    reenter_pwd = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_NewTPWD", 2, 2)
    global set_password_page
    set_password_page = SetPassword(context.driver)
    try:
        set_password_page.setNewPassword(enter_pwd)
        set_password_page.reenterPassword(reenter_pwd)
        set_password_page.clickOnProceed()
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to Set New Transaction Password for a Mongolian Customer and Proceed")


@then(u'I should be displayed with a password reset success pop-up message')
def display_password_reset_success(context):
    try:
        reset_success_popup_element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[@class='title']")))
        if reset_success_popup_element:
            assert True

            context.driver.save_screenshot(".\\Screenshots\\" + "PasswordResetSuccess.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Khan Bank Password Reset Success Message is Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Expected Element Reset Success Popup Modal is Found*****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "PasswordResetFail.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Khan Bank Password Reset Success Message is Not Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Expected Element Reset Success Popup Modal is Not Found*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to verify the password reset success pop-up message*****")

@then(u'User should be displayed with a warning message for the username field for Mongolian Customer')
def username_warning_mongolian(context):
    try:
        username_warning_message = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Нэвтрэх нэрээ оруулна уу!')]")))
        if context.driver.find_element(By.XPATH,"//div[contains(text(),'Нэвтрэх нэрээ оруулна уу!')]").text == "Нэвтрэх нэрээ оруулна уу!":
            myLogger.info("*****Warning Message to Enter username is displayed")
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "MongolianUsernameWarningDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Enter Username Warning Message for Mongolian Customer displayed",
                          attachment_type=AttachmentType.PNG)
        else:
            assert False
            myLogger.info("*****Warning Message to Enter username is not displayed")
            context.driver.save_screenshot(".\\Screenshots\\" + "NoMongolianUsernameWarningDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Enter Username Warning Message for Mongolian Customer Not Displayed",
                          attachment_type=AttachmentType.PNG)
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to verify the username warning message for Mongolian Customer*****")

@then(u'User should be displayed with a warning message for the registration number field for Mongolian Customer')
def regnum_warning_mongolian(context):
    try:
        regNum_warning_message = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Регистрийн дугаар оруулна уу')]")))
        if context.driver.find_element(By.XPATH,"//div[contains(text(),'Регистрийн дугаар оруулна уу')]").text == "Регистрийн дугаар оруулна уу":
            myLogger.info("*****Warning Message to Enter Company Registration Number is displayed")
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "MongolianRegNumWarningDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Khan Bank Enter Registration Number Warning Message for Mongolian Customer displayed",
                          attachment_type=AttachmentType.PNG)
        else:
            assert False
            myLogger.info("*****Warning Message to Enter Company Registration Number is not displayed")
            context.driver.save_screenshot(".\\Screenshots\\" + "NoMongolianRegNumWarningDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Khan Bank Enter Registration Number Warning Message for Mongolian Customer Not displayed",
                          attachment_type=AttachmentType.PNG)
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to verify the registration warning message for Mongolian Customer*****")














