import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.corporateCustomerPassword import CorporateCustomerPassword
from Utilities.customLogger import LogGen
import Utilities.excelUtils


myLogger = LogGen.logGen()


@then(u'I enter valid username and registration number - SPWD for Corporate Customer')
def enter_valid_spwd_corporate(context):
    global corporate_customer_page
    corporate_customer_page = CorporateCustomerPassword(context.driver)
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Corporate_Valid")
    for r in range(2, rows + 1):
        username = Utilities.excelUtils.readData(data_sheet_path, "Corporate_Valid", r, 1)
        registration_Number = Utilities.excelUtils.readData(data_sheet_path, "Corporate_Valid", r, 2)
        corporate_customer_page.setUsername(username)
        corporate_customer_page.setRegistrationNumber(registration_Number)
        corporate_customer_page.clickOnContinue()
        try:
            email_button_element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//span[@class='ant-page-header-heading-title'][@title='Recover password']")))
            if email_button_element:
                assert True
                myLogger.info("*****Expected Element Email Radio Button is Found")
                Utilities.excelUtils.writeData(data_sheet_path, "Corporate_Valid", r, 3, "Test Passed")
                context.driver.save_screenshot(".\\Screenshots\\" + "CorrectCorporateDataForSPWD_Passed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Khan Bank OTP Channel Selection Page Displayed",
                              attachment_type=AttachmentType.PNG)

                context.driver.find_element(By.CLASS_NAME, "ant-page-header-back-button").click()
            else:
                assert False
                Utilities.excelUtils.writeData(data_sheet_path, "Corporate_Valid", r, 3, "Test Failed")
                context.driver.save_screenshot(".\\Screenshots\\" + "CorrectCorporateDataForSPWD_Failed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Khan Bank OTP Channel Selection Page Not Displayed",
                              attachment_type=AttachmentType.PNG)

        except Exception as e:
            myLogger.exception(e)
            context.driver.close()
            myLogger.info("*****Unable to enter valid username and registration number for Corporate Customer*****")



@then(u'I enter valid username and registration number - TPWD for Corporate Customer')
def enter_valid_tpwd_corporate(context):
    global corporate_customer_page
    corporate_customer_page = CorporateCustomerPassword(context.driver)
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Corporate_Valid")
    for r in range(2, rows + 1):
        username = Utilities.excelUtils.readData(data_sheet_path, "Corporate_Valid", r, 1)
        registration_Number = Utilities.excelUtils.readData(data_sheet_path, "Corporate_Valid", r, 2)
        corporate_customer_page.setUsername(username)
        corporate_customer_page.setRegistrationNumber(registration_Number)
        corporate_customer_page.clickOnContinue()
        try:
            email_button_element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//span[@class='ant-page-header-heading-title'][@title='Recover password']")))
            if email_button_element:
                assert True
                myLogger.info("*****Expected Element Email Radio Button is Found")
                Utilities.excelUtils.writeData(data_sheet_path, "Corporate_Valid", r, 4, "Test Passed")
                context.driver.save_screenshot(".\\Screenshots\\" + "CorrectCorporateDataForTPWD_Passed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Khan Bank OTP Channel Selection Page Displayed",
                              attachment_type=AttachmentType.PNG)

                context.driver.find_element(By.CLASS_NAME, "ant-page-header-back-button").click()
            else:
                assert False
                Utilities.excelUtils.writeData(data_sheet_path, "Corporate_Valid", r, 4, "Test Failed")
                context.driver.save_screenshot(".\\Screenshots\\" + "CorrectCorporateDataForTPWD_Failed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Khan Bank OTP Channel Selection Page Not Displayed",
                              attachment_type=AttachmentType.PNG)


        except Exception as e:
            myLogger.exception(e)
            context.driver.close()
            myLogger.info("*****Unable to enter valid username and registration number for Corporate Customer*****")


