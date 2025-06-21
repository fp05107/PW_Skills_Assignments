import pandas as pd
import numpy as np

df = pd.read_csv("cricket_data.csv")

def analyze_data():
    a = df.Player_Name.unique()[:10]
    return a
