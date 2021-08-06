from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Utilities.excelUtils
from PageObjects.home import Homepage
from PageObjects.login import Login
from Utilities.customLogger import LogGen
import allure
from allure_commons.types import AttachmentType

myLogger = LogGen.logGen()

@given(u'I enter invalid set of username data to validate the warning message in English')
def step_impl(context):
    data_sheet_path = ".\\TestData\\loginData.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Username_Invalid")
    myLogger.info("The number of rows is ", rows)
    global login_page
    login_page = Login(context.driver)
    for r in range(2, rows + 1):
        try:
            username = Utilities.excelUtils.readData(data_sheet_path, "Username_Invalid", r, 1)
            login_page.setUserName(username)
            allowed_characters_warning = WebDriverWait(context.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='alert'][text()='Allowed characters 0-9, A-Z, a-z . - _']")))
            if context.driver.find_element(By.XPATH,"//div[@role='alert'][text()='Allowed characters 0-9, A-Z, a-z . - _']").text == "Allowed characters 0-9, A-Z, a-z . - _":
                assert True
                Utilities.excelUtils.writeData(data_sheet_path, "Username_Invalid", r, 3, "Test Passed")
                context.driver.save_screenshot(".\\Screenshots\\" + "AllowedCharsForUsernameDisplayed_EN.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Allowed Characters For Username Displayed in English",
                              attachment_type=AttachmentType.PNG)
                login_page.clearUsername()
            else:
                assert False
                Utilities.excelUtils.writeData(data_sheet_path, "Username_Invalid", r, 3, "Test Failed")
                context.driver.save_screenshot(".\\Screenshots\\" + "AllowedCharsForUsernameNotDisplayed_EN.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Allowed Characters For Username Not Displayed in English",
                              attachment_type=AttachmentType.PNG)
        except Exception as e:
            myLogger.exception(e)
            Utilities.excelUtils.writeData(data_sheet_path, "Username_Invalid", r, 3, "Test Failed")
            myLogger.info("*****Unable to validate username with invalid data*****")
            context.driver.close()



@given(u'I enter invalid set of username data to validate the warning message in Mongolian')
def step_impl(context):
    data_sheet_path = ".\\TestData\\loginData.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Username_Invalid")
    myLogger.info("The number of rows is ", rows)
    global login_page
    login_page = Login(context.driver)
    for r in range(2, rows + 1):
        try:
            username = Utilities.excelUtils.readData(data_sheet_path, "Username_Invalid", r, 1)
            login_page.setUserName(username)
            allowed_characters_warning = WebDriverWait(context.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@role='alert'][text()='Нэвтрэх нэр 0-9, A-Z, a-z . - _ тэмдэгтүүдээс бүрдэнэ']")))
            if context.driver.find_element(By.XPATH,
                                           "//div[@role='alert'][text()='Нэвтрэх нэр 0-9, A-Z, a-z . - _ тэмдэгтүүдээс бүрдэнэ']").text == "Нэвтрэх нэр 0-9, A-Z, a-z . - _ тэмдэгтүүдээс бүрдэнэ":
                assert True
                Utilities.excelUtils.writeData(data_sheet_path, "Username_Invalid", r, 2, "Test Passed")
                context.driver.save_screenshot(".\\Screenshots\\" + "AllowedCharsForUsernameDisplayed_MN.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Allowed Characters For Username Displayed in Mongolian",
                              attachment_type=AttachmentType.PNG)
                login_page.clearUsername()
            else:
                assert False
                Utilities.excelUtils.writeData(data_sheet_path, "Username_Invalid", r, 3, "Test Failed")
                context.driver.save_screenshot(".\\Screenshots\\" + "AllowedCharsForUsernameNotDisplayed_MN.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Allowed Characters For Username Not Displayed in Mongolian",
                              attachment_type=AttachmentType.PNG)
        except Exception as e:
            myLogger.exception(e)
            Utilities.excelUtils.writeData(data_sheet_path, "Username_Invalid", r, 2, "Test Failed")
            myLogger.info("*****Unable to validate username with invalid data*****")
            context.driver.close()


