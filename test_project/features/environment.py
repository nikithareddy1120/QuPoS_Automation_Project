import base64
import os
import time
from behave.model import Status
import log_file
from config.config_reader import config

from core_layer.driver_manager.driver_factory import DriverFactory

logging = log_file.get_logs()
SCREENSHOT_DIR = os.path.join(os.getcwd(), 'failedScreenshots')
framework_type = config.get_framework_type()
driver, locators = DriverFactory.create_driver(framework_type)

def capture_screenshot(scenario):
    driver, locators = DriverFactory.create_driver(framework_type)
    try:
        if not os.path.exists(SCREENSHOT_DIR):
            os.makedirs(SCREENSHOT_DIR)
        screenshot_path = os.path.join(SCREENSHOT_DIR, f"{scenario.name.replace(' ', '_')}_{int(time.time())}.png")
        logging.info(screenshot_path)
        driver.app.top_window().set_focus()
        driver.app.top_window().capture_as_image().save(screenshot_path)
        # driver.close_application()
        return screenshot_path
    except Exception as e:
        logging.error(f"Error capturing screenshot: {e}")

def after_scenario(context, scenario):
    if scenario.status == Status.failed:
        screenshot_path = capture_screenshot(scenario)
        embed_screenshot_to_report(context, scenario, screenshot_path)

def embed_screenshot_to_report(context, scenario, screenshot_path):
    with open(screenshot_path, "rb") as image_file:
        data_base64 = base64.b64encode(open(screenshot_path, "rb").read())
        data = data_base64.decode("utf-8").replace("\n", "")
        context.embed(mime_type="image/png", data=data, caption="Screenshot")

# def before_scenario(context, scenario):
#     context.driver, context.locators = DriverFactory.create_driver(framework_type)
#     app_path = DriverFactory.get_app_path(framework_type)
#     context.driver.launch_application_using_subprocess(app_path)

def before_all(context):
    def embed_data(mime_type, data, caption):
        non_empty_data = " " if not data else data
        for formatter in context._runner.formatters:
            if "html" in formatter.name:
                formatter.embedding(mime_type=mime_type, data=non_empty_data, caption=caption)
                return
    context.embed = embed_data