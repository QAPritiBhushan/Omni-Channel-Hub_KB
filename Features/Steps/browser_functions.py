from behave import *
from selenium import webdriver
from Utilities.customLogger import LogGen

myLogger = LogGen.logGen()

@given(u'I initiate the Microsoft Edge Browser')
def initiate_edge(context):
    context.driver = webdriver.Edge(executable_path=".\\Drivers\\Edge\\msedgedriver.exe")
    myLogger.info("*****Microsoft Driver Initialized*****")


@given(u'I initiate the Google Chrome Browser')
def initiate_chrome(context):
    context.driver = webdriver.Chrome(executable_path=".\\Drivers\\Chrome\\chromedriver.exe")
    myLogger.info("*****Google Chrome Driver Initialized*****")


@given(u'I initiate the Mozilla Firefox Browser')
def initiate_firefox(context):
    context.driver = webdriver.Firefox(executable_path=".\\Drivers\\Gecko\\geckodriver.exe")
    myLogger.info("*****Mozilla FIrefox Driver Initialized*****")


@given(u'I initiate the IE Browser')
def initiate_ie(context):
    context.driver = webdriver.Ie(executable_path=".\\Drivers\\IE\\IEDriverServer.exe")
    myLogger.info("*****IE Driver Initialized*****")


@then(u'I close the browser')
def close_browser(context):
    context.driver.close()


@given(u'I close the browser')
def close_browser(context):
    context.driver.close()
