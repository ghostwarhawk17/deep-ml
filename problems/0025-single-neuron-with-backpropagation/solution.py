import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def train_neuron(
    features: np.ndarray,
    labels: np.ndarray,
    initial_weights: np.ndarray,
    initial_bias: float,
    learning_rate: float,
    epochs: int
) -> (np.ndarray, float, list[float]):

    weights = initial_weights.copy()
    bias = initial_bias
    mse_values = []

    for _ in range(epochs):
        z = features @ weights + bias
        predictions = sigmoid(z)

        loss = np.mean((predictions - labels) ** 2)
        mse_values.append(loss)

        error = predictions - labels

        dz = 2 * error * predictions * (1 - predictions)

        dw = np.mean(features * dz[:, np.newaxis], axis=0)
        db = np.mean(dz)

        weights -= learning_rate * dw
        bias -= learning_rate * db

    return weights, bias, mse_values