from configparser import ConfigParser


def config_Read(category, key):
    config = ConfigParser()
    config.read(
        "D:\PythonSeleniumExpleo\PytestFramework\DataDrivenFrameWork\TutorialsNinja\DataProviders\config.ini"
    )
    return config.get(category, key)
