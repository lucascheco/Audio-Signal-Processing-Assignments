import sys
sys.path.append('../../software/models/')
from dftModel import dftAnal, dftSynth
from scipy.signal import get_window

import A3Part4
import A3Part5
import matplotlib.pyplot as plt
import numpy as np
import scipy.fft as fft
import math
import loadTestCases as ld

def genMultiSines(freq, ts):
    total = 0.0
    length = len(freq)

    for i in range(length):
        total += A3Part4.genSine(1.0, freq[i], 0.0, 1000.0, ts)
    
    ans = total
    return ans


freq = [110.0]

sig  = genMultiSines(freq, 0.512)[:-1]

length = len(sig)

# plot(float(44100)*np.arange(mX.size)/float(N), mX, 'r')

case = 1
testcase = ld.load(5, case)

mX1, mX2, mX3 = A3Part5.zpFFTsizeExpt(**testcase['input'])

print(f'Testcase {case}')
print(testcase['output'][0])
print(testcase['output'][1])
print(testcase['output'][2])

print()

print('Meu Resultado')
print(mX1)
print(mX2)
print(mX3)

