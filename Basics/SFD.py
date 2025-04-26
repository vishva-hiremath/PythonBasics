import numpy as np
import pandas as pd


df = pd.read_csv('test.csv');

#ges.to_csv('/Users/Downloads/test.csv', index=False)
#print(f"Printing  {ges[ges['XX'] == 'XX']}")

#filtering out based on specific condition
result = df.loc[df['XXXX'] == '1111', ['XX','STATUS','CODE', 'EXPIRATION_DT', 'MAX_AVAIL']]
#df['MEMBER_NUMBER'] == 'XX'
print(f"Printing {result}")

#Grouping by specific column and sum on the another column.
#print(f"Group by: {df.groupby('STATUS')[['MAX_AVAIL']].sum()}")

#print(result)





