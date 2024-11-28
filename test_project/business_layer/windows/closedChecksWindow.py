from config.config_reader import config
from core_layer.driver_manager.driver_factory import DriverFactory
import log_file
from core_layer.utility.yamlManager import YamlUtilities

logging = log_file.get_logs()
framework_type = config.get_framework_type()
driver, locators = DriverFactory.create_driver(framework_type)
pywinauto_config = config.get_pywinauto_config()
waits_config = config.get_waits_config()

class closedChecksWindow:
    def __init__(self):
        self.yamlmanager = YamlUtilities()

    def verifyAppVersion(self, window: str):
        appVersion = driver.utilities.get_text(driver.app, locators['loginWindow']['appVersion'], "QuPOS Application version in " + window + " window", waits_config['shortWait'])
        self.yamlmanager.read_from_yaml_file("QuPOSApplicationVersion")
        appVersionLoginWindow = self.yamlmanager.get_data_from_yaml('QuPOSApplicationVersion')
        if appVersion == appVersionLoginWindow:
            logging.info("QuPOS application version has been updated in " + window + " window")
