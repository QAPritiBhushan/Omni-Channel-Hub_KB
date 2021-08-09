import logging
import logging.handlers
import os

class LogGen:
    @staticmethod

    def logGen():
        if not os.path.exists("Logs"):
            os.makedirs("Logs")

        if not os.path.exists("Reports"):
            os.makedirs("Reports")

        if not os.path.exists("Screenshots"):
            os.makedirs("Screenshots")

        logging.basicConfig(filename="Logs/KhanBankAutomationLog.log", format='%(asctime)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S', filemode='w')
        rotate_file = logging.handlers.RotatingFileHandler("Logs/KhanBankAutomationLog.log", maxBytes=1024 * 1024 * 20,
                                                           backupCount=3)

        logger = logging.getLogger()
        logger.addHandler(rotate_file)
        logger.setLevel(logging.INFO)
        return logger
