import numpy as np

def detect_outliers_iqr(data: list[float], k: float = 1.5) -> dict:
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)

    iqr = q3 - q1

    lower_bound = q1 - (k * iqr)
    upper_bound = q3 + (k * iqr)

    outlier_indices = []
    cleaned_data = []

    for i in range(len(data)):
        if data[i] < lower_bound or data[i] > upper_bound:
            outlier_indices.append(i)
        else:
            cleaned_data.append(data[i])

    return {
        'cleaned_data': cleaned_data,
        'outlier_indices': outlier_indices,
        'lower_bound': lower_bound,
        'upper_bound': upper_bound
    }