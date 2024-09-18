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
        """
        Gets x number of Largest values
        """
        
        # Count the occurrences of each number
        number_occurrences = Counter(self.d)

        # Return the x largest numbers based on occurrences
        return [Counter.itemgetter(0)(item) for item in number_occurrences.most_common(x)]