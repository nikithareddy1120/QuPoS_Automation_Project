import importlib
import os
from abc import ABC, abstractmethod
import log_file

logging = log_file.get_logs()

class ApplicationDriver(ABC):
    """
    Abstract base class for application drivers.
    This class defines the common interface that all specific application drivers must implement.
    """
    @abstractmethod
    def launch_application(self, app_path):
        """
        Launches the application.
            :param app_path : The file path to the application to be launched.
        """
        pass

    @abstractmethod
    def close_application(self):
        """
        Closes the application.
        """
        pass
#
# class LocatorLoader(ABC):
#     def __init__(self, framework_type: str):
#         self.framework_type = framework_type
#         self.locators = {}
#
#     @abstractmethod
#     def load_locators(self):
#         pass
#
#     def _load_locators_from_module(self, module_path):
#         """Helper method to import locators from a given module path."""
#         try:
#             module = importlib.import_module(module_path)
#             module_name = module_path.split('.')[-1]  # Get the module name
#
#             # Skip logging for `__init__` modules
#             if module_name != "__init__" and hasattr(module, module_name):
#                 self.locators[module_name] = getattr(module, module_name)
#                 logging.info(f"Loaded locators from {module_path} under '{module_name}'")
#
#         except Exception as e:
#             logging.error(f"Failed to load locators from {module_path}: {e}")
#             raise
#
#     def get_locator(self, windowType):
#         # Remove any extra quotes around the window type
#         sanitized_window_type = windowType.strip('"').strip()
#         # Log to check the sanitized key and available locator keys
#         logging.debug(f"Looking up locator for sanitized window type: '{sanitized_window_type}'")
#         logging.debug(f"Available locator keys: {list(self.locators.keys())}")
#         # Retrieve and log the locator if found, otherwise log an error
#         locator = self.locators.get(sanitized_window_type)
#         if locator is None:
#             logging.error(f"Locator for '{sanitized_window_type}' not found in loaded locators.")
#         return locator

class LocatorLoader(ABC):
    def __init__(self, framework_type: str):
        self.framework_type = framework_type
        self.locators = {}

    @abstractmethod
    def load_locators(self):
        pass

    def _load_locators_from_module(self, module_path):
        """Helper method to import locators from a given module path."""
        try:
            module = importlib.import_module(module_path)
            module_name = module_path.split('.')[-1]  # Get the module name

            # Skip logging for `__init__` modules
            if module_name != "__init__" and hasattr(module, module_name):
                self.locators[module_name] = getattr(module, module_name)
                logging.info(f"Loaded locators from {module_path} under '{module_name}'")

        except Exception as e:
            logging.error(f"Failed to load locators from {module_path}: {e}")
            raise

    # def get_locator(self, windowType):
    #     # Remove any extra quotes and whitespace around the window type
    #     sanitized_window_type = windowType.strip('"').strip("'").strip()
    #     # Log to verify the sanitized key
    #     logging.debug(f"Looking up locator for sanitized window type: '{sanitized_window_type}'")
    #     locator = self.locators.get(sanitized_window_type)
    #     if locator is None:
    #         logging.error(f"Locator for '{sanitized_window_type}' not found in loaded locators.")
    #     return locator

class PywinautoLocatorLoader(LocatorLoader):
    def load_locators(self):
        base_path = "test_project.business_layer.locators.pywinauto_locators"
        locator_files = [f[:-3] for f in os.listdir(base_path.replace(".", "/")) if f.endswith(".py")]
        for file in locator_files:
            module_path = f"{base_path}.{file}"
            self._load_locators_from_module(module_path)


class WinAppDriverLocatorLoader(LocatorLoader):
    def load_locators(self):
        base_path = "test_project.business_layer.locators.winappdriver_locators"
        locator_files = [f[:-3] for f in os.listdir(base_path.replace(".", "/")) if f.endswith(".py")]
        for file in locator_files:
            module_path = f"{base_path}.{file}"
            self._load_locators_from_module(module_path)

# import importlib
# import os
# from abc import ABC, abstractmethod
# import log_file
#
# logging = log_file.get_logs()
#
# class ApplicationDriver(ABC):
#     """
#     Abstract base class for application drivers.
#     This class defines the common interface that all specific application drivers must implement.
#     """
#     @abstractmethod
#     def launch_application(self, app_path):
#         """
#         Launches the application.
#             :param app_path : The file path to the application to be launched.
#         """
#         pass
#
#     @abstractmethod
#     def close_application(self):
#         """
#         Closes the application.
#         """
#         pass
#
# class LocatorLoader(ABC):
#     def __init__(self, framework_type: str):
#         self.framework_type = framework_type
#         self.locators = {}
#
#     @abstractmethod
#     def load_locators(self):
#         pass
#
#     def _load_locators_from_module(self, module_path):
#         """Helper method to import locators from a given module path."""
#         try:
#             module = importlib.import_module(module_path)
#             module_name = module_path.split('.')[-1]  # Get the module name
#
#             # Skip logging for `__init__` modules
#             if module_name != "__init__" and hasattr(module, module_name):
#                 self.locators[module_name] = getattr(module, module_name)
#                 logging.info(f"Loaded locators from {module_path} under '{module_name}'")
#
#         except Exception as e:
#             logging.error(f"Failed to load locators from {module_path}: {e}")
#             raise






























# class PywinautoLocatorLoader(LocatorLoader):
#     def load_locators(self):
#         base_path = "test_project.business_layer.locators.pywinauto_locators"
#         locator_files = [f[:-3] for f in os.listdir(base_path.replace(".", "/")) if f.endswith(".py")]
#         for file in locator_files:
#             module_path = f"{base_path}.{file}"
#             self._load_locators_from_module(module_path)
#
# class WinAppDriverLocatorLoader(LocatorLoader):
#     def load_locators(self):
#         base_path = "test_project.business_layer.locators.winappdriver_locators"
#         locator_files = [f[:-3] for f in os.listdir(base_path.replace(".", "/")) if f.endswith(".py")]
#         for file in locator_files:
#             module_path = f"{base_path}.{file}"
#             self._load_locators_from_module(module_path)
