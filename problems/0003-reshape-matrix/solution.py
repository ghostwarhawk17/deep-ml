import numpy as np

def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    # Convert to numpy array
    arr = np.array(a)
    
    # Check if reshape is possible
    if arr.size != new_shape[0] * new_shape[1]:
        return []
    
    # Reshape and convert back to list
    reshaped_matrix = arr.reshape(new_shape).tolist()
    return reshaped_matrix
