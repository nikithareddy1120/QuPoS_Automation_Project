import configparser

import log_file

logging = log_file.get_logs()

class ConfigReader:
    """
    A utility class to read configuration settings from a config file.
    """
    def __init__(self, config_file='config.cfg'):
        """
        Initializes the ConfigReader with the provided config file.
        """
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_framework_type(self):
        """
        Retrieves the framework type from the configuration.
            :return: The type of the framework.
        """
        try:
            framework_type = self.config.get('Framework', 'type')
            logging.info(f"Framework type retrieved: {framework_type}")
            return framework_type
        except configparser.NoSectionError as e:
            logging.error(f"Framework section missing in the config file: {str(e)}")
            raise
        except configparser.NoOptionError as e:
            logging.error(f"Type option missing in the Framework section: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Error retrieving framework type: {str(e)}")
            raise

    def get_winappdriver_config(self):
        """
        Retrieves the WinAppDriver configuration from the configuration file.
            :return: A dictionary containing WinAppDriver configuration.
        """
        try:
            winappdriver_config = {
                'path': self.config.get('WinAppDriver', 'path_to_winappdriver'),
                'application_path': self.config.get('WinAppDriver', 'application_path'),
                'url': self.config.get('WinAppDriver', 'url')
            }
            # logging.info("WinAppDriver configuration retrieved successfully.")
            return winappdriver_config
        except configparser.NoSectionError as e:
            logging.error(f"WinAppDriver section missing in the config file: {str(e)}")
            raise
        except configparser.NoOptionError as e:
            logging.error(f"Required option missing in the WinAppDriver section: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Error retrieving WinAppDriver configuration: {str(e)}")
            raise

    def get_pywinauto_config(self):
        """
        Retrieves the Pywinauto configuration from the configuration file.
            :returns: A dictionary containing Pywinauto configuration.
        """
        try:
            pywinauto_config = {
                'application_path': self.config.get('Pywinauto', 'application_path'),
                'window_title': self.config.get('Pywinauto', 'window_title')
            }
            # logging.info("Pywinauto configuration retrieved successfully.")
            return pywinauto_config
        except configparser.NoSectionError as e:
            logging.error(f"Pywinauto section missing in the config file: {str(e)}")
            raise
        except configparser.NoOptionError as e:
            logging.error(f"Required option missing in the Pywinauto section: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Error retrieving Pywinauto configuration: {str(e)}")
            raise

    def get_waits_config(self):
        """
        Retrieves the Wait configuration from the configuration file.
            :returns: A dictionary containing Wait configuration.
        """
        try:
            wait_config = {
                'veryShortWait': int(self.config.get('waits', 'veryShortWait')),
                'shortWait': int(self.config.get('waits', 'shortWait')),
                'longWait': int(self.config.get('waits', 'longWait')),
                'veryLongWait': int(self.config.get('waits', 'veryLongWait'))
            }
            # logging.info("waits configuration retrieved successfully.")
            return wait_config
        except configparser.NoSectionError as e:
            logging.error(f"Waits section missing in the config file: {str(e)}")
            raise
        except configparser.NoOptionError as e:
            logging.error(f"Required option missing in the waits section: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Error retrieving waits configuration: {str(e)}")
            raise


    def get_employeeId_config(self):
        """
        Retrieves the employee id configuration from the configuration file.
            :returns: A dictionary containing employee id configuration.
        """
        try:
            pin_config = {
                'employeeId': self.config.get('employeeId', 'employeeId'),
            }
            # logging.info("employee Id configuration retrieved successfully.")
            return pin_config
        except configparser.NoSectionError as e:
            logging.error(f"employee Id section missing in the config file: {str(e)}")
            raise
        except configparser.NoOptionError as e:
            logging.error(f"employee Id option missing in the Pywinauto section: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Error retrieving employee Id configuration: {str(e)}")
            raise

config = ConfigReader()
