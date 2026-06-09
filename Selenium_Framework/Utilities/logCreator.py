import logging
import os


def log_generator():

    log_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "Logs", "testlogreport.log"
    )

    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    logging.basicConfig(
        filename=log_path,
        level=logging.DEBUG,        # DEBUG captures all levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format="%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        force=True,
    )

    return logging.getLogger()