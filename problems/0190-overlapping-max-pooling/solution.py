import numpy as np
import math

def overlapping_max_pool2d(x: np.ndarray, kernel_size: int = 3, stride: int = 2) -> np.ndarray:
    N, C, H, W = x.shape

    out_h = math.ceil((H - kernel_size) / stride) + 1
    out_w = math.ceil((W - kernel_size) / stride) + 1

    output = np.zeros((N, C, out_h, out_w), dtype=float)

    for n in range(N):
        for c in range(C):
            for i in range(out_h):
                for j in range(out_w):
                    h_start = i * stride
                    w_start = j * stride
                    h_end = min(h_start + kernel_size, H)
                    w_end = min(w_start + kernel_size, W)

                    # ✅ FIXED HERE
                    window = x[n, c, h_start:h_end, w_start:w_end]
                    output[n, c, i, j] = np.max(window)

    return output
