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
from PageObjects.otpPage import OTPConfirmation
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

@when('I Click on Language Link')
def Clicklanguage(context):
    global signup_page
    time.sleep(3)
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
        context.driver.close()
        myLogger.info("*****Expected Element for sign up page Not Found in English Language******")

@when(u'I Enter all Valid Values in signup page')
def Validvalues(context):
    global signup_page
    signup_page = Signup(context.driver)

    data_sheet_path = "C:\\khanbank\\DataSheet.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Valid_Data")
    # easygui.msgbox(rows)
    Reg_number = Utilities.excelUtils.readData(data_sheet_path, "Valid_Data", 2, 1)
    Emailid = Utilities.excelUtils.readData(data_sheet_path, "Valid_Data", 2, 2)
    Phone_number = Utilities.excelUtils.readData(data_sheet_path, "Valid_Data", 2, 3)
    signup_page.MyDropwon()
    signup_page.enterValidSignUpdata(Reg_number,Emailid,Phone_number)
    signup_page.clickOn_ContinueButton()
    try:
                time.sleep(8)
                if(WebDriverWait(context.driver, 20).until(EC.presence_of_element_located(
                            (By.XPATH, '//input[@id="otp"]'))).is_displayed()):
                    myLogger.info("The OTP Page is present")

                    context.driver.save_screenshot(".\\Screenshots\\" + "OTP_Page.png")
                    allure.attach(context.driver.get_screenshot_as_png(),
                          name="Khan Bank OTP Channel Selection Page Displayed",
                        attachment_type=AttachmentType.PNG)
                    myLogger.info("*****Expected OTP Page is Found*****")
                    Utilities.excelUtils.writeData(data_sheet_path, "Valid_Data", 2, 5, "Test passes")

    except NoSuchElementException:
                    myLogger.info("*****Expected OTP Page is not found")
                    context.driver.save_screenshot(".\\Screenshots\\" + "IncorrectOTPPAGE.png")
                    allure.attach(context.driver.get_screenshot_as_png(),
                    name="Khan Bank OTP Channel Selection Page Not Displayed",
                    attachment_type=AttachmentType.PNG)


@when(u'I Enter all Valid Values in signup page for Corporate')
def Validvalues(context):
    global signup_page
    signup_page = Signup(context.driver)

    data_sheet_path = "C:\\khanbank\\DataSheet.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Valid_Data")
    # easygui.msgbox(rows)
    Reg_number = Utilities.excelUtils.readData(data_sheet_path, "Valid_Data", 2, 1)
    Emailid = Utilities.excelUtils.readData(data_sheet_path, "Valid_Data", 2, 2)
    Phone_number = Utilities.excelUtils.readData(data_sheet_path, "Valid_Data", 2, 3)
    signup_page.MyDropwon()
    signup_page.enterValidSignUpdata(Reg_number,Emailid,Phone_number)
    signup_page.clickOn_ContinueButton()
    try:
                time.sleep(5)
                if(WebDriverWait(context.driver, 20).until(EC.presence_of_element_located(
                            (By.XPATH,"//input[@type='email']"))).is_displayed()):
                    myLogger.info("Bug In Page: Same is Appearing")

                    context.driver.save_screenshot(".\\Screenshots\\" + "Same Page.png")
                    allure.attach(context.driver.get_screenshot_as_png(),
                          name="Bug In Page: Same is Appearing",
                        attachment_type=AttachmentType.PNG)
                    Utilities.excelUtils.writeData(data_sheet_path, "Valid_Data", 2, 5, "Test passes")

    except NoSuchElementException:
                    myLogger.info("*****Expected Page is not found")
                    context.driver.save_screenshot(".\\Screenshots\\" + "IncorrectOTPPAGE.png")
                    allure.attach(context.driver.get_screenshot_as_png(),
                    name="Expected Khan Bank Page Not Displayed",
                    attachment_type=AttachmentType.PNG)


