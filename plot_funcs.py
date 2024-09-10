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

  dataset = sns.load_dataset(histobj)

  sns.histplot(dataset, x="score")