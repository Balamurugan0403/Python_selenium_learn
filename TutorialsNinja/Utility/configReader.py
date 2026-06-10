from configparser import ConfigParser
import os

def config_Read(category, key):
    config = ConfigParser()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "..", "DataProviders", "config.ini")
    
    config.read(config_path)
    return config.get(category, key)
