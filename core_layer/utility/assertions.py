import log_file

logging = log_file.get_logs()


class Assertions:
    """Class contains all assertions with log messages"""

    def __init__(self, driver):
        self.driver = driver

    def assert_equal(self, expected_value, actual_value):
        """
        This method compares the expected and actual values.
           :param expected_value : The value that is expected.
           :param actual_value : The value that is actually obtained.
        """
        try:
            assert str(expected_value).upper() == str(actual_value).upper()
            logging.info(
                f"Assertion passed: Expected value '{expected_value}' is equal to actual value '{actual_value}'.")
        except AssertionError:
            logging.error(
                f"Assertion failed: Expected value '{expected_value}' is not equal to actual value '{actual_value}'.")
            raise

    def assert_contains(self, expected_value, actual_value):
        """
        This method checks if the expected value contains the actual value.
            :param expected_value : The value that should contain the actual value.
            :param actual_value: The value that is expected to be found within the expected value.
        """
        try:
            assert (str(expected_value).upper()).__contains__(str(actual_value).upper())
            logging.info(f"Assertion passed: Expected value '{expected_value}' contains actual value '{actual_value}'.")
        except AssertionError:
            logging.error(
                f"Assertion failed: Expected value '{expected_value}' does not contain actual value '{actual_value}'.")
            raise

    def assert_not_equal(self, expected_value, actual_value):
        """
        This method compares the expected and actual values and asserts if the values are equal
            :param expected_value: The value that is expected.
            :param actual_value: The value that is actually obtained.
        """
        try:
            assert str(expected_value).upper() != str(actual_value).upper()
            logging.info(
                f"Assertion passed: Expected value '{expected_value}' is not equal to actual value '{actual_value}'.")
        except AssertionError:
            logging.error(
                f"Assertion failed: Expected value '{expected_value}' is equal to actual value '{actual_value}'.")
            raise

    def assert_is_not_none(self, value):
        """
        Asserts that a value is not None.
            :param value: The value expected not to be None.
        """
        try:
            assert value is not None
            logging.info(f"Assertion passed: Value {value} is not None.")
        except AssertionError:
            logging.error(f"Assertion failed: Value {value} is None.")
            raise

    def assert_is_none(self, value):
        """
        Asserts that a value is None.
            :param value: The value expected to be None.
        """
        try:
            assert value is None, f"Expected value to be None, but got '{value}'."
            logging.info(f"Assertion passed: Value {value} is None.")
        except AssertionError:
            logging.error(f"Assertion failed: Value {value} is not None.")
            raise

    def assert_member_in_container(self, member, container):
        """
        Asserts that a member is in a container.
            :param member: The member that is expected to be in the container.
            :param container: The container (e.g., list, string) where the member is expected to be found.
        """
        try:
            assert member in container, f"Expected '{member}' to be in '{container}'."
            logging.info(f"Assertion passed: '{member}' is in '{container}'.")
        except AssertionError:
            logging.error(f"Assertion failed: '{member}' is not in '{container}'.")
            raise

    def assert_member_not_in_container(self, member, container):
        """
        Asserts that a member is not in a container.
            :param member: The member that is expected not to be in the container.
            :param container: The container (e.g., list, string) where the member is not expected to be found.
        """
        try:
            assert member not in container, f"Expected '{member}' to not be in '{container}'."
            logging.info(f"Assertion passed: '{member}' is not in '{container}'.")
        except AssertionError:
            logging.error(f"Assertion failed: '{member}' is in '{container}'.")
            raise
