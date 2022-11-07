import math
import numpy as np
import random
import statistics

from collections import defaultdict
from typing import Any, List, Tuple

# This script should be execute from the current folder because of relative paths.
DATA_FOLDER = "./data/"
MOVIE_TSV_PATH = DATA_FOLDER + 'filmstarts.tsv'
PREPROCESSED_DATA_PATH = DATA_FOLDER + 'preprocessed_data.json'


def sample_class_data(x:List[Any], 
                      y:List[int], 
                      method:str="undersampling",
                      random_seed=42) -> Tuple[List[Any], List[int]]:
    """This method allow "undersampling", "oversampling" and "mediansampling" 
    of imbalanced class data

    Args:
        x (List[Any]): Modell Input Data
        y (List[int]): Modell Output Data
        method (str, optional): The sampling method. Defaults to "undersampling".
        random_seed (int, optional): Random seed to have the same rancomness
            everytime. Defaults to 42.

    Raises:
        ValueError: X and Y need to have the same lengths.
        ValueError: Unknown sampling method

    Returns:
        Tuple[List[Any], List[int]]: Returns sampled X and Y as a tuple
    """
    if len(x) != len(y):
        raise ValueError('X and Y have different lengths.')
    
    x_y = list(zip(x, y))
    
    classes_split = defaultdict(list)
    for e in x_y:
        # This allows the method to work with numpy arrays and one hot encoding.
        if isinstance(e[1], np.ndarray):
            classes_split["".join(map(str, e[1]))].append(e)
        else:
            classes_split[e[1]].append(e)
        
    values_per_class = 0
    if method == "undersampling":
        values_per_class = min([len(classes_split[k]) for k in classes_split])
    elif method == "oversampling":
        values_per_class = max([len(classes_split[k]) for k in classes_split])
    elif method == "mediansampling":
        # In some cases mean might be better
        values_per_class = int(statistics.median([len(classes_split[k]) for k in classes_split]))
    elif method == "none":
        return x, y
    else:
        raise ValueError('Unknown sampling method')
        
    x_y_sampled = []
    for key in classes_split:
        if len(classes_split[key]) >= values_per_class:
            x_y_sampled = x_y_sampled + classes_split[key][:values_per_class]
        else:
            oversampled = classes_split[key] * math.ceil(values_per_class/len(classes_split[key]))
            x_y_sampled = x_y_sampled + oversampled[:values_per_class]
    random.seed(random_seed)
    random.shuffle(x_y_sampled)
    return zip(*x_y_sampled)