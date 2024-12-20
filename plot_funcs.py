import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as matplt
import warnings
from collections import Counter

def construct_list(dictionary):
    # Use list comprehension to repeat the keys of the dictionary
    # value number of times and return the result as a list
    dict_to_list = [key for key, value in dictionary.d.items() for _ in range(value)]
    return dict_to_list

def plot_multiple_pmfs(pmf_list, titles):
    """
    Plots multiple PMFs in a single figure with subplots.
    
    Args:
        pmf_list (list of dict): List of PMFs (each PMF is a dictionary).
        titles (list of str): List of titles for each subplot.
    """
    num_pmfs = len(pmf_list)
    
    # Create a figure and subplots, with 1 row and 'num_pmfs' columns
    fig, axes = plt.subplots(1, num_pmfs, figsize=(5 * num_pmfs, 5))

    # Loop over each PMF and corresponding title to plot each
    for i, (pmf, title) in enumerate(zip(pmf_list, titles)):
        keys = np.array(list(pmf.d.keys()))
        probabilities = np.array(list(pmf.d.values()))
        
        # Plot the PMF on the ith subplot
        axes[i].bar(keys, probabilities, width=(max(keys) - min(keys)) / len(keys) * 0.8, color='blue', alpha=0.7)
        axes[i].set_title(title)
        axes[i].set_xlabel('Values')
        axes[i].set_ylabel('Probability')

        # Adjust x-axis ticks for clarity
        axes[i].set_xticks(keys)
        axes[i].tick_params(axis='x', rotation=45)
        
        # Add y-axis padding
        axes[i].set_ylim(0, max(probabilities) * 1.1)
    
    # Automatically adjust layout to prevent overlap
    plt.tight_layout()
    plt.show()
    

def pmf_plot(data_dict, **options):

    # Filter out keys with zero or negligible probabilities
    keys, probabilities = zip(*[(k, p) for k, p in data_dict.d.items() if p > 0])

    keys = np.array(keys)
    probabilities = np.array(probabilities)
    
    # Calculate the range of the keys and determine optimal bar width
    key_range = max(keys) - min(keys)
    num_keys = len(keys)
    
    # Set bar width as a fraction of the range to avoid overlap (adjust factor as needed)
    if num_keys > 1:
        bar_width = (key_range / num_keys) * 0.8  # Adjust bar width to be 80% of the gap between keys
    else:
        bar_width = 0.1  # Default bar width if only one key
    
    # Dynamically adjust the figure size based on the number of keys
    fig_width = max(8, num_keys * 0.5)
    fig_height = 6
    plt.figure(figsize=(fig_width, fig_height))
    
    # Create the bar plot
    plt.bar(keys, probabilities, width=bar_width, color='blue', alpha=0.7)

    # Dynamically adjust x-axis ticks to prevent overlap
    plt.xticks(keys, rotation=45, ha='right')

    # Adjust y-axis limits to provide some padding, ensuring bars are visible
    plt.ylim(0, max(probabilities) * 1.1)  # Add 10% padding to the tallest bar

    # Automatically adjust layout to prevent label cutoff
    plt.tight_layout()

     # Label the axes
    if "xlabel" in options:
        plt.xlabel(options["xlabel"])
    if "ylabel" in options:
        plt.ylabel(options["ylabel"])

    # Set title
    if "title" in options:
        plt.title(options["title"]) 
    
    # Show the plot
    plt.show()

     

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
    
    # Label the axes
    if "xlabel" in options:
        plt.xlabel(options["xlabel"])
    if "ylabel" in options:
        plt.ylabel(options["ylabel"])

    # Set title
    if "title" in options:
        plt.title(options["title"])

    plt.show()

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

        if "xlabel" in options:
            ax.set_xlabel(options["xlabel"])
        if "ylabel" in options:
            ax.set_ylabel(options["ylabel"])

        # Set title
        if "title" in options and len(options["title"]) <= nrows:
            ax.set_title(options["title"][count])
            
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

def Cdf_Plot(cdf_data, **options):
    fig = plt.figure(figsize="9, 4")

#code_V2:

def PrePlot(nplots, **options):
    """
    Sets different parameters to be parsed to the graph

    Args:
        nplots: How many plots to graph
        options: Additional keyword arguments passed to plts
    """ 

    figwidth = None
    figheight = None

    if "figwidth" in options:
        figwidth = options["figwidth"]
    if "figheight" in options:
        figheight = options["figheight"]

    fig, axes = plt.subplots(1, nplots)


