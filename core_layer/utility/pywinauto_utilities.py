import io
import sys
import time
from logging import exception

from pywinauto.timings import wait_until_passes, wait_until
import log_file
from config.config_reader import config

logging = log_file.get_logs()
pywinauto_config = config.get_pywinauto_config()


class PywinautoUtilities:

    def maximizeWindow(self, app):
        """
        This method maximizes the application.
            :param app : pywinauto Application instance.
        """
        try:
            window = app[pywinauto_config["window_title"]]
            window.maximize()
            logging.info(f"Maximized the application window.")
        except Exception:
            logging.error(f"Failed to maximize window")

    def minimizeWindow(self, app):
        """
        This method minimizes the application.
            :param app : pywinauto Application instance.
        """
        try:
            window = app[pywinauto_config["window_title"]]
            window.minimize()
            logging.info(f"Minimized the application window.")
        except Exception:
            logging.error(f"Failed to minimize window")

    def click_button(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method will click on the locator
            :param app : pywinauto Application instance.
            :param control_identifier : element locator
            :param friendlyNameOfElement: name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config['window_title']]
            control = window.child_window(**control_identifier).wrapper_object()
            wait_until(timeout, 1, control.is_enabled)
            if control.is_enabled():
                control.click_input()
            logging.info(f"Clicked on {friendlyNameOfElement}")
        except Exception:
            logging.error(f"{friendlyNameOfElement} not found")

    def enter_text(self, app, control_identifier, text, friendlyNameOfElement, timeout):
        """
        This method will enter the text in the locator
            :param app : pywinauto Application instance.
            :param control_identifier : element locator
            :param text : text to enter in input field
            :param friendlyNameOfElement: name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            control = window.child_window(**control_identifier).wrapper_object()
            # time.sleep(timeout)
            wait_until(timeout, 1, control.is_enabled)
            # Now you can interact with the control
            if control.is_enabled():
                control.set_edit_text(text)
            logging.info(f"Entered {text} into {friendlyNameOfElement}")
        except Exception:
            logging.error(f"Could not {text} into {friendlyNameOfElement}")

    def get_text(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method will get the text from the locator
            :param app : pywinauto Application instance.
            :param control_identifier : element locator
            :param friendlyNameOfElement: name of the element for logging.
            :param timeout : time to wait for element to be visible
            :return : return the text from the locator
        """
        try:
            window = app[pywinauto_config["window_title"]]
            control = window.child_window(**control_identifier).wrapper_object()
            # time.sleep(timeout)
            wait_until(timeout, 1, control.is_enabled)
            # Now you can interact with the control
            # if control.is_enabled():
            text = control.window_text()
            logging.info(f"Text from {friendlyNameOfElement} is {text}")
            return text
        except Exception:
            logging.error(f"Unable to fetch the text from the {friendlyNameOfElement}")
            return None

    def is_element_displayed(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method will wait for an element to be displayed.
            :param app : pywinauto Application instance.
            :param control_identifier : element locator
            :param friendlyNameOfElement: name of the element for logging.
            :param timeout : time to wait for element to be displayed
        """
        try:
            window = app[pywinauto_config['window_title']]
            control = window.child_window(**control_identifier).wrapper_object()
            # time.sleep(timeout)
            wait_until(timeout, 1, control.is_enabled)
            # Now you can interact with the control
            # if control.is_enabled():
            control.is_visible()
            logging.info(f"{friendlyNameOfElement} is displayed")
        except Exception:
            logging.error(f"{friendlyNameOfElement} not found")

    def waitUntilVisible(self, app, control_identifier, timeout):
        """
        This method will wait for an element to be displayed.
            :param app : pywinauto Application instance.
            :param control_identifier : element locator
            :param timeout : time to wait for element to be displayed
        """
        flag = False
        try:
            window = app[pywinauto_config['window_title']]
            control = window.child_window(**control_identifier).wrapper_object()
            # time.sleep(timeout)
            wait_until(timeout, 1, control.is_enabled)
            # Now you can interact with the control
            if control.is_enabled():
                flag = control.is_visible()
                return flag
        except Exception:
            return flag

    def is_element_selected(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method will wait for an element to be selected.
            :param app : pywinauto Application instance.
            :param control_identifier : element locator
            :param friendlyNameOfElement: name of the element for logging.
            :param timeout : time to wait for element to be displayed
        """
        try:
            window = app[pywinauto_config["window_title"]]
            control = window.child_window(**control_identifier).wrapper_object()
            # time.sleep(timeout)
            wait_until(timeout, 1, control.is_enabled)
            # Now you can interact with the control
            if control.is_enabled():
                control.is_selected()
            logging.info(f"{friendlyNameOfElement} is selected")
        except Exception:
            logging.error(f"{friendlyNameOfElement} is not selected")

    def is_element_enabled(self, app, control_identifier, timeout):
        """
        This method will wait for an element to be enabled.
            :param app : pywinauto Application instance.
            :param control_identifier : element locator
            :param timeout : time to wait for element to be enabled
        """
        flag = False
        try:
            window = app[pywinauto_config["window_title"]]
            control = window.child_window(**control_identifier).wrapper_object()
            wait_until(timeout, 1, control.is_enabled)
            if control.is_enabled():
                flag = control.is_enabled()
            # logging.info(f"{friendlyNameOfElement} is enabled")
            return flag
        except Exception as e:
            # logging.error(f"{friendlyNameOfElement} not enabled: {e}")
            return flag

    def clear_text(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method will clear the text from the element
            :param app : pywinauto Application instance.
            :param control_identifier : element locator
            :param friendlyNameOfElement: name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            control = window.child_window(**control_identifier).wrapper_object()
            # time.sleep(timeout)
            wait_until(timeout, 1, control.is_enabled)
            # Now you can interact with the control
            if control.is_enabled():
                control.set_focus()
                control.send_keys('^a')
                control.send_keys('{DELETE}')
            logging.info(f"Cleared the text from {friendlyNameOfElement}")
        except Exception:
            logging.error(f"Unable to clear the text from {friendlyNameOfElement}")

    def double_click(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method double-clicks on the element.
            :param app : pywinauto Application instance.
            :param control_identifier : element locator
            :param friendlyNameOfElement: name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            control = window.child_window(**control_identifier).wrapper_object()
            # time.sleep(timeout)
            wait_until(timeout, 1, control.is_enabled)
            # Now you can interact with the control
            if control.is_enabled():
                control.double_click_input()
            logging.info(f"Double clicked on the element with locator: {friendlyNameOfElement}")
        except Exception:
            logging.error(f"Unable to double click on the element with locator {friendlyNameOfElement}")
            raise

    def drag_and_drop(self, app, source_control_identifier, destination_control_identifier, timeout):
        """
        This method performs the drag and drop operation
            :param app: pywinauto Application instance.
            :param source_control_identifier: Element locator to start dragging from.
            :param destination_control_identifier: Element locator to drop to.
            :param timeout: Time to wait for the elements to be visible.
        """
        try:
            window = app[pywinauto_config["window_title"]]
            source_control = window.child_window(**source_control_identifier).wrapper_object()
            target_control = window.child_window(**destination_control_identifier).wrapper_object()
            time.sleep(timeout)
            source_control.drag_mouse_input()
            target_control.drop_mouse_input()
            logging.info(f"Performed drag-and-drop from {source_control_identifier} to {destination_control_identifier}")
        except Exception as e:
            logging.error(
                f"Unable to perform drag-and-drop from {source_control_identifier} to {destination_control_identifier}: {e}")
            raise

    def get_status_of_button(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method will get the status of a button in the Application.
            :param app : pywinauto Application instance.
            :param control_identifier : element locator
            :param friendlyNameOfElement: name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            flag = False
            main_dlg = app[pywinauto_config["window_title"]]
            button = main_dlg.child_window(**control_identifier, top_level_only=True)
            # time.sleep(timeout)
            wait_until(timeout, 1, button.is_enabled)
            # Now you can interact with the control
            if button.is_enabled():
                if button and button.is_visible() and button.is_enabled():
                    logging.info(f"'{friendlyNameOfElement}' field is visible and enabled")
                    flag = True
                else:
                    logging.error(f"'{friendlyNameOfElement}' field is not visible or not enabled.")
                    flag = False
        except Exception:
            logging.error(f"Exception occurred")
            flag = False
        return flag

    def mouse_hover(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method will perform a mouse hover action on the specified element.
            :param app: pywinauto Application instance.
            :param control_identifier: element locator
            :param friendlyNameOfElement: name of the element for logging.
            :param timeout: time to wait for element to be visible.
        """
        try:
            window = app[pywinauto_config["window_title"]]
            element = window.child_window(**control_identifier).wrapper_object
            wait_until(timeout, 1, element.is_enabled)
            # Now you can interact with the control
            if element.is_enabled():
                element.wait('visible', timeout=timeout)
                element.wait('enabled', timeout=timeout)
                element.move_mouse_input()
            # rect = element.rectangle()
            # mouse.move(coords=(rect.left + 5, rect.top + 5))
            logging.info(f"Mouse hover action performed on the element {friendlyNameOfElement}.")
        except Exception:
            logging.error(f"Unable to perform mouse hover action on the element {friendlyNameOfElement}")
            raise

    def close_window(self, app):
        """
         This method closes the application.
            :param app : pywinauto Application instance.
         """
        try:
            window = app[pywinauto_config["window_title"]]
            window.close()
            logging.info(f"Closed the application window.")
        except Exception as e:
            logging.error(f"Failed to close window: {e}")

    def restore_window(self, app):
        """
        This method restores the application window.
            :param app : pywinauto Application instance.
        """
        try:
            window = app[pywinauto_config["window_title"]]
            window.restore()
            logging.info(f"Restored the application window.")
        except Exception as e:
            logging.error(f"Failed to restore window: {e}")

    def is_window_active(self, app):
        """
        This method checks if the specified application window is active.
            :param app: pywinauto Application instance.
            :return: Boolean indicating whether the window is active.
        """
        try:
            window = app[pywinauto_config["window_title"]]
            active = window.is_active()
            if active:
                logging.info(f"The window '{pywinauto_config['window_title']}' is active.")
            else:
                logging.info(f"The window '{pywinauto_config['window_title']}' is not active.")
            return active
        except Exception as e:
            logging.error(f"Failed to check if window '{pywinauto_config['window_title']}' is active: {e}")
            return False

    def getWindowState(self, app):
        """
        This method will return the current state of the application .
            :param app : pywinauto Application instance.
            :return : returns the current state of the window
        """
        try:
            window = app[pywinauto_config["window_title"]]
            windowState = window.get_show_state()
            logging.info(f"Application window state : {windowState}.")
            return windowState
        except Exception as e:
            logging.error(f"Failed to return the application window state: {e}")

    def scroll_element(self, app, control_identifier, direction, amount, friendlyNameOfElement, timeout):
        """
        This method will scroll the specified element in the given direction.
            :param app: pywinauto Application instance.
            :param control_identifier: element locator
            :param direction: Direction to scroll ('up', 'down', 'left', 'right').
            :param amount: Amount to scroll ('large', 'small', 'page', 'begin', 'end').
            :param friendlyNameOfElement: name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            element = window.child_window(**control_identifier).wrapper_object
            wait_until(timeout, 1, element.is_enabled)
            # Now you can interact with the control
            if element.is_enabled():
                element.wait('visible', timeout)
            # element.wait('enabled', timeout)
                element.scroll(direction, amount)
            logging.info(f"Scrolled the element {friendlyNameOfElement}")
        except Exception:
            logging.error(f"Unable to scroll the element {friendlyNameOfElement}")
            raise

    def right_click(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method right-clicks on the element.
            :param app : pywinauto Application instance.
            :param control_identifier : element locator
            :param friendlyNameOfElement: name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            control = window.child_window(**control_identifier).wrapper_object()
            # time.sleep(timeout)
            wait_until(timeout, 1, control.is_enabled)
            # Now you can interact with the control
            if control.is_enabled():
                control.right_click_input()
            logging.info(f"Right clicked on the element with locator: {friendlyNameOfElement}")
        except Exception:
            logging.error(f"Unable to right click on the element with locator {friendlyNameOfElement}")
            raise

    def send_keyboard_shortcut_to_element(self, app, control_identifier, shortcut, friendlyNameOfElement, timeout):
        """
        This method sends a keyboard shortcut to a specified element.
            :param app: pywinauto Application instance.
            :param control_identifier: element locator
            :param shortcut: String representing the keyboard shortcut (e.g., '^s' for Ctrl+S).
            :param friendlyNameOfElement: name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            element = window.child_window(**control_identifier).wrapper_object()
            wait_until(timeout, 1, element.is_enabled)
            # Now you can interact with the control
            if element.is_enabled():
                element.wait('ready', timeout)
                element.set_focus()
                element.send_keys(shortcut)
            logging.info(
                f"Sent keyboard shortcut '{shortcut}' to the element '{friendlyNameOfElement}'.")
        except Exception:
            logging.error(
                f"Unable to send keyboard shortcut '{shortcut}' to the element '{friendlyNameOfElement}'")
            raise

    def set_focus_to_element(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method sets focus to a specified element.
            :param app: pywinauto Application instance.
            :param control_identifier: element locator
            :param friendlyNameOfElement: name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            element = window.child_window(**control_identifier).wrapper_object()
            wait_until(timeout, 1, element.is_enabled)
            # Now you can interact with the control
            if element.is_enabled():
                element.wait('ready', timeout)
                element.set_focus()
            logging.info(f"Set focus to the element '{friendlyNameOfElement}'.")
        except Exception as e:
            logging.error(
                f"Unable to set focus to the element '{friendlyNameOfElement}': {e}")
            raise

    def wait_for_window_to_be_idle(self, app, timeout):
        """
        This method waits for a window to be idle.
            :param app: pywinauto Application instance.
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            window.wait_for_idle(timeout=timeout)
            logging.info(f"Window '{pywinauto_config['window_title']}' is now idle.")
        except Exception as e:
            logging.error(f"Failed to wait for window '{pywinauto_config['window_title']}' to be idle: {e}")
            raise

    def wait_for_element(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method waits for a specified element to appear.
            :param app: pywinauto Application instance.
            :param control_identifier: element locator.
            :param friendlyNameOfElement: name of the element for logging.
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            element = window.child_window(**control_identifier).wrapper_object()
            wait_until(timeout, 1, element.is_enabled)
            # Now you can interact with the control
            if element.is_enabled():
                element.wait('exists ready', timeout=timeout)
            logging.info(f"Element {friendlyNameOfElement} is now present.")
        except Exception as e:
            logging.error(f"Failed to wait for element {friendlyNameOfElement}")
            raise

    def verify_element_text(self, app, control_identifier, expected_text, timeout):
        """
        This method verifies the text of a specified element.
            :param app: pywinauto Application instance.
            :param control_identifier: element locator.
            :param expected_text: Expected text to verify.
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            element = window.child_window(**control_identifier).wrapper_object()
            # time.sleep(timeout)
            wait_until(timeout, 1, element.is_enabled)
            # Now you can interact with the control
            if element.is_enabled():
                actual_text = element.window_text()
                assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
            logging.info(f"Element {control_identifier} text verified successfully.")
        except Exception as e:
            logging.error(f"Failed to verify text for element {control_identifier}: {e}")
            raise

    def check_element_existence(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method checks whether a specified element exists.
            :param app: pywinauto Application instance.
            :param control_identifier: element locator.
            :param friendlyNameOfElement: name of the element for logging.
            :param timeout : time to wait for element to be visible
            :return: Boolean indicating existence.
        """
        try:
            window = app[pywinauto_config["window_title"]]
            element = window.child_window(**control_identifier)
            # time.sleep(timeout)
            wait_until(timeout, 1, element.is_enabled)
            # Now you can interact with the control
            if element.is_enabled():
                exists = element.exists()
                logging.info(f"{friendlyNameOfElement} exists")
                return exists
        except Exception as e:
            logging.error(f"Failed to check existence of {friendlyNameOfElement}: {e}")
            raise

    def print_control_identifiers(self, app):
        """
        This method will print all the control identifiers displayed on the window
            :param app : pywinauto Application instance.
        """
        logging.info(f"Printing control identifiers for window: {pywinauto_config['window_title']}")
        try:
            window = app[pywinauto_config['window_title']]
            old_stdout = sys.stdout
            sys.stdout = io.StringIO()
            try:
                window.print_control_identifiers()
                control_identifiers = sys.stdout.getvalue()
            finally:
                sys.stdout = old_stdout
            return control_identifiers
        except Exception as e:
            logging.error(f"Error printing control identifiers for {pywinauto_config['window_title']}: {e}")
            return None

    def print_available_windows(self, app):
        """
        This method will print all the available windows
            :param app : pywinauto Application instance.
        """
        logging.info("Available windows:")
        for window in app.windows():
            logging.info(f"Window title: {window.window_text()}")

    def take_screenshot(self, app, save_path):
        """
        This method takes a screenshot of the application window.
            :param app: pywinauto Application instance.
            :param save_path: Path to save the screenshot.
        """
        try:
            window = app[pywinauto_config["window_title"]]
            screenshot = window.capture_as_image()
            screenshot.save(save_path)
            logging.info(f"Screenshot saved to {save_path}")
        except Exception as e:
            logging.error(f"Failed to take screenshot: {e}")
            raise

    def get_toggle_state_of_checkbox(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method retrieves the toggle state of a control (e.g., a checkbox or a toggle button).
            :param app: pywinauto Application instance.
            :param control_identifier: element locator
            :param friendlyNameOfElement: name of the element for logging.
            :param timeout: Time to wait for the element to be visible.
            :return: Toggle state (True if toggled on, False if toggled off, None if state cannot be determined).
        """
        try:
            window = app[pywinauto_config["window_title"]]
            control = window.child_window(**control_identifier).wrapper_object()
            wait_until(timeout, 1, control.is_enabled)
            # Now you can interact with the control
            if control.is_enabled():
                control.wait('exists', timeout)
                toggle_state = control.get_toggle_state()
                logging.info(f"Toggle state for {friendlyNameOfElement} is {toggle_state}.")
                return toggle_state
        except Exception as e:
            logging.error(f"Failed to get toggle state for {friendlyNameOfElement}: {e}")
            return None

    def is_element_editable(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method checks if a specified control is editable.
            :param app: pywinauto Application instance.
            :param control_identifier: Dictionary with the control's identifier.
            :param friendlyNameOfElement: name of the element for logging.
            :param timeout: Time to wait for the element to be visible.
            :return: Boolean indicating whether the control is editable.
        """
        try:
            window = app[pywinauto_config["window_title"]]
            control = window.child_window(**control_identifier).wrapper_object()
            wait_until(timeout, 1, control.is_enabled)
            # Now you can interact with the control
            if control.is_enabled():
                control.wait('exists', timeout)
                editable = control.is_editable()
                if editable:
                    logging.info(f"The control {friendlyNameOfElement} is editable.")
                else:
                    logging.info(f"The control {friendlyNameOfElement} is not editable.")
                return editable
        except Exception as e:
            logging.error(f"Failed to determine if the control {friendlyNameOfElement} is editable: {e}")
            return False

    def get_locator_by_title(self, title_value):
        return {"title": title_value}

    def get_button_locator_by_title(self, title_value):
        return {"title": title_value,  "control_type":"Button"}

    def get_item_price(self, app, button_auto_id, control_identifier, friendlyNameOfElement, timeout):
        window = app[pywinauto_config['window_title']]
        try:
            time.sleep(timeout)
            button_element = window.child_window(auto_id=button_auto_id, control_type="Button")
            item_static = button_element.child_window(**control_identifier)
            for child in button_element.children(control_type="Text"):
                if child.window_text().replace('.', '', 1).isdigit():
                    text = float(child.window_text())
                    logging.info(f"{friendlyNameOfElement}: {text}")
                    return float(child.window_text())
            logging.error(f"'{friendlyNameOfElement}' not found.")
            return None
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return None

    def clickChildLocator(self, app, button_auto_id, control_identifier, friendlyNameOfElement, timeout):
        window = app[pywinauto_config['window_title']]
        try:
            time.sleep(timeout)
            button_element = window.child_window(auto_id=button_auto_id, control_type="Button")
            item_static = button_element.child_window(**control_identifier)
            for child in button_element.children(control_type="Text"):
                if child.window_text().replace('.', '', 1).isdigit():
                    text = float(child.click_input())
                    logging.info(f"{friendlyNameOfElement}: {text}")
                    # return float(child.window_text())
            logging.error(f"'{friendlyNameOfElement}' not found.")
            return None
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return None

    def getDueAmount(self, app, control_identifier: dict, friendly_name: str, timeout):
        """
        Retrieve the numeric text from a specified control within a window.
        Args:
            app (Application): The pywinauto Application object connected to the target application.
            window_title (str): The title of the window where the control is located.
            control_identifier (dict): The properties to identify the target control.
            friendly_name (str): A friendly name for logging purposes.
            timeout (int, optional): Time to wait before searching for the control. Defaults to 5 seconds.
        Returns:
            str: The numeric text found within the control, or None if not found.
        """
        window = app[pywinauto_config['window_title']]
        try:
            time.sleep(timeout)
            # Locate the main button control using control_identifier
            button_control = window.child_window(**control_identifier)
            if button_control.exists(timeout=timeout):
                # Find the first child control of type "Text" within the button
                for child in button_control.children(control_type="Text"):
                    text = child.window_text()
                    logging.info(f"'{friendly_name}' found with text: {text}")
                    return text
                logging.info(f"No text found within '{friendly_name}' button.")
                return None
            else:
                logging.info(f"Control '{friendly_name}' not found in window '")
                return None
        except Exception as e:
            logging.error(f"Error occurred while getting text for '{friendly_name}': {e}")
            return None

    def get_item_price_without_autoid(self, app, control_identifier, friendlyNameOfElement, timeout):
        window = app[pywinauto_config['window_title']]
        try:
            time.sleep(timeout)
            item_static = window.child_window(**control_identifier)
            if item_static.exists():
                parent = item_static.parent()
                for child in parent.children(control_type="Text"):
                    if child.window_text().replace('.', '', 1).isdigit():
                        text = child.window_text()
                        logging.info(f"'{friendlyNameOfElement} : {text}'")
                        return child.window_text()
                (logging.info(f"'{friendlyNameOfElement}' not found."))
                return None
            else:
                logging.info(f"Item '{friendlyNameOfElement}' not found.")
                return None
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return None

    def get_locator_by_title(self, title_value):
        return {"title": title_value}

    # def find_elements(self, app, control_identifier, friendly_name_of_elements, timeout):
    #     # List to store matching elements
    #     elements = []
    #
    #     try:
    #         # Identify the parent window
    #         window = app[pywinauto_config["window_title"]]
    #
    #         # Assuming the parent window is a wrapper object
    #         parent_window = window.child_window(**control_identifier)
    #
    #         for i in range(1, 10):  # Searching for multiple elements (loop from 1 to 9)
    #             try:
    #                 # Only proceed with controls inside the parent window
    #                 element = parent_window.child_window(index=i, **control_identifier)
    #
    #                 # Debugging log for each element found
    #                 logging.info(f"Found element {i}: {element}")
    #
    #                 if element.is_visible():
    #                     elements.append(element)
    #             except Exception as e:
    #                 # Log the exception details for debugging
    #                 logging.error(f"Error while trying to find element {i}: {str(e)}")
    #                 break  # Stop if no more elements are found
    #
    #         # Log the number of elements found
    #         logging.info(f"Total elements found: {len(elements)}")
    #
    #     except Exception as e:
    #         logging.error(f"Error finding elements: {str(e)}")
    #
    #     return elements

    def find_elements(self, app, control_identifier, friendly_name_of_elements, timeout):
        elements = []

        try:
            # Identify the parent window
            window = app[pywinauto_config["window_title"]]

            # Assuming the parent window is a wrapper object
            parent_window = window.child_window(**control_identifier).wrapper_object()

            # Loop through elements, specifying the criteria to match each one
            for i in range(1, 10):  # Searching for multiple elements (from 1 to 9)
                try:


                    # Check if the element is visible before adding to the list
                    if parent_window.is_visible():
                        elements.append(parent_window)
                    logging.info(f"Found element {i}: {parent_window}")
                except Exception as e:
                    logging.error(f"Error finding element {i}: {str(e)}")
                    break  # Exit loop if no more elements are found

            logging.info(f"Total elements found: {len(elements)}")
        except Exception as e:
            logging.error(f"Error finding elements: {str(e)}")

        return elements