@given(u'I enter valid set of credentials to validate login functionality')
def step_impl(context):
    data_sheet_path = ".\\TestData\\loginData.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Login_Valid")
    myLogger.info("The number of rows is ", rows)
    global login_page
    login_page = Login(context.driver)
    username_element = WebDriverWait(context.driver,10).until(EC.presence_of_element_located((By.ID,"username")))

    for r in range(2, rows + 1):
        try:
            username = Utilities.excelUtils.readData(data_sheet_path, "Login_Valid", r, 1)
            password = Utilities.excelUtils.readData(data_sheet_path, "Login_Valid", r, 2)
            login_page.setUserName(username)
            login_page.setpassword(password)
            login_page.clickOnLogin()
            logout_element = WebDriverWait(context.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//li[@class='lo']")))
            if logout_element:
                Utilities.excelUtils.writeData(data_sheet_path, "Login_Valid", r, 3, "Test Passed")
                context.driver.save_screenshot(".\\Screenshots\\" + "LoginSuccessLogoutElementFound.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Logout element found - Login Successful",
                              attachment_type=AttachmentType.PNG)
                logout_element.click()
                yes_popup_element = WebDriverWait(context.driver, 10).until(
                   EC.element_to_be_clickable((By.XPATH, "//button[@class='kb-button']")))
                yes_popup_element.click()
            else:
                assert False
                Utilities.excelUtils.writeData(data_sheet_path, "Login_Valid", r, 3, "Test Failed")
                context.driver.save_screenshot(".\\Screenshots\\" + "LoginFailLogoutElementNotFound.png")
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Logout element not found - Login Failed",
                              attachment_type=AttachmentType.PNG)
        except Exception as e:
            myLogger.exception(e)
            Utilities.excelUtils.writeData(data_sheet_path, "Login_Valid", r, 3, "Test Failed")
            myLogger.info("*****Unable to validate login functionality*****")
            context.driver.close()

@when(u'I enter valid credentials')
def step_impl(context):
    data_sheet_path = ".\\TestData\\loginData.xlsx"
    global login_page
    login_page = Login(context.driver)
    username = Utilities.excelUtils.readData(data_sheet_path, "Login_Valid", 2, 1)
    password = Utilities.excelUtils.readData(data_sheet_path, "Login_Valid", 2, 2)
    try:
        login_page.setUserName(username)
        login_page.setpassword(password)
    except Exception as e:
        myLogger.exception(e)
        myLogger.info("*****Unable to enter valid credentials*****")
        context.driver.close()



@when(u'I check the Remember Me checkbox and login')
def step_impl(context):
    global login_page
    login_page = Login(context.driver)
    try:
        rememberMe_checkbox = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='ant-checkbox-inner']")))
        context.driver.execute_script("arguments[0].click()", rememberMe_checkbox)
        login_page.clickOnLogin()
    except Exception as e:
        myLogger.exception(e)
        myLogger.info("*****Unable to check Remember Me checkbox and login*****")
        context.driver.close()


@then(u'I should be displayed with the home page')
def step_impl(context):
    try:
        logout_element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@class='lo']")))
        if logout_element:
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "LogOutElementFound_HomePageDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Logout element found - Homepage displayed",
                          attachment_type=AttachmentType.PNG)

        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "LogOutElementNotFound_HomePageNotDisplayed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Logout element not found - Homepage not displayed",
                          attachment_type=AttachmentType.PNG)
    except Exception as e:
        myLogger.exception(e)
        myLogger.info("*****Unable to check if user is displayed with home page or not*****")
        context.driver.close()


@when(u'I log out')
def step_impl(context):
    global home_page
    home_page = Homepage(context.driver)
    try:
        Logout_element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@class='lo']//i[@class='icon-powerLine']")))
        home_page.clickOnLogOut()
        #yes_popup_element = WebDriverWait(context.driver, 10).until(
            #EC.element_to_be_clickable((By.XPATH, "//button[@class='kb-button']")))
        #yes_popup_element.click()
        username_element = WebDriverWait(context.driver,20).until(EC.presence_of_element_located((By.ID,"username")))
        if username_element:
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "NavigatedBackToLoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Username element found - Navigated back to Login Page",
                          attachment_type=AttachmentType.PNG)
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "NotNavigatedBackToLoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Username element not found - Not Navigated back to Login Page",
                          attachment_type=AttachmentType.PNG)
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Expected Element Logout Button Not Found******")


@when(u'I click on login button')
def step_impl(context):
    global login_page
    login_page = Login(context.driver)
    try:
        login_page.clickOnLogin()
        myLogger.info("*****Clicked on Login Button******")
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to click on login button*****")






