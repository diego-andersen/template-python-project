"""Configuration handling module."""

import logging
import pkgutil
from dataclasses import dataclass
from os import getenv

import yaml


def configure_logging():
    """Read logging configuration from embedded YAML file.

    Log level is set at runtime via APP_LOG_LEVEL variable.
    """

    try:
        log_config = yaml.safe_load(pkgutil.get_data(__name__, "logging.yaml"))
        logging.config.dictConfig(log_config)
    except Exception as err:
        print(err)
        print("Error in logging configuration. Using default.")
        logging.basicConfig()

    log = logging.getLogger()
    log.setLevel(getenv("APP_LOG_LEVEL", default="INFO").upper())
    log.info("Logging initialized")


@dataclass
class AppConfig:
    """Global module configuration."""

    print_config: bool


cfg = AppConfig(
    print_config=False,
)
