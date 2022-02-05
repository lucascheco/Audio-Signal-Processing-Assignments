import A3Part2
import matplotlib.pyplot as plt

sig = A3Part2.genSine(1.0, 100.0, 0.0, 1000.0, 0.025)

X = A3Part2.fft(sig)

mX = A3Part2.optimalZeropad(sig, 1000.0, 100.0)


