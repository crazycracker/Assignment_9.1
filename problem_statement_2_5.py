import pandas as pd
import numpy as np
import math
'''
    step 1: creating a dateTimeIndices using date_range
    step 2: creating a series with date of random numbers using numpy and index as the dateTimeIndices
    step 3: creating a list to store highest value dates
    step 4: creating a list to store corresponding highest values
    step 5: running a loop and finding the highest value for a group of four months and finding the corresponding date
    step 6: storing the highest value and corresponding date
    step 7: printing the highest value dates
    
    optional:
    Uncomment the last line to print out the highest values of the corresponding dates
'''
dateTimeIndices = pd.date_range('1/1/2015','31/12/2015')
series_of_random_numbers = pd.Series(np.random.randint(0,100,len(dateTimeIndices)),index=dateTimeIndices)
highest_value_dates = list()
highest_values = list()

for x in range(1,13,4):
    high = 0
    date = ''
    for month in range(x,x+4):
        val = series_of_random_numbers.filter(like='2015-0'+str(month)).max()
        if not math.isnan(val):
            if val > high:
                high = val
                dateSeries = series_of_random_numbers.filter(like='2015-0'+str(month))
                date = str(dateSeries.index.max())
    highest_value_dates.append(date[:10])
    highest_values.append(high)
print('dates of highest values : ' + str(highest_value_dates))
#uncomment below line to find out the corresponding highest values
#print('Corresponding highest values: ' + str(highest_values))