import numpy as np
import pandas as pd
import matplotlib as plt
from collections import Counter

def ReadCSVfile_edgecaseenter(file_path):
    df = pd.read_csv(file_path, lineterminator='\n', low_memory=False)
    return df

# When we plot Hist, Pmf and Cdf objects, they don't appear in
# the legend unless we override the default label.
DEFAULT_LABEL = "_nolegend_"

class _DictWrapper(object):
    def __init__(self, obj=None, label=None):
        """Initializes the distribution.

        obj: Hist, Pmf, Cdf, Pdf, dict, pandas Series, list of pairs
        label: string label"""

        self.label = label if label else DEFAULT_LABEL
        self.d = {}

        self.log = False

        if obj is None:
            return

        if isinstance(obj, pd.Series):
            self.d.update(obj.value_counts().items())
        elif isinstance(obj, dict):
            print(obj, "dict")
        else:
            print("list/Hist(Pmf, Cdf, Pdf, not included)")

    def __getitem__(self, value):
        return self.d.get(value, 0)

    def Items(self):
        return self.d.items()

    def Values(self):
        return self.d.values()
        

    
class Hist(_DictWrapper):
    def Freq(self, x):
        """
        Gets the frequency associated with the value x.

        Args:
                x: number value

        Returns:
                int frequency
        """

        return self.d.get(x, 0)
    def Largest(self, x):
        """Finds the x largest numbers in a dictionary, along with their occurrences.

        Args:
            x: The number of largest numbers to return

        Returns:
            A list of tuples containing the x largest numbers and their occurrences
        """

        # Sort the dictionary items in descending order based on keys
        sorted_numbers = sorted(self.d.items(), key=lambda x: x[0], reverse=True)

        # Return the x largest numbers and their occurrences
        return sorted_numbers[:x]
    
    def Smallest(self, x):
        """Finds the x smallest numbers in a dictionary, along with their occurrences.

        Args:
            x: The number of smallest numbers to return

        Returns:
            A list of tuples containing the x smallest numbers and their occurrences
        """

        # Sort the dictionary items in ascending order based on keys
        sorted_numbers = sorted(self.d.items(), key=lambda x: x[0])

        # Return the x smallest numbers and their occurrences
        return sorted_numbers[:x]