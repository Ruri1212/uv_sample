import numpy as np


def add(a: np.ndarray, b: np.ndarray) -> int:
    return a + b


if __name__ == "__main__":
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    result = add(a, b)
    print("Result:", result)
