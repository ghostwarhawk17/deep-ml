import numpy as np
from collections import defaultdict

def impute_missing_data(data: np.ndarray, strategy: str = 'mean') -> np.ndarray:
    column1 = data[:, 0].copy()
    column2 = data[:, 1].copy()

    def impute_column(column):
        valid = column[~np.isnan(column)]

        if strategy == "mean":
            value = np.mean(valid)

        elif strategy == "median":
            value = np.median(valid)

        elif strategy == "mode":
            freq = defaultdict(int)

            for x in valid:
                freq[x] += 1

            value = max(freq, key=freq.get)

        else:
            raise ValueError("strategy must be 'mean', 'median', or 'mode'")

        column[np.isnan(column)] = value
        return column

    column1 = impute_column(column1)
    column2 = impute_column(column2)

    return np.column_stack((column1, column2))