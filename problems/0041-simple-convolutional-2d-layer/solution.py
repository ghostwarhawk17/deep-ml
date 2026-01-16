import torch
import torch.nn.functional as F

def simple_conv2d(input_matrix: torch.Tensor,
                  kernel: torch.Tensor,
                  padding: int,
                  stride: int) -> torch.Tensor:
    """
    Perform a 2D convolution on a single-channel input using PyTorch's built-in conv2d.
    input_matrix: 2D tensor (H, W)
    kernel: 2D tensor (kH, kW)
    padding: int, zero-padding on all sides
    stride: int, stride of the convolution
    """

    # Reshape input to (N=1, C=1, H, W)
    input_tensor = input_matrix.unsqueeze(0).unsqueeze(0)

    # Reshape kernel to (out_channels=1, in_channels=1, kH, kW)
    kernel_tensor = kernel.unsqueeze(0).unsqueeze(0)

    # Perform convolution
    output = F.conv2d(
        input_tensor,
        kernel_tensor,
        stride=stride,
        padding=padding
    )

    # Remove batch and channel dimensions
    return output.squeeze(0).squeeze(0)
