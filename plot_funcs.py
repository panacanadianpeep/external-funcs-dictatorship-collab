import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as matplt
import seaborn as sns
import warnings

def Hist(histobj, **options):
  """Plots a Pmf or Hist with a bar plot.

  The default width of the bars is based on the minimum difference
  between values in the Hist.  If that's too small, you can override
  it by providing a width keyword argument, in the same units
  as the values.

  Args:
    hist: Hist or Pmf object
    options: keyword args passed to plt.bar

    
  """

  """Plots a histogram with a bar plot using Matplotlib's hist.

    Options can be keyword args passed to plt.hist

    Args:
        data_dict: A dictionary with bin edges as keys and frequencies as values
        options: Additional keyword arguments passed to plt.hist
    """

  # Extract bin edges and frequencies into separate lists
  bin_edges = list(data_dict.keys())
  frequencies = list(data_dict.values())

  # Sort bin edges (if not sorted)
  bin_edges.sort()

  # Shift bin edges to the left
  adjusted_bin_edges = [edge - 0.5 for edge in bin_edges]

  # Plot the histogram using Matplotlib's hist
  plt.hist(adjusted_bin_edges, frequencies, **options)

  # Set labels and title (you can adjust them as needed)
  plt.xlabel('Bin Edges')
  plt.ylabel('Frequency')
  plt.title('Histogram from Dictionary Data')
  plt.xticks(bin_edges)

  plt.show()  # Display the plot
