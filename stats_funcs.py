import numpy as np
import pandas as pd
import matplotlib as plt

def ReadCSVfile_edgecaseenter(file_path):
    df = pd.read_csv(file_path, lineterminator='\n', low_memory=False)
    return df

def Convert_Hist(df):
    df.Hist(column='column_name')

def Draw_Hist(title, xlabel, ylabel):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
