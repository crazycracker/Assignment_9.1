import pandas as pd
import numpy as np

'''
    step 1: creating a dateTimeIndices using date_range
    step 2: creating a series with date of random numbers using numpy and index as the dateTimeIndices
    step 3: creating a series with previous series values and index as the dateTimeIndices.month (returns an int for calendar month)
    step 4: creating a list to store averages as floats
    step 5: running a loop and finding the sums of integers over a month and calculating the average
    step 6: storing the average value in a list
    step 7: printing the average of every calendar month
'''
dateTimeIndices = pd.date_range('1/1/2015','31/12/2015')
series_of_random_numbers = pd.Series(np.random.randint(0,100,len(dateTimeIndices)),index=dateTimeIndices)
series_of_random_numbers1 = pd.Series(series_of_random_numbers.values,index=dateTimeIndices.month)
average_of_each_month = list()

for x in range(1,13):
    len = series_of_random_numbers1.filter(like=str(x)).__len__()
    sums = sum(series_of_random_numbers1.filter(like=str(x)))
    average_of_each_month.append(float(sums/len))
print(average_of_each_month)
