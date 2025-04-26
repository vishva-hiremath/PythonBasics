import numpy as np
import pandas as pd

start_row = 4
end_row = 280000

# Calculate the number of rows to skip and read
rows_to_skip = start_row
rows_to_read = end_row - start_row + 1

ges = pd.read_csv('/Users/aa949501/Downloads/ANALYST_Prod_Final_Latest_Date.csv', nrows=0)
#ges['DEPOSIT_DT'] = '4/16/2025'
print(ges)
ges1 = pd.read_csv('/Users/aa949501/Downloads/ANALYST_Prod_Final_Latest_Date.csv', header = 0, skiprows=1,nrows=2)
print(ges1)
combineddf = pd.concat([ges,ges1], ignore_index=False)
print(combineddf)
ges.to_csv('/Users/aa949501/Downloads/test.csv', index=False)