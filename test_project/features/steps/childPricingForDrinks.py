import json
from test_project.business_layer.windows.commonAction import commonAction
from test_project.business_layer.windows.orderWindow import orderWindow
import log_file
from config.config_reader import config
from core_layer.driver_manager.driver_factory import DriverFactory
from behave import *

logging = log_file.get_logs()
framework_type = config.get_framework_type()
driver, locators = DriverFactory.create_driver(framework_type)

@step(u'get locators')
def step_impl(context):
    orderWindow().getlocator()

@step('the user adds combo item to the order')
def step_impl(context):
    for row in context.table:
        menuOption = json.loads(row['menuOption'])
        itemName = json.loads(row['itemName'])
        comboSize = json.loads(row['comboSize'])
        autoIdOfItem = row['autoIdOfItem']
        orderWindow().addComboItemToCart(menuOption, itemName, comboSize, autoIdOfItem)

@step('the user should be able to see the "{locator}" option in "{windowType}"')
def step_impl(context, locator, windowType):
    commonAction().isTextDisplayed(locator, windowType)

@step('the user clicks on the "{locator}" button in "{windowType}" and get small Amount for drinks')
def step_impl(context, locator, windowType):
    commonAction().clickButton(locator, windowType)
    orderWindow().getSmallAmountPriceOfDrinksOrSides(locators['orderWindow']['autoIdOfFountainDrink'], locators['orderWindow']['FOUNTAIN DRINK'])

@step('no upCharge for drinks should be added to the total amount, and the item should be displayed in the cart view')
def step_impl(context):
    orderWindow().verifyNoChargeAmountAdded('DIET COKE')

@step('the upCharge for drinks should be added to the total amount, and the item should be displayed in the cart view')
def step_impl(context):
    orderWindow().verifyUpChargeAmount("HIGH MOUNTAIN COFFEE, Large", locators['orderWindow']['autoIdOfLargeHotCoffee'], locators['orderWindow']['Large'])
    commonAction().clickButton('Regular', 'orderWindow')
    orderWindow().verifyAmountOfTheItem()

@step('the user clicks on the "{locator}" option in drinks in "{windowType}"')
def step_impl(context, locator, windowType):
    orderWindow().shrinkExpandedMenu(locators['orderWindow']['shrinkFOUNTAINDRINK'])
    commonAction().clickButton(locator, windowType)

