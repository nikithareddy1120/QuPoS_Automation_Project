import json
import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import log_file

logging = log_file.get_logs()

class WinAppDriverUtilities:



    def maximizeWindow(self, app):
        """
        This method maximizes the application.
            :param app : WinAppDriver WebDriver instance.
        """
        try:
            app.maximize_window()
            logging.info("Maximized the application window.")
        except Exception:
            logging.error(f"Failed to maximize window")

    def minimizeWindow(self, app):
        """
        This method minimizes the application.
            :param app : WinAppDriver WebDriver instance.
        """
        try:
            app.minimize_window()
            logging.info("Minimized the application window.")
        except Exception:
            logging.error(f"Failed to minimize window")

    def get_locator(self, locator_json):
        """
        Extracts and maps the locator type and value from the JSON or dictionary input.
        Args:
            locator_json: JSON string or dictionary containing the locator type and its value.
        Returns:
            tuple: (By locator, locator value) or special handling for Automation ID
        Raises:
            ValueError: If the locator type is not supported or the input is invalid.
        """
        # If locator_json is a string, parse it into a Python dictionary
        if isinstance(locator_json, str):
            locator_dict = json.loads(locator_json)
        elif isinstance(locator_json, dict):
            locator_dict = locator_json
        else:
            raise ValueError("Locator should be a JSON string or a dictionary")
        # Extract the key (locator type) and value (locator itself)
        locator_type, locator_value = next(iter(locator_dict.items()))
        # Global locator map for reuse across different methods (excluding desktop specific ones)
        locator_map = {
            "id": By.ID,
            "name": By.NAME,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "class_name": By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            # Do not include ACCESSIBILITY_ID for Selenium WebDriver
        }
        if locator_type.lower() == "automation_id":
            # Custom handling for Automation ID
            return "AutomationId", locator_value  # This returns a tuple in the format expected for WinAppDriver
        else:
            # For regular locators
            by_locator = locator_map.get(locator_type.lower())
            if by_locator:
                return by_locator, locator_value
            else:
                raise ValueError(f"Locator type '{locator_type}' is not supported.")

    def locate_element(self, driver, locator_json, timeout=10):
        """
        Locates an element using the provided locator type and value.
        Args:
            driver: The WebDriver/Appium instance.
            locator_json: JSON string or dictionary containing the locator type and its value.
            timeout: Maximum time to wait for the element to be visible (default is 10 seconds).
        Returns:
            WebElement: The located element.
        Raises:
            Exception: If the element is not found or the locator type is unsupported.
        """
        # Use the utility method to get the locator
        by_locator, locator_value = self.get_locator(locator_json)

        # Create an explicit wait instance
        wait = WebDriverWait(driver, timeout)
        try:
            if by_locator == "AutomationId":
                # Custom handling for Automation ID with WinAppDriver
                return wait.until(EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID, locator_value)))
            else:
                # Regular Selenium/WebDriver handling for web elements
                return wait.until(EC.visibility_of_element_located((by_locator, locator_value)))
        except Exception as e:
            raise Exception(f"Failed to locate the element with locator {by_locator}: {locator_value}. Error: {str(e)}")

    def click_button(self, app, locator, friendlyNameOfElement, timeout):
        """
        This method will click on the locator
            :param app : WinAppDriver WebDriver instance.
            :param locator : Dictionary with locator type as key and value as locator value.
            :param friendlyNameOfElement : name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            element = self.locate_element(app, locator, timeout)
            element.click()
            logging.info(f"Clicked on {friendlyNameOfElement}")
        except Exception:
            logging.error(f"{friendlyNameOfElement} not found")

    def get_text(self, app, locator, friendlyNameOfElement, timeout):
        """
        This method will get the text from the locator
            :param app : WinAppDriver WebDriver instance.
            :param locator : Dictionary with locator type as key and value as locator value.
            :param friendlyNameOfElement : name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            element = self.locate_element(app, locator, timeout)
            text = element.text()
            logging.info(f"Text from {friendlyNameOfElement} is {text}")
        except Exception:
            logging.error(f"Unable to fetch the text from the {friendlyNameOfElement}")

    def enter_text(self, app, locator, text, friendlyNameOfElement, timeout):
        """
       This method will enter the text in the locator
            :param app : WinAppDriver WebDriver instance.
            :param locator : Dictionary with locator type as key and value as locator value.
            :param text : text to enter in input field
            :param friendlyNameOfElement : name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            element = self.locate_element(app, locator, timeout)
            element.clear()
            element.send_keys(text)
            logging.info(f"Entered {text} into {friendlyNameOfElement}")
        except Exception:
            logging.error(f"Could not {text} into {friendlyNameOfElement}")

    def is_element_displayed(self, app, locator, friendlyNameOfElement, timeout):
        """
        This method will wait for an element to be displayed.
            :param app : WinAppDriver WebDriver instance.
            :param locator : Dictionary with locator type as key and value as locator value.
            :param friendlyNameOfElement : name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            element = self.locate_element(app, locator, timeout)
            element.is_displayed()
            logging.info(f"{friendlyNameOfElement} is displayed")
        except Exception:
            logging.error(f"{friendlyNameOfElement} not found")

    def is_element_enabled(self, app, locator, timeout):
        """
        This method will wait for an element to be enabled.
            :param app : WinAppDriver WebDriver instance.
            :param locator : Dictionary with locator type as key and value as locator value.
            :param timeout : time to wait for element to be visible
        """
        flag = False
        try:
            element = self.locate_element(app, locator, timeout)
            if element.is_enabled():
                flag = element.is_enabled()
            return flag
        except Exception:
            return flag

    def clear_text(self, app, locator, friendlyNameOfElement, timeout):
        """
        This method will clear the text from the element
            :param app : WinAppDriver WebDriver instance.
            :param locator : Dictionary with locator type as key and value as locator value.
            :param friendlyNameOfElement : name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            element = self.locate_element(app, locator, timeout)
            element.clear()
            logging.info(f"Cleared the text from {friendlyNameOfElement}")
        except Exception:
            logging.error(f"Unable to clear the text from {friendlyNameOfElement}")

    def double_click(self, app, locator, friendlyNameOfElement, timeout):
        """
        This method double-clicks on the element
            :param app : WinAppDriver WebDriver instance.
            :param locator : Dictionary with locator type as key and value as locator value.
            :param friendlyNameOfElement : name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            element = self.locate_element(app, locator, timeout)
            actions = ActionChains(app)
            actions.double_click(element).perform()
            logging.info(f"Double clicked on the element with locator: {friendlyNameOfElement}")
        except Exception:
            logging.error(f"Unable to double click on the element with locator {friendlyNameOfElement}")

    def drag_and_drop(self, app, source_locator, destination_locator, friendlyNameOfElement, timeout):
        """
        This method performs the drag and drop operation
            :param app : WinAppDriver WebDriver instance.
            :param source_locator : Dictionary with source_locator type as key and value as source_locator value.
            :param destination_locator : Dictionary with destination_locator type as key and value as destination_locator value.
            :param friendlyNameOfElement : name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            source_element = self.locate_element(app, source_locator, timeout)
            target_element = self.locate_element(app, destination_locator, timeout)
            actions = ActionChains(app)
            actions.drag_and_drop(source_element, target_element).perform()
            logging.info(f"Performed drag-and-drop from {source_locator} to {destination_locator}")
        except Exception as e:
            logging.error(
                f"Unable to perform drag-and-drop from {source_locator} to {destination_locator}: {e}")
            raise

    def mouse_hover(self, app, locator, friendlyNameOfElement, timeout):
        """
        This method will perform a mouse hover action on the specified element.
            :param app : WinAppDriver WebDriver instance.
            :param locator : Dictionary with locator type as key and value as locator value.
            :param friendlyNameOfElement : name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            element = self.locate_element(app, locator, timeout)
            actions = ActionChains(app)
            actions.move_to_element(element).perform()
            logging.info(f"Mouse hover action performed on the element {friendlyNameOfElement}.")
        except Exception:
            logging.error(f"Unable to perform mouse hover action on the element {friendlyNameOfElement}")
            raise

    def get_status_of_button(self, app, locator, friendlyNameOfElement, timeout):
        """
        This method will get the status of a button in the Application.
            :param app : WinAppDriver WebDriver instance.
            :param locator : Dictionary with locator type as key and value as locator value.
            :param friendlyNameOfElement : name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            flag = False
            element = self.locate_element(app, locator, timeout)
            if element.is_enabled():
                if element and element.is_visible() and element.is_enabled():
                    logging.info(f"'{friendlyNameOfElement}' field is visible and enabled")
                    flag = True
            else:
                logging.error(f"'{friendlyNameOfElement}' field is not visible or not enabled.")
                flag = False
        except Exception:
            logging.error(f"Exception occurred")
            flag = False
        return flag

    @staticmethod
    def wait_for_time(wait_in_seconds):
        """
        This method waits for the mentioned time
            :param wait_in_seconds : time (in seconds)
        """
        logging.info(f"Waiting for {wait_in_seconds} seconds")
        time.sleep(wait_in_seconds)
