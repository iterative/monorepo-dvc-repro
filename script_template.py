import random
import pandas as pd
import numpy as np
import dvc.api
import yaml

params = dvc.api.params_show(stages="generate_table")

# params = yaml.safe_load(open("params.yaml"))

random.seed(params["seed"])


df2 = pd.DataFrame(
    np.array(
        [
            [random.random(), random.random(), random.random()],
            [random.random(), random.random(), random.random()],
            [random.random(), random.random(), random.random()]
        ]
    ), columns=['a', 'b', 'c']
    )

df2.to_csv("table.csv")
