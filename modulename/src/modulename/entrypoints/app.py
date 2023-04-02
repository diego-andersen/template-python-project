"""System entrypoint."""

import logging
from importlib import metadata

from modulename.bootstrap import bootstrap


def main():
    """Main function."""

    bootstrap()

    log = logging.getLogger("main")
    log.info("Modulename v%s initialized", metadata.version("modulename"))


if __name__ == "__main__":
    main()
