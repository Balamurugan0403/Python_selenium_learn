import logging
import os


def log_generator():

    log_path = os.path.join(
        os.path.dirname(__file__), "..", "Logs", "testlogreport.log"
    )

    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    return logging.getLogger()
