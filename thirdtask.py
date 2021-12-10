import numpy as np

def chessboard_matrix(n):
    print("Checkerboard pattern:")
    
    x = np.ones((n,n),dtype=int)
    x[1::2,::2] = -1
    x[::2,1::2] = -1
    return x


#test
A=np.array([[1, -1, 1],[-1, 1, -1],[1, -1, 1]])
assert chessboard_matrix(3).all()==A.all()
print("OK")


