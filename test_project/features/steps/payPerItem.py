import json
from test_project.business_layer.windows.commonAction import commonAction
from test_project.business_layer.windows.loginWindow import loginWindow
from test_project.business_layer.windows.orderWindow import orderWindow
from behave import *
import log_file
from config.config_reader import config
from core_layer.driver_manager.driver_factory import DriverFactory
from test_project.business_layer.windows.paymentWindow import paymentWindow

logging = log_file.get_logs()
framework_type = config.get_framework_type()
driver, locators = DriverFactory.create_driver(framework_type)


@given(u'the user launches the "Qu POS" desktop application')
def step_impl(context):
    loginWindow().launchApp()
    logging.info("Qu POS application has launched successfully")


@step(u'the user enter an employee "ID" on a counter login screen and select "Log In" button')
def step_impl(context):
    loginWindow().enterEmployeeID()
    loginWindow().clickLoginButton()


@step(u'the user selects the "{locator}" in the bottom right corner in "{windowType}"')
def step_impl(context, locator, windowType):
    commonAction().clickButton(locator, windowType)


@step(u'the user should be able to see the "{locator}" button on the top navigation menu of the screen in "{windowType}"')
def step_impl(context, locator, windowType):
    commonAction().isButtonDisplayed(locator, windowType)


@step(u'the user clicks on the "{locator}" button in "{windowType}"')
def step_impl(context, locator, windowType):
    commonAction().clickButton(locator, windowType)


@step(u'the user should be able to see the "{locator}" popup in "{windowType}"')
def step_impl(context, locator, windowType):
    commonAction().isTextDisplayed(locator, windowType)


@step(u'the user select "Claim" on an available till and verify the "Till, Successfully Claimed!" text and "current cash"')
def step_impl(context):
    orderWindow().claimAvailableTill()


@step(u'the user clicks on the "{locator}" button on the till pop-up in "{windowType}"')
def step_impl(context, locator, windowType):
    commonAction().clickButton(locator, windowType)


@step(u'the user should be able to see the "{locator}" dropdown in "{windowType}"')
def step_impl(context, locator, windowType):
    commonAction().isButtonDisplayed(locator, windowType)


@step('the user adds multiple entree items to the order')
def step_impl(context):
    for row in context.table:
        menuOption = json.loads(row['menuOption'])
        itemName = json.loads(row['itemName'])
        autoIdOfItem = row['autoIdOfItem']
        orderWindow().addEntreeItemToCart(menuOption, itemName, autoIdOfItem)

@step(u'each item should display in the cart view on the left side of the screen')
def step_impl(context):
    for row in context.table:
        itemsInCart = json.loads(row['itemsInCart'])
        orderWindow().verify_items_in_cart(itemsInCart)

@step(u'the subtotal, tax, and total should update as each item is added')
def step_impl(context):
    orderWindow().verifyAmountOfTheItem()


@step(u'the user selects the entrée "{locator}" in the cart in "{windowType}"')
def step_impl(context, locator, windowType):
    commonAction().clickButton(locator, windowType)


@step(u'user should see "{locator}" entree is selected in "{windowType}"')
def step_impl(context, locator, windowType):
    commonAction().isTextDisplayed(locator, windowType)


@step(u'the user removes a default modifier "{locator}" by clicking "-" button in "{windowType}"')
def step_impl(context, locator, windowType):
    commonAction().clickButton(locator, windowType)


@step(u'the text "No HAM" should be displayed in the cart in "orderWindow"')
def step_impl(context):
    orderWindow().verifyDefaultModifier()


@step(u'the user adds a free modifier "{locator}" by clicking "+" button in "{windowType}"')
def step_impl(context, locator, windowType):
    commonAction().clickButton(locator, windowType)


@step(u'the text "ADD MAYO" should be displayed in the cart in "orderWindow"')
def step_impl(context):
    orderWindow().verifyFreeModifier()


@step(u'the user adds a priced modifier "{locator}" by clicking on it in "{windowType}"')
def step_impl(context, locator, windowType):
    commonAction().clickButton(locator, windowType)


@step(u'the text "Add JALAPENOS" should be displayed and the total should reflect the additional price of the modifier')
def step_impl(context):
    orderWindow().verifyPricedModifier()

@step(u'the user should be able to see the "{locator}" payment method in "{windowType}"')
def step_impl(context, locator, windowType):
    commonAction().isButtonDisplayed(locator, windowType)

@step(u'the "Total" amount should match the total amount displayed in the cart')
def step_impl(context):
    paymentWindow().verifyCheckTotalAmount()

@step(u'the "Due" amount should match the "Total" amount of the items in the cart')
def step_impl(context):
    paymentWindow().verifyDueAmount(locators['paymentWindow']['dueAmountCash'])

@step(u'the amount of each item in the "Select Check Items to Pay" pop-up should match the amount of the items displayed in the cart')
def step_impl(context):
    for row in context.table:
        itemsInPayPerItemPopup = json.loads(row['itemsInPayPerItemPopup'])
        paymentWindow().getItemPriceInPayPerItemPopup(itemsInPayPerItemPopup)
    paymentWindow().verifyItemPriceInPayPerItemPopup()

@step(u'the user selects the following items in the pop-up, click "OK" button and the total Amount for the selected item should match the due Amount')
def step_impl(context):
    items_locators = [eval(row['itemsInPayPerItemPopup']) for row in context.table]
    paymentWindow().selectItemsForPaymentAndVerifyDueAmount(items_locators)

@step(u'the user selects the following items in the pop-up, click "OK" button')
def step_impl(context):
    items_locators = [eval(row['itemsInPayPerItemPopup']) for row in context.table]
    paymentWindow().selectItemsForPayment(items_locators)

@step(u'the sum of the "Tendered" amount and the "Due" amount should be equal to the "Total" amount')
def step_impl(context):
    paymentWindow().verifySumOfDueAndTenderedAmount()

@step(u'the "Total" amount should be zero and the "No Checks" text should be displayed')
def step_impl(context):
    orderWindow().verifyPaymentSuccessful()

