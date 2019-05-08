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
    for j in range(nSpin):
        conf.append([])
        for i in range(nSpin):
            if i == j or i == (j+1)%nSpin:
                conf[j].append(func(sites[i]))
            else:
                conf[j].append(iden(sites[i]))
    mats = []
    for i in conf:
        res = sparse.bsr_matrix(1)
        for mat in i:
            res = sparse.kron(res, mat)
        mats.append(res.astype(np.float16))
    return np.sum(mats)

def totalHamiltonian(nSpin, nImp):
    h = (naiveHamiltonian(matx, nSpin, nImp) + 
        naiveHamiltonian(maty, nSpin, nImp) + 
        naiveHamiltonian(matz, nSpin, nImp))
    return h

def sparceDiagonalization(h, n, which='SA'):
    if n==2:
        return lin.eigsh(h, 1, which=which)[0]/n/2
    else:
        return lin.eigsh(h, 1, which=which)[0]/n

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

def CM(nSpin, nImp):
    sites = impuritieState(nSpin, nImp)
    H = 0
    for i in range(nSpin):
        H += (-1)**(i)*sites[i]*(-1)**((i+1)%nSpin)*sites[(i+1)%nSpin]
    if nSpin == 2: return H/nSpin
    else: return H/nSpin

def SWdft(nSpin, nImp):
    sites = impuritieState(nSpin, nImp)
    Delta = (2-np.pi)/np.pi
    H = 0
    for i in range(nSpin):
        H += (-1)**(i)*sites[i]*(-1)**((i+1)%nSpin)*sites[(i+1)%nSpin] + Delta*sites[i]
    if nSpin==2: return H/nSpin/2
    else: return H/nSpin

def makeSpinsPlot(nSpin=12):
    eExact1 = []
    eExact05 = []
    eCM1 = []
    eSW1 = []
    eCM05 = []
    eSW05 = []
    nSpin = nSpin+1
    for i in range(2, nSpin):
        mat = totalHamiltonian(i, i)
        eig = sparceDiagonalization(mat, i)
        eExact1.append(eig)
        eSW1.append(SWdft(i, i))
        eCM1.append(CM(i, i))

        mat = totalHamiltonian(i, 0)
        eig = sparceDiagonalization(mat, i)
        eExact05.append(eig)
        eSW05.append(SWdft(i, 0))
        eCM05.append(CM(i, 0))
    
    plt.figure(figsize=(12,4.5))
    plt.subplot(131)
    plt.title(r'$(A)S=1/2$', fontsize=15)
    plt.plot(range(2, nSpin), eExact05, label=r'$E_0^{exat}$', marker='o', markerfacecolor='black', color='black', ms=10)
    plt.plot(range(2, nSpin), eSW05, label=r'$E_0^{LSA-SW}$', marker='s', markerfacecolor='red', color='red', ms=10) 
    plt.plot(range(2, nSpin), eCM05,  label=r'$E_0^{CM}$', marker='*', markerfacecolor='blue', color='blue', ms=10)

    plt.legend(fontsize=15)
    plt.xlabel('# Spins', fontsize=15)
    plt.ylabel(r'$\frac{E_0}{-NJ}/$', fontsize=20)

    plt.subplot(132)
    plt.title(r'$(B)S=1$', fontsize=15)
    plt.plot(range(2, nSpin), eExact1, label=r'$E_0^{exat}$', marker='o', markerfacecolor='black', color='black', ms=10)
    plt.plot(range(2, nSpin), eSW1, label=r'$E_0^{LSA-SW}$', marker='s', markerfacecolor='red', color='red', ms=10)
    plt.plot(range(2, nSpin), eCM1, label=r'$E_0^{CM}$', marker='*', markerfacecolor='blue', color='blue', ms=10)

    plt.legend(fontsize=15)
    plt.xlabel('# Spins', fontsize=15)
    plt.ylabel(r'$\frac{E_0}{-NJ}$', fontsize=20)

    plt.subplot(133)

    plt.plot(range(2, nSpin), [ (i-j)/j for i, j in zip(eSW1, eExact1)], 
            markerfacecolor='red', color='red', ms=10, label=r'$S=1$', marker='v')
    plt.plot(range(2, nSpin), [ (i-j)/j for i, j in zip(eSW05, eExact05)], 
            markerfacecolor='blue', color='blue', ms=10, label=r'$S=1/2$', marker='^')
    plt.title('(C)', fontsize=15)

    plt.xlabel('# Spins', fontsize=15)
    plt.ylabel(r'$\mu$', fontsize=20)
    plt.legend(fontsize=15)


    plt.tight_layout()

def makeImpuritiesPlot(nSpin=4):
    eExact = []
    eSW = []
    eCM = []
    for i in range(nSpin+1):
        mat = totalHamiltonian(nSpin, i)
        eig = sparceDiagonalization(mat, nSpin)
        eExact.append(eig)
        eSW.append(SWdft(nSpin, i))
        eCM.append(CM(nSpin, i))

    plt.figure(figsize=(12,4.5))
    plt.figure
    plt.subplot(121)
    plt.plot(eExact, label=r'$E_0^{exat}$', marker='o', markerfacecolor='black', color='black', ms=10)
    plt.plot(eSW, label=r'$E_0^{LSA-SW}$', marker='s', markerfacecolor='red', color='red', ms=10)
    plt.plot(eCM, label=r'$E_0^{CM}$', marker='*', markerfacecolor='blue', color='blue', ms=10)
    plt.legend(fontsize=15)
    plt.xlabel('# impurezas', fontsize=15)
    plt.ylabel(r'$\frac{E[S_i]}{-NJ}$', fontsize=20)
    plt.title('(A)', fontsize=15)

    plt.subplot(122)
    plt.plot(range(0, nSpin+1), [ (i-j)/j for i, j in zip(eSW, eExact)], 
            marker='*', markerfacecolor='black', color='black', ms=10, label='Desvio Rel.')
    plt.xlabel('# Impurezas', fontsize=15)
    plt.ylabel(r'$\mu$', fontsize=15)
    plt.legend(fontsize=15)
    plt.title('(B)', fontsize=15)
    plt.tight_layout()


    


