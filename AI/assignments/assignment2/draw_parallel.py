import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
data = pd.read_csv("data_2.csv")
plt.figure()
parallel_coordinates(data, "cluster", color=["red", "green", "blue"])
plt.show()
