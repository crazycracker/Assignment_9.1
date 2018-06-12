import pandas as pd
import numpy as np

series_of_dates = pd.bdate_range('2015-01-01','2015-12-31')
df = pd.DataFrame(np.random.randint(0,100,size=(1,len(series_of_dates))), columns=series_of_dates)
print(df)