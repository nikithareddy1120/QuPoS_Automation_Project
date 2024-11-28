import time
from config.config_reader import config
from core_layer.driver_manager.driver_factory import DriverFactory
import log_file
from core_layer.utility.yamlManager import YamlUtilities

logging = log_file.get_logs()
framework_type = config.get_framework_type()
driver, locators = DriverFactory.create_driver(framework_type)
pywinauto_config = config.get_pywinauto_config()
waits_config = config.get_waits_config()
employeeid = config.get_employeeId_config()

class loginWindow:

    def __init__(self):
        self.yamlmanager = YamlUtilities()

    def enterEmployeeID(self):
        for digit in employeeid["employeeId"]:
            button_locator = driver.utilities.get_button_locator_by_title(digit)
            driver.utilities.click_button(driver.app, button_locator, digit, waits_config['veryShortWait'])

    def launchApp(self):
        driver.launch_application_using_subprocess(pywinauto_config["application_path"])

    def getAppVersion(self):
        appVersion = driver.utilities.get_text(driver.app, locators['loginWindow']['appVersion'], "QuPOS Application version in LogIn Window", waits_config['veryShortWait'])
        self.yamlmanager.write_to_yaml_file(yaml_data={'QuPOSApplicationVersion': appVersion}, filename="QuPOSApplicationVersion")

    def clickLoginButton(self):
        driver.utilities.click_button(driver.app, locators['loginWindow']['Log In'], "Log In button", waits_config['veryShortWait'])  # loginbutton
        if driver.utilities.waitUntilVisible(driver.app, locators['loginWindow']['administratorButton'], waits_config['veryShortWait']):
            logging.info("Administrator button is displayed")
            driver.utilities.click_button(driver.app, locators['loginWindow']['administratorButton'], "Administrator button", waits_config['veryShortWait'])
            driver.utilities.click_button(driver.app, locators['loginWindow']['clockInLogInButton'], "Clock In & Log In button", waits_config['veryShortWait'])
        else:
            logging.info("Application is logged in as an Administrator.")

    def closeApplication(self):
        driver.close_application()
