import numpy as np
import pandas as pd
import sys

# script's input args:
# 1: the run # to make 

wind_speed = np.array(list(range(5, 25)))
angleRelX = np.array(list(range(-20, 20)))/2
optim_iterations = np.array([1,1000])

index = pd.MultiIndex.from_product(
    [wind_speed.tolist(), angleRelX.tolist(), optim_iterations.tolist()])
df = pd.DataFrame(index=index).reset_index()

df.loc[sys.argv[1]].to_csv("matlab_data.csv", header = False)
