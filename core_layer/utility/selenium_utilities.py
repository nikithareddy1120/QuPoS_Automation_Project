import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import log_file
from config.config_reader import config
from core_layer.driver_manager.selenium_driver import SeleniumDriver

waits_config = config.get_waits_config()

logger = log_file.get_logs()

class SafeActions:

    def __init__(self):
        self.driver = SeleniumDriver().driver

    def wait_until_visible(self, locator=None, friendlyElement=None, timeout=None):
        """
        This method waits until element to be visible.

        Parameters:
            locator: element locator
            timeout: time to wait for element to be visible

        Returns: element
        """
        global element
        try:
            logger.info(f"Waiting for {timeout} until {locator} is visible")
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located(locator))
        except NoSuchElementException:
            logger.error(f"{friendlyElement} not found in {timeout}")
            logger.exception("No Such Element Exception")
        except TimeoutException:
            logger.error(f"{friendlyElement} not found in {timeout}")
            logger.exception("TimeOut Exception")
        return element

    # def wait_until_clickable(self, locator=None, timeout=None):
    #     """
    #     This method waits until element is clickable
    #
    #     Parameters:
    #         locator: element locator
    #         timeout: time to wait for element to be clickable
    #
    #     Returns: element
    #     """
    #     global element
    #     try:
    #         logger.info(f"Waiting for {timeout} until {locator} is clickable")
    #         element = WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
    #     except NoSuchElementException:
    #         logger.error(f"{locator} not found in {timeout}")
    #         logger.exception("No Such Element Exception")
    #     except TimeoutException:
    #         logger.error(f"{locator} not found in {timeout}")
    #         logger.exception("TimeOut Exception")
    #     return element
    #
    # def safe_click(self, locator=None, friendlyElement=None, timeout=30):
    #     web_element = self.wait_until_clickable(locator, timeout)
    #     try:
    #         web_element.click()
    #         logger.info(f"Clicked on {friendlyElement}")
    #     except Exception as e:
    #         logger.error(f"Failed to click on {friendlyElement}: {e}")
    #         raise

    def safe_click(self, locator=None, friendlyElement=None, timeout=30):
        """
        Click on an element safely.

        Parameters:
            locator (tuple): Element locator.
            friendlyElement (str): Friendly name for logging.
            timeout (int): Maximum wait time.

        Raises:
            Exception: If click operation fails.
        """
        try:
            web_element = self.wait_until_clickable(locator, timeout)
            # Scroll into view if needed
            ActionChains(self.driver).move_to_element(web_element).perform()
            web_element.click()
            logger.info(f"Clicked on {friendlyElement}")
        except Exception as e:
            logger.error(f"Failed to click on {friendlyElement}: {e}")
            raise

    from selenium.webdriver.common.action_chains import ActionChains

    def wait_until_clickable(self, locator=None, timeout=30):
        """
        Wait until an element is clickable.

        Parameters:
            locator (tuple): Element locator.
            timeout (int): Maximum wait time.

        Returns:
            WebElement: The located element.
        """
        try:
            logger.info(f"Waiting for {timeout} seconds until {locator} is clickable")
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.element_to_be_clickable(locator)
            )
            logger.info(f"Element {locator} is clickable")
            return element
        except TimeoutException:
            logger.error(f"Timeout: {locator} not found or not clickable in {timeout} seconds")
            raise
        except Exception as e:
            logger.error(f"Error while waiting for element {locator}: {str(e)}")
            raise

    def safe_get_text(self, locator, friendlyElement, timeout):
        """
        Safely retrieve text from an element.
        Parameters:
            locator (tuple): Element locator.
            friendlyElement (str): Friendly name for logging.
            timeout (int): Maximum wait time.
        Returns:
            str: The text of the element.
        Raises:
            Exception: If the text retrieval fails.
        """
        try:
            # Wait for the element to be visible
            web_element = self.wait_until_visible(locator, timeout)
            # Retrieve the text
            element_text = web_element.text
            logger.info(f"Retrieved text from {friendlyElement}: '{element_text}'")
            return element_text
        except Exception as e:
            logger.error(f"Failed to retrieve text from {friendlyElement}: {e}")
            raise

    def highlight(self, web_element):
        """Highlights (blinks) a Selenium Webdriver element"""

        # driver = element._parent
        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                       web_element, s)

        apply_style("border: {0}px solid {1};".format(1, "red"))


    def safe_enter_text(self, locator, text, friendlyElement, timeout):
        web_element = self.wait_until_clickable(locator, timeout)
        try:
            web_element.send_keys(text)
            logger.info(f"Entered {text} into element {friendlyElement}")
        except Exception as e:
            logger.error(f"Could not enter {text} into {friendlyElement}: {e}")
            raise

    def get_title(self):
        """ This method returns page title"""
        return self.driver.title

    @staticmethod
    def wait_for_time(wait_in_seconds):
        """ This method returns page url"""
        logger.info(f"Waiting for {wait_in_seconds} seconds")
        time.sleep(wait_in_seconds)

    def get_url(self):
        """ This method returns page url"""
        return self.driver.current_url

    def scroll_into_view(self, locator, friendlyElement, timeout):
        """
        Scroll an element into view.

        Parameters:
            locator (tuple): Element locator (e.g., ('xpath', '//button[@id="submit"]')).
            friendlyElement (str): A user-friendly name for the element for logging (e.g., "Submit Button").
            timeout (int): Maximum wait time to locate the element.

        Returns:
            WebElement: The element scrolled into view.

        Raises:
            TimeoutException: If the element is not found within the timeout.
        """
        try:
            friendly_name = friendlyElement or "Element"
            logger.info(f"Waiting for {timeout} seconds to locate {friendly_name} ({locator}) for scrolling")

            # Wait for the element to be present in the DOM
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )

            # Scroll element into view
            logger.info(f"Scrolling to {friendly_name} ({locator})")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

            # Optional: Highlight the element for debugging (remove if not needed)
            self.driver.execute_script("arguments[0].style.border='3px solid red'", element)

            logger.info(f"Successfully scrolled to {friendly_name} ({locator})")
            return element
        except TimeoutException:
            logger.error(f"Timeout: {friendlyElement} ({locator}) not found within {timeout} seconds for scrolling")
            raise
        except Exception as e:
            logger.error(f"Error while scrolling to {friendlyElement} ({locator}): {str(e)}")
            raise

    def switch_to_frame(self, locator, friendlyElement, timeout):
        """
        Switches to the specified iframe.

        Parameters:
            locator: Locator tuple for the iframe (e.g., ('id', 'iframe-id'))
            friendlyElement: Friendly name for the iframe (for logging purposes)
            timeout: Time in seconds to wait for the iframe to be present

        Returns:
            None
        """
        try:

            # Wait until the iframe is present
            iframe_element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )

            # Switch to the iframe
            self.driver.switch_to.frame(iframe_element)
            logger.info(f"Switched to {friendlyElement} successfully")

        except TimeoutException:
            logger.error(f"Timeout: {friendlyElement} not found within {timeout} seconds for switching")
            raise


        except Exception as e:
            logger.error(f"Unexpected error while switching to {friendlyElement} : {e}")
            raise