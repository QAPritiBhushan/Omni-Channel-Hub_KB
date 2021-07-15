
from behave import *
from PageObjects.login import Login


@when(u'I enter the valid credentials')
def step_impl(context):
    global login_page
    login_page = Login(context.driver)
    login_page.setUserName("infura1")
    login_page.setpassword("infura12#")




