import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

class Naive():
    def __init__(self, n ):
        self.__n = n
        self.__dim = int(2**n)

    def generateH(self):
        Hdic = {}
        for a in range(int(2**self.__n)):
            for i in range(self.__n):
                binary = self.getBinary(a)
                j = (i+1) % self.__n
                if binary[i] == binary[j]:
                    if (a,a) in Hdic:
                        Hdic[(a,a)] += 1/4
                    else: 
                        Hdic.update({(a,a): 1/4})
                else:
                    if (a,a) in Hdic:
                        Hdic[(a,a)] -= 1/4
                    else: 
                        Hdic.update({(a,a): -1/4})

                    b = self.flipBit(binary, i, j)
                    b = self.getInt(b)
                    if (a,b) in Hdic:
                        Hdic[(a,b)] -= 1/4
                    else: 
                        Hdic.update({(a,b): -1/2})
        return Hdic

    def dictinary2sparce(self):
        Hdic = self.generateH()
        data = []
        for i in Hdic.items():
            aux = i[0]
            data.append([aux[0], aux[1], i[1]])
        data = np.array(data)
        row = np.int32(data[:,0])
        col = np.int32(data[:,1])
        data = np.float32(data[:,2])
        
        mat = sp.coo_matrix((data, (row, col)), shape=(self.__dim, self.__dim))
        return mat

    def getEigenState(self):
        mat = self.dictinary2sparce()
        return eigsh(mat, k=1, which='SA', return_eigenvectors=False)[0]

    @staticmethod
    def EigenState(n):
        h = Naive(n) 
        return h.getEigenState()/n

    def flipBit(self, binary, i, j):
        binary[i] = (binary[i] + 1) % 2
        binary[j] = (binary[j] + 1) % 2
        return binary

    def getInt(self, binary):
        return  binary.dot(2**np.arange(self.__n)[::-1])
        
    def getBinary(self, integer):
        binary = np.binary_repr(integer, self.__n)
        return np.array([int(i) for i in binary])

