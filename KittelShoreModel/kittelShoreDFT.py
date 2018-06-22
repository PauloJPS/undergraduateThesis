import numpy as np
import matplotlib.pyplot as plt

n = 5
spinsDistribution = np.array([ (-1)**(n)/2 for n in range(n)])

def homogeniusSD(nSpin):
    return 

def inemogeniosSD(nSpins, nImp):
    nImsList = [(-1)**i for i in range(nImp)]
    nSpinList = [(-1)**(i+1)/2 for i in range(nImp)]
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

