import sys
sys.path.append('../../software/models/')
from dftModel import dftAnal, dftSynth
from scipy.signal import get_window

import A3Part4
import matplotlib.pyplot as plt
import numpy as np
import scipy.fft as fft
import math
import loadTestCases as ld

def genMultiSines(freq, ts):
    total = 0.0
    length = len(freq)

    for i in range(length):
        total += A3Part4.genSine(1.0, freq[i], 0.0, 44100.0, ts)
    
    ans = total
    return ans


freq = [40.0, 100.0, 200.0, 1000.0]
freq2 = [23.0, 36.0, 230.0, 900.0, 2300.0]

sig  = genMultiSines(freq2, 1.0)

length = len(sig)

X = fft.fft(sig)
SIG = X[:length//2 + 1]

N = pow(2, math.ceil(np.log10(length)/np.log10(2)))
 
yfilter = A3Part4.suppressFreqDFTmodel(sig, 44100.0, int(N))
# plot(float(44100)*np.arange(mX.size)/float(N), mX, 'r')

case = 1
testcase = ld.load(4, case)
y, yfilt = A3Part4.suppressFreqDFTmodel(**testcase['input'])

print(f'Testcase {case}')
print(testcase['output'][0])
print(testcase['output'][1])

print()

print('Meu Resultado')
print(y)
print(yfilt)

plt.plot(testcase['output'][1], 'r')
plt.plot(yfilt, 'b')

plt.show()
