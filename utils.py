import numpy as np 


def convert_to_floats(rows):
    """convert a list of string tuples to a  ndarray of floats"""

    # create a a result list ( later to be converted to np array matrix)
    result = []
    # To-Do Loop through the list and convert row by row
    # a loop should be written 
    for row in rows:

       value = np.asarray(row)
       value = value.astype(np.float)

       result.append(value)  # Vstack means we are adding a row

    return np.array(result)


