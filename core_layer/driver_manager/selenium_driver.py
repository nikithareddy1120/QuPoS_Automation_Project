import json
import pickle

from selenium import webdriver
from abc import ABCMeta
import log_file
from config.config_reader import config
from core_layer.driver_manager.application_driver import ApplicationDriver

waits_config = config.get_waits_config()

edge_driver_path = r"D://Users//nreddy//Downloads//geckodriver-v0.35.0-win64//geckodriver.exe"
chrome_driver_path = r"D://Users//nreddy//Downloads//chromedriver-win64//chromedriver-win64//chromedriver.exe"

logging = log_file.get_logs()

class Singleton(type):
    """
    Singleton class to ensure that only one instance of a class is created.
    This pattern is useful for creating a single instance of the driver.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonABCMeta(Singleton, ABCMeta):
    """
    A metaclass combining Singleton and ABCMeta, ensuring that subclasses of this class
    follow both the Singleton and Abstract Base Class (ABC) design patterns.
    """
    pass


class SeleniumDriver(ApplicationDriver, metaclass=SingletonABCMeta):
    """
    SeleniumDriver class responsible for launching and interacting with web applications using Selenium.
    Implements the ApplicationDriver interface and uses the Singleton pattern to ensure a single instance.
    """
    def __init__(self):
        """
        Initializes the SeleniumDriver with a browser instance.
        """
        self.driver = None

    def launch_application(self, app_url):
        """
        Launches the web application using the provided URL.
            :param app_url: The URL of the web application to be launched.
            :return: An instance of the Selenium WebDriver.
        """
        try:
            logging.info("Launching web application with Selenium")
            self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
            self.driver.get(app_url)
            # self.driver.refresh()
            # cookies = self.driver.get_cookies()
            #
            # # Save cookies to a file
            # with open("cookies.pkl", "wb") as file:
            #     pickle.dump(cookies, file)

            # with open("cookies.pkl", "rb") as file:
            #     cookies = pickle.load(file)
            #
            # # Add each cookie to the new session
            # for cookie in cookies:
            #     self.driver.add_cookie(cookie)

            # with open("cookies_cleaned.json", "r") as file:
            #     cookies = json.load(file)
            # for cookie in cookies:
            #     if "expiry" in cookie:
            #         cookie["expiry"] = int(cookie["expiry"])  # Ensure expiry is an integer
            #     self.driver.add_cookie(cookie)
            #
            # self.driver.refresh()
            # self.driver.maximize_window()
            # logging.info("Web application launched successfully")
            # self.driver.maximize_window()

            logging.info("Web application launched successfully")
        except Exception as e:
            logging.error(f"Failed to launch web application: {e}")
            raise
        return self.driver

    def close_application(self):
        """
        Closes the web application and quits the WebDriver instance.
        """
        try:
            if self.driver:
                logging.info("Closing web application")
                self.driver.quit()
                logging.info("Web application closed successfully")
            else:
                logging.warning("No web application instance to close")
        except Exception as e:
            logging.error(f"Failed to close web application with Selenium: {e}")
            raise
