import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh
from matrixWork import *

class Naive(data2matrix):
    def __init__(self, n ):
        self.__n = n
        self.__dim = int(2**n)
        super(Naive, self).__init__(n)

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
                    if (a,a) in Hdic:
                        Hdic[(a,b)] = 1/2
                    else: 
                        Hdic.update({(a,b): 1/2})

 
        return Hdic

    @staticmethod
    def EigenState(n):
        return Naive(n).getEigenState()/n
  



