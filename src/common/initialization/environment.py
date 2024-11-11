import logging
import os

from src.common.config.app_config import AppConfig


def load_enviroment(config: AppConfig):
    log = logging.getLogger(__name__)
    environment = {
        'LANGCHAIN_TRACING_V2': config.get("api.langchain.tracing"),
        'LANGCHAIN_API_KEY': config.get("api.langchain.key"),
        'TAVILY_API_KEY': config.get("api.tavily.key"),
        'OPENAI_API_KEY': config.get("api.openai.key"),
        'USER_AGENT': "ai-agent-playground"
    }

    for key, value in environment.items():
        log.debug(f'Setting environment variable: {key}')
        os.environ[key] = str(value)
