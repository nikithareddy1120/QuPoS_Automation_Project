from test_project.business_layer.windows.commonAction import commonAction
from test_project.business_layer.windows.orderWindow import orderWindow
import log_file
from config.config_reader import config
from core_layer.driver_manager.driver_factory import DriverFactory
from behave import *

logging = log_file.get_logs()
framework_type = config.get_framework_type()
driver, locators = DriverFactory.create_driver(framework_type)

@step('the user clicks on the "{locator}" button in "{windowType}" and get small Amount of Sides')
def step_impl(context, locator, windowType):
    commonAction().clickButton("Drinks", "orderWindow")
    commonAction().clickButton("HOT COFFEE", "orderWindow")
    commonAction().clickButton(locator, windowType)
    orderWindow().getSmallAmountPriceOfDrinksOrSides(locators['orderWindow']['autoIdOfFrenchFries'], locators['orderWindow']['FRENCH FRIES'])

@step('the upCharge for large french Fries should be added to the total amount, and the item should be displayed in the cart view')
def step_impl(context):
    orderWindow().verifyUpChargeAmount("FRENCH FRIES, Large", locators['orderWindow']['autoIdOfLargeFrenchFries'], locators['orderWindow']['Large'])

@step('no upCharge for sides should be added to the total amount, and the item should be displayed in the cart view')
def step_impl(context):
    orderWindow().verifyNoChargeAmountAdded("1 JUMBO EGG ROLL")
    orderWindow().verifyAmountOfTheItem()

@step('the user clicks on the "{locator}" in Sides button in "{windowType}"')
def step_impl(context, locator, windowType):
    orderWindow().shrinkExpandedMenu(locators['orderWindow']['shrinkEGGROLL'])
    commonAction().clickButton(locator, windowType)

@step('the upCharge for 3 EGG ROLLS should be added to the total amount, and the item should be displayed in the cart view')
def step_impl(context):
    orderWindow().verifyUpChargeAmount("3 EGG ROLLS", locators['orderWindow']['autoIdOfThreeEggRolls'], locators['orderWindow']['3 EGG ROLLS'])