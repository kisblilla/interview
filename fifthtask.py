import numpy as np
from scipy.linalg import block_diag

def block_matrix_maker(list_of_matrices):
    P = np.zeros((2, 0), dtype='int32')
    D=[list_of_matrices]
    return block_diag(*list_of_matrices)


print(block_matrix_maker([[[1, 0, 3 ],[0, 1, 3], [2, 3, 1]], [[3, 3, 4], [6, 7, 9 ], [2,1,4]], [2,3], [1,2]]))