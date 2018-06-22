import numpy as np
import matplotlib.pyplot as plt

n = 5
spinsDistribution = np.array([ (-1)**(n)/2 for n in range(n)])

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



