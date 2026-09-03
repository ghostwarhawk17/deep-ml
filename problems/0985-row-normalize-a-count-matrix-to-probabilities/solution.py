def row_normalize(counts: list[list[float]]) -> list[list[float]]:
    ans = []

    for row in counts:
        row_sum = sum(row)

        if row_sum == 0:
            ans.append([0.0] * len(row))
        else:
            ans.append([x / row_sum for x in row])

    return ans