import numpy as np

def adam_optimizer(f, grad, x0, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, num_iterations=10):
    # Note: `f` is accepted only for interface parity with the PyTorch/Tinygrad
    # variants, which derive gradients from it via autograd. This version uses
    # `grad` only — the objective value `f` is never evaluated.
    # Your code here
    x = np.array(x0)
    m = np.zeros_like(x)
    v = np.zeros_like(x)

    

    for t in range(1,1 + num_iterations):
        grd = grad(x)
        # first moment
        m = beta1 * m + (1 - beta1) * grd

        # SECOND MOMENT
        v = beta2 * v + (1 - beta2) * (grd ** 2)

        # bias correction
        m_hat = m/(1 - beta1 ** t)
        v_hat = v/(1 - beta2 ** t)

        x -= learning_rate * m_hat/(np.sqrt(v_hat) + epsilon)

    return x
