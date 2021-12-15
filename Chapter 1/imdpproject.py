import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = (r'C:\Users\DELL\Downloads\ai_nov21-main\ai_nov21\Chapter 1\08. Matplotlib\100_movies (6).csv')
data = pd.read_csv(url)
data.info()