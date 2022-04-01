import numpy as np
import pandas as pd
import os

wind_speed = np.array(list(range(5, 25)))
angleRelX = np.array(list(range(-20, 20)))/2
optim_iterations = np.array([1000, 1])

output_dict = {}

for wind in wind_speed:
    for angle in angleRelX:
        for optim_iter in optim_iterations:

            # execute the command to the terminal
            os.system("sbatch matlab_caller.sh $" + str(wind) + " $" + 
                str(angle) + " $" + str(optim_iter))
            
            # read the csv 
            df = pd.read_csv("wind_speed_" + str(wind_speed) + "_wind_angle_" + 
                str(wind_angle) + "_optim_" + str(optim_iterations))
            output_dict["wind_speed"] = output_dict["wind_speed"].append(df.loc[0])
            output_dict["wind_angle"] = output_dict["wind_angle"].append(df.loc[1])
            output_dict["optim"] = output_dict["optim"].append(df.loc[2])

            # ^--- fails. sbatch needs time to run. 