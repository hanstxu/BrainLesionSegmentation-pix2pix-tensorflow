"""
compare.py : Dice coefficient for comparing set similarity.
Taken and extended from https://gist.github.com/JDWarner/6730747
"""

import numpy as np
from scipy import misc
import sys
from os import listdir
from os.path import isfile, join

def main():
    only_files = [f for f in listdir("test_results/images/") if isfile(join("test_results/images/", f))]
    outputs_targets = list(filter(lambda x:x.endswith(("outputs.png", "targets.png")), only_files))
    
    sum = 0
    count = 0
    min_score = sys.maxsize
    max_score = 0
    
    for output, target in zip(outputs_targets[::2], outputs_targets[1::2]):
        arr1 = misc.imread(output)
        arr2 = misc.imread(target)
        dice_score = dice(arr1, arr2)
        sum += dice_score
        count += 1
        min_score = min(min_score, dice_score)
        max_score = max(max_score, dice_score)
    
    print "average: ", sum/count
    print "minimum score: ", min_score
    print "maximum score: ", max_score

def dice(im1, im2):
    """
    Computes the Dice coefficient, a measure of set similarity.
    Parameters
    ----------
    im1 : array-like, bool
        Any array of arbitrary size. If not boolean, will be converted.
    im2 : array-like, bool
        Any other array of identical size. If not boolean, will be converted.
    Returns
    -------
    dice : float
        Dice coefficient as a float on range [0,1].
        Maximum similarity = 1
        No similarity = 0
        
    Notes
    -----
    The order of inputs for `dice` is irrelevant. The result will be
    identical if `im1` and `im2` are switched.
    """
    im1 = np.asarray(im1).astype(np.bool)
    im2 = np.asarray(im2).astype(np.bool)

    if im1.shape != im2.shape:
        raise ValueError("Shape mismatch: im1 and im2 must have the same shape.")

    # Compute Dice coefficient
    intersection = np.logical_and(im1, im2)

    return 2. * intersection.sum() / (im1.sum() + im2.sum())
    
if __name__ == "__main__":
    main()