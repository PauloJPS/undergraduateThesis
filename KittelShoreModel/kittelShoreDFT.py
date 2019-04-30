import numpy as np
import matplotlib.pyplot as plt

n = 5
spinsDistribution = np.array([ (-1)**(n)/2 for n in range(n)])

def homogeniusSD(nSpin):
    return 

def inemogeniosSD(nSpins, nImp):
    nImsList = [(-1)**i for i in range(nImp)]
    nSpinList = [(-1)**(i+1)/2 for i in range(nSpins)]
    return np.array(nImsList + nSpinList)


def homogeniosSpinsDist(n):
    return np.array([ (-1)**(n)/2 for n in range(n)])

def corretalation(spinsDistribution):
    st = np.sum(spinsDistribution)
    sigma = np.sum(np.abs(spinsDistribution))
    return (-st + sigma)/2

def meanField(spinsDistribution):
    st = np.sum(spinsDistribution)**2
    n = len(spinsDistribution)  
    ns2 = np.sum(spinsDistribution**2)
    return (-st + ns2)/2

def lsaFunctional(spinsDistribution):
    eMeanField = meanField(spinsDistribution)
    eCorrelation = corretalation(spinsDistribution)
    return eMeanField + eCorrelation

def exactKittelShore(spinsDistribution):
    st = np.sum(spinsDistribution)
    st = st*(st+1)
    s = np.abs(spinsDistribution)
    s = [i*(i+1) for i in s]
    return (-st + np.sum(s))/2

def plotSpinsImp():
    n = [i for i in range(30)]
    exac = [-exactKittelShore(inemogeniosSD(i-30, i)) for i in n]
    ks = [-lsaFunctional(inemogeniosSD(i-30, i)) for i in n]

    plt.scatter(n, ks, marker='s', color='red', label=r'$E_0^{LSA}$', edgecolor='black', s=100)
    plt.scatter(n, exac, marker='o',  color='blue', label=r'$E_0^{Exa}$', edgecolor='black')
    plt.scatter(n, [exac[i]-ks[i] for i in n], marker='*', label=r'$\Delta(E_0^{Exa}-E_0^{LSA})$', color='black')

    plt.ylabel('Energia [J]', fontsize=15)
    plt.xlabel(r'$\# Impurezas$', fontsize=15)
    
    plt.legend(fontsize='x-large')
    plt.tight_layout() 



def plotSpinsLSAxExacHomogenio():
    N = list(range(50, 1000, 50))
    spins = [1/2, 1, 3/2, 2]
    labels = ['1/2', '1', '3/2', '2']
    colors = ['red', 'blue', 'green', 'orange']
    fig, ax = plt.subplots(1, 4)
    fig.set_size_inches(10,3)
    for spin in range(len(spins)):
        lsaF = []
        exac = [] 
        for n in N:
            spinsDistribution = np.array([ spin*(-1)**(n) for n in range(n)])
            lsaF.append(lsaFunctional(spinsDistribution))
            exac.append(exactKittelShore(spinsDistribution))
        lsaF = np.array(lsaF)
        exac = np.array(exac)
        ax[spin].plot(N, lsaF - exac , color=colors[spin], label='spin' + ' ' + labels[spin])
        ax[spin].set_xlabel(r'$N$', fontsize=15)
        ax[spin].set_ylabel(r'$\Delta\left(E^{Exato}_0 - E^{LSA}_0\right)$', fontsize=15)
        ax[spin].legend()
    plt.tight_layout()

    return lsaF, exac




