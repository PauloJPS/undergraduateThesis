from scipy.sparse import linalg as lin
import scipy.sparse as sparse
import numpy as np
import matplotlib.pyplot as plt 
import sys

sys.path.insert(0, '/home/bilu/Documents/undergraduateThesis/KittelShoreModel')

from matrixes import *

       
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
        sites = self.impuritieState()

        e05 = oneDimHeisenberg(self.nSpin, 0)
        e05 = e05.sparceDiagonalization()
        e01 = oneDimHeisenberg(self.nSpin, self.nSpin)
        e01 = e01.sparceDiagonalization()

        dic = {1:e01, 0.5:e05}
        H = 0
        for i in range(self.nSpin):
            H += ((-1)**(i)*sites[i]*(-1)**((i+1)%self.nSpin)*sites[(i+1)%self.nSpin] +
                    dic[sites[i]] + sites[i]**2)

        if self.nSpin==2: return H/self.nSpin/2
        else: return H/self.nSpin

def makeSpinsPlot(nSpin=12):
    eExact1 = []
    eExact05 = []
    eCM1 = []
    eSW1 = []
    eEX1 = []
    eCM05 = []
    eSW05 = []
    eEX05 = []
    nSpin = nSpin+1
    n = np.arange(4, nSpin, 2)
    for i in n:
        heisen = oneDimHeisenberg(i, i)
        eExact1.append(heisen.sparceDiagonalization())
        eSW1.append(heisen.SWdft())
        eCM1.append(heisen.CM())
        eEX1.append(heisen.ExaDFT())

        heisen = oneDimHeisenberg(i, 0)
        eExact05.append(heisen.sparceDiagonalization())
        eSW05.append(heisen.SWdft())
        eCM05.append(heisen.CM())
        eEX05.append(heisen.ExaDFT())

    plt.figure(figsize=(12,4.5))
    plt.subplot(131)
    plt.title(r'$(A)S=1/2$', fontsize=15)
    plt.plot(n , eExact05, label=r'$E_0^{exat}$', marker='o', markerfacecolor='black', color='black', ms=10, markeredgecolor='black')
    plt.plot(n , eSW05, label=r'$E_0^{LSA-SW}$', marker='s', markerfacecolor='red', color='red', ms=10, markeredgecolor='black') 
    plt.plot(n , eCM05,  label=r'$E_0^{CM}$', marker='*', markerfacecolor='blue', color='blue', ms=10, markeredgecolor='black')
    plt.plot(n , eEX05,  label=r'$E_0^{LSA-EX}$', marker='*', markerfacecolor='green', color='green', ms=10, markeredgecolor='black')

    plt.legend(fontsize=10)
    plt.ylim(-1.2, 0)
    plt.xlabel('# Spins', fontsize=15)
    plt.ylabel(r'$\frac{E_0}{-NJ}$', fontsize=20)

    plt.subplot(132)
    plt.title(r'$(B)S=1$', fontsize=15)
    plt.plot( n, eExact1, label=r'$E_0^{exat}$', marker='o', markerfacecolor='black', color='black', ms=10, markeredgecolor='black')
    plt.plot( n, eSW1, label=r'$E_0^{LSA-SW}$', marker='s', markerfacecolor='red', color='red', ms=10, markeredgecolor='black')
    plt.plot( n, eCM1, label=r'$E_0^{CM}$', marker='*', markerfacecolor='blue', color='blue', ms=10, markeredgecolor='black')
    plt.plot( n, eEX1,  label=r'$E_0^{LSA-EX}$', marker='*', markerfacecolor='green', color='green', ms=10, markeredgecolor='black')

    plt.legend(fontsize=10)
    plt.ylim(-3.5, 0)
    plt.xlabel('# Spins', fontsize=15)
    plt.ylabel(r'$\frac{E_0}{-NJ}$', fontsize=20)

    plt.subplot(133)

    plt.plot(n , [ (i-j)/j for i, j in zip(eSW1, eExact1)], 
            markerfacecolor='red', color='red', ms=10, label=r'$LSA(S=1)$', marker='s', markeredgecolor='black')
    plt.plot(n , [ (i-j)/j for i, j in zip(eSW05, eExact05)], 
            markerfacecolor='red', color='red', ms=10, label=r'$LSA(S=1/2)$', marker='o', markeredgecolor='black')

    plt.plot(n , [ (i-j)/j for i, j in zip(eEX1, eExact1)], 
            markerfacecolor='green', color='green', ms=10, label=r'$EX(S=1)$', marker='s', markeredgecolor='black')
    plt.plot(n , [ (i-j)/j for i, j in zip(eEX05, eExact05)], 
            markerfacecolor='green', color='green', ms=7, label=r'$EX(S=1/2)$', marker='o', markeredgecolor='black')

    plt.title('(C)', fontsize=15)

    plt.xlabel('# Spins', fontsize=15)
    plt.ylabel(r'$\mu$', fontsize=20)
    plt.legend(fontsize=10)


    plt.tight_layout()

def makeImpuritiesPlot(nSpin=4):
    eExact = []
    eSW = []
    eCM = []
    eEX = []
    for i in range(nSpin+1):
        heisen = oneDimHeisenberg(nSpin, i)
        eExact.append(heisen.sparceDiagonalization())
        eSW.append(heisen.SWdft())
        eCM.append(heisen.CM())
        eEX.append(heisen.ExaDFT())

    plt.figure(figsize=(12,4.5))
    plt.figure
    plt.subplot(121)
    plt.plot(eExact, label=r'$E_0^{exat}$', marker='o', markerfacecolor='black', color='black', ms=10)
    plt.plot(eSW, label=r'$E_0^{LSA-SW}$', marker='s', markerfacecolor='red', color='red', ms=10)
    plt.plot(eCM, label=r'$E_0^{CM}$', marker='*', markerfacecolor='blue', color='blue', ms=10)
    plt.plot(eEX, label=r'$E_0^{LSA-EX}$', marker='^', markerfacecolor='green', color='green', ms=10)
    plt.legend(fontsize=15)
    plt.xlabel('# impurezas', fontsize=15)
    plt.ylabel(r'$\frac{E[S_i]}{-NJ}$', fontsize=20)
    plt.title('(A)', fontsize=15)

    plt.subplot(122)
    plt.plot(range(0, nSpin+1), [ (i-j)/j for i, j in zip(eSW, eExact)], 
            marker='s', markerfacecolor='red', color='red', ms=10, label='LSA')
    plt.plot(range(0, nSpin+1), [ (i-j)/j for i, j in zip(eEX, eExact)], 
            marker='^', markerfacecolor='green', color='green', ms=10, label='EX')
    plt.xlabel('# Impurezas', fontsize=15)
    plt.ylabel(r'$\mu$', fontsize=15)
    plt.legend(fontsize=15)
    plt.title('(B)', fontsize=15)
    plt.tight_layout()


    


