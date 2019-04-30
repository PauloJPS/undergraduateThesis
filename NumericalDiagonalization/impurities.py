from scipy.sparse import linalg as lin
import scipy.sparse as sparse
import numpy as np
import matplotlib.pyplot as plt 


def matx():
    col = [1, 0, 2, 1]
    row = [0, 1, 1, 2]
    data = [1, 1, 1, 1]
    return sparse.bsr_matrix((data, (row, col)), shape=(3, 3))

def maty():
    col = [1, 0, 2, 1]
    row = [0, 1, 1, 2]
    data = [1, -1, 1, -1]
    return sparse.bsr_matrix((data, (row, col)), shape=(3, 3))

def matz():
    col = [0, 2]
    row = [0, 2]
    data = [1, -1]
    return sparse.bsr_matrix((data, (row, col)), shape=(3, 3))

def iden():
    col = [0,1,2]
    row = [0,1,2]
    data = [1, 1, 1]
    return sparse.bsr_matrix((data, (row, col)), shape=(3, 3))

def naiveHamiltonian(n=10):
    conf = []
    for j in range(n):
        conf.append([])
        for i in range(n):
            if i == j or i == (j+1)%n:
                conf[j].append(matx())
            else:
                conf[j].append(iden())
    mats = []
    for i in conf:
        res = sparse.bsr_matrix(1)
        for mat in i:
            res = sparse.kron(res, mat)
        mats.append(res)
    return mats.astype(float)

