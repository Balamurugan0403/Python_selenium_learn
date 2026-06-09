import logging
import Utilities.logCreator as logCreator
def log_generator():
    logging.basicConfig(
        filename="testlogreport.log",
        level=logging.INFO,
        format='%(asctime)s-%(levelname)s-%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p'
        
    )
    return logging.getLogger()