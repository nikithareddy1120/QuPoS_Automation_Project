from datetime import datetime
import logging
import os
import allure

current_date = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
root_directory = os.path.abspath(os.curdir)
log_directory = os.path.join(root_directory, f"Reports/Logs/LatestLogs_{current_date}")
os.makedirs(log_directory, exist_ok=True)
log_path = os.path.join(log_directory, "Logs.log")

class LoggingHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        level_name = record.levelname.lower()
        # with allure.step(f"{level_name.capitalize()} Log: {log_entry}"):
        if level_name == "error":
            assert False, log_entry

def get_logs():
    logger = logging.getLogger()
    if logger.hasHandlers():
        logger.handlers.clear()
    logging.basicConfig(
        format="%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)",
        datefmt='%d/%m/%Y %I:%M:%S %p',
        level=logging.INFO
    )
    filehandler = logging.FileHandler(log_path, mode='w')
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s: %(module)s: (%(funcName)s): %(message)s",
        datefmt='%d/%m/%Y %I:%M:%S %p'
    )
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    allure_handler = LoggingHandler()
    allure_handler.setFormatter(formatter)
    logger.addHandler(allure_handler)
    return logger
