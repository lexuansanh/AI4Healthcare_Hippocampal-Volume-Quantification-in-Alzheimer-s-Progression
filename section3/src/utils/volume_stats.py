"""
Contains various functions for computing statistics over 3D volumes
"""
import numpy as np

def Dice3d(a, b):
    """
    This will compute the Dice Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks -
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # TASK: Write implementation of Dice3D. If you completed exercises in the lessons
    # you should already have it.
    # Calculate the number of intersecting voxels (where both a and b are greater than 0)
    intersection = np.sum((a > 0) & (b > 0))

    # Calculate the total number of non-zero voxels in both a and b
    volumes = np.sum(a > 0) + np.sum(b > 0)

    # Check if both volumes are zero (avoid division by zero)
    if volumes == 0:
        return -1

    # Calculate the Dice coefficient using the intersection and total volumes
    dice_coefficient = 2. * intersection / volumes

    return dice_coefficient

def Jaccard3d(a, b):
    """
    This will compute the Jaccard Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks - 
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # TASK: Write implementation of Jaccard similarity coefficient. Please do not use 
    # the Dice3D function from above to do the computation ;)
    intersection = np.sum((a > 0) & (b > 0))

    # Calculate the number of non-zero voxels in both a and b
    total_non_zero_voxels = np.sum(a > 0) + np.sum(b > 0)

    # Calculate the number of voxels in the union of a and b
    union = total_non_zero_voxels - intersection

    # Check if the union of non-zero voxels is zero (avoid division by zero)
    if union == 0:
        return -1

    # Calculate the Jaccard coefficient using the intersection and union
    jaccard_coefficient = float(intersection) / float(union)

    return jaccard_coefficient