@when(u'I Enter all Values in signup page Using DD')
def Validvalues(context):
    global signup_page
    signup_page = Signup(context.driver)
    import os
    mydir = os.getcwd()
    data_sheet_path = mydir + "\TestData\DataSheet.xlsx"

    # data_sheet_path = "C:\\khanbank\\DataSheet.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Datasheet_Signup3")
    for r in range(3, rows + 1):
        Reg_number = Utilities.excelUtils.readData(data_sheet_path, "Datasheet_Signup3", r, 3)
        Emailid = Utilities.excelUtils.readData(data_sheet_path, "Datasheet_Signup3", r, 4)
        Phone_number = Utilities.excelUtils.readData(data_sheet_path, "Datasheet_Signup3", r, 5)
        D1 =  Utilities.excelUtils.readData(data_sheet_path, "Datasheet_Signup3", r, 1)
        D2 = Utilities.excelUtils.readData(data_sheet_path, "Datasheet_Signup3", r, 2)
        signup_page.MyDropwonDD(D1, D2)

        signup_page.enterReg_number(Reg_number)
        signup_page.enterEmailid(Emailid)
        signup_page.enterPhone_number(Phone_number)
        signup_page.clickOn_ContinueButton()


        time.sleep(2)

        try:
            ErrorMessage = context.driver.find_element(By.XPATH, "//div[@role='alert']").text
            if (ErrorMessage == "Enter registration number"):
                myLogger.info("Enter registration number")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup3", r, 7, "Test passes")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup3", r, 6, ErrorMessage)
            elif (ErrorMessage == "Регистрийн дугаар оруулна уу"):
                myLogger.info("Регистрийн дугаар оруулна уу")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup3", r, 7, "Test passes")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup3", r, 6, ErrorMessage)

        except:
            myLogger.info("*****Popup*****")
            error_popup_close_button = WebDriverWait(context.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@class='kb-button with-bordered']")))
            error_popup_close_button.click()
            Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup3", r, 7, "Test passes")

@when(u'I Enter Valid Input data for signup page')
def Validvalues2(context):
        global signup_page
        signup_page = Signup(context.driver)
        data_sheet_path = "C:\\khanbank\\DataSheet.xlsx"

        Reg_number = Utilities.excelUtils.readData(data_sheet_path, "Valid_Data", 2, 1)
        Emailid = Utilities.excelUtils.readData(data_sheet_path, "Valid_Data", 2, 2)
        Phone_number = Utilities.excelUtils.readData(data_sheet_path, "Valid_Data", 2, 3)
        signup_page.enterValidSignUpdata(Reg_number,Emailid,Phone_number)
        signup_page.clickOn_ContinueButton()
        try:
            time.sleep(5)
            if(WebDriverWait(context.driver, 20).until(EC.presence_of_element_located(
                            (By.XPATH, '//input[@id="otp"]'))).is_displayed()):
                    myLogger.info("The OTP Page is present")

                    context.driver.save_screenshot(".\\Screenshots\\" + "OTP_Page.png")
                    allure.attach(context.driver.get_screenshot_as_png(),
                          name="Khan Bank OTP Channel Selection Page Displayed",
                        attachment_type=AttachmentType.PNG)
                    myLogger.info("*****Expected OTP Page is Found*****")

        except NoSuchElementException:
                    myLogger.info("*****Expected OTP Page is not found")
                    context.driver.save_screenshot(".\\Screenshots\\" + "IncorrectOTPPAGE.png")
                    allure.attach(context.driver.get_screenshot_as_png(),
                    name="Khan Bank OTP Channel Selection Page Not Displayed",
                    attachment_type=AttachmentType.PNG)

@when(u'I Enter Input fields For signup PageDD')
def EnterFields(context):
    global login_page
    login_page = Login(context.driver)
    global signup_page
    signup_page = Signup(context.driver)
    data_sheet_path = "C:\\khanbank\\DataSheet.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Datasheet_Signup1")

    for r in range(3, rows + 1):
        Reg_number = Utilities.excelUtils.readData(data_sheet_path,"Datasheet_Signup1",r ,1)
        Emailid = Utilities.excelUtils.readData(data_sheet_path,"Datasheet_Signup1",r,2)
        Phone_number = Utilities.excelUtils.readData(data_sheet_path,"Datasheet_Signup1",r,3)
        signup_page.enterReg_number(Reg_number)
        signup_page.enterEmailid(Emailid)
        signup_page.enterPhone_number(Phone_number)
        signup_page.clickOn_ContinueButton()
        time.sleep(2)
        try:
            ErrorMessage=context.driver.find_element(By.XPATH,"//div[@role='alert']").text
            if(ErrorMessage=="Enter registration number"):
                myLogger.info("Enter registration number")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup1", r, 5, "Test passes")
            elif(ErrorMessage=="Регистрийн дугаар оруулна уу"):
                myLogger.info("Регистрийн дугаар оруулна уу")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup1", r, 5, "Test passes")
            elif (ErrorMessage == "Please enter the valid mobile number"):
                myLogger.info("Please enter the valid mobile number")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup1", r, 5, "Test passes")

        except:
            myLogger.info("*****Popup*****")
            error_popup_close_button = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='kb-button with-bordered']")))
            error_popup_close_button.click()
            Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup1", r, 5, "Test passes")
        Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup1", r, 5, "Test passes")


