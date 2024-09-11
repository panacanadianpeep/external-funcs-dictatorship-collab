import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as matplt
import seaborn as sns
import warnings


def hist_plot(data_dict, **options):
    """Plots a histogram with a bar plot using Matplotlib's bar.

    Options can be keyword args passed to plt.bar

    Args:
        data_dict: A dictionary with bin edges as keys and frequencies as values
        options: Additional keyword arguments passed to plt.bar
    """

    # Extract bin edges and frequencies into separate lists
    bin_edges = list(data_dict.keys())
    frequencies = list(data_dict.values())

    # Sort bin edges (if not sorted)
    bin_edges.sort()

    # Create adjusted bin edges for plotting
    left_edges = [edge - 0.5 * (bin_edges[1] - edge) for edge in bin_edges]

    # Plot the histogram using Matplotlib's bar
    plt.bar(left_edges, frequencies, **options)

    # Set labels and title (you can adjust them as needed)
    plt.xlabel('Bin Edges')
    plt.ylabel('Frequency')
    plt.title('Histogram from Dictionary Data')
    plt.xticks(bin_edges)

    plt.show()  # Display the plot