from test_project.business_layer.windows.paymentWindow import paymentWindow
import log_file
from config.config_reader import config
from core_layer.driver_manager.driver_factory import DriverFactory
from behave import *

logging = log_file.get_logs()
framework_type = config.get_framework_type()
driver, locators = DriverFactory.create_driver(framework_type)

@step(u'the "Due" amount for Offline Credit Card Payment should match the "Total" amount of the items in the cart')
def step_impl(context):
    paymentWindow().verifyDueAmount(locators['paymentWindow']['dueAmountOfflineCredit'])

@step(u'the "Apply Payment" confirmation pop-up and the text "Apply & <Due amount> payment + $0.00 tip, and close check?" should be displayed')
def step_impl(context):
    paymentWindow().verifyApplyPaymentConfirmationPopup()

