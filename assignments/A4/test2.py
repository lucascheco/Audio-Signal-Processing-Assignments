import sys
sys.path.append('../../software/models/')
from dftModel import dftAnal, dftSynth
from scipy.signal import get_window

import A4Part2
import matplotlib.pyplot as plt
import numpy as np
import scipy.fft as fft
import math
import loadTestCases as ld


case = 1
testcase = ld.load(2, case)

result = A4Part2.computeSNR(**testcase['input'])

print(f'Testcase {case}')
print(testcase['output'])

print()

print('Meu Resultado')
print(result)