@then(u'I enter invalid username and registration number - SPWD for Corporate Customer')
def enter_invalid_spwd_corporate(context):

    global corporate_customer_page
    corporate_customer_page = CorporateCustomerPassword(context.driver)
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Corporate_Invalid")
    for r in range(2, rows + 1):
        username = Utilities.excelUtils.readData(data_sheet_path, "Corporate_Invalid", r, 1)
        registration_Number = Utilities.excelUtils.readData(data_sheet_path, "Corporate_Invalid", r, 2)
        corporate_customer_page.setUsername(username)
        corporate_customer_page.setRegistrationNumber(registration_Number)
        corporate_customer_page.clickOnContinue()
        try:
            error_popup_close_button = WebDriverWait(context.driver, 19).until(
                EC.presence_of_element_located((By.XPATH, "//button[@class='kb-button with-bordered']")))
            if error_popup_close_button:
                assert True
                myLogger.info("*****Expected Error Popup Message Displayed")
                Utilities.excelUtils.writeData(data_sheet_path, "Corporate_Invalid", r, 3, "Test Passed")
                context.driver.save_screenshot(".\\Screenshots\\" + "IncorrectCorporateDataForSPWD_Passed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Error Message for Incorrect Username/Registration Number Displayed",
                              attachment_type=AttachmentType.PNG)
                error_popup_close_button.click()
                username_text_button = WebDriverWait(context.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "//div[@class='ant-form-item-control-input-content']/input[@id='customerAuthForm_loginUserId']")))

                corporate_customer_page.clearUsername()
                corporate_customer_page.clearRegistrationNumber()
            else:
                assert False
                Utilities.excelUtils.writeData(data_sheet_path, "Corporate_Invalid", r, 3, "Test Failed")
                context.driver.save_screenshot(".\\Screenshots\\" + "IncorrectCorporateDataForSPWD_Failed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Error Message for Incorrect Username/Registration Number Not Displayed",
                              attachment_type=AttachmentType.PNG)


        except Exception as e:
            myLogger.exception(e)
            context.driver.close()
            myLogger.info("*****Unable to enter invalid username and registration number for Corporate Customer*****")


@then(u'I enter invalid username and registration number - TPWD for Corporate Customer')
def enter_invalid_tpwd_corporate(context):
    global corporate_customer_page
    corporate_customer_page = CorporateCustomerPassword(context.driver)
    data_sheet_path = ".\\TestData\\forgotPasswordData.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Foreign_Invalid")
    for r in range(2, rows + 1):
        username = Utilities.excelUtils.readData(data_sheet_path, "Corporate_Invalid", r, 1)
        registration_Number = Utilities.excelUtils.readData(data_sheet_path, "Corporate_Invalid", r, 2)
        corporate_customer_page.setUsername(username)
        corporate_customer_page.setRegistrationNumber(registration_Number)
        corporate_customer_page.clickOnContinue()
        try:
            error_popup_close_button = WebDriverWait(context.driver, 19).until(
                EC.presence_of_element_located((By.XPATH, "//button[@class='kb-button with-bordered']")))
            if error_popup_close_button:
                assert True
                myLogger.info("*****Expected Error Popup Message Displayed")
                Utilities.excelUtils.writeData(data_sheet_path, "Corporate_Invalid", r, 4, "Test Passed")
                context.driver.save_screenshot(".\\Screenshots\\" + "IncorrectCorporateDataForTPWD_Passed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Error Message for Incorrect Username/Registration Number Displayed",
                              attachment_type=AttachmentType.PNG)
                error_popup_close_button.click()
                username_text_button = WebDriverWait(context.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "//div[@class='ant-form-item-control-input-content']/input[@id='customerAuthForm_loginUserId']")))


                corporate_customer_page.clearUsername()
                corporate_customer_page.clearRegistrationNumber()
            else:
                assert False
                Utilities.excelUtils.writeData(data_sheet_path, "Corporate_Invalid", r, 4, "Test Failed")
                context.driver.save_screenshot(".\\Screenshots\\" + "IncorrectCorporateDataForTPWD_Failed.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Error Message for Incorrect Username/Registration Number Not Displayed",
                              attachment_type=AttachmentType.PNG)

        except Exception as e:
            myLogger.exception(e)
            context.driver.close()
            myLogger.info("*****Unable to enter invalid username and registration number for Corporate Customer*****")



