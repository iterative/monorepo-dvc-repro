import random
import numpy as np
import pandas as pd
import dvc.api

params = dvc.api.params_show(stages="create_plots")
random.seed(params["seed"])


x = np.linspace(0, 10, 11)
y = [3.9, 4.4, random.uniform(4.5, 8.9), 10.3, 11.2, 13.1, random.uniform(12.5, 16.7),  9.9, 13.9, 15.1, 12.5]

pd.DataFrame(data={"x":x, "y":y}).to_csv("scatter.csv", index=False)