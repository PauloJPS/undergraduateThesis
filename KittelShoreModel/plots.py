from exactKS import *
from kittelShoreDFT import *
import numpy as np
import matplotlib.pyplot as plt
from kittelShoreDFT import *

def plotSpinHomo():
    exac05 = []
    ks05 = []
    cm05 = []

    exac1 = []
    ks1 = []
    cm1 = []
    n = [i for i in range(2,30, 2)]
    for i in n:
        sistem05 = kittelShoreDFT(i, 0)
        sistem1 = kittelShoreDFT(i, i)

        exac05.append(sistem05.exactKittelShore())
        ks05.append(sistem05.lsaFunctional())
        cm05.append(sistem05.meanField())

        exac1.append(sistem1.exactKittelShore())
        ks1.append(sistem1.lsaFunctional())
        cm1.append(sistem1.meanField())


    plt.figure(figsize=(12, 6.5))

    plt.subplot(121)
    plt.title('(A)' + r'$S=1/2$', fontsize=15)
    plt.plot(n, cm05, marker='*',   label=r'$E_0^{CM}$', markeredgecolor='black', color='blue', ms=13)
    plt.plot(n, ks05, marker='o',  label=r'$E_0^{LSA}$', markeredgecolor='black', color='red', ms=13)
    plt.plot(n, exac05, marker='o',   label=r'$E_0^{Exa}$', markeredgecolor='black', color='black', ms=5)
 
    plt.ylabel(r'$\frac{E_0}{J}$', fontsize=30, rotation=0, labelpad=20)
    plt.xlabel('N', fontsize=25)
    plt.legend(fontsize=20)

    plt.subplot(122)
    plt.title('(B)' + r'$S=1$', fontsize=15)
    plt.plot(n, cm1, marker='*',   label=r'$E_0^{CM}$', markeredgecolor='black', color='blue', ms=13)
    plt.plot(n, ks1, marker='o',  label=r'$E_0^{LSA}$', markeredgecolor='black', color='red', ms=13)
    plt.plot(n, exac1, marker='o',   label=r'$E_0^{Exa}$', markeredgecolor='black', color='black', ms=5)
 
    plt.ylabel(r'$\frac{E_0}{J}$', fontsize=30, rotation=0, labelpad=20)
    plt.xlabel('N', fontsize=25)
    plt.legend(fontsize=20)

    plt.tight_layout() 



def plotSpinsImp():
    exac = []
    ks = []
    cm = []
    n = [i for i in range(2,30, 2)]
    for i in n:
        sistem = kittelShoreDFT(30, i)
        exac.append(sistem.exactKittelShore())
        ks.append(sistem.lsaFunctional())
        cm.append(sistem.meanField())

    plt.figure(figsize=(12, 6.5))

    plt.plot(n, cm, marker='*',   label=r'$E_0^{CM}$', 
        markeredgecolor='black', color='blue', ms=13)
    plt.plot(n, ks, marker='o',  label=r'$E_0^{LSA}$', 
            markeredgecolor='black', color='red', ms=13)
    plt.plot(n, exac, marker='o',   label=r'$E_0^{Exa}$',
        markeredgecolor='black', color='black', ms=5)
    
    plt.ylabel(r'$\frac{E_0}{J}$', fontsize=30, rotation=0, labelpad=20)
    plt.xlabel(r'$N_i$', fontsize=25)
    plt.legend(fontsize=15)

    plt.tight_layout() 

