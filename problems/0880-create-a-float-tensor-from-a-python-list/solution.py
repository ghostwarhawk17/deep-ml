import torch

def to_float_tensor(values):
    # TODO: return a torch.float32 tensor built from `values`

    x = torch.tensor(values)
    x = x.to(torch.float32)
    return x

