import numpy as np

def linear_regression_gradient_descent(
    X: np.ndarray,
    y: np.ndarray,
    alpha: float,
    iterations: int
) -> np.ndarray:
    """
    Perform linear regression using gradient descent.
    """

    m, n = X.shape
    y = y.reshape(-1, 1)      # Ensure column vector
    theta = np.zeros((n, 1)) # Initialize parameters

    for _ in range(iterations):
        # Predictions
        y_pred = X @ theta

        # Gradient computation
        gradient = (1 / m) * (X.T @ (y_pred - y))

        # Parameter update
        theta -= alpha * gradient

    return np.round(theta.flatten(), 4)
