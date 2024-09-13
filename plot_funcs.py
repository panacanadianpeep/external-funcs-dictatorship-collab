import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as matplt
import seaborn as sns
import warnings

def construct_list(dictionary, options):
    # Use list comprehension to repeat the keys of the dictionary
    # value number of times and return the result as a list
    dict_to_list = [key for key, value in dictionary.d.items() for _ in range(value)]
    df = pd.DataFrame(dict_to_list, columns=[options[''], options.y])
    return df
def hist_plot(data_dict, ngraphs, **options):
    """Plots a histogram with a bar plot using Matplotlib'hist.

    Options can be keyword args passed to hist

    Args:
        data_dict: A dictionary with bin edges as keys and frequencies as values
        options: Additional keyword arguments passed to plt.bar
    """

    array = construct_list(data_dict)
    nbins = len(data_dict)
    n, bins, patches = plt.hist(x=array, bins=nbins, color='#0504aa',
                            alpha=0.7, rwidth=0.85)