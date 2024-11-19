import subprocess
from appium import webdriver
from core_layer.utility.winappdriver_utilities import WinAppDriverUtilities
from core_layer.driver_manager.application_driver import ApplicationDriver
from abc import ABCMeta
import log_file

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


class WinAppDriver(ApplicationDriver, metaclass=SingletonABCMeta):
    """
    WinAppDriver class responsible for launching and closing applications using WinAppDriver.
    Implements the ApplicationDriver interface and uses the Singleton pattern to ensure a single instance.
    """
    def __init__(self):
        """
         Initializes the WinAppDriver class with a driver instance, the WinAppDriver process,
        and utility methods.
        """
        self.app = None
        self.winappdriver_process = None
        self.utilities = WinAppDriverUtilities()

    def launch_winappdriver(self, path_to_winappdriver):
        """
        Launches the WinAppDriver server using the provided path.
            :param path_to_winappdriver: The file path to the WinAppDriver executable.
         """
        try:
            self.winappdriver_process = subprocess.Popen([path_to_winappdriver])
            logging.info("WinAppDriver launched successfully.")
        except Exception as e:
            logging.error(f"Failed to launch WinAppDriver: {e}")
            raise

    def launch_application(self, app_path):
        """
        Launches the application using WinAppDriver and initializes the WebDriver.
            :param app_path: The file path to the application to be launched.
            :return: An instance of the initialized WebDriver.
        """
        self.launch_winappdriver("C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe")
        desired_caps = {}
        desired_caps["app"] = app_path
        try:
            self.app = webdriver.Remote(
                command_executor="http://127.0.0.1:4723",
                desired_capabilities=desired_caps)
            logging.info("Driver initialized successfully.")
            return self.app
        except Exception as e:
            logging.error(f"Failed to initialize driver: {e}")
            raise

    def close_application(self):
        """
        Closes the application and terminates the WinAppDriver server.
        """
        try:
            self.app.quit()
            logging.info("Driver quit successfully.")
        except Exception as e:
            logging.error(f"Failed to quit driver: {e}")
        # Terminate WinAppDriver
        if self.winappdriver_process:
            try:
                self.winappdriver_process.terminate()
                self.winappdriver_process.wait()
                logging.info("WinAppDriver terminated successfully.")
            except Exception as e:
                logging.error(f"Failed to terminate WinAppDriver: {e}")
