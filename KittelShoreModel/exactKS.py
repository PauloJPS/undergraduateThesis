from scipy.sparse import linalg as lin
import scipy.sparse as sparse
import numpy as np
import matplotlib.pyplot as plt 
from matrixes import *


def naiveHamiltonian(ax, nSpin, nImp):
    print(operators)
    conf = []
    sites = impuritieState(nSpin, nImp)
    n=0
    for i in range(nSpin):
        for k in range(i+1, nSpin):
            conf.append([])
            for j in range(nSpin):
                if j==k or j==i:
                    conf[n].append(operators.mat(sites[j], ax))
                    #conf[n].append(('func(sites[i])', '%i'%sites[j]))
                else:
                    conf[n].append(operators.mat(sites[j], 'i'))
                    #conf[n].append(('iden(sites[i])', '%i'%sites[j]))

            n += 1
    conf = np.array(conf)
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
    h = (naiveHamiltonian('x', nSpin, nImp) +
        naiveHamiltonian('y', nSpin, nImp) +
        naiveHamiltonian('z', nSpin, nImp))
    return h


