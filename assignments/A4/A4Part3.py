import os
import sys
import numpy as np
from scipy.signal import get_window
import matplotlib.pyplot as plt


sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models/'))
import stft
import utilFunctions as UF

eps = np.finfo(float).eps

"""
A4-Part-3: Computing band-wise energy envelopes of a signal

Write a function that computes band-wise energy envelopes of a given audio signal by using the STFT.
Consider two frequency bands for this question, low and high. The low frequency band is the set of 
all the frequencies between 0 and 3000 Hz and the high frequency band is the set of all the 
frequencies between 3000 and 10000 Hz (excluding the boundary frequencies in both the cases). 
At a given frame, the value of the energy envelope of a band can be computed as the sum of squared 
values of all the frequency coefficients in that band. Compute the energy envelopes in decibels. 

Refer to "A4-STFT.pdf" document for further details on computing bandwise energy.

The input arguments to the function are the wav file name including the path (inputFile), window 
type (window), window length (M), FFT size (N) and hop size (H). The function should return a numpy 
array with two columns, where the first column is the energy envelope of the low frequency band and 
the second column is that of the high frequency band.

Use stft.stftAnal() to obtain the STFT magnitude spectrum for all the audio frames. Then compute two 
energy values for each frequency band specified. While calculating frequency bins for each frequency 
band, consider only the bins that are within the specified frequency range. For example, for the low 
frequency band consider only the bins with frequency > 0 Hz and < 3000 Hz (you can use np.where() to 
find those bin indexes). This way we also remove the DC offset in the signal in energy envelope 
computation. The frequency corresponding to the bin index k can be computed as k*fs/N, where fs is 
the sampling rate of the signal.

To get a better understanding of the energy envelope and its characteristics you can plot the envelopes 
together with the spectrogram of the signal. You can use matplotlib plotting library for this purpose. 
To visualize the spectrogram of a signal, a good option is to use colormesh. You can reuse the code in
sms-tools/lectures/4-STFT/plots-code/spectrogram.py. Either overlay the envelopes on the spectrogram 
or plot them in a different subplot. Make sure you use the same range of the x-axis for both the 
spectrogram and the energy envelopes.

NOTE: Running these test cases might take a few seconds depending on your hardware.

Test case 1: Use piano.wav file with window = 'blackman', M = 513, N = 1024 and H = 128 as input. 
The bin indexes of the low frequency band span from 1 to 69 (69 samples) and of the high frequency 
band span from 70 to 232 (163 samples). To numerically compare your output, use loadTestCases.py
script to obtain the expected output.

Test case 2: Use piano.wav file with window = 'blackman', M = 2047, N = 4096 and H = 128 as input. 
The bin indexes of the low frequency band span from 1 to 278 (278 samples) and of the high frequency 
band span from 279 to 928 (650 samples). To numerically compare your output, use loadTestCases.py
script to obtain the expected output.

Test case 3: Use sax-phrase-short.wav file with window = 'hamming', M = 513, N = 2048 and H = 256 as 
input. The bin indexes of the low frequency band span from 1 to 139 (139 samples) and of the high 
frequency band span from 140 to 464 (325 samples). To numerically compare your output, use 
loadTestCases.py script to obtain the expected output.

In addition to comparing results with the expected output, you can also plot your output for these 
test cases.You can clearly notice the sharp attacks and decay of the piano notes for test case 1 
(See figure in the accompanying pdf). You can compare this with the output from test case 2 that 
uses a larger window. You can infer the influence of window size on sharpness of the note attacks 
and discuss it on the forums.
"""

def energy(signal):
    value = 0.0
    for i in range(len(signal)):
        value += np.power(abs(signal[i]), 2)

    return value

def bandEnergy(spec, index, initialBin, finalBin):
    value = 0.0
    
    i = initialBin
    while (i <= finalBin):
        value += np.power(abs(spec[index]), 2)

        i+=1
    return value
    
def freq2bin(freq, sr, N):
    return int(freq * N/sr)

def computeEngEnv(inputFile, window, M, N, H):
    
    (fs, x) = UF.wavread(inputFile)
    
    w = get_window(window, M, False)

    (mX, pX) = stft.stftAnal(x, w, N, H)

    frames = pow(10.0, mX/20.0)

    prevBin = -1
    lowBins = []
    i=1
    while (i < 3000):
        posBin = freq2bin(float(i), 44100.0, 1024.0)
        if (prevBin != posBin):
            lowBins.append(posBin)
        prevBin = posBin
        i += 1
    
    lowBins.pop(0)
    highBins = []
    prevBin = -1
    i+=1
    while (i < 10000):
        posBin = freq2bin(float(i), 44100.0, 1024.0)
        if (prevBin != posBin):
            highBins.append(posBin)
        prevBin = posBin
        i += 1

    highBins.pop(0)
    lowEnv = np.arange(float(len(frames)))

    outLowArr = lowBins.copy()
    lowSize = len(lowBins)
    outIndex = outLowArr[lowSize-1]
    for i in range(len(frames)):
        lowEnv[i]= sum(np.power(abs(frames[i][lowBins[0]:outIndex+1]), 2))

    outHighArr = highBins.copy()
    highSize = len(highBins)
    outIndex = outHighArr[highSize-1]
    highEnv = np.arange(float(len(frames)))
    for i in range(len(frames)):
        highEnv[i]= sum(np.power(abs(frames[i][highBins[0]:outIndex+1]), 2))

    energyLow_dB = 10.0 * np.log10(lowEnv)
    energyHigh_dB = 10.0 * np.log10(highEnv)

    returnArr = np.ndarray([len(energyLow_dB), 2], float)  
    
    for i in range(len(energyLow_dB)):
        arr = np.arange(float(2))
        
        arr[0] = energyLow_dB[i]
        arr[1] = energyHigh_dB[i]

        returnArr[i] = arr
        
    return returnArr
