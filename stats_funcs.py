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
        
        if isinstance(obj, (_DictWrapper, Cdf, Pdf)):
            self.label = label if label is not None else obj.label
        elif isinstance(obj, pd.Series):
            self.d.update(obj.value_counts().items())
        elif isinstance(obj, dict):
            self.d.update(obj.items())
        else:
            # finally, treat it like a list
            self.d.update(Counter(obj))
        if len(self) > 0 and isinstance(self, Pmf):
            self.Normalize()

    def __len__(self):
        return len(self.d)

    def __getitem__(self, value):
        return self.d.get(value, 0)

    def Items(self):
        return self.d.items()

    def Values(self):
        return self.d.values()
    
    def Total(self):
        """Returns the total of the frequencies/probabilities in the map."""
        total = sum(self.d.values())
        return total
        

    
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

        # Sort the dictionary keys in ascending order
        sorted_keys = sorted(self.d.keys(), reverse=True)

        # Ensure that x is within the correct bounds
        x = min(x, len(sorted_keys))

        # Return the x smallest keys and their occurrences without any formatting issues
        return [(key, self.d[key]) for key in sorted_keys[:x]]
    
    def Smallest(self, x):
        """Finds the x smallest numbers in a dictionary, along with their occurrences.

        Args:
            x: The number of smallest numbers to return

        Returns:
            A list of tuples containing the x smallest numbers and their occurrences
        """

        # Sort the dictionary keys in ascending order
        sorted_keys = sorted(self.d.keys())

        # Ensure that x is within the correct bounds
        x = min(x, len(sorted_keys))

        # Return the x smallest keys and their occurrences without any formatting issues
        return [(key, self.d[key]) for key in sorted_keys[:x]]

class Pmf(_DictWrapper):
    def Normalize(self, fraction = 1):
        """Normalizes this PMF so the sum of all probs is fraction.

        Args:
            fraction: what the total should be after normalization

        Returns: the total probability before normalizing
        """
        if self.log:
            raise ValueError("Normalize: Pmf is under a log transform")

        total = self.Total()
        if total == 0:
            raise ValueError("Normalize: total probability is zero.")

        factor = fraction / total
        for x in self.d:
            self.d[x] *= factor

        return total
    
    def Prob(self, x, default=0):
        """Find proabibilities of a specfic PMF item in the PMNF dictonary
        Args:
            x: the value for the prob function to find
            default: the default value to return if not found in the function
        
        Returns: Proabibility of a specfic item
        """

        return self.d.get(x, default)
    
    def __getitem__(self, value, default=0):
        return self.d.get(value, default)
    
class Cdf:
    def temp_to_delete():
        pass

class Pdf:
    def temp_to_delete():
        pass
