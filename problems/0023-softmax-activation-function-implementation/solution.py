import math

def softmax(scores: list[float]) -> list[float]:
    m = max(scores)
    exp = [math.exp(s - m) for s in scores]
    ans = [0] * len(scores)
    for i in range(len(scores)):
        ans[i] = exp[i] / sum(exp)
    return ans