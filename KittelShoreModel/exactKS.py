from scipy.sparse import linalg as lin
import scipy.sparse as sparse
import numpy as np
import matplotlib.pyplot as plt 

def matx(n):
    if n==1:
        col = [1, 0, 2, 1]
        row = [0, 1, 1, 2]
        data = 1/np.sqrt(2)*np.array([1, 1, 1, 1])
        return sparse.bsr_matrix((data, (row, col)), shape=(3, 3))
    elif n==0.5:
        col = [1, 0]
        row = [0, 1]
        data = 1/2*np.array([1, 1])
        return sparse.bsr_matrix((data, (row, col)), shape=(2, 2))
    else:
        return 0

def maty(n):
    if n==1:
        col = [1, 0, 2, 1]
        row = [0, 1, 1, 2]
        data = 1/np.sqrt(2)/1j*np.array([1, -1, 1, -1])
        return sparse.bsr_matrix((data, (row, col)), shape=(3, 3))
    elif n==0.5:
        col = [1, 0]
        row = [0, 1]
        data = 1/2*np.array([(0. -1.j), (0. +1.j)])
        return sparse.bsr_matrix((data, (row, col)), shape=(2, 2))
    else: return 0

def matz(n):
    if n==1:
        col = [0, 2]
        row = [0, 2]
        data = [1., -1.]
        return sparse.bsr_matrix((data, (row, col)), shape=(3, 3))
    elif n==0.5:
        col = [0, 1]
        row = [0, 1]
        data = 1/2*np.array([1, -1])
        return sparse.bsr_matrix((data, (row, col)), shape=(2, 2))
    else: return 0


def iden(n):
    if n==1:
        col = [0,1,2]
        row = [0,1,2]
        data = [1, 1, 1]
        return sparse.bsr_matrix((data, (row, col)), shape=(3, 3))
    elif n==0.5:
        col = [0,1]
        row = [0,1]
        data = [1, 1]
        return sparse.bsr_matrix((data, (row, col)), shape=(2, 2))
    else: return 0

def naiveHamiltonian(func, nSpin, nImp):
    conf = []
    sites = impuritieState(nSpin, nImp)
    n=0
    for i in range(nSpin-1):
        for k in range(i+1, nSpin):
            conf.append([])
            for j in range(nSpin):
                if j==k or j==i:
                    conf[n].append(func(sites[i]))
                else:
                    conf[n].append(iden(sites[i]))

            n += 1
    mats = []
    for i in conf:
        res = sparse.bsr_matrix(1)
        for mat in i:
            res = sparse.kron(res, mat)
        mats.append(res.astype(np.float16))
    return np.sum(mats)


def impuritieState(nSpin, nImp):
    sites = []
    for i in range(nSpin):
        sites.append(1/2)
    aux = 0
    for j in range(nImp):
        sites[aux] = 1
        if aux+2 >= nSpin:
            aux = 1
        else: aux += 2
    return sites

def totalHamiltonian(nSpin, nImp):
    h = (naiveHamiltonian(matx, nSpin, nImp) +
        naiveHamiltonian(maty, nSpin, nImp) +
        naiveHamiltonian(matz, nSpin, nImp))
    return h


