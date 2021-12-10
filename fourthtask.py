import numpy as np

def eucledian(twoD_vector):

    return (np.sum(np.abs(twoD_vector) ** 2, axis = -1) ** (1 / 2)).round(decimals=3)

# Test
A=np.array([3.162, 5.831, 4.583])
B=np.array([3.162, 1.732, 4.583])
C=np.array([1, 1, 1, 1])
assert eucledian([[1,0,3], [3,4,3], [2,4,1]]).all()==A.all()
assert eucledian([[1,0,3], [1,1,1], [2,4,1]]).all()==B.all()
assert(eucledian([[1], [-1], [1], [-1]])).all()==C.all()
print("OK")