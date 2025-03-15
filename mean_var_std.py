import numpy as np

def calculate(list):
    my_list = list
    my_array = np.array(my_list)
    if len(my_array) != 9:
        raise ValueError(f'"List must contain nine numbers."')
    if len(my_array) == 9:
        # Reshape the 1D array into a 3x3 2D array
        my_array = my_array.reshape(3, 3)
    sum = 0

    calculations = {
        'mean': [
            my_array.mean(axis=0).tolist(),
            my_array.mean(axis=1).tolist(),
            my_array.mean()
        ],
        'variance': [
            my_array.var(axis=0).tolist(),
            my_array.var(axis=1).tolist(),
            my_array.var()
        ],
        'standard deviation': [
            my_array.std(axis=0).tolist(),
            my_array.std(axis=1).tolist(),
            my_array.std()
        ],
        'max': [
            my_array.max(axis=0).tolist(),
            my_array.max(axis=1).tolist(),
            my_array.max()
        ],
        'min': [
            my_array.min(axis=0).tolist(),
            my_array.min(axis=1).tolist(),
            my_array.min()
        ],
        'sum': [
            my_array.sum(axis=0).tolist(),
            my_array.sum(axis=1).tolist(),
            my_array.sum()
        ]
    }

    return calculations