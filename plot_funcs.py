import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as matplt
import seaborn as sns
import warnings
from collections import Counter

def construct_list(dictionary):
    # Use list comprehension to repeat the keys of the dictionary
    # value number of times and return the result as a list
    try:
        dict_to_list = [key for key, value in dictionary.d.items() for _ in range(value)]
        return dict_to_list
    except:
        keys = list(dictionary.keys())
        probabilities = list(dictionary.values())
        return keys, probabilities

def pmf_plot(data_dict, **options):
    keys, probabilities = construct_list(data_dict)
    plt.figure(figsize=(8, 5))
    plt.bar(keys, probabilities, width=0.1, color='blue', alpha=0.7)

        

def hist_plot(data_dict, **options):
    """Plots a histogram with a bar plot using Matplotlib'hist.

    Options can be keyword args passed to hist

    Args:
        data_dict: A dictionary with bin edges as keys and frequencies as values
        options: Additional keyword arguments passed to plt.bar
    """

    array = construct_list(data_dict)
    nbins = len(data_dict.d)
    n, bins, patches = plt.hist(x=array, bins=nbins, color='#0504aa',
                            alpha=0.7, rwidth=0.85)

def Hists_Plot(datasets, **options):
    """
    Plot Mutiple Histograms. Takes in a list of Hist objects

    Args:
        datasets: A list of Hist objects to plot
        options: Additional keyword arguments passed to plt.bar
    """ 

    datasets_list = construct_datasets_list(datasets)

    # Determine the number of rows and columns based on the number of datasets
    nrows = len(datasets_list)  # number of rows
    ncols = 1  # number of columns = 

    fig, axes = plt.subplots(nrows, ncols)

    count = 0

    # Iterate through datasets and axes to populate each subplot
    for dataset, ax in zip(datasets_list, axes):
        # Assume each dataset is a list of values
        values = dataset
        nbins = len(datasets[count].d)

        # Plot the histogram on the current subplot
        ax.hist(values, bins=nbins)
        
        count = count + 1

    # Adjust layout parameters to avoid overlapping plots
    plt.tight_layout()

    # Show the plot
    plt.show()

def construct_datasets_list(listofhists):
    datasets_list = []
    for specficdict in listofhists:
      converted_array = construct_list(specficdict)
      array = np.array(converted_array)
      datasets_list.append(array)

    return datasets_list