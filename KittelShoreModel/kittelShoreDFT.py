import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import linalg as lin
import scipy.sparse as sparse


class kittelShoreDFT():
    def __init__(self, nSpin, nImp):
        self.nSpin = nSpin
        self.nImp = nImp
        self.spinSD = self.groudStateFunctional()

    def groudStateFunctional(self):
        sites = ([1/2*(-1)**i for i in range(self.nSpin-self.nImp)] +
        [1*(-1)**(i+1) for i in range(self.nImp)])
        return np.array(sites)

    def corretalation(self):
        st = np.sum(self.spinSD)
        sigma = np.sum(np.abs(self.spinSD))
        return (st - sigma)/2

    def meanField(self):
        st = np.sum(self.spinSD)**2
        n = len(self.spinSD)  
        ns2 = np.sum(self.spinSD**2)
        return (st - ns2)/2

    def lsaFunctional(self):
        eMeanField = self.meanField()
        eCorrelation = self.corretalation()
        return (eMeanField + eCorrelation)

    def exactKittelShore(self):
        spinsDistribution = self.spinSD
        st = np.sum(spinsDistribution)
        st = st*(st+1)
        s = np.abs(spinsDistribution)
        s = [i*(i+1) for i in s]
        return (st - np.sum(s))/2



