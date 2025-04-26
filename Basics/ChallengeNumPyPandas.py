import numpy as np
import pandas as pd

#1. Create a NumPy array containing numbers from 1 to 15. Reshape it into a 3×5 matrix.
arr = np.arange(0,15)
print(arr)
reShapArr = arr.reshape((3, 5))
print(reShapArr)

# 2. Create a Pandas DataFrame with columns for ‘Product’, ‘Price’, and ‘Quantity’. Add a few rows of data.
data = {"Product":["Earbuds","Speakers", "Headphones"],
        "Price":[100,200, 50],
        "Quantity":[2, 1, 10]}
df = pd.DataFrame(data)
print(df)

# 3. Calculate a new ‘Total Cost’ column (Price * Quantity) in your DataFrame.
df['Total Cost'] = df['Price'] * df['Quantity']
print(f"Printing after adding Total Cost: {df}")

#4. Select only the rows where the ‘Price’ is above a certain value.
print(f"Printing products having price > 100: {df[df['Price'] > 100]}")

ges = pd.read_csv('/Users/aa949501/Downloads/Status_Prod_Apr22_5pm.csv');
#ges['DEPOSIT_DT'] = '4/16/2025'
#ges.to_csv('/Users/Downloads/test.csv', index=False)
#print(f"Printing  {ges[ges['MEMBER_NUMBER'] == '69JRY32']}")

#df.loc[df['diagnosis'] == 'B', ['diagnosis','radius_mean','perimeter_mean','area_mean']]
result = ges.loc[ges['MEMBER_NUMBER'] == '69JRY32', ['MEMBER_NUMBER','STATUS','CODE', 'EXPIRATION_DT']]
print(result)





