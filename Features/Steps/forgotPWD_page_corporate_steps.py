import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.mongolianCustomerPassword import MongolianCustomerPassword
from selenium.webdriver.common.by import By
from Utilities.customLogger import LogGen

myLogger = LogGen.logGen()

@when(u'I click on the Click here link for Corporate Customer')
def click_corporate_customer_link(context):
    global mongolian_customer_page
    mongolian_customer_page = MongolianCustomerPassword(context.driver)
    try:
        mongolian_customer_page.clickOnCorporateCustomer()
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to Click on the Forgot Password link for Corporate Customer*****")


@then(u'I should be displayed with the Forgot password page for Corporate Customer')
def display_forgotPWD_corporate_customer(context):
    try:
        username_element = WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.ID,"customerAuthForm_loginUserId")))
        if username_element:
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "CorporateCustomerPWDPage.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Khan Bank in Corporate Domain - Forgot Password Page Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Forgot Password Page for a Corporate Customer is displayed*****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "CorporateCustomerPWDPageNotDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Khan Bank in Corporate Domain - Forgot Password Page Not Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Forgot Password Page for a Corporate Customer is not displayed*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to verify the presence of username element*****")


@then(u'I click on the Click here link for Corporate Customer')
def click_corporate_customer_link(context):
    global mongolian_customer_page
    mongolian_customer_page = MongolianCustomerPassword(context.driver)
    try:
        mongolian_customer_page.clickOnCorporateCustomer()
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to Click on the Forgot Password link for Corporate Customer*****")