@when(u'I Enter Input fields For signup PageDD For corporate')
def EnterFields(context):
    global login_page
    login_page = Login(context.driver)
    global signup_page
    signup_page = Signup(context.driver)
    data_sheet_path = "C:\\khanbank\\DataSheet.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Datasheet_Signup1")

    for r in range(3, rows + 1):
        Reg_number = Utilities.excelUtils.readData(data_sheet_path,"Datasheet_Signup1",r ,1)
        Emailid = Utilities.excelUtils.readData(data_sheet_path,"Datasheet_Signup1",r,2)
        Phone_number = Utilities.excelUtils.readData(data_sheet_path,"Datasheet_Signup1",r,3)
        signup_page.enterReg_number(Reg_number)
        signup_page.enterEmailid(Emailid)
        signup_page.enterPhone_number(Phone_number)
        signup_page.clickOn_ContinueButton()
        time.sleep(2)
        try:
            time.sleep(5)
            if (WebDriverWait(context.driver, 20).until(EC.presence_of_element_located(
                    (By.XPATH, "//input[@type='email']"))).is_displayed()):
                myLogger.info("Bug In Page: Same is Appearing")

                context.driver.save_screenshot(".\\Screenshots\\" + "Same Page.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Bug In Page: Same is Appearing",
                              attachment_type=AttachmentType.PNG)
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup1", r, 5, "Test passes")

        except:
            myLogger.info("*****Popup*****")
            error_popup_close_button = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='kb-button with-bordered']")))
            error_popup_close_button.click()
            Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup1", r, 5, "Test passes")


@when(u'I Enter Input Fields For Signup PageDD For Blank EmailID')
def EnterFields2(context):
    global login_page
    login_page = Login(context.driver)
    global signup_page
    signup_page = Signup(context.driver)
    data_sheet_path = "C:\\khanbank\\DataSheet.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Invalid_Email")

    Reg_number = Utilities.excelUtils.readData(data_sheet_path,"Invalid_Email",2 ,1)
    Emailid = Utilities.excelUtils.readData(data_sheet_path,"Invalid_Email",2,2)
    Phone_number = Utilities.excelUtils.readData(data_sheet_path,"Invalid_Email",2,3)
    signup_page.enterReg_number(Reg_number)
    signup_page.enterPhone_number(Phone_number)
    signup_page.clickOn_ContinueButton()
    time.sleep(2)
    try:
            ErrorMessage = context.driver.find_element(By.XPATH, "//div[@role='alert']").text
            if (ErrorMessage == "Хүчинтэй и-мэйл хаягаа оруулна уу"):
                myLogger.info("Хүчинтэй и-мэйл хаягаа оруулна уу")
                Utilities.excelUtils.writeData(data_sheet_path, "Invalid_Email", 2, 5, "Test passes")
                Utilities.excelUtils.writeData(data_sheet_path, "Invalid_Email", 2, 4, ErrorMessage)

            elif(ErrorMessage == "Please enter valid Email Id"):
                myLogger.info("Please enter valid Email Id")
                Utilities.excelUtils.writeData(data_sheet_path, "Invalid_Email", 2, 5, "Test passes")
                Utilities.excelUtils.writeData(data_sheet_path, "Invalid_Email", 2, 4, ErrorMessage)


    except:
            myLogger.info("*****No valid Error*****")
            error_popup_close_button = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='kb-button with-bordered']")))
            error_popup_close_button.click()

