from behave import *
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType
from PageObjects.mongolianCustomerPassword import MongolianCustomerPassword
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.customLogger import LogGen


myLogger = LogGen.logGen()

@when(u'I click on the Click here link for Foreign Customer')
def step_impl(context):
    global mongolian_password_page
    mongolian_password_page = MongolianCustomerPassword(context.driver)
    try:
        mongolian_password_page.clickOnForeignCustomer()

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to click on 'Click Here' link for Foreign Customer")

@then(u'I click on the Click here link for Foreign Customer')
def step_impl(context):
    global mongolian_password_page
    mongolian_password_page = MongolianCustomerPassword(context.driver)
    try:
        mongolian_password_page.clickOnForeignCustomer()

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to click on 'Click Here' link for Foreign Customer")


@then(u'I should be displayed with the Forgot password page for Foreign Customer')
def step_impl(context):
    try:
        passport_number_element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='ant-col ant-col-22']/input[@class='ant-input']")))
        assert True
        context.driver.save_screenshot(".\\Screenshots\\" + "ForeignCustomerPWDPage.png")
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="Khan Bank Foreign Customer Forgot Password Page Displayed",
                      attachment_type=AttachmentType.PNG)
        myLogger.info("*****Expected Element Passport Number Field Found*****")

    except:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Expected Element Passport Number Field Not Found*****")
