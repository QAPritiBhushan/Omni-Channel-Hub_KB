import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.foreignCustomerPassword import ForeignCustomerPassword
from PageObjects.selectPassword import SelectPwd
from Utilities.customLogger import LogGen
import Utilities.excelUtils


myLogger = LogGen.logGen()

@then(u'I select the login password to be reset')
def select_login_pwd(context):
    global select_password_page
    select_password_page = SelectPwd(context.driver)
    try:
        select_password_page.selectLoginPassword()
        select_password_page.clickOnContinue()
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to select login password to be reset*****")


@then(u'I enter valid username and passport - SPWD for Foreign Customer')
def enter_valid_spwd_foreign(context):
    global foreign_customer_page
    foreign_customer_page = ForeignCustomerPassword(context.driver)
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Foreign_Valid")
    for r in range(2, rows + 1):
        username = Utilities.excelUtils.readData(data_sheet_path, "Foreign_Valid", r, 1)
        passport = Utilities.excelUtils.readData(data_sheet_path, "Foreign_Valid", r, 2)
        foreign_customer_page.setUsername(username)
        foreign_customer_page.setPassportNumber(passport)
        foreign_customer_page.clickOnContinue()
        try:
            email_button_element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//span[@class='ant-page-header-heading-title'][@title='Recover password']")))
            if email_button_element:
                assert True
                myLogger.info("*****Expected Element Email Radio Button is Found")
                Utilities.excelUtils.writeData(data_sheet_path, "Foreign_Valid", r, 3, "Test Passed")
                context.driver.save_screenshot(".\\Screenshots\\" + "CorrectForeignDataForSPWD_Passed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Khan Bank OTP Channel Selection Page Displayed",
                              attachment_type=AttachmentType.PNG)

                context.driver.find_element(By.CLASS_NAME, "ant-page-header-back-button").click()
            else:
                assert False
                Utilities.excelUtils.writeData(data_sheet_path, "Foreign_Valid", r, 3, "Test Failed")
                context.driver.save_screenshot(".\\Screenshots\\" + "CorrectForeignDataForSPWD_Failed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Khan Bank OTP Channel Selection Page Not Displayed",
                              attachment_type=AttachmentType.PNG)

        except Exception as e:
            myLogger.exception(e)
            context.driver.close()
            myLogger.info("*****Unable to enter valid username and passport number for Foreign Customer*****")



@then(u'I enter valid username and passport - TPWD for Foreign Customer')
def enter_valid_tpwd_foreign(context):
    global foreign_customer_page
    foreign_customer_page = ForeignCustomerPassword(context.driver)
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Foreign_Valid")
    for r in range(2, rows + 1):
        username = Utilities.excelUtils.readData(data_sheet_path, "Foreign_Valid", r, 1)
        passport = Utilities.excelUtils.readData(data_sheet_path, "Foreign_Valid", r, 2)
        foreign_customer_page.setUsername(username)
        foreign_customer_page.setPassportNumber(passport)
        foreign_customer_page.clickOnContinue()
        try:
            email_button_element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//span[@class='ant-page-header-heading-title'][@title='Recover password']")))
            if email_button_element:
                assert True
                myLogger.info("*****Expected Element Email Radio Button is Found")
                Utilities.excelUtils.writeData(data_sheet_path, "Foreign_Valid", r, 4, "Test Passed")
                context.driver.save_screenshot(".\\Screenshots\\" + "CorrectForeignDataForTPWD_Passed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Khan Bank OTP Channel Selection Page Displayed",
                              attachment_type=AttachmentType.PNG)

                context.driver.find_element(By.CLASS_NAME, "ant-page-header-back-button").click()
            else:
                assert False
                Utilities.excelUtils.writeData(data_sheet_path, "Foreign_Valid", r, 4, "Test Failed")
                context.driver.save_screenshot(".\\Screenshots\\" + "CorrectForeignDataForTPWD_Failed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Khan Bank OTP Channel Selection Page Not Displayed",
                              attachment_type=AttachmentType.PNG)


        except Exception as e:
            myLogger.exception(e)
            context.driver.close()
            myLogger.info("*****Unable to enter valid username and passport number for Foreign Customer*****")


