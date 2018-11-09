import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
from scipy.stats import norm
from scipy import stats
import matplotlib.pyplot as plt
# %matplotlib inline
from scipy.stats import skew
from scipy.stats.stats import pearsonr
# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"

train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")
print