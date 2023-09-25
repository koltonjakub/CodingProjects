from lib import Simulator
from lib import ImageAnalyzer

import matplotlib.pyplot as plt

if __name__ == "__main__":
    sim = Simulator.Simulation()

    plt.imshow(sim.imageAnalyzer.image)
    plt.gray()
    plt.xticks([])
    plt.yticks([])
    plt.show()

    plt.imshow(sim.imageAnalyzer.bitMap)
    plt.gray()
    plt.xticks([])
    plt.yticks([])
    plt.show()