@then(u'I enter invalid username and passport - SPWD for Foreign Customer')
def enter_invalid_spwd_foreign(context):
    global foreign_customer_page
    foreign_customer_page = ForeignCustomerPassword(context.driver)
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Foreign_Invalid")
    for r in range(2, rows + 1):
        username = Utilities.excelUtils.readData(data_sheet_path, "Foreign_Invalid", r, 1)
        passport = Utilities.excelUtils.readData(data_sheet_path, "Foreign_Invalid", r, 2)
        foreign_customer_page.setUsername(username)
        foreign_customer_page.setPassportNumber(passport)
        foreign_customer_page.clickOnContinue()
        try:
            error_popup_close_button = WebDriverWait(context.driver, 19).until(
                EC.presence_of_element_located((By.XPATH, "//button[@class='kb-button with-bordered']")))
            if error_popup_close_button:
                assert True
                myLogger.info("*****Expected Error Popup Message Displayed")
                Utilities.excelUtils.writeData(data_sheet_path, "Foreign_Invalid", r, 3, "Test Passed")
                context.driver.save_screenshot(".\\Screenshots\\" + "IncorrectForeignDataForSPWD_Passed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Error Message for Incorrect Username/Passport Number Displayed",
                              attachment_type=AttachmentType.PNG)
                error_popup_close_button.click()
                username_text_button = WebDriverWait(context.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "//div[@class='ant-form-item-control-input-content']/input[@id='customerAuthForm_loginUserId']")))

                foreign_customer_page.clearUsername()
                foreign_customer_page.clearPassportNumber()
            else:
                assert False
                Utilities.excelUtils.writeData(data_sheet_path, "Foreign_Invalid", r, 3, "Test Failed")
                context.driver.save_screenshot(".\\Screenshots\\" + "IncorrectForeignDataForSPWD_Failed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Error Message for Incorrect Username/Passport Number Not Displayed",
                              attachment_type=AttachmentType.PNG)


        except Exception as e:
            myLogger.exception(e)
            context.driver.close()
            myLogger.info("*****Unable to enter invalid username and passport number for Foreign Customer*****")


@then(u'I enter invalid username and passport - TPWD for Foreign Customer')
def enter_invalid_tpwd_foreign(context):
    global foreign_customer_page
    foreign_customer_page = ForeignCustomerPassword(context.driver)
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Foreign_Invalid")
    for r in range(2, rows + 1):
        username = Utilities.excelUtils.readData(data_sheet_path, "Foreign_Invalid", r, 1)
        passport = Utilities.excelUtils.readData(data_sheet_path, "Foreign_Invalid", r, 2)
        foreign_customer_page.setUsername(username)
        foreign_customer_page.setPassportNumber(passport)
        foreign_customer_page.clickOnContinue()
        try:
            error_popup_close_button = WebDriverWait(context.driver, 19).until(
                EC.presence_of_element_located((By.XPATH, "//button[@class='kb-button with-bordered']")))
            if error_popup_close_button:
                assert True
                myLogger.info("*****Expected Error Popup Message Displayed")
                Utilities.excelUtils.writeData(data_sheet_path, "Foreign_Invalid", r, 4, "Test Passed")
                context.driver.save_screenshot(".\\Screenshots\\" + "IncorrectForeignDataForTPWD_Passed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Error Message for Incorrect Username/Passport Number Displayed",
                              attachment_type=AttachmentType.PNG)
                error_popup_close_button.click()
                username_text_button = WebDriverWait(context.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "//div[@class='ant-form-item-control-input-content']/input[@id='customerAuthForm_loginUserId']")))

                foreign_customer_page.clearUsername()
                foreign_customer_page.clearPassportNumber()
            else:
                assert False
                Utilities.excelUtils.writeData(data_sheet_path, "Foreign_Invalid", r, 4, "Test Failed")
                context.driver.save_screenshot(".\\Screenshots\\" + "IncorrectForeignDataForTPWD_Failed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Error Message for Incorrect Username/Passport Number Not Displayed",
                              attachment_type=AttachmentType.PNG)

        except Exception as e:
            myLogger.exception(e)
            context.driver.close()
            myLogger.info("*****Unable to enter invalid username and passport number for Foreign Customer*****")



