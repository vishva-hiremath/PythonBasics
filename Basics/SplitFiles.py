import numpy as np
import pandas as pd

start_row = 210001
end_row = 280000

# Calculate the number of rows to skip and read
rows_to_skip = start_row
rows_to_read = end_row - start_row + 1

ges = pd.read_csv('/Users/aa949501/Downloads/test.csv', skiprows=rows_to_skip, nrows=rows_to_read)
#ges['DEPOSIT_DT'] = '4/16/2025'
ges.to_csv('/Users/aa949501/Downloads/ANALYST_Prod_Final_Latest_Date_70k_test.csv', index=False)