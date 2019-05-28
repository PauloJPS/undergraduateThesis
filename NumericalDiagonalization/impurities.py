from scipy.sparse import linalg as lin
import scipy.sparse as sparse
import numpy as np
import matplotlib.pyplot as plt 
import sys

sys.path.insert(0, '/home/bilu/Documents/undergraduateThesis/KittelShoreModel')

from matrixes import *

sys.path.append('../HeisenbergModel/')

from naiveHeisenberg import *
from exploringMag import *


       
class oneDimHeisenberg(operators):
    def __init__(self, nSpin, nImp):
        self.nSpin = nSpin
        self.nImp = nImp

    def naiveHamiltonian(self, ax):
        conf = []
        sites = self.impuritieState()
        for j in range(self.nSpin):
            conf.append([])
            for i in range(self.nSpin):
                if i == j or i == (j+1)%self.nSpin:
                    conf[j].append(operators.mat(sites[i], ax))
                else:
                    conf[j].append(operators.mat(sites[i], 'i'))
        mats = []
        for i in conf:
            res = sparse.bsr_matrix(1)
            for mat in i:
                res = sparse.kron(res, mat)
            mats.append(res.astype(np.float16))
        return np.sum(mats)

    def totalHamiltonian(self):
        h = (self.naiveHamiltonian('x') + 
            self.naiveHamiltonian('y') + 
            self.naiveHamiltonian('z'))
        return h

    def sparceDiagonalization(self):
        h = self.totalHamiltonian()
        if self.nSpin==2:
            return lin.eigsh(h, 1, which='SA')[0]/self.nSpin/2
        else:
            return lin.eigsh(h, 1, which='SA')[0]/self.nSpin

    def impuritieState(self):
        sites = []
        for i in range(self.nSpin):
            sites.append(1/2)
        aux = 0 
        for j in range(self.nImp):
            sites[aux] = 1
            if aux+2 >= self.nSpin:
                aux = 1
            else: aux += 2
        return sites

    def CM(self):
        sites = self.impuritieState()
        H = 0
        for i in range(self.nSpin):
            H += (-1)**(i)*sites[i]*(-1)**((i+1)%self.nSpin)*sites[(i+1)%self.nSpin]
        if self.nSpin == 2: return H/self.nSpin
        else: return H/self.nSpin

    def SWdft(self):
        sites = self.impuritieState()
        Delta = (2-np.pi)/np.pi
        H = 0
        for i in range(self.nSpin):
            H += (-1)**(i)*sites[i]*(-1)**((i+1)%self.nSpin)*sites[(i+1)%self.nSpin] + Delta*sites[i]
        if self.nSpin==2: return H/self.nSpin/2
        else: return H/self.nSpin

    def ExaDFT(self):
        e0data = np.loadtxt('../HeisenbergModel/Heisenberg12.txt')
        sites = self.impuritieState()
        if 1 in sites: 
            e05 = oneDimHeisenberg(self.nSpin, 0)
            e05 = e05.sparceDiagonalization()
            e01 = oneDimHeisenberg(self.nSpin, self.nSpin)
            e01 = e01.sparceDiagonalization()
            print('ooooi')
        else:
            e05 = e0data[self.nSpin - 4][1]
            e01 = 1

        dic = {1:e01, 0.5:e05}
        H = 0
        for i in range(self.nSpin):
            H += ((-1)**(i)*sites[i]*(-1)**((i+1)%self.nSpin)*sites[(i+1)%self.nSpin] +
                    dic[sites[i]] + sites[i]**2)

        if self.nSpin==2: return H/self.nSpin/2
        else: return H/self.nSpin



