from test_project.business_layer.windows.commonAction import commonAction
from test_project.business_layer.windows.loginWindow import loginWindow
from test_project.business_layer.windows.closedChecksWindow import closedChecksWindow
from test_project.business_layer.windows.informationAndToolsWindow import informationAndToolsWindow
import log_file
from behave import *

logging = log_file.get_logs()


@step(u'the user should be able to see the "{locator}" button in "{windowType}"')
def step_impl(context, locator, windowType):
    commonAction().isButtonDisplayed(locator, windowType)

@step(u'the user should be able to see the version of the application')
def step_impl(context):
    loginWindow().getAppVersion()

@step(u'the application version displayed in the "Search Closed Checks" window should match the version retrieved from the "LogIn" window')
def step_impl(context):
    closedChecksWindow().verifyAppVersion("Search Closed Checks")

@step(u'the application version displayed in the "Information and Tools" window should match the version retrieved from the "LogIn" window')
def step_impl(context):
    closedChecksWindow().verifyAppVersion("Information and Tools")

@step(u'the software version displayed in the "Terminal Configuration" should match the version retrieved from the "LogIn" window')
def step_impl(context):
    informationAndToolsWindow().verifySoftwareVersion()
