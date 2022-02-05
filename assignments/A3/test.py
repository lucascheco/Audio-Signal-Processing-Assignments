import A3Part1
import matplotlib.pyplot as plt

sig1 = A3Part1.genSine(1.0, 80.0, 0.0, 10000.0, 0.08)
sig2 = A3Part1.genSine(1.0, 200.0, 0.0, 10000.0, 0.08)

sigtotal = sig1 + sig2
X = A3Part1.fft(sigtotal)

mX = A3Part1.minimizeEnergySpreadDFT(sigtotal, 10000.0, 80.0, 200.0)

plt.plot(mX)

plt.show()
