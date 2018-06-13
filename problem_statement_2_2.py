import pandas as pd
import numpy as np

'''
    step 1: creating a dateTimeIndices using date_range
    step 2: creating a series with date of random numbers using numpy and index as the dateTimeIndices
'''
dateTimeIndices = pd.date_range('1/1/2015','31/12/2015')
series_of_random_numbers = pd.Series(np.random.randint(0, 100 ,len(dateTimeIndices)),index=dateTimeIndices)
print(series_of_random_numbers)
