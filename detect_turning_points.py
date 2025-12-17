import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(signal, filename="turning_points.pdf"):

    diff = np.diff(signal)    #discrete differences

    turning_points = []         #turning points

    for i in range(1, len(diff)):
        if diff[i - 1] * diff[i] < 0:
            turning_points.append(i)

    turning_points = np.array(turning_points)

    plt.plot(signal, label="Signal")     #Plot signal

    if len(turning_points) > 0:       #Mark turning points
        plt.plot(turning_points, signal[turning_points], 'ro', label="Turning points")

    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Signal with Turning Points")
    plt.legend()

    plt.savefig(filename)
    plt.show()

    return turning_points

