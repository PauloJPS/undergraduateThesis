import numpy
import matplotlib.pyplot as plt
from impurities import *



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
    plt.plot(eExact, label=r'$E_0^{exat}$', marker='o', markerfacecolor='black', color='black', ms=10, markeredgecolor='black')
    plt.plot(eSW, label=r'$E_0^{LSA-SW}$', marker='s', markerfacecolor='red', color='red', ms=10, markeredgecolor='black')
    plt.plot(eCM, label=r'$E_0^{CM}$', marker='*', markerfacecolor='blue', color='blue', ms=10, markeredgecolor='black')
    plt.plot(eEX, label=r'$E_0^{LSA-EX}$', marker='^', markerfacecolor='green', color='green', ms=10, markeredgecolor='black')
    plt.legend(fontsize=15)
    plt.xlabel('# impurezas', fontsize=15)
    plt.ylabel(r'$\frac{E[S_i]}{-NJ}$', fontsize=20)
    plt.title('(A)', fontsize=15)

    plt.subplot(122)
    plt.plot(range(0, nSpin+1), [ (i-j)/j for i, j in zip(eSW, eExact)], 
            marker='s', markerfacecolor='red', color='red', ms=10, label='LSA', markeredgecolor='black')
    plt.plot(range(0, nSpin+1), [ (i-j)/j for i, j in zip(eEX, eExact)], 
            marker='^', markerfacecolor='green', color='green', ms=10, label='EX', markeredgecolor='black')
    plt.xlabel('# Impurezas', fontsize=15)
    plt.ylabel(r'$\mu$', fontsize=15)
    plt.legend(fontsize=15)
    plt.title('(B)', fontsize=15)
    plt.tight_layout()


    

