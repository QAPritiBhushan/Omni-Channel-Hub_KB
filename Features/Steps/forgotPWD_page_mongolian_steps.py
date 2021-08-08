import time
import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObjects.selectPassword import SelectPwd
from PageObjects.mongolianCustomerPassword import MongolianCustomerPassword
from Utilities.constants import Constants
from Utilities.customLogger import LogGen

myLogger = LogGen.logGen()



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

