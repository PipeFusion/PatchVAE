from patchvae.models.layers.conv2d import PatchConv2d

import torch.nn as nn

class Conv2dAdapter(nn.Module):
    def __init__(self, conv2d: nn.Conv2d):
        super().__init__()
        self.conv2d = PatchConv2d(
            in_channels=conv2d.in_channels,
            out_channels=conv2d.out_channels,
            kernel_size=conv2d.kernel_size,
            stride=conv2d.stride,
            padding=conv2d.padding,
            dilation=conv2d.dilation,
            groups=conv2d.groups,
            bias=conv2d.bias is not None,
            padding_mode=conv2d.padding_mode,
            device=conv2d.weight.device,
            dtype=conv2d.weight.dtype
        )
        self.conv2d.weight.data = conv2d.weight.data
        self.conv2d.bias.data = conv2d.bias.data

    def forward(self, x):
        return self.conv2d(x)
