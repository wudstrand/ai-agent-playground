import logging
from typing import Optional, Any
import yaml

from src.gData import GlobalData


class AppConfig:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self._yaml_file_path = GlobalData.app_config
        self.config = self._load_yaml()

    def _load_yaml(self):
        self.log.debug(f'Loading config from {self._yaml_file_path}')
        with open(self._yaml_file_path, 'r') as file:
            result = yaml.safe_load(file)
            self.log.debug(f'Loaded config: {result}')
            return result

    def get(self, key: str) -> Optional[Any]:
        self.log.debug(f'Getting config value for key: {key}')
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
        return value