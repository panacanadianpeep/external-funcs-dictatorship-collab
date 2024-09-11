import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as matplt
import seaborn as sns

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

  # Convert the dictionary to a pandas Series
  data_series = pd.Series(histobj)

  # Sort the Series by bin edges
  data_series = data_series.sort_index()

  # Plot the histogram using Seaborn's barplot
  sns.barplot(data_series, **options)