@then(u'username field should display the loginID entered for Mongolian Language')
def step_impl(context):
    data_sheet_path = ".\\TestData\\loginData.xlsx"
    loginID_entered = Utilities.excelUtils.readData(data_sheet_path, "Remember_Me_MN", 2, 1)
    global login_page
    login_page = Login(context.driver)
    try:
        username_element = context.driver.find_element(By.ID, "username")
        loginID_rememberMe = username_element.get_attribute('value')
        if loginID_entered == loginID_rememberMe:
            assert True
            Utilities.excelUtils.writeData(data_sheet_path, "Remember_Me_MN", 2, 2, "Test Passed")
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginIDDisplayedChecked_MN_Passed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Login ID displayed when user checked Remember Me for Mongolian Language",
                          attachment_type=AttachmentType.PNG)
        else:
            assert False
            Utilities.excelUtils.writeData(data_sheet_path, "Remember_Me_MN", 2, 2, "Test Failed")
    except Exception as e:
        myLogger.exception(e)
        myLogger.info("*****Unable to validate username field retaining the loginID entered for Mongolian Language")
        context.driver.close()




@then(u'username field should not display the loginID entered for Mongolian Language')
def step_impl(context):
    data_sheet_path = ".\\TestData\\loginData.xlsx"
    username_element = context.driver.find_element(By.ID,"username")
    loginID_rememberMe = username_element.get_attribute('value')
    try:
        if loginID_rememberMe == "":
            assert True
            Utilities.excelUtils.writeData(data_sheet_path, "Remember_Me_MN", 2, 3, "Test Passed")
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginIDNotDisplayedUnchecked_MN_Passed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Login ID displayed when user checked Remember Me for Mongolian Language",
                          attachment_type=AttachmentType.PNG)
        else:
            assert False
            Utilities.excelUtils.writeData(data_sheet_path, "Remember_Me_MN", 2, 3, "Test Failed")
    except Exception as e:
        myLogger.exception(e)
        myLogger.info("*****Unable to validate username field not retaining the loginID entered for Mongolian Language")
        context.driver.close()







@then(u'username field should display the loginID entered for English Language')
def step_impl(context):
    data_sheet_path = ".\\TestData\\loginData.xlsx"
    loginID_entered = Utilities.excelUtils.readData(data_sheet_path, "Remember_Me_EN", 2, 1)
    global login_page
    login_page = Login(context.driver)
    username_element = context.driver.find_element(By.ID,"username")
    loginID_rememberMe = username_element.get_attribute('value')
    try:
        if loginID_entered == loginID_rememberMe:
            assert True
            Utilities.excelUtils.writeData(data_sheet_path, "Remember_Me_EN", 2, 2, "Test Passed")
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginIDDisplayedChecked_EN_Passed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Login ID displayed when user checked Remember Me for Mongolian Language",
                          attachment_type=AttachmentType.PNG)
        else:
            assert False
            Utilities.excelUtils.writeData(data_sheet_path, "Remember_Me_EN", 2, 2, "Test Failed")
    except Exception as e:
        myLogger.exception(e)
        myLogger.info("*****Unable to validate username field retaining the loginID entered for English Language*****")
        context.driver.close()



@then(u'username field should not display the loginID entered for English Language')
def step_impl(context):
    data_sheet_path = ".\\TestData\\loginData.xlsx"
    username_element = context.driver.find_element(By.ID,"username")
    loginID_rememberMe = username_element.get_attribute('value')
    try:
        if loginID_rememberMe == "":
            assert True
            Utilities.excelUtils.writeData(data_sheet_path, "Remember_Me_EN", 2, 3, "Test Passed")
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginIDNotDisplayedUnchecked_EN_Passed.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Login ID displayed when user checked Remember Me for Mongolian Language",
                          attachment_type=AttachmentType.PNG)
        else:
            assert False
            Utilities.excelUtils.writeData(data_sheet_path, "Remember_Me_EN", 2, 3, "Test Failed")
    except Exception as e:
        myLogger.exception(e)
        myLogger.info("*****Unable to validate username field not retaining the loginID entered for English Language*****")
        context.driver.close()





@given(u'I change to English Language')
def step_impl(context):
    login_page = Login(context.driver)
    try:
        login_page.setLanguage()
        forgotPWD_english_element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/auth/forgotpassword/step/1']")))
    except Exception as e:
        myLogger.exception(e)
        myLogger.info("*****Unable to change to English Language*****")
        context.driver.close()



