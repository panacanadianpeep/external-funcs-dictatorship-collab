import numpy as np
import pandas as pd
import matplotlib as plt

def ReadCSVfile_edgecaseenter(file_path):
    df = pd.read_csv(file_path, lineterminator='\n', low_memory=False)
    return df

class _DictWrapper(object):
    def __init__(self, obj=None, label=None):
        """Initializes the distribution.

        obj: Hist, Pmf, Cdf, Pdf, dict, pandas Series, list of pairs
        label: string label"""

        if isinstance(obj, pd.DataFrame)
            print(obj, "pandas")
        elif isinstance(obj, dict):
            print(obj, "dict")
        else:
            print("list/Hist(Pmf, Cdf, Pdf, not included)")
