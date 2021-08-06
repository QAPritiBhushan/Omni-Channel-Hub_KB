import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.mongolianCustomerPassword import MongolianCustomerPassword
from PageObjects.login import Login
from Utilities.customLogger import LogGen
import Utilities.excelUtils


myLogger = LogGen.logGen()

@when(u'I change to English Language')
def change_to_english(context):
    login_page = Login(context.driver)
    login_page.setLanguage()
    forgot_password_title = WebDriverWait(context.driver,20).until(EC.presence_of_element_located((By.XPATH,"//span[@class='ant-page-header-heading-title'][@title='Forgot Password']")))


@then(u'I enter invalid username and registration number - SPWD for Mongolian Customer')
def enter_invalid_spwd_mongolian(context):
    global mongolian_customer_page
    mongolian_customer_page = MongolianCustomerPassword(context.driver)
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Mongolian_Valid")
    for r in range(2, rows + 1):
        username = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Invalid", r, 1)
        registration_number = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Invalid", r, 2)
        regNum1 = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Invalid", r, 3)
        regNum2 = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Invalid", r, 4)
        mongolian_customer_page.setUsername(username)
        mongolian_customer_page.selectRegValues(regNum1,regNum2)
        mongolian_customer_page.setRegNum(registration_number)
        mongolian_customer_page.clickOnContinue()
        try:
            error_popup_close_button = WebDriverWait(context.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[@class='ant-modal-close']")))
            if error_popup_close_button:
                assert True
                myLogger.info("*****Expected Error Popup Message Displayed")
                Utilities.excelUtils.writeData(data_sheet_path, "Mongolian_Invalid", r, 5, "Test Passed")
                context.driver.save_screenshot(".\\Screenshots\\" + "IncorrectMongolianDataForSPWD_Passed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Error Message for Incorrect Username/Registration Number Displayed",
                              attachment_type=AttachmentType.PNG)
                error_popup_close_button.click()
                username_text_button = WebDriverWait(context.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "//div[@class='ant-form-item-control-input-content']/input[@id='customerAuthForm_loginUserId']")))

                mongolian_customer_page.clearUsername()
                mongolian_customer_page.clearRegistrationNumber()
            else:
                assert False
                Utilities.excelUtils.writeData(data_sheet_path, "Mongolian_Invalid", r, 5, "Test Failed")
                context.driver.save_screenshot(".\\Screenshots\\" + "IncorrectMongolianDataForSPWD_Failed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Error Message for Incorrect Username/Registration Number Not Displayed",
                              attachment_type=AttachmentType.PNG)


        except Exception as e:
            myLogger.exception(e)
            context.driver.close()
            myLogger.info("*****Unable to test invalid set of data for SPWD for Mongolian Customer*****")


@then(u'I enter invalid username and registration number - TPWD for Mongolian Customer')
def enter_invalid_tpwd_mongolian(context):
    global mongolian_customer_page
    mongolian_customer_page = MongolianCustomerPassword(context.driver)
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Mongolian_Valid")
    for r in range(2, rows + 1):
        username = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Invalid", r, 1)
        registration_number = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Invalid", r, 2)
        regNum1 = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Invalid", r, 3)
        regNum2 = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Invalid", r, 4)
        mongolian_customer_page.setUsername(username)
        mongolian_customer_page.selectRegValues(regNum1,regNum2)
        mongolian_customer_page.setRegNum(registration_number)
        mongolian_customer_page.clickOnContinue()
        try:
            error_popup_close_button = WebDriverWait(context.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[@class='ant-modal-close']")))
            if error_popup_close_button:
                assert True
                myLogger.info("*****Expected Error Popup Message Displayed")
                Utilities.excelUtils.writeData(data_sheet_path, "Mongolian_Invalid", r, 6, "Test Passed")
                context.driver.save_screenshot(".\\Screenshots\\" + "IncorrectMongolianDataForTPWD_Passed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Error Message for Incorrect Username/Registration Number Displayed",
                              attachment_type=AttachmentType.PNG)
                error_popup_close_button.click()
                username_text_button = WebDriverWait(context.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "//div[@class='ant-form-item-control-input-content']/input[@id='customerAuthForm_loginUserId']")))

                mongolian_customer_page.clearUsername()
                mongolian_customer_page.clearRegistrationNumber()
            else:
                assert False
                Utilities.excelUtils.writeData(data_sheet_path, "Mongolian_Invalid", r, 6, "Test Failed")
                context.driver.save_screenshot(".\\Screenshots\\" + "IncorrectMongolianDataForTPWD_Failed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Error Message for Incorrect Username/Registration Number Not Displayed",
                              attachment_type=AttachmentType.PNG)


        except Exception as e:
            myLogger.exception(e)
            context.driver.close()
            myLogger.info("*****Unable to test invalid set of data for TPWD for Mongolian Customer*****")

