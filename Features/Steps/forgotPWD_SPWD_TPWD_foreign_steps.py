import time

import allure
from allure_commons.types import AttachmentType
from behave import *
from PageObjects.recoverPassword import RecoverPassword
from PageObjects.otpConfirmationPage import OTPConfirmation
from PageObjects.foreignCustomerPassword import ForeignCustomerPassword
from Utilities.constants import Constants
from Utilities.customLogger import LogGen

myLogger = LogGen.logGen()

@when(u'I enter username and passport number')
def step_impl(context):
    global foreign_customer_page
    foreign_customer_page = ForeignCustomerPassword(context.driver)
    foreign_customer_page.setUsername("19810923")
    foreign_customer_page.setPassportNumber("CHN4567890123456")