@when(u'I clear the username')
def step_impl(context):
    try:
        login_page = Login(context.driver)
        login_page.clearUsername()
    except Exception as e:
        myLogger.exception(e)
        myLogger.info("*****Unable to clear the username*****")
        context.driver.close()


@when(u'I clear the password')
def step_impl(context):
    data_sheet_path = ".\\TestData\\loginData.xlsx"
    login_page = Login(context.driver)
    username = Utilities.excelUtils.readData(data_sheet_path, "Login_Valid", 2, 1)
    try:
        login_page.setUserName(username)
        login_page.clearPassword()
    except Exception as e:
        myLogger.exception(e)
        myLogger.info("*****Unable to clear the password*****")
        context.driver.close()


@then(u'I should be displayed with a warning message to enter username in Mongolian')
def step_impl(context):
    try:
        username_warning_message = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Нэвтрэх нэрээ оруулна уу!')]")))
        if context.driver.find_element(By.XPATH,"//div[contains(text(),'Нэвтрэх нэрээ оруулна уу!')]").text == "Нэвтрэх нэрээ оруулна уу!":
            myLogger.info("*****Warning Message to Enter username is displayed")
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginUsernameWarningDisplayed_MN.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Enter Username Warning Message for Login Page displayed",
                          attachment_type=AttachmentType.PNG)
        else:
            assert False
            myLogger.info("*****Warning Message to Enter username is not displayed")
            context.driver.save_screenshot(".\\Screenshots\\" + "NoLoginUsernameWarningDisplayed_MN.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Enter Username Warning Message for Login Page Not Displayed",
                          attachment_type=AttachmentType.PNG)
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to validate the warning message to Enter Username*****")


@then(u'I should be displayed with a warning message to enter password in Mongolian')
def step_impl(context):
    try:
        username_warning_message = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Нууц үгээ оруулна уу!')]")))
        if context.driver.find_element(By.XPATH,
                                       "//div[contains(text(),'Нууц үгээ оруулна уу!')]").text == "Нууц үгээ оруулна уу!":
            myLogger.info("*****Warning Message to Enter password is displayed")
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginPasswordWarningDisplayed_MN.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Khan Bank Enter Password Warning Message for Login Page displayed",
                          attachment_type=AttachmentType.PNG)
        else:
            assert False
            myLogger.info("*****Warning Message to Enter Password is not displayed")
            context.driver.save_screenshot(".\\Screenshots\\" + "NoLoginPasswordWarningDisplayed_MN.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Khan Bank Enter Password Warning Message for Login Page Not Displayed",
                          attachment_type=AttachmentType.PNG)
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to validate the warning message to Enter Password*****")


@then(u'I should be displayed with a warning message to enter username in English')
def step_impl(context):
    try:
        username_warning_message = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Enter username')]")))
        if context.driver.find_element(By.XPATH,"//div[contains(text(),'Enter username')]").text == "Enter username":
            myLogger.info("*****Warning Message to Enter username is displayed")
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginUsernameWarningDisplayed_EN.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Enter Username Warning Message for Login Page displayed",
                          attachment_type=AttachmentType.PNG)
        else:
            assert False
            myLogger.info("*****Warning Message to Enter username is not displayed")
            context.driver.save_screenshot(".\\Screenshots\\" + "NoLoginUsernameWarningDisplayed_EN.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Enter Username Warning Message for Login Page Not Displayed",
                          attachment_type=AttachmentType.PNG)
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to validate the warning message to Enter Username*****")


@then(u'I should be displayed with a warning message to enter password in English')
def step_impl(context):
    try:
        username_warning_message = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Please enter your password')]")))
        if context.driver.find_element(By.XPATH,
                                       "//div[contains(text(),'Please enter your password')]").text == "Please enter your password":
            myLogger.info("*****Warning Message to Enter password is displayed")
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginPasswordWarningDisplayed_EN.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Khan Bank Enter Password Warning Message for Login Page displayed",
                          attachment_type=AttachmentType.PNG)
        else:
            assert False
            myLogger.info("*****Warning Message to Enter Password is not displayed")
            context.driver.save_screenshot(".\\Screenshots\\" + "NoLoginPasswordWarningDisplayed_EN.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Khan Bank Enter Password Warning Message for Login Page Not Displayed",
                          attachment_type=AttachmentType.PNG)
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Unable to validate the warning message to Enter Password*****")



