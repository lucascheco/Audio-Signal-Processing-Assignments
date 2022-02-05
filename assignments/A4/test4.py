import sys
sys.path.append('../../software/models/')
from dftModel import dftAnal, dftSynth
from scipy.signal import get_window

import A4Part4
import matplotlib.pyplot as plt
import numpy as np
import scipy.fft as fft
import math
import loadTestCases as ld


case = 1
testcase = ld.load(4, case)

energy = A4Part4.computeODF(**testcase['input'])

print(f'Testcase {case}')
print(len(testcase['output']))
print(testcase['output'])
plt.plot(testcase['output'])
    
print()

print('Meu Resultado')
print(len(energy[0]))
print(energy)
plt.plot(energy)

plt.show()


