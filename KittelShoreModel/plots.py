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
    n = [i for i in range(2,30)]
    for i in n:
        sistem05 = kittelShoreDFT(i, 0)
        sistem1 = kittelShoreDFT(i, i)

        exac05.append(sistem05.exactKittelShore())
        ks05.append(sistem05.lsaFunctional())
        cm05.append(sistem05.meanField())

        exac1.append(sistem1.exactKittelShore())
        ks1.append(sistem1.lsaFunctional())
        cm1.append(sistem1.meanField())


    plt.figure(figsize=(12, 4.5))

    plt.subplot(131)
    plt.title('(A)' + r'$S=1/2$', fontsize=15)
    plt.plot(n, ks05, marker='s',  label=r'$E_0^{LSA}$', markeredgecolor='red', color='red', ms=10)
    plt.plot(n, exac05, marker='o',   label=r'$E_0^{Exa}$', markeredgecolor='black', color='black', ms=7)
    plt.plot(n, cm05, marker='*',   label=r'$E_0^{CM}$', markeredgecolor='blue', color='blue', ms=10)
 
    plt.ylabel(r'$\frac{E_0}{-NJ}$', fontsize=20)
    plt.xlabel('# Spins', fontsize=15)
    plt.legend(fontsize=15)

    plt.subplot(132)
    plt.title('(B)' + r'$S=1$', fontsize=15)
    plt.plot(n, ks1, marker='s',  label=r'$E_0^{LSA}$', markeredgecolor='red', color='red', ms=10)
    plt.plot(n, exac1, marker='o',   label=r'$E_0^{Exa}$', markeredgecolor='black', color='black', ms=7)
    plt.plot(n, cm1, marker='*',   label=r'$E_0^{CM}$', markeredgecolor='blue', color='blue', ms=10)
 
    plt.ylabel(r'$\frac{E_0}{-NJ}$', fontsize=20)
    plt.xlabel('# Spins', fontsize=15)
    plt.legend(fontsize=15)

    plt.subplot(133)
    plt.title('(C)', fontsize=15)
    plt.plot(n, [(i-j)/i for i, j in zip(exac05, ks05)], marker='s', label=r'$S=1/2$', color='blue', ms=10)
    plt.plot(n, [(i-j)/i for i, j in zip(exac1, ks1)], marker='o', label=r'$S=1$', color='red', ms=7)

    plt.ylabel(r'$\mu$', fontsize=20)
    plt.xlabel('# Spins', fontsize=15)
    
    plt.legend(fontsize=15)
    plt.tight_layout() 



def plotSpinsImp():
    exac = []
    ks = []
    cm = []
    n = [i for i in range(2,30)]
    for i in n:
        sistem = kittelShoreDFT(30, i)
        exac.append(sistem.exactKittelShore())
        ks.append(sistem.lsaFunctional())
        cm.append(sistem.meanField())

    plt.figure(figsize=(12, 4.5))

    plt.subplot(121)
    plt.title('(A)', fontsize=15)
    plt.plot(n, ks, marker='s',  label=r'$E_0^{LSA}$', markeredgecolor='red', color='red', ms=10)
    plt.plot(n, exac, marker='o',   label=r'$E_0^{Exa}$', markeredgecolor='black', color='black', ms=7)
    plt.plot(n, cm, marker='*',   label=r'$E_0^{CM}$', markeredgecolor='blue', color='blue', ms=10)
 
    plt.ylabel(r'$\frac{E_0}{-NJ}$', fontsize=20)
    plt.xlabel('# Impurezas', fontsize=15)
    plt.legend(fontsize=15)

    plt.subplot(122)
    plt.title('(B)', fontsize=15)
    plt.plot(n, [(i-j)/i for i, j in zip(exac, ks)], marker='*', label=r'$\Delta(E_0^{Exa}-E_0^{LSA})$', color='black', ms=10)

    plt.ylabel(r'$\mu$', fontsize=20)
    plt.xlabel('# Impurezas', fontsize=15)
    
    plt.legend(fontsize=15)
    plt.tight_layout() 

