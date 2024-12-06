import re
from core_layer.utility.assertions import Assertions
from config.config_reader import config
from core_layer.driver_manager.driver_factory import DriverFactory
import log_file
from core_layer.utility.yamlManager import YamlUtilities

logging = log_file.get_logs()
framework_type = config.get_framework_type()
driver, locators = DriverFactory.create_driver(framework_type)
waits_config = config.get_waits_config()
prices= []

class paymentWindow:
    def __init__(self):
        self.assertion = Assertions(driver)
        self.yamlmanager = YamlUtilities()

    def verifyCheckTotalAmount(self):
        checkTotalAmount = driver.utilities.get_text(driver.app, locators['paymentWindow']['checkTotalAmount'], "Check Total Amount", waits_config['veryShortWait'])
        self.yamlmanager.read_from_yaml_file("totalAmount")
        totalAmountOfbreakEntreeItem = self.yamlmanager.get_data_from_yaml('totalAmountOfItemsInCart')
        amount_match = re.search(r"\d+\.\d+", checkTotalAmount)
        if amount_match:
            extracted_amount = float(amount_match.group())
            self.assertion.assert_equal(totalAmountOfbreakEntreeItem, extracted_amount)
            logging.info("Total amount of items is equal to the Check Total amount")

    def verifyDueAmount(self, paymentMethod):
        dueAmount = driver.utilities.getDueAmount(driver.app, paymentMethod, "Due Amount", waits_config['shortWait'])
        self.yamlmanager.read_from_yaml_file("totalAmount")
        totalAmountOfbreakEntreeItem = self.yamlmanager.get_data_from_yaml('totalAmountOfItemsInCart')
        self.assertion.assert_equal(totalAmountOfbreakEntreeItem, dueAmount)
        logging.info("Total amount of items is equal to the Due amount")

    def verifyApplyPaymentConfirmationPopup(self):
        driver.utilities.is_element_displayed(driver.app, locators['paymentWindow']['applyPaymentConfirmationPopup'], "Apply Payment confirmation Popup", waits_config['veryShortWait'])
        confirmationText = driver.utilities.get_text(driver.app, locators['paymentWindow']['applyPaymentConfirmationText'], "Apply Payment button", waits_config['veryShortWait'])
        match = re.search(r'\$?(\d+\.\d{2})', confirmationText)
        if match:
            amount = match.group(1)  # Extracts the matched amount
            logging.info(f"Extracted amount: {amount}")
            self.yamlmanager.read_from_yaml_file("totalAmount")
            totalAmountOfbreakEntreeItem = self.yamlmanager.get_data_from_yaml('totalAmountOfItemsInCart')
            self.assertion.assert_equal(totalAmountOfbreakEntreeItem, amount)
            logging.info("Total amount of items is equal to the amount in the Apply Payment confirmation popup")
            logging.info(f"Apply ${totalAmountOfbreakEntreeItem} 'payment + $0.00 tip, and close check? text is displayed")

    def getItemPriceInPayPerItemPopup(self, locator, itemName):
        priceOfItem = float(driver.utilities.get_text(driver.app, locator, itemName, waits_config['shortWait']))
        prices.append(priceOfItem)
        self.yamlmanager.write_to_yaml_file(yaml_data={"ListOfPricesOfItemsInPayPerItemPopup": prices}, filename="pricesOfItemsListInPayPerItemPopup")

    def verifyItemPriceInPayPerItemPopup(self):
        self.yamlmanager.read_from_yaml_file("pricesOfItemsListInPayPerItemPopup")
        ListOfPricesOfItemsInPayPerItemPopup = self.yamlmanager.get_data_from_yaml("ListOfPricesOfItemsInPayPerItemPopup")
        self.yamlmanager.read_from_yaml_file("pricesOfItems")
        priceOfItemsList = self.yamlmanager.get_data_from_yaml("priceOfItemsList")
        self.assertion.assert_equal(ListOfPricesOfItemsInPayPerItemPopup, priceOfItemsList)
        logging.info("Amount of items in cart is equal to the amount of items in pay per item")

    def selectItemsForPaymentAndVerifyDueAmount(self, items_locators):
        prices = []
        gst_percentage = 8.7156
        for locator in items_locators:
            price_of_item = float(driver.utilities.get_text(driver.app, locator, locator, waits_config['shortWait']))
            gst_amount = price_of_item * (gst_percentage / 100)
            final_price_with_gst = price_of_item + gst_amount
            prices.append(final_price_with_gst)
            driver.utilities.click_button(driver.app, locator, locator, waits_config['shortWait'])
        driver.utilities.click_button(driver.app, locators['orderWindow']['OK'], "Ok button",
                                      waits_config['veryShortWait'])
        price_of_items_selected = round(sum(prices), 2)
        due_amount = float(driver.utilities.getDueAmount(driver.app, locators['paymentWindow']['dueAmountCash'], "Due Amount",
                                          waits_config['veryShortWait']))
        self.assertion.assert_equal(price_of_items_selected, due_amount)
        logging.info("Amount of items selected in pay per item is equal to the due amount")
        logging.info(f"Total price with GST: {price_of_items_selected}, Due Amount: {due_amount}")

    def selectItemsForPayment(self, locator):
        # float(driver.utilities.get_text(driver.app, locator, locator, waits_config['shortWait']))
        driver.utilities.click_button(driver.app, locator, locator, waits_config['shortWait'])
        driver.utilities.click_button(driver.app, locators['orderWindow']['OK'], "Ok button",
                                      waits_config['veryShortWait'])

    def verifySumOfDueAndTenderedAmount(self):
        tenderedAmount = driver.utilities.get_text(driver.app, locators['paymentWindow']['tenderedAmount'], 'Tendered Amount : ', waits_config['veryShortWait'])
        tendered_amount = tenderedAmount.replace('$', '').strip()
        DueAmount = driver.utilities.get_text(driver.app, locators['paymentWindow']['dueAmountInCart'], 'Due Amount in cart : ', waits_config['veryShortWait'])
        due_amount = DueAmount.replace('$', '').strip()
        TotalAmount = float(tendered_amount) + float(due_amount)
        total = driver.utilities.get_text(driver.app, locators['paymentWindow']['totalAmount'], 'Total Amount : ', waits_config['veryShortWait'])
        total_Amount = total.replace('$', '').strip()
        self.assertion.assert_equal(total_Amount, round(TotalAmount, 2))
        logging.info("Sum of Due and Tendered amount is equal to the total amount")
