import numpy as np

def weighted_index_score(Q, K, W):
    index_score = []

    for t in range(len(Q)):
        row = []
        for s in range(len(K)):
            total_sum = 0

            for h in range(len(Q[t])):
                dot_product = np.dot(Q[t][h], K[s])

                relu = max(0, dot_product)

                weight_product = relu * W[t][h]
                total_sum += weight_product

            row.append(total_sum)

        index_score.append(row)

    return index_score

            

    

