import random
import pandas as pd
import numpy as np
import dvc.api

params = dvc.api.params_show()
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




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
print('13392-19506')