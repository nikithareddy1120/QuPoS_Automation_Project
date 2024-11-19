import importlib
import json

from core_layer.driver_manager.pywinauto_driver import PywinautoDriver
from core_layer.driver_manager.winappdriver_driver import WinAppDriver
import log_file
from config.config_reader import config
from core_layer.driver_manager.application_driver import PywinautoLocatorLoader, WinAppDriverLocatorLoader

logging = log_file.get_logs()

class DriverFactory:
    """
    Factory class to create and return the appropriate driver instance based on the framework type.
    """
    @staticmethod
    def create_driver(framework_type):
        try:
            logging.info(f"Creating driver for framework: {framework_type}")
            if framework_type == 'pywinauto':
                driver = PywinautoDriver()
                locator_loader = PywinautoLocatorLoader(framework_type)
            elif framework_type == 'winappdriver':
                driver = WinAppDriver()
                locator_loader = WinAppDriverLocatorLoader(framework_type)
            else:
                logging.error(f"Unknown framework type: {framework_type}")
                raise ValueError(f"Unknown framework type: {framework_type}")
            locator_loader.load_locators()
            logging.debug(f"Loaded locators: {str(locator_loader.locators)}")
            return driver, locator_loader.locators
        except ValueError as ve:
            logging.error(f"Driver creation failed due to an invalid framework type: {ve}")
            raise
        except Exception as e:
            logging.error(f"An unexpected error occurred while creating the driver: {e}")
            raise

# class DriverFactory:
#     """
#     Factory class to create and return the appropriate driver instance and locator loader based on the framework type.
#     """
#
#     @staticmethod
#     def create_driver(framework_type):
#         try:
#             logging.info(f"Creating driver for framework: {framework_type}")
#
#             # Create the driver and locator loader based on framework type
#             if framework_type == 'pywinauto':
#                 driver = PywinautoDriver()
#                 locator_loader = PywinautoLocatorLoader(framework_type)
#             elif framework_type == 'winappdriver':
#                 driver = WinAppDriver()
#                 locator_loader = WinAppDriverLocatorLoader(framework_type)
#             else:
#                 logging.error(f"Unknown framework type: {framework_type}")
#                 raise ValueError(f"Unknown framework type: {framework_type}")
#
#             # Load locators and log the loaded locators for debugging
#             locator_loader.load_locators()
#             logging.debug(f"Loaded locators for '{framework_type}': {str(locator_loader.locators)}")
#
#             # Return both the driver instance and the locator loader instance
#             return driver, locator_loader
#
#         except ValueError as ve:
#             logging.error(f"Driver creation failed due to an invalid framework type: {ve}")
#             raise
#         except Exception as e:
#             logging.error(f"An unexpected error occurred while creating the driver: {e}")
#             raise

    @staticmethod
    def get_app_path(framework_type):
        """Retrieve the application path dynamically based on the framework type."""
        if framework_type == 'pywinauto':
            pywinauto_config = config.get_pywinauto_config()
            return pywinauto_config['application_path']
        elif framework_type == 'winappdriver':
            winappdriver_config = config.get_winappdriver_config()
            return winappdriver_config['application_path']
        else:
            raise ValueError(f"Unsupported framework type: {framework_type}")
