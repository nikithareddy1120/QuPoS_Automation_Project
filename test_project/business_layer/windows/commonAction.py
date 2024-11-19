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

class commonAction:
    def __init__(self):

        self.assertion = Assertions(driver)
        self.yamlmanager = YamlUtilities()
        # self.yamlmanager.read_from_yaml_file()

    def clickButton(self, locator, windowType):
        driver.utilities.click_button(driver.app, locators[windowType][locator], locator + " button", waits_config['veryShortWait'])

    def isButtonDisplayed(self, locator, windowType):
        driver.utilities.is_element_displayed(driver.app, locators[windowType][locator], locator + " button",
                                      waits_config['veryShortWait'])

    def isTextDisplayed(self, locator, windowType):
        driver.utilities.is_element_displayed(driver.app, locators[windowType][locator], locator + " text",
                                      waits_config['veryShortWait'])