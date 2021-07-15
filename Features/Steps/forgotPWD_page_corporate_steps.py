import time

import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from PageObjects.login import Login

from Utilities.constants import Constants
from Utilities.customLogger import LogGen

myLogger = LogGen.logGen()

@given(u'I launch the Khan Bank application in Corporate domain')
def step_impl(context):
    context.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    myLogger.info("*****Driver Initialized*****")
    global login_page
    login_page = Login(context.driver)
    try:

        context.driver.get(Constants.CORPORATE_URL)
        context.driver.maximize_window()
        login_page.clearDomain()
        login_page.setCorporateDomain()
        login_page.clickOnDomainButton()
        if context.driver.title == Constants.CORPORATE_HOMEPAGE_TITLE:
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank in Corporate Domain - LoginPage Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Homepage title matches****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank in Corporate Domain - LoginPage Not Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Homepage title does not match*****")
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to launch the application")


