import re

from config.config_reader import config
from core_layer.driver_manager.driver_factory import DriverFactory
import log_file
from core_layer.utility.yamlManager import YamlUtilities

logging = log_file.get_logs()
framework_type = config.get_framework_type()
driver, locators = DriverFactory.create_driver(framework_type)
pywinauto_config = config.get_pywinauto_config()
waits_config = config.get_waits_config()

class informationAndToolsWindow:
    def __init__(self):
        self.yamlmanager = YamlUtilities()

    def verifySoftwareVersion(self):
        self.yamlmanager.read_from_yaml_file("QuPOSApplicationVersion")
        appVersionLoginWindow = self.yamlmanager.get_data_from_yaml('QuPOSApplicationVersion')
        softwareVersion = re.search(r"v(\d+\.\d+\.\d+\.\d+)", appVersionLoginWindow)
        if softwareVersion:
            software_version = softwareVersion.group(1)
            logging.info(f"Software Version in LogIn Window: {software_version}")
        teminalConfigurationInfo = driver.utilities.get_text(driver.app, locators['informationAndToolsWindow']['terminalConfigurationInfo'], "Terminal Configuration", waits_config['shortWait'])
        extractedVersion = re.search(r"Software Version:\s*(\d+\.\d+\.\d+\.\d+)", teminalConfigurationInfo)
        if extractedVersion:
            extracted_version = extractedVersion.group(1)
            logging.info(f"Extracted Version in Terminal Configuration: {extracted_version}")
            if extracted_version == software_version:
                logging.info("QuPOS application software version has been updated in Terminal Configuration")
            else:
                logging.info("QuPOS application software version has not been updated in Terminal Configuration")
        else:
            logging.info("Software version not found in the extracted text.")
