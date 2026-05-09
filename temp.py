import pandas as pd
from src.data_loader import df

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 77]

pd.set_option('display.max_rows', None)

arr_of_arr = []
arr_to_append = []
for i in range(0, len(arr)-1):
    if arr[i+1]-1 == arr[i]:
        arr_to_append.append(arr[i])
    else:
        arr_of_arr.append(arr_to_append)
        arr_to_append = []


print(df.loc[(df['sleep_quality'] == 'good')
             | (df['sleep_quality'] == 'excellent')
             | (df['sleep_quality'] == 'average')])