@then(u'I enter valid username and registration number - SPWD for Mongolian Customer')
def enter_valid_spwd_mongolian(context):
    global mongolian_customer_page
    mongolian_customer_page = MongolianCustomerPassword(context.driver)
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Mongolian_Valid")
    for r in range(2, rows + 1):
        username = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Valid", r, 1)
        registration_number = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Valid", r, 2)
        regNum1 = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Valid", r, 3)
        regNum2 = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Valid", r, 4)
        mongolian_customer_page.setUsername(username)
        mongolian_customer_page.selectRegValues(regNum1,regNum2)
        mongolian_customer_page.setRegNum(registration_number)
        mongolian_customer_page.clickOnContinue()
        try:
            email_radiobutton_element = WebDriverWait(context.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='EMAIL']")))
            if email_radiobutton_element:
                assert True


                Utilities.excelUtils.writeData(data_sheet_path, "Mongolian_Valid", r, 5, "valid Data _ Test Passed")
                context.driver.save_screenshot(".\\Screenshots\\" + "CorrectMongolianDataForTPWD_Passed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                      name="Khan Bank OTP Selection Page Displayed",
                      attachment_type=AttachmentType.PNG)
                myLogger.info("*****Expected Email Element Displayed*****")
                context.driver.find_element(By.XPATH,"//span[@class='anticon anticon-arrow-left']").click()
            else:
                assert False
                context.driver.save_screenshot(".\\Screenshots\\" + "CorrectMongolianDataForTPWD_Failed.png")
                Utilities.excelUtils.writeData(data_sheet_path, "Mongolian_Valid", r, 5, "valid Data _ Test Failed")
                allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank OTP Selection Page Not Displayed",
                              attachment_type=AttachmentType.PNG)
                myLogger.info("*****Expected Element Email Radio Button Not Found*****")

        except Exception as e:
            myLogger.exception(e)
            context.driver.close()
            myLogger.info("*****Unable to test valid set of data for SPWD for Mongolian Customer*****")


@then(u'I enter valid username and registration number - TPWD for Mongolian Customer')
def enter_valid_tpwd_mongolian(context):
    global mongolian_customer_page
    mongolian_customer_page = MongolianCustomerPassword(context.driver)
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Mongolian_Valid")
    for r in range(2, rows + 1):
        username = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Valid", r, 1)
        registration_number = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Valid", r, 2)
        regNum1 = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Valid", r, 3)
        regNum2 = Utilities.excelUtils.readData(data_sheet_path, "Mongolian_Valid", r, 4)
        mongolian_customer_page.setUsername(username)
        mongolian_customer_page.selectRegValues(regNum1,regNum2)
        mongolian_customer_page.setRegNum(registration_number)
        mongolian_customer_page.clickOnContinue()
        try:
            email_radiobutton_element = WebDriverWait(context.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='EMAIL']")))
            if email_radiobutton_element:
                assert True


                Utilities.excelUtils.writeData(data_sheet_path, "Mongolian_Valid", r, 6, "valid Data _ Test Passed")
                context.driver.save_screenshot(".\\Screenshots\\" + "CorrectMongolianDataForTPWD_Passed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                      name="Khan Bank OTP Selection Page Displayed",
                      attachment_type=AttachmentType.PNG)
                myLogger.info("*****Expected Email Element Displayed*****")
                context.driver.find_element(By.XPATH,"//span[@class='anticon anticon-arrow-left']").click()
            else:
                assert False
                context.driver.save_screenshot(".\\Screenshots\\" + "CorrectMongolianDataForTPWD_Failed.png")
                Utilities.excelUtils.writeData(data_sheet_path, "Mongolian_Valid", r, 6, "valid Data _ Test Failed")
                allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank OTP Selection Page Not Displayed",
                              attachment_type=AttachmentType.PNG)
                myLogger.info("*****Expected Element Email Radio Button Not Found*****")

        except Exception as e:
            myLogger.exception(e)
            context.driver.close()
            myLogger.info("*****Unable to test valid set of data for TPWD for Mongolian Customer*****")









