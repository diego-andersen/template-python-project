"""Bootstrapping module.

Initializes all adapters, logging, and injects configuration where necessary.
Returns whatever initialized components the entrypoint requires to function.
"""

import logging

from modulename.config import cfg, configure_logging


def bootstrap():
    """System bootstrap procedure.

    Initializes all system components, injects dependencies & config where necessary,
    returns components required by entrypoints.
    """

    configure_logging()
    log = logging.getLogger("bootstrap")

    if cfg.print_config:
        log.info("Config:")
        log.info(cfg)
    else:
        log.debug("Config:")
        log.debug(cfg)

    log.info("Bootstrap complete")
