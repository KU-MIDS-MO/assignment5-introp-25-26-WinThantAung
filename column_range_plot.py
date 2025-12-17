import numpy as np
import matplotlib.pyplot as plt


def column_range_plot(A, filename="column_ranges.pdf"):

    max_vals = np.max(A, axis=0)
    min_vals = np.min(A, axis=0)

    ranges = max_vals - min_vals       # column range

    x = np.arange(len(ranges))        # bar plot
    plt.bar(x, ranges)

    plt.xlabel("Column index")
    plt.ylabel("Range (max - min)")
    plt.title("Column Ranges")

    plt.savefig(filename)
    plt.show()

    return ranges
