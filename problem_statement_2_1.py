import pandas as pd


def distance(s):
    x1 = pd.Series((s != 0).cumsum())
    y1 = pd.Series(x1 != x1.shift())
    y1 = y1.groupby((y1 != y1.shift()).cumsum()).cumsum()
    return y1


l = [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]
df = pd.DataFrame({'X': l})
s = pd.Series(l)
y = distance(s)
df['Y'] = pd.Series(y).astype(int)
print(df)