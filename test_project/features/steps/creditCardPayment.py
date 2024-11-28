from test_project.business_layer.windows.paymentWindow import paymentWindow
import log_file
from config.config_reader import config
from core_layer.driver_manager.driver_factory import DriverFactory
from behave import *

logging = log_file.get_logs()
framework_type = config.get_framework_type()
driver, locators = DriverFactory.create_driver(framework_type)

breakfastEntreeItem_config = config.get_breakfastEntreeItem_config()


# @step(u'the user adds an item to the order with ')
# def step_impl(context):
#     orderWindow().addBreakfastEntreeItemToCart(breakfastEntreeItem_config['breakfastLocator'], breakfastEntreeItem_config['breakfastEntreeItem'], breakfastEntreeItem_config['autoIdOfBreakfastEntreeItem'])
#     orderWindow().addEntreeItemToCart()
#
# @step(u'the user should be able to see the cart view, subtotal, tax, total on the left side of the screen')
# def step_impl(context):
#     orderWindow().verifyBreakfastEntreeItemInCart(breakfastEntreeItem_config['breakfastEntreeItemCartView'])
#     orderWindow().verifyAmountOfTheItem()
#
# @step(u'the user clicks on the "Payment" button')
# def step_impl(context):
#     orderWindow().clickPaymentButton()
#
# @step(u'the "ROUND UP DONATION" pop-up should be displayed')
# def step_impl(context):
#     orderWindow().verifyRoundUpDonationPopup()
#
# @step(u'the user clicks on the "NO THANKS" button')
# def step_impl(context):
#     orderWindow().clickNoThanksButton()
#
# @step(u'the "Offline Credit" payment method should be displayed')
# def step_impl(context):
#     paymentWindow().verifyOfflineCreditPaymentMethod()
#
# @step(u'the "Check Total" amount should match the total amount displayed in the cart')
# def step_impl(context):
#     paymentWindow().verifyCheckTotalAmount()
#
# @step(u'the user clicks on the "Offline Credit" button')
# def step_impl(context):
#     paymentWindow().clickOfflineCreditPaymentmethod()
#
# @step(u'the "Due" amount should match the total amount of the item')
# def step_impl(context):
#     paymentWindow().verifyDueAmount()
#
# @step(u'the user clicks on the "Apply Payment" button')
# def step_impl(context):
#     paymentWindow().clickApplyPaymentForOfflineCreditPaymentMethod()

@step(u'the "Due" amount for Offline Credit Card Payment should match the "Total" amount of the items in the cart')
def step_impl(context):
    paymentWindow().verifyDueAmount(locators['paymentWindow']['dueAmountOfflineCredit'])

@step(u'the "Apply Payment" confirmation pop-up and the text "Apply & <Due amount> payment + $0.00 tip, and close check?" should be displayed')
def step_impl(context):
    paymentWindow().verifyApplyPaymentConfirmationPopup()

