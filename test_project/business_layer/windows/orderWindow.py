from core_layer.utility.assertions import Assertions
from config.config_reader import config
from core_layer.driver_manager.driver_factory import DriverFactory
import log_file
from core_layer.utility.yamlManager import YamlUtilities
from test_project.business_layer.windows.paymentWindow import paymentWindow

logging = log_file.get_logs()
framework_type = config.get_framework_type()
driver, locators = DriverFactory.create_driver(framework_type)
waits_config = config.get_waits_config()
prices= []

class orderWindow:
    def __init__(self):
        self.paymentwindow = paymentWindow()
        self.assertion = Assertions(driver)
        self.yamlmanager = YamlUtilities()

    def claimAvailableTill(self):
        tillAvailability = driver.utilities.waitUntilVisible(driver.app, locators['orderWindow']['reconcileButton'], waits_config['veryShortWait'])
        if tillAvailability:
            logging.info("Till already claimed!")
            self.verifyCurrentCash()
        else:
            driver.utilities.click_button(driver.app, locators['orderWindow']['claimButton'], "Claim button", waits_config['shortWait'])
            self.verifyTillClaimedText()
            self.verifyCurrentCash()
        prices.clear()

    def verifyTillClaimedText(self):
        driver.utilities.is_element_displayed(driver.app, locators['orderWindow']['Till, Successfully Claimed!'], "Till, Successfully Claimed! text", waits_config['veryShortWait'])  #cliamed

    def verifyCurrentCash(self):
        driver.utilities.is_element_displayed(driver.app, locators['orderWindow']['current cash'], "Current cash text", waits_config['veryShortWait']) #current cash

    def addEntreeItemToCart(self, menuOption, itemName, auto_id):
        driver.utilities.click_button(driver.app, menuOption, menuOption, waits_config['shortWait'])
        EntreeItemPrice = driver.utilities.get_item_price(driver.app, auto_id,
                                                                   locators['orderWindow']['breakfastEntreeItem'],
                                                                   "Price of ", waits_config['shortWait'])
        driver.utilities.click_button(driver.app, itemName , itemName, waits_config['veryShortWait'])
        prices.append(EntreeItemPrice)

    def addComboItemToCart(self, menuOption, itemName, comboSize, auto_id):
        driver.utilities.click_button(driver.app, menuOption, menuOption, waits_config['shortWait'])
        driver.utilities.click_button(driver.app, itemName, itemName, waits_config['veryShortWait'])
        priceOfCombo = float(driver.utilities.get_item_price(driver.app, auto_id,
                                                       locators['orderWindow']['breakfastEntreeItem'],
                                                       "price of" + str(itemName) , waits_config['shortWait']))
        driver.utilities.click_button(driver.app, comboSize, comboSize, waits_config['veryShortWait'])
        self.yamlmanager.write_to_yaml_file(yaml_data={"totalAmountOfItemsInCart":priceOfCombo}, filename="totalAmount")
        prices.append(priceOfCombo)

    # def verifyBreakfastEntreeItemInCart(self, itemInCart):
    #     driver.utilities.is_element_displayed(driver.app, itemInCart, "Breakfast Entree item in cart", waits_config['veryShortWait'])

    def verify_items_in_cart(self, itemsInCart):
        driver.utilities.is_element_displayed(driver.app, itemsInCart, itemsInCart, waits_config['shortWait'])

    def verifyUpChargeAmount(self, selectedTItemsextInCart, autoIdOfItem, itemName):
        ItemsInCart = driver.utilities.get_text(driver.app, locators['orderWindow']['upChargeAmountInCart'],
                                                "Items in cart", waits_config['shortWait'])
        self.assertion.assert_contains(ItemsInCart, selectedTItemsextInCart)
        logging.info(str(selectedTItemsextInCart) + " in cart is displayed")
        itemPrice = driver.utilities.get_item_price(driver.app, autoIdOfItem, itemName,
                                                      "Price Of " + str(itemName), waits_config['shortWait'])
        self.yamlmanager.read_from_yaml_file(filename='upChargeAmount')
        smallItemPrice = self.yamlmanager.get_data_from_yaml("smallComboPrice")
        upChargeitemPriceforSelectedCombo = float(itemPrice) - float(smallItemPrice)
        self.yamlmanager.read_from_yaml_file("totalAmount")
        comboPriceOfItem = self.yamlmanager.get_data_from_yaml("totalAmountOfItemsInCart")
        subtotal = float(driver.utilities.get_text(driver.app, locators['orderWindow']['subTotalAmount'], "Subtotal Amount",
                                             waits_config['veryShortWait']))
        upChargeAmountInChart = float(round(subtotal, 1)) - float(round(comboPriceOfItem, 1))
        self.assertion.assert_equal(round(upChargeitemPriceforSelectedCombo , 1), round(upChargeAmountInChart, 1))
        prices.append(upChargeitemPriceforSelectedCombo)
        self.yamlmanager.write_to_yaml_file(yaml_data={'smallComboPrice' : prices}, filename="upChargeAmount")
        logging.info("Up charge amount for the selected item is correctly in the cart")

    def verifyNoChargeAmountAdded(self, ItemNameInCartOfNoCharge):
        upchargeItemsInCart = driver.utilities.get_text(driver.app, locators['orderWindow']['upChargeAmountInCart'],
                                  "No Up charge Items in cart", waits_config['shortWait'])
        self.assertion.assert_contains(upchargeItemsInCart, ItemNameInCartOfNoCharge)
        subtotal = driver.utilities.get_text(driver.app, locators['orderWindow']['subTotalAmount'], "Subtotal Amount",
                                             waits_config['veryShortWait'])
        self.yamlmanager.read_from_yaml_file("totalAmount")
        totalAmountOfItem = self.yamlmanager.get_data_from_yaml('totalAmountOfItemsInCart')
        self.assertion.assert_equal(totalAmountOfItem, subtotal)
        logging.info("No Up charge amount for the selected item is displayed in the cart")

    def getSmallAmountPriceOfDrinksOrSides(self, autoIdOfSmallCombo, itemName):
        smallComboPrice = driver.utilities.get_item_price(driver.app, autoIdOfSmallCombo, itemName , "Price Of " + str(itemName), waits_config['shortWait'])
        self.yamlmanager.write_to_yaml_file(yaml_data={'smallComboPrice' : smallComboPrice}, filename="upChargeAmount")

    def shrinkExpandedMenu(self, titleOfExpandedMenu):
        driver.utilities.click_button(driver.app, titleOfExpandedMenu, str(titleOfExpandedMenu) + " to shrink menu", waits_config['veryShortWait'])

    def verifyAmountOfTheItem(self):
        subtotal = driver.utilities.get_text(driver.app, locators['orderWindow']['subTotalAmount'], "Subtotal Amount",
                                                                  waits_config['shortWait'])
        self.assertion.assert_equal(round(sum(prices), 2), subtotal)
        tax = driver.utilities.get_text(driver.app, locators['orderWindow']['tax'], "Tax", waits_config['veryShortWait'])
        total = []
        total.append(tax)
        totalAmount = driver.utilities.get_text(driver.app, locators['orderWindow']['totalAmount'], "Total Amount ",
                                                waits_config['veryShortWait'])
        total.append(prices)
        calculated_total = sum(prices) + float(tax)
        self.assertion.assert_equal(float(totalAmount.replace('$', '')), round(calculated_total, 2))
        logging.info("The sum of items added to cart is equal to the total amount in the cart")
        totalAmountOfbreakEntreeItem = float(totalAmount.replace('$', ''))
        self.yamlmanager.write_to_yaml_file(yaml_data={'totalAmountOfItemsInCart': totalAmountOfbreakEntreeItem}, filename="totalAmount", )

    def verfiyModifiers(self):
        text = driver.utilities.get_text(driver.app, locators['orderWindow']['modifiersInCart'], "Modifier", waits_config['veryShortWait'])
        return text

    def verifyDefaultModifier(self):
        text = self.verfiyModifiers()
        self.assertion.assert_contains(text, "No HAM")

    def verifyFreeModifier(self):
        text = self.verfiyModifiers()
        self.assertion.assert_contains(text, "ADD MAYO")

    def verifyPricedModifier(self):
        text = self.verfiyModifiers()
        jalapenos = driver.utilities.get_item_price(driver.app, locators['orderWindow']['autoIdOfJALAPENOS'], locators['orderWindow']['JALAPENOS'], "Price of JALAPENOS : ", waits_config['veryShortWait'])
        # prices.append(jalapenos)
        prices[0] += float(jalapenos)
        self.assertion.assert_contains(text, "ADD JALAPENOS")
        subtotal = driver.utilities.get_text(driver.app, locators['orderWindow']['subTotalAmount'], "Subtotal Amount", waits_config['veryShortWait'])
        self.assertion.assert_equal(round(sum(prices), 2), subtotal)
        totalAmount = driver.utilities.get_text(driver.app, locators['orderWindow']['totalAmount'], "Total Amount ",
                                                waits_config['veryShortWait'])
        totalAmountOfItemAfterModifications = float(totalAmount.replace('$', ''))
        self.yamlmanager.write_to_yaml_file(yaml_data={'totalAmountOfItemsInCart': totalAmountOfItemAfterModifications}, filename="totalAmount")
        self.yamlmanager.write_to_yaml_file(yaml_data={'priceOfItemsList': prices}, filename="pricesOfItems")

    def verifyPaymentSuccessful(self):
        driver.utilities.is_element_displayed(driver.app, locators['orderWindow']['noCheckText'], "No Checks text", waits_config['veryShortWait'])
        total = driver.utilities.get_text(driver.app, locators['orderWindow']['totalAmount'], "Total Amount", waits_config['veryShortWait'])
        if float(total.replace('$', '')) == 0.00:
            logging.info("Payment was successful")
        else:
            logging.error("Payment was not successful")