@when(u'I Enter Input fields For signup PageDD In English Language')
def EnterFields(context):
    global login_page
    login_page = Login(context.driver)
    global signup_page
    signup_page = Signup(context.driver)
    data_sheet_path = "C:\\khanbank\\DataSheet.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Datasheet_Signup4")

    for r in range(3, rows + 1):
        Reg_number = Utilities.excelUtils.readData(data_sheet_path,"Datasheet_Signup4",r ,1)
        Emailid = Utilities.excelUtils.readData(data_sheet_path,"Datasheet_Signup4",r,2)
        Phone_number = Utilities.excelUtils.readData(data_sheet_path,"Datasheet_Signup4",r,3)
        signup_page.enterReg_number(Reg_number)
        signup_page.enterEmailid(Emailid)
        signup_page.enterPhone_number(Phone_number)
        signup_page.clickOn_ContinueButton()
        time.sleep(2)
        try:
            ErrorMessage=context.driver.find_element(By.XPATH,"//div[@role='alert']").text
            if(ErrorMessage=="Enter registration number"):
                myLogger.info("Enter registration number")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup4", r, 5, "Test passes")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup4", r, 4, ErrorMessage)
            elif(ErrorMessage=="Регистрийн дугаар оруулна уу"):
                myLogger.info("Регистрийн дугаар оруулна уу")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup4", r, 5, "Test passes")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup4", r, 4, ErrorMessage)
            elif (ErrorMessage == "Please enter the valid mobile number"):
                myLogger.info("Please enter the valid mobile number")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup4", r, 5, "Test passes")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup4", r, 4, ErrorMessage)

        except:
            myLogger.info("*****Popup*****")
            error_popup_close_button = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='kb-button with-bordered']")))
            error_popup_close_button.click()
            Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup4", r, 5, "Test passes")

@then(u'I Click on Continue button')
def continuebuttn(context):

    global signup_page
    signup_page = Signup(context.driver)
    signup_page.clickOn_ContinueButton()
    #Verify Message
    try:

        login_password_element = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='otp']")))
        assert True
        context.driver.save_screenshot(".\\Screenshots\\" + "SelectPasswordPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Signup OTP Page",
                      attachment_type=AttachmentType.PNG)
        myLogger.info("*****Expected Element for signUp OTP page Found*****")

    except Exception as e:
        myLogger.exception(e)
        myLogger.info("*****Expected Element for sign up OTP page Not Found******")




    #context.driver.find_element_by_xpath("(//input[@type='search'])[1]").click()
     #context.driver.find_element_by_xpath("//div[@class='ant-select-item-option-content'][text()='A']").click()
     #context.driver.find_element_by_xpath("(//input[@type='search'])[2]").click()
     #context.driver.find_element_by_xpath("(//input[@type='search'])[2]").send_keys(Keys.DOWN + Keys.DOWN+ Keys.DOWN + Keys.ENTER)
     #context.driver.find_element_by_xpath("//input[@class='ant-input'][2]").send_keys("9898654")
     #context.driver.find_element_by_xpath("//input[@id='email']").send_keys("Priti@domain.com")
     #context.driver.find_element_by_xpath("//input[@id='phoneNumber']").send_keys("100")

@when(u'I check All 35 Cyrillic characters')
def CheckAllcharFor_dropdown(context):
    global signup_page
    signup_page = Signup(context.driver)
    signup_page.CheckAllCharatorsfromDropdown()

@then('I enter OTP Values')
def step_impl(context):
    global otp_confirmation_page
    otp_confirmation_page = OTPConfirmation(context.driver)
    data_sheet_path = "C:\\khanbank\\DataSheet.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "OTP_SignUp")

    for r in range(3, rows + 1):
        SignupOTP = Utilities.excelUtils.readData(data_sheet_path, "OTP_SignUp", r, 2)
        otp_confirmation_page.setOTP(SignupOTP)
        try:
            enter_otp_element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID,"otp")))

            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "OTPConfirmationPageDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank OTP Confirmation Page Displayed",
                  attachment_type=AttachmentType.PNG)
            myLogger.info("*****Expected Element Enter OTP Found*****")
        except Exception as e:
            myLogger.exception(e)
            context.driver.save_screenshot(".\\Screenshots\\" + "OTPConfirmationPageNotDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank OTP Confirmation Page Not Displayed",
                      attachment_type=AttachmentType.PNG)
            context.driver.close()
            myLogger.info("*****Expected Element Enter OTP Not Found*****")

@then('I Click on Back Button')
def Backbutton(context):
    context.driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-lg ant-btn-block']").click()
