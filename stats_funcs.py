import numpy as np
import pandas as pd
import matplotlib as plt
from collections import Counter
import copy
import bisect
import logging

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
    
    def Copy(self, label=None):
        """Returns a copy.

        Make a shallow copy of d.  If you want a deep copy of d,
        use copy.deepcopy on the whole object.

        label: string label for the new Hist

        returns: new _DictWrapper with the same type
        """
        new = copy.copy(self)
        new.d = copy.copy(self.d)
        new.label = label if label is not None else self.label
        return new
    
    def Total(self):
        """Returns the total of the frequencies/probabilities in the map."""
        total = sum(self.d.values())
        return total
    
    def Incr(self, x, term=1):
        self.d[x] = self.d.get(x, 0) + term

    def Mult(self, x, factor = 1):
        self.d[x] = self.d.get(x, 0) * factor
        

    
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
    """Represents a cumulative distribution function.

    Attributes:
        xs: sequence of values
        ps: sequence of probabilities
        label: string used as a graph label.
    """

    def __init__(self, obj=None, ps=None, label=None):
        """Initializes.

        If ps is provided, obj must be the corresponding list of values.

        obj: Hist, Pmf, Cdf, Pdf, dict, pandas Series, list of pairs
        ps: list of cumulative probabilities
        label: string label
        """
        self.label = label if label is not None else DEFAULT_LABEL

        if isinstance(obj, (_DictWrapper, Cdf, Pdf)):
            if not label:
                self.label = label if label is not None else obj.label

        if obj is None:
            # caller does not provide obj, make an empty Cdf
            self.xs = np.asarray([])
            self.ps = np.asarray([])
            if ps is not None:
                logging.warning("Cdf: can't pass ps without also passing xs.")
            return
        else:
            # if the caller provides xs and ps, just store them
            if ps is not None:
                if isinstance(ps, str):
                    logging.warning("Cdf: ps can't be a string")

                self.xs = np.asarray(obj)
                self.ps = np.asarray(ps)
                return

        # caller has provided just obj, not ps
        if isinstance(obj, Cdf):
            self.xs = copy.copy(obj.xs)
            self.ps = copy.copy(obj.ps)
            return

        if isinstance(obj, _DictWrapper):
            dw = obj
        else:
            dw = Hist(obj)

        if len(dw) == 0:
            self.xs = np.asarray([])
            self.ps = np.asarray([])
            return

        xs, freqs = zip(*sorted(dw.Items()))
        self.xs = np.asarray(xs)
        self.ps = np.cumsum(freqs, dtype=float)
        self.ps /= self.ps[-1]


class Pdf:
    def temp_to_delete():
        pass
