# import pandas and numpy
import pandas as pd
import numpy as np

# simple array
data = np.array(['g', 'e', 'e', 'k', 's'])

# providing an index
ser = pd.Series(data, index=[10, 11, 12, 13, 14])

ser = pd.Series(data, index=['mandeep', 'sanjeev', '12', 'sanjeev', '14'])

value_loc = ser.loc['mandeep']

print(value_loc)
print(type(value_loc))

print(ser['mandeep'])
