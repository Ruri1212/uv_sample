import logging
from pathlib import Path

from rich.logging import RichHandler

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[]",
    handlers=[RichHandler(rich_tracebacks=True)],
)


class RichLogger:
    @staticmethod
    def get_logger(save_dir: str) -> logging.Logger:
        file_handler = logging.FileHandler(Path(save_dir) / "output.log", encoding="utf-8")
        file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(file_formatter)
        logger = logging.getLogger(__name__)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger
