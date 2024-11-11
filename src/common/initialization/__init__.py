from msilib.schema import AppId

from src.common.config.app_config import AppConfig
from src.common.initialization.environment import load_enviroment
from src.common.initialization.logs import initialize_logger


def default_app_initialization():
    config = app_config()
    initialize_logger()
    load_enviroment(config = config)

def app_config():
    config = AppConfig()
    return config