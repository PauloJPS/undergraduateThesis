import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh
from matrixWork import *

class Magneto(data2matrix):
    def __init__(self, n):
        self.__n = n
        self.__dim = int(2**n)
        super(Magneto, self).__init__(n)

    def generateH(self, which='large'):
        if which == 'all':
            stateList = self.getStateList()
        elif which == 'large':
            stateList, dim = self.getLargeSectorStateList()
        Hdic = {}
        for state in stateList:
            for i in range(self.__n):
                binary = self.getBinary(state)
                j = (i+1) % self.__n
                c = stateList.index(state)
                if binary[i] == binary[j]:
                    if (c, c) in Hdic: 
                        Hdic[(c, c)] += 1/4
                    else: 
                        Hdic.update({(c, c): 1/4})
                else:
                    if (c, c) in Hdic: 
                        Hdic[(c, c)] -= 1/4
                    else: 
                        Hdic.update({(c, c): -1/4})

                    s = self.flipBit(np.copy(binary), i, j)
                    s1 = self.getInt(s)
                    
                    b = self.findState(stateList, s1)

                    if (c, b)  in Hdic:
                        Hdic[(c, b)]  = 1/2
                    else: 
                        Hdic.update({(c, b):1/2})
        return Hdic, dim

    def getStateList(self):
        stateList = [0 for i in range(self.__dim)]
        aux = 0
        for nUp in range(self.__n + 1):
            for i in range(self.__dim):
                binary = self.getBinary(i)
                if np.sum(binary) == nUp : 
                    stateList[aux] = i
                    aux += 1
        return stateList

    def getLargeSectorStateList(self):
        nUp = int(self.__n/2)
        size = np.math.factorial(self.__n)/np.math.factorial(nUp)/np.math.factorial(self.__n - nUp)
        size = int(size)
        stateList = [0 for i in range(size)]
        aux = 0
        for i in range(self.__dim):
            binary = self.getBinary(i)
            if np.sum(binary) == nUp : 
                stateList[aux] = i
                aux += 1
        return stateList, size

    def findState(self, stateList, s):
        return np.searchsorted(stateList, s)

    @staticmethod
    def EigenState(n, which='large'):
        m = Magneto(n)
        return m.getEigenState(which)/n

