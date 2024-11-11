import os

class GlobalData:
    base_dir: str = os.path.dirname(os.path.dirname(__file__))
    config_dir: str = os.path.join(base_dir, 'config')
    logging_config: str = os.path.join(config_dir, 'logging.yaml')
    app_config: str = os.path.join(config_dir, 'app-config.yaml')