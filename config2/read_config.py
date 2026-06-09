from configparser import ConfigParser
import os

def get_config(category, key):
    config = ConfigParser()
    
    # Get the directory where read_config.py live
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "config.ini")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"config.ini not found at: {config_path}")
    config.read(config_path)
    return config.get(category, key)
