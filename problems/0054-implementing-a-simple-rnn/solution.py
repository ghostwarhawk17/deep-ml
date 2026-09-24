import numpy as np

def rnn_forward(input_sequence: list[list[float]],
                initial_hidden_state: list[float],
                Wx: list[list[float]],
                Wh: list[list[float]],
                b: list[float]) -> list[float]:

    h = np.array(initial_hidden_state, dtype=float)

    for x in input_sequence:
        x_array = np.array(x, dtype=float)

        h = np.tanh(Wx @ x_array + Wh @ h + b)

    return np.round(h, 4)