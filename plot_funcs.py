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

    df = pd.DataFrame([data_dict])
    df = df.T
    df.hist()