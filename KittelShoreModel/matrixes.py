from scipy.sparse import linalg as lin
import scipy.sparse as sparse
import numpy as np
import matplotlib.pyplot as plt 


class operators():
    def __init__(self, n, ax):
        self.n = n
        self.ax = ax

    @staticmethod
    def mat(n, ax):
        op = operators(n, ax)
        if ax == 'x': return op.matx()
        elif ax == 'y': return op.maty()
        elif ax == 'z': return op.matz()
        elif ax == 'i': return op.iden()
        else: return 0

    def matx(self):
        if self.n==1:
            col = [1, 0, 2, 1]
            row = [0, 1, 1, 2]
            data = 1/np.sqrt(2)*np.array([1, 1, 1, 1])
            return sparse.bsr_matrix((data, (row, col)), shape=(3, 3))
        elif self.n==0.5:
            col = [1, 0]
            row = [0, 1]
            data = 1/2*np.array([1, 1])
            return sparse.bsr_matrix((data, (row, col)), shape=(2, 2))
        else:
            return 0

    def maty(self):
        if self.n==1:
            col = [1, 0, 2, 1]
            row = [0, 1, 1, 2]
            data = 1/np.sqrt(2)/1j*np.array([1, -1, 1, -1])
            return sparse.bsr_matrix((data, (row, col)), shape=(3, 3))
        elif self.n==0.5:
            col = [1, 0]
            row = [0, 1]
            data = 1/2*np.array([(0. -1.j), (0. +1.j)])
            return sparse.bsr_matrix((data, (row, col)), shape=(2, 2))
        else: return 0

    def matz(self):
        if self.n==1:
            col = [0, 2]
            row = [0, 2]
            data = [1., -1.]
            return sparse.bsr_matrix((data, (row, col)), shape=(3, 3))
        elif self.n==0.5:
            col = [0, 1]
            row = [0, 1]
            data = 1/2*np.array([1, -1])
            return sparse.bsr_matrix((data, (row, col)), shape=(2, 2))
        else: return 0


    def iden(self):
        if self.n==1:
            col = [0,1,2]
            row = [0,1,2]
            data = [1, 1, 1]
            return sparse.bsr_matrix((data, (row, col)), shape=(3, 3))
        elif self.n==0.5:
            col = [0,1]
            row = [0,1]
            data = [1, 1]
            return sparse.bsr_matrix((data, (row, col)), shape=(2, 2))

