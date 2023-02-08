import logging
import os
from pathlib import Path

LOG_DIR = Path(os.getenv("LOG_DIR", Path(__file__).parent.parent / "logs"))

if not LOG_DIR.exists():
    LOG_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_FORMATTER = logging.Formatter(
    "%(asctime)s | %(levelname)-8s | %(name)s | pid:%(process)d | thread:%(thread)d | %(message)s"
)


def configure(root_level: int = logging.INFO):
    _root = logging.getLogger()
    _root.setLevel(root_level)

    _root_console = logging.StreamHandler()
    _root_console.setFormatter(DEFAULT_FORMATTER)
    _root.addHandler(_root_console)

    return _root


def get_pid_file_logger(name: str, level: int = logging.INFO):
    _logger = logging.getLogger(name)
    _logger.setLevel(level)

    log_file = LOG_DIR / f"{os.getpid()}_{name}.log"
    file_handler = logging.FileHandler(filename=log_file, mode="w", encoding="utf-8")
    file_handler.setFormatter(DEFAULT_FORMATTER)
    _logger.addHandler(file_handler)

    return _logger
