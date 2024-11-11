import logging.config
import yaml

from src.gData import GlobalData


def initialize_logger():
    with open(GlobalData.logging_config, 'r') as file:
        config = yaml.safe_load(file)

    # Configure the logging module
    logging.config.dictConfig(config)
