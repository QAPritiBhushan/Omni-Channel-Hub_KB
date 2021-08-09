import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.signUpPage import Signup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from PageObjects.login import Login
from Utilities.constants import Constants
from Utilities.customLogger import LogGen
from selenium.webdriver.firefox.options import Options

myLogger = LogGen.logGen()

@given(u'I launch the Khan Bank Corporate application in Firefox')
def step_impl(context):
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
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank CORPORATE LoginPage Displayed ",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Homepage title matches****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank CORPORATE LoginPage Not Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Homepage title does not match*****")
    except:
        myLogger.info("*****Unable to launch the application")

@given(u'I launch the Khan Bank Retail application in Firefox')
def Firefox(context):
    option1 = Options()
    option1.add_argument("--disable-notifications")

    #context.driver = webdriver.Firefox()
    myLogger.info("*****Driver Initialized*****")
    #easygui.msgbox("loginFirefox")
    global login_page
    login_page = Login(context.driver)

    try:
        context.driver.get(Constants.RETAIL_URL)
        context.driver.maximize_window()
        login_page.clearDomain()
        login_page.setRetailDomain()
        login_page.clickOnDomainButton()
        #login_page.refreshPage()
        #easygui.msgbox("loginFirefoxDomain")

        if context.driver.title == Constants.RETAIL_HOMEPAGE_TITLE:
            assert True
            context.driver.save_screenshot(".\\Screenshots\\"+"LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank LoginPage",attachment_type = AttachmentType.PNG)
            myLogger.info("*****Homepage title matches*****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank LoginPage",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Homepage title does not match*****")
    except:
        myLogger.info("*****Unable to launch the application")


@given(u'I launch the Khan Bank Retail application in Chrome')
def Chrome(context):

    #context.driver = webdriver.Chrome()
    myLogger.info("*****Driver Initialized*****")
    #easygui.msgbox("loginFirefox")
    global login_page
    login_page = Login(context.driver)

    try:
        context.driver.get(Constants.RETAIL_URL)
        context.driver.maximize_window()
        login_page.clearDomain()
        login_page.setRetailDomain()
        login_page.clickOnDomainButton()
        #login_page.refreshPage()
        #easygui.msgbox("loginFirefoxDomain")

        if context.driver.title == Constants.RETAIL_HOMEPAGE_TITLE:
            assert True
            context.driver.save_screenshot(".\\Screenshots\\"+"LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank LoginPage",attachment_type = AttachmentType.PNG)
            myLogger.info("*****Homepage title matches*****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank LoginPage",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Homepage title does not match*****")
    except:
        myLogger.info("*****Unable to launch the application")


@when(u'I select dropdown Values for Firefox')
def Validvaluesdropdown(context):
    global signup_page
    signup_page = Signup(context.driver)
    signup_page.MyDropwon()

@when('I Click on SignUp link in Firefox')
def Signup1(context):
    global login_page
    login_page = Login(context.driver)


    try:
        login_page.clickOnSignupLink()
        login_password_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//input[@id='email']")))
        assert True
        context.driver.save_screenshot(".\\Screenshots\\" + "ClickSignupPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank SignUp Page",
                      attachment_type=AttachmentType.PNG)
        myLogger.info("*****Expected Element for sign up page Found*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Expected Element for sign up page Not Found******")


@when('I Click on SignUp link in Chrome')
def Signup1(context):
    global login_page
    login_page = Login(context.driver)


    try:
        login_page.clickOnSignupLink()
        login_password_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//input[@id='email']")))
        assert True
        context.driver.save_screenshot(".\\Screenshots\\" + "ClickSignupPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank SignUp Page",
                      attachment_type=AttachmentType.PNG)
        myLogger.info("*****Expected Element for sign up page Found*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Expected Element for sign up page Not Found******")
