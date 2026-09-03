
import numpy as np
import heapq

def euclidean(x1, y1, x2, y2):
    distance = np.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
    return distance


def smote(X_minority: np.ndarray, n_synthetic: int, k: int = 5) -> np.ndarray:
    n_samples = len(X_minority)
    n_features = len(X_minority[0])

    if k == 0 or n_synthetic == 0:
        return np.zeros((0, n_features))

    k = min(k, n_samples - 1)
    ans = []

    for _ in range(n_synthetic):
        i = np.random.randint(0, n_samples)
        minheap = []

        for j in range(len(X_minority)):
            if i == j:
                continue

            distance = np.linalg.norm(X_minority[i] - X_minority[j])
            heapq.heappush(minheap, (distance, j))

        neighbours = []

        for _ in range(k):
            neighbours.append(heapq.heappop(minheap)[1])

        j = np.random.randint(0, k)
        x_nn = X_minority[neighbours[j]]

        gap = float(np.random.random())

        x_synthetic = X_minority[i] + gap * (x_nn - X_minority[i])

        ans.append(x_synthetic)

    return np.array(ans)



