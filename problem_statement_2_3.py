import pandas as pd
import numpy as np

'''
    step 1: creating a dateTimeIndices using date_range
    step 2: creating a series with data of random numbers using numpy and index as the dateTimeIndices
    step 3: creating a series with previous series values and index as the dateTimeIndices.dayOfWeek (returns an int for days in a week)
    step 4: filtering the series with wednesdays (value = 2)
'''
dateTimeIndices = pd.date_range('1/1/2015','31/12/2015')
series_of_random_numbers = pd.Series(np.random.randint(0,100,len(dateTimeIndices)),index=dateTimeIndices)
series_of_random_numbers1 = pd.Series(series_of_random_numbers.values,index=dateTimeIndices.dayofweek)
print(sum(series_of_random_numbers1.filter(like='2')))
