import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

class data2matrix():
    def __init__(self, n):
        self.__n = n
        self.__dim = int(2**n)

    def dictinary2sparce(self, which='large'):
        data = []
        Hdic, dim = self.generateH(which)
        for i in Hdic.items():
            aux = i[0]
            data.append([aux[0], aux[1], i[1]])
        data = np.array(data)
        row = np.int32(data[:,1])
        col = np.int32(data[:,0])
        data = np.float32(data[:,2])
        
        mat = sp.coo_matrix((data, (row, col)), shape=(dim, dim))
        return mat

    def getEigenState(self, which='large'):
        mat = self.dictinary2sparce(which)
        return eigsh(mat, k=1, which='SA', return_eigenvectors=False)[0]

    def flipBit(self, binary, i, j):
        #binary[self.__n - 1 -i] = (binary[self.__n - 1 -i] + 1) % 2
        #binary[self.__n - 1 -j] = (binary[self.__n - 1 -j] + 1) % 2
        binary[i] = (binary[i] + 1) % 2
        binary[j] = (binary[j] + 1) % 2
        return binary

    def getInt(self, binary):
        return  binary.dot(2**np.arange(self.__n)[::-1])
        
    def getBinary(self, integer):
        binary = np.binary_repr(integer, self.__n)
        return np.array([int(i) for i in binary])

