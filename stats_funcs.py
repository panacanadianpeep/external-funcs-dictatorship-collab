import numpy as np
import pandas as pd

def ReadCSVfile_edgecaseenter(file_path):
    df = pd.read_csv(file_path, lineterminator='\n', low_memory=False)
    return df