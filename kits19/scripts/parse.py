#!/usr/bin/env python3

from utils import *
import numpy as np
from pathlib import Path
import struct

def export_segmentation(case_num: int, output: Path, cull: bool = True):
    """Export segmentation.nii.gz file in our own binary format:
    Parameters:
        * case_num - case number
        * output - path to output file
        * cull - whether or not to skip early/late slices that are all zeros
    Binary format:
        <n><w><h>
        <slice 1>
        ...
        <slice n>
    """
    seg = load_volume(case_num)
    data: np.ndarray = seg.get_fdata().astype(dtype="uint8", order="C", copy=False)
    n, w, h = data.shape
    with open(output, "wb") as f:
        f.write(n.to_bytes(4, "little"))
        f.write(w.to_bytes(4, "little"))
        f.write(h.to_bytes(4, "little"))
        for i in range(200, 201):
            slice = data[i, :, :]
            f.write(slice.tobytes(order="C"))


def main():
    export_segmentation(0, "../case0.bin", cull=False)

if __name__ == "__main__":
    main()

nifti = load_volume(0)
print(nifti.affine)
data: np.ndarray = nifti.get_fdata()
print(data.dtype)
print(data.shape)
slice = data[0, :, :]
print(slice.min(), slice.max())
print(slice[0:30, 0:10])

# print(data.astype(dtype=))
mask = data[147, :, :] > 0
# print((512 * 512 * 611) / (2**20))

