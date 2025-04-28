import numpy as np

from src.library import RichLogger


def add(a: np.ndarray, b: np.ndarray) -> int:
    return a + b


if __name__ == "__main__":
    save_dir = "data/output"
    logger = RichLogger.get_logger(save_dir)
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    result = add(a, b)
    logger.info("Result: %s", result)
