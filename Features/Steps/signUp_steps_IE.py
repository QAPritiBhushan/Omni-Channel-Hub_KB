import time
import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.login import Login
from PageObjects.selectPassword import SelectPwd
from PageObjects.signUpPage import Signup
from PageObjects.mongolianCustomerPassword import MongolianCustomerPassword
from Utilities.constants import Constants
from Utilities.customLogger import LogGen
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
import easygui
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import *
from selenium.webdriver.common.by import By
from PageObjects.login import Login
from PageObjects.selectPassword import SelectPwd
from PageObjects.mongolianCustomerPassword import MongolianCustomerPassword
from Utilities.constants import Constants
from Utilities.customLogger import LogGen
from selenium.webdriver.firefox.options import Options
import Utilities.excelUtils
from selenium.common.exceptions import *

myLogger = LogGen.logGen()

@given(u'I Launch the Khan Bank Retail application in IE')
def step_impl(context):
    #context.driver = webdriver.Ie()
    myLogger.info("*****Driver Initialized*****")
    global login_page
    login_page = Login(context.driver)
    try:

        context.driver.get(Constants.RETAIL_URL)
        context.driver.maximize_window()
        login_page.clearDomain()
        login_page.setRetailDomain()
        login_page.clickOnDomainButton()
        time.sleep(3)
        if context.driver.title == Constants.RETAIL_HOMEPAGE_TITLE:
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Retail LoginPage Displayed ",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Homepage title matches****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Retail LoginPage Not Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Homepage title does not match*****")
    except:
        myLogger.info("*****Unable to launch the application")

@when('I Click on Language Link in IE')
def Clicklanguage(context):
    global signup_page
    #time.sleep(8)
    signup_page = Signup(context.driver)
    try:
        signup_page.ClickonLanguageLink()
        login_password_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//a[@href='/auth/signup/step/1']")))
        assert True
        if(context.driver.find_element(By.XPATH,"//a[normalize-space()='Sign Up']").is_displayed):
            context.driver.save_screenshot(".\\Screenshots\\" + "EnglishLanguagePage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank SignUp Page is in English Language",
                       attachment_type=AttachmentType.PNG)
            myLogger.info("*****Expected Element for sign up page Found in English Language*****")
        else:
            myLogger.info("*****Expected Element for sign up page Not Found in English Language*****")

    except Exception as e:
        myLogger.exception(e)
        #context.driver.close()
        myLogger.info("*****Expected Element for sign up page Not Found in English Language******")


@given(u'I Launch the Khan Bank Corporate application in IE')
def step_impl(context):
    #context.driver = webdriver.Ie()
    myLogger.info("*****Driver Initialized*****")
    global login_page
    login_page = Login(context.driver)
    try:

        context.driver.get(Constants.CORPORATE_URL)
        context.driver.maximize_window()
        login_page.clearDomain()
        login_page.setCorporateDomain()
        login_page.clickOnDomainButton()
        time.sleep(3)
        if context.driver.title == Constants.CORPORATE_HOMEPAGE_TITLE:
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Retail LoginPage Displayed ",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Homepage title matches****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Retail LoginPage Not Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Homepage title does not match*****")
    except:
        myLogger.info("*****Unable to launch the application")


@when('I Click on SignUp link in IE')
def Signup1(context):
    global login_page
    login_page = Login(context.driver)

    try:
        login_page.clickOnSignupLink()
        login_password_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//input[@id='email']")))
        assert True
        context.driver.save_screenshot(".\\Screenshots\\" + "SelectPasswordPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank SignUp Page",
                      attachment_type=AttachmentType.PNG)
        myLogger.info("*****Expected Element for sign up page Found*****")

    except Exception as e:
        myLogger.exception(e)
       # context.driver.close()
        myLogger.info("*****Expected Element for sign up page Not Found******")

@when(u'I Select dropdown Values for IE')
def Validvaluesdropdown(context):
    global signup_page
    signup_page = Signup(context.driver)
    signup_page.MyDropwonForIE()

@when(u'I Enter Input fields For signUp In IE')
def EnterFieldsIE(context):
    global login_page
    login_page = Login(context.driver)
    global signup_page
    signup_page = Signup(context.driver)
    data_sheet_path = "C:\\khanbank\\DataSheet.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Datasheet_Signup1")

    for r in range(3, rows + 1):
        #signup_page.MyDropwon()
        Reg_number = Utilities.excelUtils.readData(data_sheet_path,"Datasheet_Signup1",r ,1)
        Emailid = Utilities.excelUtils.readData(data_sheet_path,"Datasheet_Signup1",r,2)
        Phone_number = Utilities.excelUtils.readData(data_sheet_path,"Datasheet_Signup1",r,3)
        signup_page.enterReg_number(Reg_number)
        signup_page.enterEmailid(Emailid)
        signup_page.enterPhone_number(Phone_number)
        signup_page.clickOn_ContinueButton()
        time.sleep(8)
        try:
            ErrorMessage = context.driver.find_element(By.XPATH, "//div[@role='alert']").text
            if (ErrorMessage == "Enter registration number"):
                myLogger.info("Enter registration number")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup1", r, 5, "Test passes")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup1", r, 4, ErrorMessage)
            elif (ErrorMessage == "Регистрийн дугаар оруулна уу"):
                myLogger.info("Регистрийн дугаар оруулна уу")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup1", r, 5, "Test passes")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup1", r, 4, ErrorMessage)
            elif (ErrorMessage == "Please enter the valid mobile number"):
                myLogger.info("Please enter the valid mobile number")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup1", r, 5, "Test passes")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup1", r, 4, ErrorMessage)
            elif (ErrorMessage == "Ашиглаж буй утасны дугаараа оруулна уу"):
                myLogger.info("Ашиглаж буй утасны дугаараа оруулна уу")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup1", r, 5, "Test passes")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup1", r, 4, ErrorMessage)

        except:
            easygui.msgbox("exIE")
            error_popup_close_button = WebDriverWait(context.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@class='kb-button with-bordered']")))
            error_popup_close_button.click()
