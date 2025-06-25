def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []

    if mode == "row":
        for i in range(len(matrix)):
            curr = 0
            for j in range(len(matrix[0])):
                curr += matrix[i][j]
            mean = curr / len(matrix[0])
            means.append(mean)
    else:
        for j in range(len(matrix[0])):
            curr = 0
            for i in range(len(matrix)):
                curr += matrix[i][j]
            mean = curr / len(matrix)
            means.append(mean)

    return means
